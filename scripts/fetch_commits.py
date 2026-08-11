#!/usr/bin/env python3
"""Fetch commits from all valkey-io repos and generate leaderboard data.

Only counts commits that have an associated merged PR with at least one
approval from someone other than the commit author. Also tracks who
reviewed each commit to build a reviews leaderboard.
"""

import json
import os
import re
import shutil
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

SINCE_DEFAULT = "2024-03-28T00:00:00Z"
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
COMMITS_FILE = DATA_DIR / "commits.json"
LEADERBOARD_FILE = DATA_DIR / "leaderboard.json"
PROFILES_FILE = DATA_DIR / "profiles.json"
CONTRIBUTORS_DIR = ROOT_DIR / "content" / "contributors"
ORG = "valkey-io"

# Errors that apply to one resource only: empty repo (409), missing repo or
# deleted user (404), DMCA-blocked repo (451). Skip the resource, keep going.
SKIP_HTTP_CODES = (404, 409, 451)

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
        # Stop early to preserve rate limit for other CI steps
        remaining = int(resp.headers.get("X-RateLimit-Remaining", "999"))
        if remaining < 100:
            log(f"Rate limit low ({remaining} remaining). Saving partial results.")
            rate_limited = True
        return data, link
    except urllib.error.HTTPError as e:
        if e.code in (403, 429):
            log(f"Rate limited (HTTP {e.code}). Saving partial results.")
            rate_limited = True
            return None, ""
        if e.code in SKIP_HTTP_CODES:
            log(f"HTTP {e.code}: {e.reason} for {url}. Skipping.")
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


def get_default_branch(repo, token):
    data, _ = api_get(f"https://api.github.com/repos/{repo}", token)
    if data:
        return data.get("default_branch", "main")
    return "main"


def fetch_commits(repo, since, token):
    owner, name = repo.split("/")
    url = (f"https://api.github.com/repos/{owner}/{name}/commits"
           f"?since={since}&per_page=100&sha={get_default_branch(repo, token)}")
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
                "message": c["commit"]["message"].split("\n")[0],
                "date": c["commit"]["committer"]["date"],
                "repo": name,
            })
            count += 1
        log(f"    Page {page}: {count} commits (total: {len(all_commits)})")
        url = parse_next_url(link)
        page += 1
    return all_commits


def check_reviewed(commit, token):
    """Check if commit has a merged PR with a non-author approval.

    Returns (approvers, pr_url) or (None, None) on rate limit.
    approvers is a list of logins, or empty list if no approval.
    """
    repo = f"{ORG}/{commit['repo']}"
    sha = commit["sha"]
    author = commit["author_login"]

    prs, _ = api_get(
        f"https://api.github.com/repos/{repo}/commits/{sha}/pulls", token
    )
    if prs is None:
        return None, None

    for pr in prs:
        if pr.get("state") != "closed" or not pr.get("merged_at"):
            continue
        pr_url = pr.get("html_url", "")
        reviews, _ = api_get(
            f"https://api.github.com/repos/{repo}/pulls/{pr['number']}/reviews?per_page=100",
            token,
        )
        if reviews is None:
            return None, None
        approvers = []
        for review in reviews:
            reviewer = review.get("user", {}).get("login", "")
            if review.get("state") == "APPROVED" and reviewer != author:
                approvers.append({
                    "login": reviewer,
                    "date": review.get("submitted_at", ""),
                })
        if approvers:
            return approvers, pr_url
    return [], ""


def needs_review_check(commit):
    r = commit.get("reviewed")
    return r is None or r is True


def needs_detail_backfill(commit):
    """True if commit is missing message or pr_url fields."""
    return "message" not in commit or "pr_url" not in commit


def load_store():
    if COMMITS_FILE.exists():
        return json.loads(COMMITS_FILE.read_text())
    return {"last_fetched": SINCE_DEFAULT, "commits": []}


def load_profiles():
    if PROFILES_FILE.exists():
        return json.loads(PROFILES_FILE.read_text())
    return {}


def fetch_profiles(logins, profiles, token):
    """Fetch GitHub user profiles for logins not already cached."""
    new = [l for l in logins if l not in profiles]
    if not new:
        return
    log(f"Fetching {len(new)} user profiles...")
    for i, login in enumerate(new):
        if rate_limited:
            break
        data, _ = api_get(f"https://api.github.com/users/{login}", token)
        if data is None:
            if rate_limited:
                break
            # Account no longer exists. Cache an empty profile so we stop asking.
            profiles[login] = {"name": "", "company": ""}
            continue
        profiles[login] = {
            "name": data.get("name") or "",
            "company": (data.get("company") or "").strip().lstrip("@"),
        }
        if (i + 1) % 50 == 0:
            log(f"    Fetched {i + 1}/{len(new)} profiles")
            save_json(PROFILES_FILE, profiles)
    save_json(PROFILES_FILE, profiles)


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n")


def _reviewer_login(r):
    """Extract login from reviewer entry (str=old format, dict=new format)."""
    return r["login"] if isinstance(r, dict) else r


def _reviewer_month(r, fallback):
    """Month of the review itself; falls back to the commit month for entries
    recorded before review dates were stored."""
    if isinstance(r, dict) and r.get("date"):
        return r["date"][:7]
    return fallback


def month_range(start, end):
    """Inclusive list of YYYY-MM keys, so the UI gets a gapless timeline."""
    year, month = int(start[:4]), int(start[5:7])
    end_year, end_month = int(end[:4]), int(end[5:7])
    out = []
    while (year, month) <= (end_year, end_month):
        out.append(f"{year:04d}-{month:02d}")
        month += 1
        if month > 12:
            year, month = year + 1, 1
    return out


def generate_leaderboard(commits, profiles=None):
    """Return (contributors, months). Each contributor's per_repo maps
    repo -> {YYYY-MM: [commits, reviews]} so the site can filter by time."""
    profiles = profiles or {}
    by_login = {}
    seen_months = set()

    def is_bot(login):
        return "[bot]" in login or login in ("Copilot",)

    def ensure_user(login, avatar):
        if login not in by_login:
            p = profiles.get(login, {})
            by_login[login] = {
                "login": login, "id": 0,
                "avatar_url": avatar or f"https://github.com/{login}.png?size=64",
                "name": p.get("name", ""),
                "company": p.get("company", ""),
                "commits": 0, "reviews": 0,
                "per_repo": {},
            }
        if avatar:
            by_login[login]["avatar_url"] = avatar

    def bump(login, repo, month, idx):
        bucket = by_login[login]["per_repo"].setdefault(repo, {})
        bucket.setdefault(month, [0, 0])[idx] += 1
        seen_months.add(month)

    seen_prs = set()  # (author_login, pr_url) — dedup rebase-and-merge

    for c in commits:
        reviewers = c.get("reviewed")
        if not reviewers or not isinstance(reviewers, list):
            continue
        if is_bot(c["author_login"]):
            continue

        # Deduplicate: multiple commits from same PR count as one
        pr_url = c.get("pr_url", "")
        pr_key = (c["author_login"], pr_url) if pr_url else None
        if pr_key and pr_key in seen_prs:
            continue
        if pr_key:
            seen_prs.add(pr_key)

        author = c["author_login"]
        repo = c["repo"]
        month = c["date"][:7]

        ensure_user(author, c["avatar_url"])
        by_login[author]["id"] = c["author_id"]
        by_login[author]["commits"] += 1
        bump(author, repo, month, 0)
        for r in reviewers:
            reviewer_login = _reviewer_login(r)
            if is_bot(reviewer_login):
                continue
            ensure_user(reviewer_login, None)
            by_login[reviewer_login]["reviews"] += 1
            bump(reviewer_login, repo, _reviewer_month(r, month), 1)

    contributors = sorted(
        by_login.values(),
        key=lambda x: x["commits"] + x["reviews"],
        reverse=True,
    )
    for entry in contributors:
        entry["score"] = entry["commits"] + entry["reviews"]
        entry["per_repo"] = {
            repo: dict(sorted(buckets.items()))
            for repo, buckets in sorted(entry["per_repo"].items())
        }
        # Repos touched by either commits or reviews, matching what the site
        # counts when filters are applied.
        entry["repos"] = sorted(entry["per_repo"])
    months = month_range(min(seen_months), max(seen_months)) if seen_months else []
    return contributors, months


def generate_contributor_pages(commits, contributors):
    """Generate a markdown page per contributor with their commit/review details."""
    # Build per-user commit and review lists
    user_commits = {}  # login -> [commit_info]
    user_reviews = {}  # login -> [commit_info]

    seen_prs = set()

    for c in commits:
        reviewers = c.get("reviewed")
        if not reviewers or not isinstance(reviewers, list):
            continue

        pr_url = c.get("pr_url", "")
        pr_key = (c["author_login"], pr_url) if pr_url else None
        if pr_key and pr_key in seen_prs:
            continue
        if pr_key:
            seen_prs.add(pr_key)

        info = {
            "sha": c["sha"][:10],
            "message": c.get("message", c["sha"][:10]),
            "date": c["date"][:10],
            "repo": c["repo"],
            "pr_url": c.get("pr_url", ""),
            "commit_url": f"https://github.com/{ORG}/{c['repo']}/commit/{c['sha']}",
        }
        user_commits.setdefault(c["author_login"], []).append(info)
        for reviewer_login in (_reviewer_login(r) for r in reviewers):
            user_reviews.setdefault(reviewer_login, []).append(info)

    # Clean and regenerate
    if CONTRIBUTORS_DIR.exists():
        shutil.rmtree(CONTRIBUTORS_DIR)
    CONTRIBUTORS_DIR.mkdir(parents=True)

    # Write _index.md for the section
    (CONTRIBUTORS_DIR / "_index.md").write_text(
        "---\ntitle: Contributors\n---\n"
    )

    for entry in contributors:
        login = entry["login"]
        commits_list = sorted(
            user_commits.get(login, []), key=lambda x: x["date"], reverse=True
        )
        reviews_list = sorted(
            user_reviews.get(login, []), key=lambda x: x["date"], reverse=True
        )

        data = {
            "title": login,
            "login": login,
            "avatar_url": entry["avatar_url"],
            "score": entry["score"],
            "commit_count": entry["commits"],
            "review_count": entry["reviews"],
            "repos": entry["repos"],
            "commit_list": commits_list,
            "review_list": reviews_list,
        }

        # Write as JSON front matter so Hugo can access structured data
        page = json.dumps(data, indent=2) + "\n"
        (CONTRIBUTORS_DIR / f"{login}.md").write_text(page)

    log(f"Generated {len(contributors)} contributor pages")


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0,
                        help="Max total commits to check/backfill (0=unlimited)")
    args = parser.parse_args()

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
    log(f"Found {len(repos)} repos")

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

    # Check review status for commits that need it
    unchecked = [c for c in store["commits"] if needs_review_check(c)]
    if unchecked:
        if args.limit:
            unchecked = unchecked[:args.limit]
        log(f"Checking review status for {len(unchecked)} commits...")
        for i, c in enumerate(unchecked):
            if rate_limited:
                break
            approvers, pr_url = check_reviewed(c, token)
            if approvers is None:
                if rate_limited:
                    break
                continue
            c["reviewed"] = approvers if approvers else False
            c["pr_url"] = pr_url or ""
            if (i + 1) % 50 == 0:
                log(f"    Checked {i + 1}/{len(unchecked)}")
                save_json(COMMITS_FILE, store)
        checked = sum(1 for c in unchecked if not needs_review_check(c))
        log(f"    Checked {checked}/{len(unchecked)}")

    # Backfill message/pr_url for old commits that are missing them
    need_backfill = [c for c in store["commits"]
                     if needs_detail_backfill(c) and isinstance(c.get("reviewed"), list)]
    if need_backfill and not rate_limited:
        if args.limit:
            need_backfill = need_backfill[:args.limit]
        log(f"Backfilling details for {len(need_backfill)} commits...")
        for i, c in enumerate(need_backfill):
            if rate_limited:
                break
            repo = f"{ORG}/{c['repo']}"
            # Fetch commit detail for message
            if "message" not in c:
                detail, _ = api_get(
                    f"https://api.github.com/repos/{repo}/commits/{c['sha']}", token
                )
                if detail is None:
                    if rate_limited:
                        break
                    continue
                c["message"] = detail["commit"]["message"].split("\n")[0]
            # Fetch PR URL
            if "pr_url" not in c:
                prs, _ = api_get(
                    f"https://api.github.com/repos/{repo}/commits/{c['sha']}/pulls", token
                )
                if prs is None:
                    if rate_limited:
                        break
                    continue
                c["pr_url"] = ""
                for pr in prs:
                    if pr.get("merged_at"):
                        c["pr_url"] = pr.get("html_url", "")
                        break
            if (i + 1) % 50 == 0:
                log(f"    Backfilled {i + 1}/{len(need_backfill)}")
                save_json(COMMITS_FILE, store)
        backfilled = sum(1 for c in need_backfill if not needs_detail_backfill(c))
        log(f"    Backfilled {backfilled}/{len(need_backfill)}")

    # Only advance last_fetched if we're not rate-limited (got everything)
    if not rate_limited and not args.limit:
        store["last_fetched"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    save_json(COMMITS_FILE, store)

    reviewed = sum(1 for c in store["commits"] if isinstance(c.get("reviewed"), list))
    pending = sum(1 for c in store["commits"] if needs_review_check(c))
    log(f"Commits: {reviewed} reviewed, {pending} pending check")

    # Fetch user profiles (name, company) for leaderboard display
    profiles = load_profiles()
    all_logins = set()
    for c in store["commits"]:
        if isinstance(c.get("reviewed"), list):
            all_logins.add(c["author_login"])
            all_logins.update(_reviewer_login(r) for r in c["reviewed"])
    all_logins -= {l for l in all_logins if "[bot]" in l or l == "Copilot"}
    if not rate_limited:
        fetch_profiles(all_logins, profiles, token)

    contributors, months = generate_leaderboard(store["commits"], profiles)
    leaderboard = {
        "generated": store["last_fetched"],
        "months": months,
        "contributors": contributors,
    }
    save_json(LEADERBOARD_FILE, leaderboard)
    log(f"Leaderboard: {len(contributors)} contributors")

    generate_contributor_pages(store["commits"], contributors)


if __name__ == "__main__":
    main()
