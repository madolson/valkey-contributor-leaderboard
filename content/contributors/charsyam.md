{
  "title": "charsyam",
  "login": "charsyam",
  "avatar_url": "https://avatars.githubusercontent.com/u/439301?v=4",
  "score": 16,
  "commit_count": 15,
  "review_count": 1,
  "repos": [
    "valkey"
  ],
  "commit_list": [
    {
      "sha": "faec379ecd",
      "message": "Fix GEOSEARCH repeated BYPOLYGON memory leak (#4995)",
      "date": "2026-10-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/4995",
      "commit_url": "https://github.com/valkey-io/valkey/commit/faec379ecd35a9f9d333b2bf42667f5b4fa408c7"
    },
    {
      "sha": "e50b62d0bb",
      "message": "[correctness] Fix LSET modifying elements for out-of-range 64-bit indexes (#4823)",
      "date": "2026-10-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/4823",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e50b62d0bb33dedb0222f65ef36d9537f9e864ea"
    },
    {
      "sha": "e23cab1355",
      "message": "Optimize B+tree ZSCAN with item references and prefetch (#4856)",
      "date": "2026-10-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/4856",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e23cab13559a8950eadc19c6c88e7843e1136c51"
    },
    {
      "sha": "0704408262",
      "message": "aof: write directly to server.aof_buf in feedAppendOnlyFile (#3496)",
      "date": "2026-10-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3496",
      "commit_url": "https://github.com/valkey-io/valkey/commit/070440826261994f8133a2914010f16f821e2e09"
    },
    {
      "sha": "d379883ae8",
      "message": "Optimize B+tree ZPOP by detaching edge items (#4852)",
      "date": "2026-10-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/4852",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d379883ae8d7573a7f2b364f7d787643c3414731"
    },
    {
      "sha": "b3a1356376",
      "message": "Optimize infoCommand with SDS pre-allocation (#3413)",
      "date": "2026-10-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3413",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b3a13563766cecbf9d859c7641d1ed00bf75108e"
    },
    {
      "sha": "c79f17d251",
      "message": "zset: add in-place fast path for score updates in listpack encoding (#3491)",
      "date": "2026-09-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3491",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c79f17d251038cfb660a5ad836053d06d25d8342"
    },
    {
      "sha": "47b497e4e3",
      "message": "Fix stale MY_PRIMARY_FAIL gossip flag (#4533)",
      "date": "2026-09-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/4533",
      "commit_url": "https://github.com/valkey-io/valkey/commit/47b497e4e39a1b05f1244a30a134818d9f7b4a5c"
    },
    {
      "sha": "bb88665578",
      "message": "hashtable: fix dismissHashtable madvise size (#3533)",
      "date": "2026-04-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3533",
      "commit_url": "https://github.com/valkey-io/valkey/commit/bb88665578b8da8ef94e9b17d32859c25b09688d"
    },
    {
      "sha": "9709843446",
      "message": "Optimize HGETDEL to pause auto shrink when deleting multiple items (#3535)",
      "date": "2026-04-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3535",
      "commit_url": "https://github.com/valkey-io/valkey/commit/97098434463c4687f8ed1f4567717fea4c6bce21"
    },
    {
      "sha": "c4db208e9b",
      "message": "enhance raxLowWalk: use memchr() for child-edge lookup in non-compressed nodes (#3472)",
      "date": "2026-04-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3472",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c4db208e9b2c1d41b3a8c6db8a8b982df2dc11c0"
    },
    {
      "sha": "be52d8b81a",
      "message": "Fix trivial double-free issue in rdbLoadObject (#3453)",
      "date": "2026-04-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3453",
      "commit_url": "https://github.com/valkey-io/valkey/commit/be52d8b81a82b81d3b3482ff89236513d195e3b1"
    },
    {
      "sha": "2585f60ebc",
      "message": "Fix RDB expiry write length and leak when loading zipmap (#3422)",
      "date": "2026-04-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3422",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2585f60ebc93c7b44a23e4df9fb02f2012e185fd"
    },
    {
      "sha": "48277209b9",
      "message": "Fix valkey-cli memory leak (#2177)",
      "date": "2025-06-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2177",
      "commit_url": "https://github.com/valkey-io/valkey/commit/48277209b991253c4fa0e9a718b0651494708048"
    },
    {
      "sha": "b5e012a108",
      "message": "Fix invalid functionname processMultibulkBuffer typo in comments. (#2097)",
      "date": "2025-06-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2097",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b5e012a1083cbfda3ab27c6df3fc8d82534d6a80"
    }
  ],
  "review_list": [
    {
      "sha": "7c7436bfc9",
      "message": "Deflake Dual-channel load converges after primary repl-compression test (#4966)",
      "date": "2026-10-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/4966",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7c7436bfc909bd5cf2b3f52c8b4fb3e028265171"
    }
  ]
}
