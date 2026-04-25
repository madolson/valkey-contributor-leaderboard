#!/usr/bin/env python3
"""Fetch commits from GitHub repos and generate leaderboard data."""

import json
import os
import re
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

SINCE_DEFAULT = "2024-03-28T00:00:00Z"
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
COMMITS_FILE = DATA_DIR / "commits.json"
LEADERBOARD_FILE = DATA_DIR / "leaderboard.json"


def log(msg):
    print(msg, file=sys.stderr)


def make_request(url, token=None):
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        resp = urllib.request.urlopen(req)
        data = json.loads(resp.read().decode())
        link = resp.headers.get("Link", "")
        return data, link
    except urllib.error.HTTPError as e:
        if e.code in (403, 429):
            log(f"Rate limited (HTTP {e.code}). Saving partial results.")
            return None, ""
        log(f"HTTP {e.code}: {e.reason} for {url}")
        sys.exit(1)


def parse_next_url(link_header):
    m = re.search(r'<([^>]+)>;\s*rel="next"', link_header)
    return m.group(1) if m else None


def fetch_commits(repo, since, token):
    owner, name = repo.split("/")
    url = f"https://api.github.com/repos/{owner}/{name}/commits?since={since}&per_page=100"
    all_commits = []
    page = 1
    while url:
        data, link = make_request(url, token)
        if data is None:
            break
        count = 0
        for c in data:
            author = c.get("author")
            if not author:
                continue
            all_commits.append({
                "sha": c["sha"],
                "author_login": author["login"],
                "author_id": author["id"],
                "avatar_url": author["avatar_url"],
                "date": c["commit"]["committer"]["date"],
                "repo": name,
            })
            count += 1
        log(f"  Page {page}: {count} commits (total: {len(all_commits)})")
        url = parse_next_url(link)
        page += 1
    return all_commits


def load_commits():
    if COMMITS_FILE.exists():
        return json.loads(COMMITS_FILE.read_text())
    return {"last_fetched": SINCE_DEFAULT, "commits": []}


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n")


def generate_leaderboard(commits):
    by_author = {}
    for c in commits:
        aid = c["author_id"]
        if aid not in by_author:
            by_author[aid] = {
                "login": c["author_login"],
                "id": aid,
                "avatar_url": c["avatar_url"],
                "commits": 0,
                "repos": set(),
            }
        by_author[aid]["commits"] += 1
        by_author[aid]["repos"].add(c["repo"])
        # Keep latest avatar/login
        by_author[aid]["login"] = c["author_login"]
        by_author[aid]["avatar_url"] = c["avatar_url"]

    contributors = sorted(by_author.values(), key=lambda x: x["commits"], reverse=True)
    for entry in contributors:
        entry["repos"] = sorted(entry["repos"])
    return contributors


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Fetch commits and build leaderboard")
    parser.add_argument("--repo", default="valkey-io/valkey", help="owner/repo to fetch")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if token:
        log("Using GITHUB_TOKEN for authentication")
    else:
        log("No GITHUB_TOKEN set — using unauthenticated requests (60 req/hr)")

    store = load_commits()
    existing_shas = {c["sha"] for c in store["commits"]}
    since = store["last_fetched"]

    log(f"Fetching {args.repo} since {since}")
    new_commits = fetch_commits(args.repo, since, token)

    added = 0
    for c in new_commits:
        if c["sha"] not in existing_shas:
            store["commits"].append(c)
            existing_shas.add(c["sha"])
            added += 1

    store["last_fetched"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    save_json(COMMITS_FILE, store)
    log(f"Added {added} new commits (total: {len(store['commits'])})")

    contributors = generate_leaderboard(store["commits"])
    leaderboard = {
        "generated": store["last_fetched"],
        "contributors": contributors,
    }
    save_json(LEADERBOARD_FILE, leaderboard)
    log(f"Leaderboard: {len(contributors)} contributors")


if __name__ == "__main__":
    main()
