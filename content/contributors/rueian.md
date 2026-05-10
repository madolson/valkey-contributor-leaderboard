{
  "title": "rueian",
  "login": "rueian",
  "avatar_url": "https://avatars.githubusercontent.com/u/2727535?v=4",
  "score": 35,
  "commit_count": 8,
  "review_count": 27,
  "repos": [
    "valkey",
    "valkey-doc",
    "valkey-glide"
  ],
  "commit_list": [
    {
      "sha": "c6af7b1ba4",
      "message": "Update valkey-go's client_capa_redirect feature (#369)",
      "date": "2025-10-13",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/369",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/c6af7b1ba4faca99df13ae3e9627037543a1e6f1"
    },
    {
      "sha": "b0411b7e8b",
      "message": "Go: fix unsafe precondition violation for slice::from_raw_parts (#3351)",
      "date": "2025-03-17",
      "repo": "valkey-glide",
      "pr_url": "https://github.com/valkey-io/valkey-glide/pull/3351",
      "commit_url": "https://github.com/valkey-io/valkey-glide/commit/b0411b7e8b88d127da377c4ea583509366f9524a"
    },
    {
      "sha": "e516f0b38f",
      "message": "Go: fix data race on the coreClient with `sync.Mutex` and a channel map (#3236)",
      "date": "2025-02-28",
      "repo": "valkey-glide",
      "pr_url": "https://github.com/valkey-io/valkey-glide/pull/3236",
      "commit_url": "https://github.com/valkey-io/valkey-glide/commit/e516f0b38f52fda390928ab3783afdb32291377f"
    },
    {
      "sha": "6b46401130",
      "message": "Go: Fix channel passing from Go to Rust by using `runtime.Pinner` or `cgo.Handle` (#3208)",
      "date": "2025-02-25",
      "repo": "valkey-glide",
      "pr_url": "https://github.com/valkey-io/valkey-glide/pull/3208",
      "commit_url": "https://github.com/valkey-io/valkey-glide/commit/6b464011307c8c1bd3bdb645bfd6ebf2d337432a"
    },
    {
      "sha": "0a89571dcc",
      "message": "Skip logreqres on tests for the HELLO command (#1528)",
      "date": "2025-01-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1528",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0a89571dccc5ac007a9fbbda99c5e47dff615227"
    },
    {
      "sha": "dc4628d444",
      "message": "Add `availability_zone` to the HELLO command history (#1524)",
      "date": "2025-01-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1524",
      "commit_url": "https://github.com/valkey-io/valkey/commit/dc4628d444cdc871b2e009b8de523451d17c795a"
    },
    {
      "sha": "5453dd4814",
      "message": "Add availability_zone to the HELLO command documentation (#208)",
      "date": "2025-01-08",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/208",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/5453dd48146e73d77bdc2c5433c14e179515a3e9"
    },
    {
      "sha": "3b52186b6a",
      "message": "Add `availability_zone` to the HELLO response (#1487)",
      "date": "2025-01-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1487",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3b52186b6a6199884edf447c52828d5ca882142f"
    }
  ],
  "review_list": [
    {
      "sha": "15edca2217",
      "message": "Pin dependencies in GitHub Workflows and dockertest.sh (#132)",
      "date": "2026-05-09",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/132",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/15edca2217bb0141b439f0fefcfbbb4f53f75b91"
    },
    {
      "sha": "a87459a484",
      "message": "Call hmset from valkeycompat hmset (#128)",
      "date": "2026-04-18",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/128",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/a87459a484e11a689974834608ed6c267d4b5a06"
    },
    {
      "sha": "df9bebbb23",
      "message": "Make Pipeliner be a Cmdable instead of CoreCmdable (#126)",
      "date": "2026-04-11",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/126",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/df9bebbb2393a15bfe1f8da77a170eaa66f296fe"
    },
    {
      "sha": "227a6ba72f",
      "message": "Unify CacheCompat to use value receivers. (#120)",
      "date": "2026-03-08",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/120",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/227a6ba72ff619a454f1a7a85de6f3cc9a871b82"
    },
    {
      "sha": "833625daaf",
      "message": "fix: #111 #112 (#116)",
      "date": "2026-03-03",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/116",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/833625daafb092a1d617eb63b37951e14bfc93f0"
    },
    {
      "sha": "410437b7a8",
      "message": "feat(otel): Reduce cache hit/miss allocs (#117)",
      "date": "2026-02-26",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/117",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/410437b7a84fad672d5b0cf1716e260c40a26a51"
    },
    {
      "sha": "5fb014b365",
      "message": "style(gofix): Apply `go fix` (#115)",
      "date": "2026-02-22",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/115",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/5fb014b365197576961ac353727b41fd685d359b"
    },
    {
      "sha": "cd4d3d3466",
      "message": "feat(otel): Optimize metrics recording (#110)",
      "date": "2026-02-20",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/110",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/cd4d3d34664fd0456fd1b500e0b78097c7460e21"
    },
    {
      "sha": "96d12e3429",
      "message": "fix: race condition in Lua script SHA-1 loading (#108)",
      "date": "2026-02-02",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/108",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/96d12e3429ec743da635b175dba7a97d049ccdf1"
    },
    {
      "sha": "77aa0ab14c",
      "message": "feat: add ability to get AZ from an INFO command (#105)",
      "date": "2026-01-19",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/105",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/77aa0ab14c9481474f17e4a12e896b785c2b9911"
    },
    {
      "sha": "05f746de79",
      "message": "fix: valkeycompat NewAdapter sets maxp incorrectly (#102)",
      "date": "2025-12-31",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/102",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/05f746de793ffe435ba165f0feaae3141592d334"
    },
    {
      "sha": "d8b00ff9ee",
      "message": "Set `server.*` attrs in more cases (#95)",
      "date": "2025-12-19",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/95",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/d8b00ff9ee0a256d24612323746a66878f36ac71"
    },
    {
      "sha": "427e84058d",
      "message": "feat: Add MaxMovedRedirections option to prevent infinite redirect loops (#92)",
      "date": "2025-12-03",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/92",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/427e84058df04c8fa4f1da5739616b35b4b0aed0"
    },
    {
      "sha": "05bd542b17",
      "message": "Add atomic slot migration commands for Valkey 9.0 (#88)",
      "date": "2025-11-13",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/88",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/05bd542b17f33e2e813d8dc4b68678baf2c1e141"
    },
    {
      "sha": "b219bd1ace",
      "message": "Valkeyotel cache key pattern (#87)",
      "date": "2025-11-13",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/87",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/b219bd1acee4e13d1e413fd023b02d7f08d87fee"
    },
    {
      "sha": "183878e224",
      "message": "feat : add all Valkey 8.1/9.0 filters to CLIENT LIST and Client KILL (#83)",
      "date": "2025-10-04",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/83",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/183878e224665f20b85f8d0ad3d684ad6172cb45"
    },
    {
      "sha": "65c2a6a53a",
      "message": "feat: client capa redirect (#82)",
      "date": "2025-10-01",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/82",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/65c2a6a53a5fff0822f469b5e8cc6dacc143632f"
    },
    {
      "sha": "38ea07007f",
      "message": "fix redirections that happen for cmds with InitSlot (#80)",
      "date": "2025-09-24",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/80",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/38ea07007f052324423dbd19eb3c559d8110a281"
    },
    {
      "sha": "d4865cbdee",
      "message": "Support new DELIFEQ command #67 (#70)",
      "date": "2025-08-25",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/70",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/d4865cbdee31fe21eaebf5b567ee7aa3e8a60836"
    },
    {
      "sha": "0386cc0245",
      "message": "Update README.md to reflect algorithm used (#64)",
      "date": "2025-08-10",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/64",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/0386cc02456ee57c070f5da133acfd1a42191d01"
    },
    {
      "sha": "39c6d451c5",
      "message": "fix(pipeline): clear placeholder pipeline error after execution (#61)",
      "date": "2025-07-28",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/61",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/39c6d451c54fc107f6d670aeda8796af5f67d4bd"
    },
    {
      "sha": "021a1bafa8",
      "message": "Return a singleClient instance even when Dial fails if ForceSingleClient is true (#58)",
      "date": "2025-07-10",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/58",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/021a1bafa87cbc3928705ed1e962aedc121631e3"
    },
    {
      "sha": "bb44796393",
      "message": "docs: update valkeylock comment (#57)",
      "date": "2025-07-04",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/57",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/bb44796393dda0da3c5abd6d8a8d241adbd65cfb"
    },
    {
      "sha": "14a7de54d6",
      "message": "Spelling (#53)",
      "date": "2025-06-12",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/53",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/14a7de54d6daa157cc00115f621325186311ae42"
    },
    {
      "sha": "f68a678f7c",
      "message": "Ensure deterministic routing in _pickMulti and _pickMultiCache (#52)",
      "date": "2025-06-10",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/52",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/f68a678f7c413b13e6579e3ec30e554bf2cb224b"
    },
    {
      "sha": "6f8a56c05f",
      "message": "feat: update commands.json to forbid cross slots (#41)",
      "date": "2025-04-12",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/41",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/6f8a56c05fabe87c612f465eed97dccfbd74a274"
    },
    {
      "sha": "0afe1a355e",
      "message": "add linters go vet and staticcheck",
      "date": "2024-05-07",
      "repo": "valkey-go",
      "pr_url": "https://github.com/valkey-io/valkey-go/pull/7",
      "commit_url": "https://github.com/valkey-io/valkey-go/commit/0afe1a355e9eee0c850449286ad82918d8c39c61"
    }
  ]
}
