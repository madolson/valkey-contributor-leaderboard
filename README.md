# Valkey Contributor Leaderboard

A leaderboard tracking commits to [valkey-io/valkey](https://github.com/valkey-io/valkey) since the Redis→Valkey fork (March 28, 2024).

**Live site:** https://madolson.github.io/valkey-contributor-leaderboard/

## How it works

1. A Python script (`scripts/fetch_commits.py`) fetches commits from the GitHub API incrementally
2. Commit data is stored in `data/commits.json` and aggregated into `data/leaderboard.json`
3. Hugo builds a static site from the leaderboard data
4. GitHub Actions deploys to GitHub Pages daily

## Run locally

```bash
# Fetch commit data (uses GITHUB_TOKEN if set)
export GITHUB_TOKEN=ghp_...  # optional, increases rate limit
python3 scripts/fetch_commits.py

# Build and serve
brew install hugo
hugo server
```

## Adding more repos

The script supports a `--repo` flag:

```bash
python3 scripts/fetch_commits.py --repo valkey-io/valkey
python3 scripts/fetch_commits.py --repo valkey-io/valkey-glide
```

Each run appends to the same `data/commits.json`, and the leaderboard aggregates across all repos.

## License

BSD 3-Clause. See [LICENSE](LICENSE).
