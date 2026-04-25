#!/usr/bin/env python3
"""Fetch commits from all valkey-io repos and generate leaderboard data.

Only counts commits that have an associated merged PR with at least one
approval from someone other than the commit author.
"""

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
ORG = "valkey-io"

rate_limited = False


def log(msg):
    print(msg, file=sys.stderr)


def api_get(url, token=None):
    global rate_limited
    if rate_limited:
        return None, ""
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        resp = urllib.request.urlopen(req, timeout=30)
        data = json.loads(resp.read().decode())
        link = resp.headers.get("Link", "")
        return data, link
    except urllib.error.HTTPError as e:
        if e.code in (403, 429):
            log(f"Rate limited (HTTP {e.code}). Saving partial results.")
            rate_limited = True
            return None, ""
        log(f"HTTP {e.code}: {e.reason} for {url}")
        sys.exit(1)
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        log(f"Network error: {e}. Saving partial results.")
        rate_limited = True
        return None, ""


def parse_next_url(link_header):
    m = re.search(r'<([^>]+)>;\s*rel="next"', link_header)
    return m.group(1) if m else None


def fetch_org_repos(token):
    """Get all non-fork, non-archived repos in the org."""
    repos = []
    url = f"https://api.github.com/orgs/{ORG}/repos?per_page=100&type=public"
    while url:
        data, link = api_get(url, token)
        if data is None:
            break
        for r in data:
            if not r.get("fork") and not r.get("archived"):
                repos.append(r["full_name"])
        url = parse_next_url(link)
    repos.sort()
    return repos


def fetch_commits(repo, since, token):
    owner, name = repo.split("/")
    url = f"https://api.github.com/repos/{owner}/{name}/commits?since={since}&per_page=100&sha={get_default_branch(repo, token)}"
    all_commits = []
    page = 1
    while url:
        data, link = api_get(url, token)
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
        log(f"    Page {page}: {count} commits (total: {len(all_commits)})")
        url = parse_next_url(link)
        page += 1
    return all_commits


def get_default_branch(repo, token):
    data, _ = api_get(f"https://api.github.com/repos/{repo}", token)
    if data:
        return data.get("default_branch", "main")
    return "main"


def check_reviewed(commit, token):
    """Check if commit has a merged PR with a non-author approval.

    Returns True/False, or None if we couldn't check (rate limited).
    """
    repo = f"{ORG}/{commit['repo']}"
    sha = commit["sha"]
    author = commit["author_login"]

    # Find associated PRs
    prs, _ = api_get(
        f"https://api.github.com/repos/{repo}/commits/{sha}/pulls", token
    )
    if prs is None:
        return None

    for pr in prs:
        if pr.get("state") != "closed" or not pr.get("merged_at"):
            continue
        # Check reviews on this merged PR
        reviews, _ = api_get(
            f"https://api.github.com/repos/{repo}/pulls/{pr['number']}/reviews?per_page=100",
            token,
        )
        if reviews is None:
            return None
        for review in reviews:
            reviewer = review.get("user", {}).get("login", "")
            if review.get("state") == "APPROVED" and reviewer != author:
                return True
    return False


def load_store():
    if COMMITS_FILE.exists():
        return json.loads(COMMITS_FILE.read_text())
    return {"last_fetched": SINCE_DEFAULT, "commits": []}


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n")


def generate_leaderboard(commits):
    by_author = {}
    for c in commits:
        if not c.get("reviewed"):
            continue
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
        by_author[aid]["login"] = c["author_login"]
        by_author[aid]["avatar_url"] = c["avatar_url"]

    contributors = sorted(by_author.values(), key=lambda x: x["commits"], reverse=True)
    for entry in contributors:
        entry["repos"] = sorted(entry["repos"])
    return contributors


def main():
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        log("Using GITHUB_TOKEN for authentication")
    else:
        log("No GITHUB_TOKEN set — using unauthenticated requests (60 req/hr)")

    store = load_store()
    existing_shas = {c["sha"] for c in store["commits"]}
    since = store["last_fetched"]

    # Discover all repos
    log(f"Discovering {ORG} repos...")
    repos = fetch_org_repos(token)
    log(f"Found {len(repos)} repos: {', '.join(r.split('/')[1] for r in repos)}")

    # Fetch new commits from each repo
    total_added = 0
    for repo in repos:
        if rate_limited:
            break
        log(f"  Fetching {repo} since {since}")
        new_commits = fetch_commits(repo, since, token)
        added = 0
        for c in new_commits:
            if c["sha"] not in existing_shas:
                store["commits"].append(c)
                existing_shas.add(c["sha"])
                added += 1
        if added:
            log(f"    Added {added} new commits")
        total_added += added

    log(f"Total: {total_added} new commits ({len(store['commits'])} total)")

    # Check review status for commits that haven't been checked yet
    unchecked = [c for c in store["commits"] if "reviewed" not in c]
    if unchecked:
        log(f"Checking review status for {len(unchecked)} commits...")
        for i, c in enumerate(unchecked):
            if rate_limited:
                break
            result = check_reviewed(c, token)
            if result is None:
                break
            c["reviewed"] = result
            if (i + 1) % 50 == 0:
                log(f"    Checked {i + 1}/{len(unchecked)}")
                save_json(COMMITS_FILE, store)  # checkpoint
        checked = sum(1 for c in unchecked if "reviewed" in c)
        log(f"    Checked {checked}/{len(unchecked)}")

    store["last_fetched"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    save_json(COMMITS_FILE, store)

    reviewed = sum(1 for c in store["commits"] if c.get("reviewed"))
    pending = sum(1 for c in store["commits"] if "reviewed" not in c)
    log(f"Commits: {reviewed} reviewed, {len(store['commits']) - reviewed - pending} rejected, {pending} pending")

    contributors = generate_leaderboard(store["commits"])
    leaderboard = {
        "generated": store["last_fetched"],
        "contributors": contributors,
    }
    save_json(LEADERBOARD_FILE, leaderboard)
    log(f"Leaderboard: {len(contributors)} contributors")


if __name__ == "__main__":
    main()
