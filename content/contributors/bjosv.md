{
  "title": "bjosv",
  "login": "bjosv",
  "avatar_url": "https://avatars.githubusercontent.com/u/60651423?v=4",
  "score": 248,
  "commit_count": 123,
  "review_count": 125,
  "repos": [
    "libvalkey",
    "valkey",
    "valkey-doc",
    "valkey-helm",
    "valkey-operator"
  ],
  "commit_list": [
    {
      "sha": "a2d8cf876a",
      "message": "Release valkey-operator 0.6.0 (#244)",
      "date": "2026-09-01",
      "repo": "valkey-helm",
      "pr_url": "https://github.com/valkey-io/valkey-helm/pull/244",
      "commit_url": "https://github.com/valkey-io/valkey-helm/commit/a2d8cf876aa81432e248a1ec3787098f7702c613"
    },
    {
      "sha": "4160d5470f",
      "message": "ci: remove unnecessary disk space reclaim from publish workflow (#384)",
      "date": "2026-08-18",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/384",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/4160d5470f8e07a097469f7aa004b0082813ab3b"
    },
    {
      "sha": "2c3d72c4db",
      "message": "CI: cache Go build outputs and drop redundant go mod tidy (#372)",
      "date": "2026-08-13",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/372",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/2c3d72c4db3fc14b57174905dd7c5f12ab4ba0e9"
    },
    {
      "sha": "2fc6fef3c0",
      "message": "ci: build multi-arch images natively to avoid QEMU emulation (#366)",
      "date": "2026-08-13",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/366",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/2fc6fef3c0cef422b8ddb72e2c690d190dae378e"
    },
    {
      "sha": "a7fa7bb8c7",
      "message": "fix: set version/branch labels in valkey_operator_build_info metric (#336)",
      "date": "2026-07-27",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/336",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/a7fa7bb8c7751bcac442c1b1540a284876ac3652"
    },
    {
      "sha": "3f2444a224",
      "message": "Add option to attach an adapter in valkeyAsyncConnectWithOptions() (#331)",
      "date": "2026-07-23",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/331",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/3f2444a224294089589af82637e069a499fd4bd3"
    },
    {
      "sha": "1f741666d8",
      "message": "docs: rewrite dev.guide for local runs using kind and add macOS support (#193)",
      "date": "2026-07-15",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/193",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/1f741666d8327498db5e09caf90ab72cfbe564e9"
    },
    {
      "sha": "4bb5ea6cb7",
      "message": "Fix async command timeout never firing under continuous writes (#328)",
      "date": "2026-06-29",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/328",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/4bb5ea6cb7fedfd0da70661efaedba0f93243c8f"
    },
    {
      "sha": "248d7f5ce3",
      "message": "Add c-ares support for DNS resolution with timeout (#323)",
      "date": "2026-06-24",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/323",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/248d7f5ce3ef4ce006d1dec0b04bd24fdf37c9f5"
    },
    {
      "sha": "b64aa06988",
      "message": "Suppress constant-promotion warnings on Solaris Sun CC (#326)",
      "date": "2026-06-23",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/326",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/b64aa06988a1afc33fa97e9ce5aaaba71bc027f5"
    },
    {
      "sha": "6249038b07",
      "message": "Replace strncpy with length-validated memcpy for Unix socket path (#327)",
      "date": "2026-06-23",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/327",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/6249038b0794b85bc480a71639f96e5a36965a9f"
    },
    {
      "sha": "2cdedcf710",
      "message": "Fix unused variable warnings in rdma.c with NDEBUG (#312)",
      "date": "2026-06-23",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/312",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/2cdedcf710d9739b7b2f1b2237587bd23c8d4a9b"
    },
    {
      "sha": "3e068f0a3e",
      "message": "fix: roll primaries shard-by-shard during rolling update without persistence (#252)",
      "date": "2026-06-18",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/252",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/3e068f0a3e18b47f038d07a4948c0b43c5c849af"
    },
    {
      "sha": "cebde2510d",
      "message": "fix: recover cluster when majority of primaries are lost (#244)",
      "date": "2026-06-17",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/244",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/cebde2510d38dd51817865baa2b608142cb59278"
    },
    {
      "sha": "dd70f1cee6",
      "message": "Filter Secrets by managed-by label to reduce cache memory usage (#238)",
      "date": "2026-06-11",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/238",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/dd70f1cee6309eb99edf3a9c662adb6fecac8bae"
    },
    {
      "sha": "3c72d4a181",
      "message": "fix: disable replica migration and validity factor in cluster config (#222)",
      "date": "2026-06-07",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/222",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/3c72d4a1816e5a5dfa066ca6831abedc1ed641b6"
    },
    {
      "sha": "45f0074b0f",
      "message": "Fix issues in valkeyClusterAsyncCallback (#306)",
      "date": "2026-06-05",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/306",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/45f0074b0f0a55a035891b4df4d5ce871457be28"
    },
    {
      "sha": "6be74d2ebb",
      "message": "fix: rolling update loses all keys when replicas are not synced (#208)",
      "date": "2026-06-02",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/208",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/6be74d2ebbbab4f1ec982a7464d36c9c6a36d3f0"
    },
    {
      "sha": "37421b7157",
      "message": "fix: check primary node first when resolving shard index (#207)",
      "date": "2026-05-31",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/207",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/37421b715702b102a972fff4408e3d75a7287318"
    },
    {
      "sha": "6e04a99e03",
      "message": "Set config epoch on new nodes before MEET to prevent slot loss (#197)",
      "date": "2026-05-27",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/197",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/6e04a99e03cb42f455893ca66b349f11d24d985d"
    },
    {
      "sha": "f7f193738f",
      "message": "fix: handle fragmented slot ranges in assignSlotsToPendingPrimaries (#196)",
      "date": "2026-05-26",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/196",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/f7f193738ffb4716df6a2d4cd32e804bdc077c3a"
    },
    {
      "sha": "6985556263",
      "message": "Filter informer cache to operator-managed resources only (#194)",
      "date": "2026-05-26",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/194",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/6985556263b6d60d9ba5fc014bb2963012ce1306"
    },
    {
      "sha": "8421ca3426",
      "message": "fixup: update chart version and add changelog file",
      "date": "2026-05-14",
      "repo": "valkey-helm",
      "pr_url": "https://github.com/valkey-io/valkey-helm/pull/174",
      "commit_url": "https://github.com/valkey-io/valkey-helm/commit/8421ca342657efa3bbec12cf01c1bbd7ef6e3b32"
    },
    {
      "sha": "fdf13ca0de",
      "message": "Update deps/libvalkey to version 0.5.0 (#3697)",
      "date": "2026-05-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3697",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fdf13ca0def87dd31bf29c0b2be4021d8d9ad7b4"
    },
    {
      "sha": "afc8294635",
      "message": "Fix intermittent test failures due to the toleration test (#170)",
      "date": "2026-05-11",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/170",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/afc8294635b9abbaa9cbea76a889f5293c3068cf"
    },
    {
      "sha": "311cb25412",
      "message": "Delete old events in BeforeSuite to prevent stale event assertions (#169)",
      "date": "2026-05-11",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/169",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/311cb254125db76723c7fbe5a78abab164242cba"
    },
    {
      "sha": "d2b80dc111",
      "message": "Fix flaky metrics exporter test by waiting for cluster Ready (#173)",
      "date": "2026-05-11",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/173",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/d2b80dc111e8784774ce96855b075c25e5295df1"
    },
    {
      "sha": "b272a09c86",
      "message": "[docs] Add quickstart guide and restructure README for v0.1.0 (#155)",
      "date": "2026-05-11",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/155",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/b272a09c867a341f4d224ab815b5a6c66bdafb67"
    },
    {
      "sha": "6eecd591bc",
      "message": "Use status patch to eliminate resource version conflicts (#171)",
      "date": "2026-05-11",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/171",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/6eecd591bc3d070bb7ba9335866e0ab26edd064b"
    },
    {
      "sha": "cd3d5d8ff9",
      "message": "Fix potential heap-buffer-overflow in cluster error reply parsing (#305)",
      "date": "2026-04-22",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/305",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/cd3d5d8ff9a302099e7884da46427b96b8ece607"
    },
    {
      "sha": "32c7c5d094",
      "message": "Refactor error handling to use valkeySetErrorFromErrno and valkeyClearError (#303)",
      "date": "2026-04-20",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/303",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/32c7c5d09431800763013a369748d6dfe75ee3f1"
    },
    {
      "sha": "61b27c4530",
      "message": "Try all addresses from DNS before failing to connect (#300)",
      "date": "2026-04-16",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/300",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/61b27c4530f12b305d2a807babeb6be62e5d383c"
    },
    {
      "sha": "c5c54ac1d0",
      "message": "Correcting controller-gen version in valkeynodes.valkey.io (#112)",
      "date": "2026-03-11",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/112",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/c5c54ac1d0ce659c54a4fc334ed7c01aa83fba02"
    },
    {
      "sha": "04fb400765",
      "message": "Add additional checks in CI (#109)",
      "date": "2026-03-11",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/109",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/04fb4007650c8ac19687f296e2adb5a245cc8641"
    },
    {
      "sha": "747af1a85d",
      "message": "Use ar archiver installed by brew in CI `build-macos-latest` (#3317)",
      "date": "2026-03-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3317",
      "commit_url": "https://github.com/valkey-io/valkey/commit/747af1a85d6c1d43a749c59238a19d5b4b25e343"
    },
    {
      "sha": "24b67843ac",
      "message": "Update deps/libvalkey to version 0.4.0 (#3216)",
      "date": "2026-02-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3216",
      "commit_url": "https://github.com/valkey-io/valkey/commit/24b67843ac5ef3b9d21e0a2ffdc757271c6a88bc"
    },
    {
      "sha": "9a724fb61e",
      "message": "Split e2e-tests to separate files (#80)",
      "date": "2026-02-06",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/80",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/9a724fb61e4af19254f88d4165795eec82a2d3b6"
    },
    {
      "sha": "110b830790",
      "message": "Upgrade kubebuilder scaffolding from v4.10.1 to v4.11.0 (#71)",
      "date": "2026-02-01",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/71",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/110b83079078eb5fe046a309449aaf66cc44bf43"
    },
    {
      "sha": "8f9051ae0a",
      "message": "Correcting command parser bug (#277)",
      "date": "2026-01-23",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/277",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/8f9051ae0aa19305b710f5f2675ec172a6a1261b"
    },
    {
      "sha": "31aa8c8aaf",
      "message": "fixup: do not run CI-job solaris-developer-studio on external PRs",
      "date": "2026-01-20",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/272",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/31aa8c8aaf15882439e8d4b828926368868a3b52"
    },
    {
      "sha": "e052508b7a",
      "message": "Add rudimentary reconciliation using Deployment (#24)",
      "date": "2025-12-15",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/24",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/e052508b7aee3e18ba928b7b965c30b8724ecd0c"
    },
    {
      "sha": "43739cb337",
      "message": "Move exporter options to own sub-category in the ValkeyCluster CRD (#23)",
      "date": "2025-12-02",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/23",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/43739cb337f6e9ad59e249c9ad0d70785b261ece"
    },
    {
      "sha": "ae341dea5f",
      "message": "Support slotmap updates using CLUSTER NODES in RESP3 (#262)",
      "date": "2025-11-25",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/262",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/ae341dea5f11fced6e1f835a9988154fd898177c"
    },
    {
      "sha": "d3bf87c949",
      "message": "Correcting the RESP3 reply type on commands returning a verbatim string (#384)",
      "date": "2025-11-25",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/384",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/d3bf87c949709e20a41961ccdde045424a500868"
    },
    {
      "sha": "9c7867fb4e",
      "message": "Upgrade kubebuilder scaffolding from v4.9.0 to v4.10.1 (#21)",
      "date": "2025-11-21",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/21",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/9c7867fb4e3d383958b463b59d77725c719bc578"
    },
    {
      "sha": "5bed44d697",
      "message": " Fix linker errors when building with Makefile and `--no-undefined` (#250)",
      "date": "2025-10-20",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/250",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/5bed44d697741a1a8f6b8133b60c24296bc799cd"
    },
    {
      "sha": "76b275773f",
      "message": "Add initial developer guide documentation (#6)",
      "date": "2025-10-17",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/6",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/76b275773f4a0cbda502aba6aea47a5291a52577"
    },
    {
      "sha": "15974930d7",
      "message": "Add option to select a logical database (#244)",
      "date": "2025-10-01",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/244",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/15974930d7a43d6fdf9146b932b5432f448416c1"
    },
    {
      "sha": "2db4eeb1fc",
      "message": "Remove temporary build correction for RDMA and libvalkey 0.1.0",
      "date": "2025-08-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2534",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2db4eeb1fcd8316a792476c3023e705be24fdd70"
    },
    {
      "sha": "a449f0ea18",
      "message": "Don't expose internal functions in shared libraries (#205)",
      "date": "2025-06-27",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/205",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/a449f0ea188d61448a6b726341d32df74af53e4e"
    },
    {
      "sha": "178e350c75",
      "message": "Cluster code cleanup (#216)",
      "date": "2025-06-10",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/216",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/178e350c757a15fdbe1ded697a4f051baf0388df"
    },
    {
      "sha": "99aa158bcb",
      "message": "Use existing connections for blocking slotmap updates (#199)",
      "date": "2025-05-23",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/199",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/99aa158bcbacadd6c39992fdbd523aea43570abf"
    },
    {
      "sha": "41c5911f11",
      "message": "Remove macro UNUSED from public API (#200)",
      "date": "2025-05-14",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/200",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/41c5911f114e2a5fad058d6075f0a4195e3d941d"
    },
    {
      "sha": "969a8c546a",
      "message": "Fix dependency issue with RDMA (#201)",
      "date": "2025-05-09",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/201",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/969a8c546af28993f03ab6ba00744697de716fc1"
    },
    {
      "sha": "b5c7743971",
      "message": "Replace dependency `hiredis` with `libvalkey` (#2032)",
      "date": "2025-05-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2032",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b5c7743971df5476acbdbbbd3b378496e885e1e4"
    },
    {
      "sha": "abcd27fbf6",
      "message": "Support additional client options in a cluster client (#197)",
      "date": "2025-04-30",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/197",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/abcd27fbf62a044dce5da5255d8a161a99af23fb"
    },
    {
      "sha": "a31021bd52",
      "message": "Update and unify version tags on installed shared libraries (#196)",
      "date": "2025-04-30",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/196",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/a31021bd5224adfa4a72bf36c765372b4a818f45"
    },
    {
      "sha": "8ea7226ab5",
      "message": "Correcting the connect callback in examples",
      "date": "2025-04-29",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/195",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/8ea7226ab509ef65ce1bfe1d8b0f07e9dea27866"
    },
    {
      "sha": "89b6b5418d",
      "message": "Minor corrections in tests and build of tests. (#193)",
      "date": "2025-04-28",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/193",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/89b6b5418d2fa318aa5527774fd9fc53e8e48fc8"
    },
    {
      "sha": "5e212e6dab",
      "message": "Support empty endpoints in redirects (#160)",
      "date": "2025-04-25",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/160",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/5e212e6dab44c148ec76c8936415fb86dc1a0692"
    },
    {
      "sha": "aad85cbf8e",
      "message": "Output failure log when a test fails in CMake builds",
      "date": "2025-04-11",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/190",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/aad85cbf8e0688cb92c95a05623ce9fed3ab1260"
    },
    {
      "sha": "0b10912ad3",
      "message": "Update the nodeIterator memory blob to fit Valkeys dict iterator",
      "date": "2025-04-02",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/182",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/0b10912ad334e22e0dcbde172b413b0f8fdbabc2"
    },
    {
      "sha": "517e6264bb",
      "message": "Update minimum required CMake version (#181)",
      "date": "2025-03-21",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/181",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/517e6264bb14ec330baee3bba311cca2549e0718"
    },
    {
      "sha": "0b569b6882",
      "message": "Fix Coverity warnings (#179)",
      "date": "2025-03-17",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/179",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/0b569b6882ed501e8de00d4b3d9305af9a581d44"
    },
    {
      "sha": "136ede057c",
      "message": "Refactor `dict` (#173)",
      "date": "2025-03-06",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/173",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/136ede057c1088be5ca87c20a9fb32c8ac877aae"
    },
    {
      "sha": "64153055ec",
      "message": "Remove APIs for separate init and connect of async cluster contexts (#165)",
      "date": "2025-02-07",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/165",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/64153055ecfadef6c8d790051e8b8861a81225f0"
    },
    {
      "sha": "0101cf6276",
      "message": "Introduce configuration options in the cluster API (#137)",
      "date": "2025-02-03",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/137",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/0101cf6276189eec7e5202652219b46e72c31fd1"
    },
    {
      "sha": "fb8af4c786",
      "message": "Retry when an async slotmap update fails  (#159)",
      "date": "2025-01-23",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/159",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/fb8af4c786c073a64264ccb478364e85502aca64"
    },
    {
      "sha": "c793fa15db",
      "message": "Handle empty addresses in `CLUSTER NODES` responses (#148)",
      "date": "2025-01-15",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/148",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/c793fa15db433c7b9403e4cbb8c6445016e4e3ec"
    },
    {
      "sha": "ca3dac9ac7",
      "message": "Simplify API by only using non-const connect callbacks (#142)",
      "date": "2024-12-30",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/142",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/ca3dac9ac7a45998d8c9c51d236b7214fdfa59c6"
    },
    {
      "sha": "ea72f483d4",
      "message": "Rename offensive defines and members in API (#140)",
      "date": "2024-12-18",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/140",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/ea72f483d475af44d2399807bc01caab919a89de"
    },
    {
      "sha": "6f2ba3af0e",
      "message": " Refactor the internal function `parse_cluster_nodes` (#119)",
      "date": "2024-10-28",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/119",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/6f2ba3af0e59630abbe890704a3dbff76554b21a"
    },
    {
      "sha": "c95220a927",
      "message": "Create request list when initiating valkeyClusterContext",
      "date": "2024-10-23",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/123",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/c95220a927ede9dd1fa69f40faaa1d3abd7be890"
    },
    {
      "sha": "0985c622b0",
      "message": "Remove API valkeyClusterSetOptionAddNode",
      "date": "2024-10-22",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/122",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/0985c622b0c004365e452fce79e5b644026dd016"
    },
    {
      "sha": "a97a74e832",
      "message": "Add unit tests for `CLUSTER NODES` parsing (#112)",
      "date": "2024-10-14",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/112",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/a97a74e8320447d0373846be806b8405f61a8b8e"
    },
    {
      "sha": "732e25f62b",
      "message": "Install the Valkey package when available in CI",
      "date": "2024-10-13",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/115",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/732e25f62b39726ae7cd9428e7f2ec013bc39fca"
    },
    {
      "sha": "daf8537092",
      "message": "Modify the `nodeIterator` layout and update CI (#114)",
      "date": "2024-10-11",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/114",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/daf8537092e49e2518e4a744aa9e69c3ae98e21b"
    },
    {
      "sha": "21b08270c1",
      "message": "Check for null pointer in dictRelease, listRelease and cluster_slot_destroy (#113)",
      "date": "2024-10-10",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/113",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/21b08270c1b6673db3d430ff0955cf790f71b818"
    },
    {
      "sha": "432f689663",
      "message": "Remove `dict` from user-facing API (#87)",
      "date": "2024-10-09",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/87",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/432f6896630e45be07496aef1efbb971bb120a38"
    },
    {
      "sha": "761cbf4348",
      "message": "Use -std=c99 when building with CMake",
      "date": "2024-10-07",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/108",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/761cbf4348ecb65b635deb242d3017c4e6b3240f"
    },
    {
      "sha": "1d9e49c2e3",
      "message": "Refactor slotmap update functions (#107)",
      "date": "2024-10-04",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/107",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/1d9e49c2e38b4eae9a436efaddfc3541293e32ed"
    },
    {
      "sha": "952b59b0db",
      "message": "Event adapter corrections (#106)",
      "date": "2024-10-01",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/106",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/952b59b0dbad99a578b919c3504760b8ac7ca127"
    },
    {
      "sha": "1c57bf667a",
      "message": "Replace the term SSL with TLS (#103)",
      "date": "2024-09-26",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/103",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/1c57bf667af3d1e4c4ddd025c4ea0e404b17eb98"
    },
    {
      "sha": "a79c56494a",
      "message": "Cleanup of SSL init function in cluster context",
      "date": "2024-09-25",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/102",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/a79c56494a7a165df2e70b84897e68748fdc794a"
    },
    {
      "sha": "98be43b72d",
      "message": "Add a source code spellchecker to CI  (#101)",
      "date": "2024-09-25",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/101",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/98be43b72d383adf61348248de9b177bc17c49cb"
    },
    {
      "sha": "2e605df183",
      "message": "Use Valkey 7.2.5 in CI for macOS",
      "date": "2024-09-24",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/100",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/2e605df18343e837ad545e19ada1fb06f3dc5adf"
    },
    {
      "sha": "9c181fbbe1",
      "message": "Add a CMake build with type=Debug to CI",
      "date": "2024-09-20",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/95",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/9c181fbbe1d72baccce4d75937a5e7c383b5ae7e"
    },
    {
      "sha": "47956fa9b6",
      "message": "Enable Coverity scans in CI",
      "date": "2024-09-16",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/94",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/47956fa9b6ae248e9569eb101786f3a2d3d74ee7"
    },
    {
      "sha": "fbbf80ecbd",
      "message": "Cleanup of cluster internal error functions",
      "date": "2024-09-13",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/93",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/fbbf80ecbd39d66c5d67ce5610ffaf26015de372"
    },
    {
      "sha": "5f59243e2b",
      "message": "Add sanitizers to CI and fix a found test issue (#92)",
      "date": "2024-09-11",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/92",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/5f59243e2b5374d5f141a9ead7a08bb04d5100c5"
    },
    {
      "sha": "f3217e2605",
      "message": "Cleanup of cluster free functions",
      "date": "2024-09-10",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/91",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/f3217e260549a53f8961cd7873ac4dd4a2dc5e82"
    },
    {
      "sha": "8bfb414bee",
      "message": "Make ssl.h include order independant",
      "date": "2024-09-08",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/88",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/8bfb414bee0aa8426677efbb0541450915257f50"
    },
    {
      "sha": "01c226ecd6",
      "message": "Add initial migration guide (#85)",
      "date": "2024-09-05",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/85",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/01c226ecd660bf0a3348c143bd233c2ba842237d"
    },
    {
      "sha": "5bb15a9136",
      "message": "Remove `sds` from user-facing API  (#86)",
      "date": "2024-09-04",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/86",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/5bb15a91366d6b491a8c083021d4274ca1f0086e"
    },
    {
      "sha": "207b95ce12",
      "message": "Rename APIs to get a standalone context from the cluster context",
      "date": "2024-09-03",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/38",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/207b95ce12811afbdb54cd92df68ab76b341b26d"
    },
    {
      "sha": "39c564d75b",
      "message": "Move missing information from libvalkey/README.md",
      "date": "2024-09-02",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/83",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/39c564d75be8a66c08c38707a235a8557a61f147"
    },
    {
      "sha": "e01e63c4b0",
      "message": "Add initial CONTRIBUTING.md (#82)",
      "date": "2024-08-30",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/82",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/e01e63c4b011e8f91b7047d73b307617d7fabc84"
    },
    {
      "sha": "e5bd195a70",
      "message": "Enable release-drafter in CI",
      "date": "2024-08-30",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/81",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/e5bd195a7076e7f01e758cd94aac7341dc765555"
    },
    {
      "sha": "1ce574c28e",
      "message": "Add initial cluster docs (#80)",
      "date": "2024-08-28",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/80",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/1ce574c28ecf137329a410381ce03c453616a9f9"
    },
    {
      "sha": "71dc8a49b7",
      "message": "Fix build issues with Qt adapter example",
      "date": "2024-08-26",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/76",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/71dc8a49b7102e8532d1c907571390943ffb8f86"
    },
    {
      "sha": "1afa9a67c1",
      "message": "No slot map updates during a cluster client disconnect",
      "date": "2024-08-23",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/73",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/1afa9a67c1c3064179a304fda56001433f6529d4"
    },
    {
      "sha": "6cfbdb2506",
      "message": "Fix possible leak when failing to send a async cluster command (#71)",
      "date": "2024-08-23",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/71",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/6cfbdb250669fdb724b7913a3c8becb18777a8f1"
    },
    {
      "sha": "219a129fb0",
      "message": "Add file COPYING (#75)",
      "date": "2024-08-22",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/75",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/219a129fb0a83cd54ddbd6963d5bc36a42eff283"
    },
    {
      "sha": "2561649589",
      "message": "Remove non-working support for building a NuGet package",
      "date": "2024-08-21",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/74",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/2561649589d17dc002e7b8001a89c524000084e3"
    },
    {
      "sha": "0cbffcfd3e",
      "message": "Add new APIs for variadic cluster commands",
      "date": "2024-08-19",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/70",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/0cbffcfd3ea87d8ec8fbd6c16ca9b14ab4ac8802"
    },
    {
      "sha": "ba319233f5",
      "message": "Converge the warning-flags in Makefile and CMake builds     (#67)",
      "date": "2024-08-14",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/67",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/ba319233f5d139d8c345977747296d91fa0b0692"
    },
    {
      "sha": "e861276818",
      "message": "CI corrections (#60)",
      "date": "2024-08-02",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/60",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/e861276818e2ad4c1248ccf5ddb2ba0a98463b23"
    },
    {
      "sha": "ec4fff9e29",
      "message": "Use SSL when verifying an installation in CI",
      "date": "2024-08-02",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/59",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/ec4fff9e290d99809f4cbb57fe44e1cc2ea8436e"
    },
    {
      "sha": "2e4e6e692a",
      "message": "Replace CentOS7 with AlmaLinux 8 in CI",
      "date": "2024-07-31",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/58",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/2e4e6e692a2342fa7fde514de4be865ecc44f504"
    },
    {
      "sha": "7e361d6f38",
      "message": "Cleanup of unused and superfluous code in `src/vkutil.*` (#41)",
      "date": "2024-07-01",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/41",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/7e361d6f3810684c6b364db4383172ed2d4e1b4b"
    },
    {
      "sha": "a5b7e1da13",
      "message": "Fix ISO C naming violations of function names and header guards (#21)",
      "date": "2024-07-01",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/21",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/a5b7e1da1393a0a747da570280c0749be62e915e"
    },
    {
      "sha": "ac0991314d",
      "message": "Refactor the parsing of a key in a command (#37)",
      "date": "2024-07-01",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/37",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/ac0991314d48855dc73547d3fd946df42e717b4a"
    },
    {
      "sha": "899ac88182",
      "message": "Remove support for splitting multi-key commands per slot (#23)",
      "date": "2024-06-28",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/23",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/899ac88182473ff9ff0f587f1aeb0ab24a2703d6"
    },
    {
      "sha": "a84615c8bd",
      "message": "Pin Github Action versions in CI  (#34)",
      "date": "2024-06-28",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/34",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/a84615c8bdfef135bb8a7f0744c07b08bddca748"
    },
    {
      "sha": "e82b06890f",
      "message": "Remove parsing of unused cluster slot information (#25)",
      "date": "2024-06-27",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/25",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/e82b06890feb407d1e050d4bb3e0167a88f9f1bf"
    },
    {
      "sha": "fd3358b717",
      "message": "Fix issues in CI (#32)",
      "date": "2024-06-27",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/32",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/fd3358b71718c3b1b1c88a988ea2c81bf5c7298e"
    },
    {
      "sha": "53015864c9",
      "message": "Add installation tests to CI (#30)",
      "date": "2024-06-26",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/30",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/53015864c9257c9a0564f1f75b59a227ee87617e"
    },
    {
      "sha": "cdd5d81236",
      "message": "Move libvalkeycluster examples to new file structure (#28)",
      "date": "2024-06-26",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/28",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/cdd5d812362c1418fc6022e623c3db99b573933c"
    },
    {
      "sha": "4b601d9fe3",
      "message": "Fix CI issues (#29)",
      "date": "2024-06-26",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/29",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/4b601d9fe34b21d3a41d747c8cb64ce810ef971a"
    },
    {
      "sha": "8cd807df5f",
      "message": "Move remaining tests and build/run all legacy tests using CMake (#26)",
      "date": "2024-06-25",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/26",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/8cd807df5f423741947fddcac1373bfc15a64683"
    },
    {
      "sha": "f3776bd781",
      "message": "Rebranding of code in libvalkeycluster (#15)",
      "date": "2024-06-20",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/15",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/f3776bd7818035ba4c6f330894b94456f5fb5981"
    },
    {
      "sha": "39d4b43d4b",
      "message": "Pin versions of Github Actions in CI (#221)",
      "date": "2024-05-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/221",
      "commit_url": "https://github.com/valkey-io/valkey/commit/39d4b43d4beba0b656929a09d48ade662f52edf9"
    },
    {
      "sha": "1c282a9306",
      "message": "Set permissions for Github Actions in CI (#312)",
      "date": "2024-04-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/312",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1c282a9306b6623ae258f365d1b759fdd4a4ade9"
    }
  ],
  "review_list": [
    {
      "sha": "d8fef4a59e",
      "message": "(feat) version gating initial support  (#307)",
      "date": "2026-09-04",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/307",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/d8fef4a59e2cc69632538d31f2b63447d06df28c"
    },
    {
      "sha": "7c3b716ad6",
      "message": "feat: discovery preferredEndpointType and headless serviceName (#378)",
      "date": "2026-09-02",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/378",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/7c3b716ad67c4802a9625fe1e03b01df090db798"
    },
    {
      "sha": "9f541b24fe",
      "message": "fix: use workloadRevision for determining proactive failover (#402)",
      "date": "2026-08-27",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/402",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/9f541b24fe1d09e51547306ded562ea27f6714ba"
    },
    {
      "sha": "626ca51469",
      "message": "fix: generate the commands.allow/deny pattern and widen it to what Valkey accepts (#398)",
      "date": "2026-08-26",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/398",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/626ca5146914beea8013f4b8eee988cb0806e1d0"
    },
    {
      "sha": "c33988f583",
      "message": "feat: gate ACLApplied on an ACL revision user so permission edits are honest (#382)",
      "date": "2026-08-18",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/382",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/c33988f58364d6850380cabd926871d5f39d6c45"
    },
    {
      "sha": "79866214ad",
      "message": "test(e2e): assert cluster teardown against the cluster the spec deletes (#379)",
      "date": "2026-08-18",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/379",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/79866214ad3affee9f6867e4760514848ccd739f"
    },
    {
      "sha": "5676fb960e",
      "message": "fix: skip reconciliation while ValkeyCluster is being deleted (#374)",
      "date": "2026-08-13",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/374",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/5676fb960e788360b41bd0dbc85e61d7ce5654fd"
    },
    {
      "sha": "dd2d78213a",
      "message": "Merge pull request #240 from valkey-io/jdheyburn/valkey-operator-0.5",
      "date": "2026-08-11",
      "repo": "valkey-helm",
      "pr_url": "https://github.com/valkey-io/valkey-helm/pull/240",
      "commit_url": "https://github.com/valkey-io/valkey-helm/commit/dd2d78213ae4e7b229074d473612999c7324d9be"
    },
    {
      "sha": "c34252e6e9",
      "message": "Update UPGRADE.md",
      "date": "2026-08-11",
      "repo": "valkey-helm",
      "pr_url": "https://github.com/valkey-io/valkey-helm/pull/240",
      "commit_url": "https://github.com/valkey-io/valkey-helm/commit/c34252e6e97efbc89626f8fb0abcb520e431078e"
    },
    {
      "sha": "59b39e4039",
      "message": "feat: add scheduling.zone.pinning (#344)",
      "date": "2026-08-10",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/344",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/59b39e4039d1e45cae65457bc2a9299d95c877b2"
    },
    {
      "sha": "6fbed7fa74",
      "message": "test(e2e): add shutdown-on-sigterm failover test (#295)",
      "date": "2026-08-09",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/295",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/6fbed7fa7442fd97074eb0b09b31b8b49e9e0db4"
    },
    {
      "sha": "709bf5380a",
      "message": "feat: stage pod template rolls via Spec.WorkloadRevision (#338)",
      "date": "2026-08-05",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/338",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/709bf5380a1d0ddd2e47b17358fbbe43283144cc"
    },
    {
      "sha": "93f137a5f0",
      "message": "refactor(api)!: move ValkeyCluster TLS under spec.networking (#339)",
      "date": "2026-08-05",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/339",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/93f137a5f033b2a925774f94f72f6ed7bfefeb53"
    },
    {
      "sha": "82324d5887",
      "message": "feat: Add args configuration support to exporter (#345)",
      "date": "2026-08-04",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/345",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/82324d5887c982438cb49ca2af916c9634962153"
    },
    {
      "sha": "05010b1afe",
      "message": "feat: Add zone scheduling axis (#340)",
      "date": "2026-07-30",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/340",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/05010b1afe27976bc174790e006d22b52bb3813f"
    },
    {
      "sha": "7b02994693",
      "message": "test: add e2e test for operator permissions (#245)",
      "date": "2026-07-30",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/245",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/7b0299469398a0fee726768d03b2e5ed0cea96ed"
    },
    {
      "sha": "1c64d35ba4",
      "message": "fix: Set debug level for \"getting system users secret\" output (#330)",
      "date": "2026-07-24",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/330",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/1c64d35ba47c6083937bd98a1c334cdb9be30981"
    },
    {
      "sha": "3180cb6f7a",
      "message": "Add `maxdepth` member to `valkeyReader`.",
      "date": "2026-07-23",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/336",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/3180cb6f7a7acf5224de13ae5deb44ff5744d92b"
    },
    {
      "sha": "f8715f6847",
      "message": "fix: scheduling correct internal imports (#322)",
      "date": "2026-07-17",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/322",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/f8715f6847076e8c6f14dca6699652aa98a7f059"
    },
    {
      "sha": "7888b68250",
      "message": "fix!: Rename go module to github.com/valkey-io/valkey-operator (#316)",
      "date": "2026-07-17",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/316",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/7888b682504daa6ec67b5cdcc2c1301e05df07e2"
    },
    {
      "sha": "3a92e94921",
      "message": "feat: implement scheduling against node axis (#310)",
      "date": "2026-07-17",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/310",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/3a92e949218f64ee3a56808b2dc5abc0ceba37b1"
    },
    {
      "sha": "49622ac494",
      "message": "test: add default user password for e2e cluster test (#292)",
      "date": "2026-07-05",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/292",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/49622ac4942b8af1ca50cb0dfc06356e3163b6d8"
    },
    {
      "sha": "799e8af298",
      "message": "chore(deps): bump docker/build-push-action from 7.2.0 to 7.3.0 (#291)",
      "date": "2026-07-02",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/291",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/799e8af29838c6bc1f8400dc7d477a7f28ec9d3e"
    },
    {
      "sha": "e0a3d581c6",
      "message": "add dedicated replication system user (#237)",
      "date": "2026-07-01",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/237",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/e0a3d581c66ea5d8e52aced11a7e34b73ee28940"
    },
    {
      "sha": "bedf2d79f0",
      "message": "Init cluster metrics (#285)",
      "date": "2026-07-01",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/285",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/bedf2d79f0b5f24aa3c70028d7225024ec7c465c"
    },
    {
      "sha": "5ac4d51170",
      "message": "fix: Ensure shards required (#283)",
      "date": "2026-06-26",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/283",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/5ac4d51170d6199140348a39259d8b60239ae81e"
    },
    {
      "sha": "21dd262717",
      "message": "feat: inject shutdown-on-sigterm failover by default (#268)",
      "date": "2026-06-23",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/268",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/21dd262717e51d28f647d49ead4a73d4185768be"
    },
    {
      "sha": "45a5668d98",
      "message": "Merge pull request #171 from tkarger/patch-2",
      "date": "2026-06-22",
      "repo": "valkey-helm",
      "pr_url": "https://github.com/valkey-io/valkey-helm/pull/171",
      "commit_url": "https://github.com/valkey-io/valkey-helm/commit/45a5668d98b3aca60a86bd62a02f02596b657778"
    },
    {
      "sha": "4cfb2d60e6",
      "message": "feat: fail over to the highest-offset replica (#249)",
      "date": "2026-06-19",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/249",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/4cfb2d60e66adfff2a6ad95f3fbe4bf3ce8dcda4"
    },
    {
      "sha": "06cd2def59",
      "message": "chore(kubebuilder): update scaffold v4.14.0 -> v4.15.0 (#254)",
      "date": "2026-06-18",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/254",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/06cd2def5916d41e8588cff92de44cc996329448"
    },
    {
      "sha": "10a5affed8",
      "message": "feat: add operator-specific Prometheus metrics (#159)",
      "date": "2026-06-17",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/159",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/10a5affed8ea3629f722006f9552d09455d875e2"
    },
    {
      "sha": "51fc871b48",
      "message": "Make `ffc.h` the default string to double parser (#318)",
      "date": "2026-06-15",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/318",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/51fc871b4802b23ee46a05d5142bb56bcf51036b"
    },
    {
      "sha": "12dc308b17",
      "message": "Merge pull request #179 from jdheyburn/valkey-operator-0.2.0",
      "date": "2026-06-10",
      "repo": "valkey-helm",
      "pr_url": "https://github.com/valkey-io/valkey-helm/pull/179",
      "commit_url": "https://github.com/valkey-io/valkey-helm/commit/12dc308b17320e3995e1b62ad0735adb94cf3ab9"
    },
    {
      "sha": "42e477760d",
      "message": "Merge pull request #172 from jdheyburn/valkey-operator/feat/add-watch-namespaces",
      "date": "2026-06-10",
      "repo": "valkey-helm",
      "pr_url": "https://github.com/valkey-io/valkey-helm/pull/172",
      "commit_url": "https://github.com/valkey-io/valkey-helm/commit/42e477760ddd15673f2ea0041a386843cd0db043"
    },
    {
      "sha": "c9a0e9276f",
      "message": "feat: Live configuration apply framework with MVP configs (#209)",
      "date": "2026-06-09",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/209",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/c9a0e9276fce41fa12b5908d9bde155b2eea1b94"
    },
    {
      "sha": "d1947d293f",
      "message": "[enhancement] Roll replicas first during ValkeyNode updates (#228)",
      "date": "2026-06-08",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/228",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/d1947d293f6056821610e0105ce375070f1f2c6c"
    },
    {
      "sha": "4c52117093",
      "message": "fix: New cluster rolls immediately after creation (#230)",
      "date": "2026-06-08",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/230",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/4c521170931f56aabda583e4c164f77f1420b7bc"
    },
    {
      "sha": "a759ded4af",
      "message": "enhancement: Use Recreate deployment strategy (#225)",
      "date": "2026-06-08",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/225",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/a759ded4af16de5493ff96063e9b71187485222f"
    },
    {
      "sha": "a87fed98a5",
      "message": "feat: add shard-aware topology spread constraints (#163)",
      "date": "2026-06-07",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/163",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/a87fed98a50a5d93551e0dfcc2a1a12f7a184915"
    },
    {
      "sha": "2aee18775f",
      "message": "chore(deps): bump docker/setup-buildx-action from 4.0.0 to 4.1.0 (#219)",
      "date": "2026-06-07",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/219",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/2aee18775f1a00fe814994a1a3f406fd88870ec5"
    },
    {
      "sha": "b0422e080e",
      "message": "chore(deps): bump docker/metadata-action from 6.0.0 to 6.1.0 (#220)",
      "date": "2026-06-05",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/220",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/b0422e080e8e75987aae96ec6e6f0e5e932489e7"
    },
    {
      "sha": "2894a1f0a0",
      "message": "chore(deps): bump actions/checkout from 6.0.2 to 6.0.3 (#221)",
      "date": "2026-06-05",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/221",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/2894a1f0a0d93a826c9a69d0bd52621053ac3955"
    },
    {
      "sha": "0315f36b07",
      "message": "chore(deps): bump docker/login-action from 4.1.0 to 4.2.0 (#217)",
      "date": "2026-06-05",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/217",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/0315f36b072a80b0e7f391fd0b58d7d40d3701eb"
    },
    {
      "sha": "2b7d06b2ff",
      "message": "feat: add watch-namespace flag to filter namespaces to watch for resources (#175)",
      "date": "2026-05-27",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/175",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/2b7d06b2ff92920cf2f26aba83ec6a11190d635b"
    },
    {
      "sha": "edecf1be7a",
      "message": "perf: pipeline getNodeState to save valkey roundtrips (#195)",
      "date": "2026-05-26",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/195",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/edecf1be7aa31e62777892cb622b37306a20d7a7"
    },
    {
      "sha": "0289b2f41a",
      "message": "chore: Add prefix to headless service resource (#189)",
      "date": "2026-05-22",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/189",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/0289b2f41a013ebfb2a9311a82077d20136c6f5f"
    },
    {
      "sha": "2425608c6e",
      "message": "docs: Add doc about updating RBAC permissions (#192)",
      "date": "2026-05-22",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/192",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/2425608c6e8cc4fcaa5971aa413fc2779077fd5b"
    },
    {
      "sha": "080ba9d87f",
      "message": "chore: remove ConfigMap suffix from managed resource names (#190)",
      "date": "2026-05-21",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/190",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/080ba9d87f6153325ef3b254cf5223e94637fa9e"
    },
    {
      "sha": "193e5e86e8",
      "message": "[feat] Add minimal pod disruption budget (#182)",
      "date": "2026-05-18",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/182",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/193e5e86e83097c0211ba7c926921a85298ee0b6"
    },
    {
      "sha": "0886dc4946",
      "message": "[fix] Switch to test-e2e context if it exists already (#181)",
      "date": "2026-05-18",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/181",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/0886dc49469817ed0619c2f68edb4035780ff682"
    },
    {
      "sha": "363d2dace0",
      "message": "add resetpass to UserAclSpec (#166)",
      "date": "2026-05-15",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/166",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/363d2dace00a78b9985b0fc68e3aa20a29380df8"
    },
    {
      "sha": "3c08e8d7b9",
      "message": "docs: Remove image.tag=main override in quickstart (#183)",
      "date": "2026-05-14",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/183",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/3c08e8d7b9f7edecc17446c206ec1d58da90cba3"
    },
    {
      "sha": "a420772789",
      "message": "docs: Add valkeynode-design.md (#162)",
      "date": "2026-05-11",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/162",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/a420772789c03bf0721e179fb2d5fe367400368e"
    },
    {
      "sha": "0b8b87d10d",
      "message": "fixed pre-commit local go version (#168)",
      "date": "2026-05-11",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/168",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/0b8b87d10d3ab47a4b0bdf527c88f4c6e24949e5"
    },
    {
      "sha": "bd677c75e5",
      "message": "Add prefix to container image version tags. (#174)",
      "date": "2026-05-11",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/174",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/bd677c75e5eb5cd4a83ceb2d4cae5aea56f4b5d8"
    },
    {
      "sha": "2f846003ec",
      "message": "Fix e2e tests - pod already exists intermittent issue (#172)",
      "date": "2026-05-11",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/172",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/2f846003ecc3e92d0e7e1e51ce0536bbb3d73541"
    },
    {
      "sha": "473c344c00",
      "message": "docs: Add valkeycluster docs (#165)",
      "date": "2026-05-11",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/165",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/473c344c00eddab62e2f6ab18fb752c5df6efa86"
    },
    {
      "sha": "426218dc3c",
      "message": "[feat] Roll ValkeyNodes on changes to ValkeyCluster.Spec.Config (#164)",
      "date": "2026-05-09",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/164",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/426218dc3ca9a9fc9fc1b8372e82fb81cf684d73"
    },
    {
      "sha": "426218dc3c",
      "message": "[feat] Roll ValkeyNodes on changes to ValkeyCluster.Spec.Config (#164)",
      "date": "2026-05-09",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/164",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/426218dc3ca9a9fc9fc1b8372e82fb81cf684d73"
    },
    {
      "sha": "c7b51b3613",
      "message": "chore(kubebuilder): update scaffold v4.13.1 -> v4.14.0 (#161)",
      "date": "2026-05-08",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/161",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/c7b51b361387e1f24b15b7724656bd00182ced97"
    },
    {
      "sha": "323c70b609",
      "message": "Update valkey-operator helm install notes",
      "date": "2026-05-08",
      "repo": "valkey-helm",
      "pr_url": "https://github.com/valkey-io/valkey-helm/pull/171",
      "commit_url": "https://github.com/valkey-io/valkey-helm/commit/323c70b609f61febe52178bf06247d153b9342b5"
    },
    {
      "sha": "f12ce2d3f9",
      "message": "feat: add initial Helm chart for valkey-operator (#162)",
      "date": "2026-05-01",
      "repo": "valkey-helm",
      "pr_url": "https://github.com/valkey-io/valkey-helm/pull/162",
      "commit_url": "https://github.com/valkey-io/valkey-helm/commit/f12ce2d3f9762a834413fc347703e08b7142d234"
    },
    {
      "sha": "e356730264",
      "message": "Update Go build (#150)",
      "date": "2026-04-24",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/150",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/e356730264bc8e9368a8e85c8ea6546ca707424d"
    },
    {
      "sha": "ddc13a8417",
      "message": "Setup container image publishing (#102)",
      "date": "2026-04-23",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/102",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/ddc13a8417366b5ade6c8d72f87d8c1b42e19d4e"
    },
    {
      "sha": "7c9bad6c13",
      "message": "feat: proactive failovers before cluster rolls (#128)",
      "date": "2026-04-21",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/128",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/7c9bad6c134e6600d98137f68889b8e2c669528b"
    },
    {
      "sha": "2b3718a3e5",
      "message": "feat: initial tls support for valkey cluster (#133)",
      "date": "2026-04-20",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/133",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/2b3718a3e5aa5f25d008cbeee0836e6822aa0399"
    },
    {
      "sha": "e4b548b328",
      "message": "Remove support for external dict while still supporting external sds (#302)",
      "date": "2026-04-16",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/302",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/e4b548b3284cecdeeba19f4a6b949b1d92636653"
    },
    {
      "sha": "8aff94fab3",
      "message": "RDMA: Fix lost EPOLLIN/POLLIN events",
      "date": "2026-04-16",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/301",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/8aff94fab311fc61fc9a034986e991dcaafbf0ba"
    },
    {
      "sha": "3943c459e3",
      "message": "Add build info metric (#106)",
      "date": "2026-04-08",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/106",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/3943c459e344ed6cf7566e9dda65f817f554346a"
    },
    {
      "sha": "3b8c66bd52",
      "message": "chore(kubebuilder): update scaffold v4.13.0 -> v4.13.1 (#125)",
      "date": "2026-03-31",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/125",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/3b8c66bd521569f26796d38d83903eb277439e7e"
    },
    {
      "sha": "c92a1efa39",
      "message": "feat: Sequentially update workloads one-by-one (#116)",
      "date": "2026-03-20",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/116",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/c92a1efa39ddfdde67a925cb6d4fe0fb28008838"
    },
    {
      "sha": "b9285b5fcc",
      "message": "Optimize read buffer compaction and reduce copying (#294)",
      "date": "2026-03-19",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/294",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/b9285b5fcca91ae6bb4b212fc5d5af1460c6d0a4"
    },
    {
      "sha": "89eb055a48",
      "message": "feat: ValkeyNode integration with ValkeyCluster (#113)",
      "date": "2026-03-16",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/113",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/89eb055a4896bcc907fc816366d6b953e937796d"
    },
    {
      "sha": "e6d9dad5c6",
      "message": "Implement strategic merge patch (#62) (#108)",
      "date": "2026-03-16",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/108",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/e6d9dad5c62c529a21a0931351185a6c1ed45e00"
    },
    {
      "sha": "78139b06ee",
      "message": "Add scale-in support with slot draining (#107)",
      "date": "2026-03-12",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/107",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/78139b06eef1829cbb5bbea44ed6d7b2b7a4383a"
    },
    {
      "sha": "0fa8098772",
      "message": "Additional overflow protection for MAP/ATTR",
      "date": "2026-03-11",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/292",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/0fa8098772fad670bfd5e22e2aeca17e97e80af9"
    },
    {
      "sha": "41e9a48972",
      "message": "feat: Add ValkeyNode CRD and controller for abstracting pod mgmt (#94)",
      "date": "2026-03-10",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/94",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/41e9a48972bbb148d2907a4f6508459e31960264"
    },
    {
      "sha": "94febf3bc6",
      "message": "chore(kubebuilder): Upgrade the Scaffold: v4.11.1 -> v4.13.0 (#97)",
      "date": "2026-03-04",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/97",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/94febf3bc6523a0e941e2df3fca49866498da926"
    },
    {
      "sha": "b26c56e873",
      "message": "Fix gcc warnings (#287)",
      "date": "2026-03-03",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/287",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/b26c56e87318d45b339747fcd6e2cf62d132cbe4"
    },
    {
      "sha": "39fa3f5ee6",
      "message": "Fix slot-range parsing during migration and add rebalance planning logic (#92)",
      "date": "2026-02-27",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/92",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/39fa3f5ee60785fdc8a426b2bba9c4a29e69ddbb"
    },
    {
      "sha": "3a1e5d5ce9",
      "message": "Lazy loading of RDMA libs in CLI/Benchmark when building as module (#3072)",
      "date": "2026-02-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3072",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3a1e5d5ce9a45eeb6aaaba710f9bf191c9b16a27"
    },
    {
      "sha": "8d9217dba2",
      "message": "Adds tech call to README (#93)",
      "date": "2026-02-26",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/93",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/8d9217dba28ecedf200ae7cde50ab871865add8a"
    },
    {
      "sha": "c7a77e8655",
      "message": "Batch pending node processing across MEET, slot assignment, and replication (#90)",
      "date": "2026-02-24",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/90",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/c7a77e8655792e0b685ab3972732eb16cc5e41ea"
    },
    {
      "sha": "40d6590d77",
      "message": "Implement runtime dynamic loading for RDMA libraries (#284)",
      "date": "2026-02-23",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/284",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/40d6590d7758d45305be584089a099428ff3741c"
    },
    {
      "sha": "d777c83bae",
      "message": "Handle post-failover pod replacement gracefully (#86)",
      "date": "2026-02-19",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/86",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/d777c83baed0873ad30bb010d6f4e0ea2d456fbe"
    },
    {
      "sha": "35e6aa7f5c",
      "message": "added replication check before marking cluster ready status (#87)",
      "date": "2026-02-18",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/87",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/35e6aa7f5c8cb7b7c7afae839f886d76235bf452"
    },
    {
      "sha": "a554f09421",
      "message": "Fix potential uint32_t underflow issue (#280)",
      "date": "2026-02-16",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/280",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/a554f094218272b38ee706083c43612abfdef608"
    },
    {
      "sha": "02eedafc3b",
      "message": "Use deterministic deployment names to encode shard topology (#81)",
      "date": "2026-02-16",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/81",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/02eedafc3b50742714bb7ef118ec021abd6aa04a"
    },
    {
      "sha": "75a3a9d9b2",
      "message": "(chore) scaffold update: v4.11.0 -> v4.11.1 (#78)",
      "date": "2026-02-05",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/78",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/75a3a9d9b24a07549e2e89da555fa75b2ea4197e"
    },
    {
      "sha": "cabfcd9e36",
      "message": "migrate to new Kubernetes events recorder API (#72)",
      "date": "2026-02-05",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/72",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/cabfcd9e36745a9775d9f362b92b7f4d9cc5cd67"
    },
    {
      "sha": "a00dfe2290",
      "message": "Pin GitHub Actions (#73)",
      "date": "2026-02-04",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/73",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/a00dfe2290dec77cf304cd7d47af223a3c3d3a8e"
    },
    {
      "sha": "bf79b9058b",
      "message": "add startup probe to valkey containers (#68)",
      "date": "2026-01-31",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/68",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/bf79b9058ba0a576ead24a11016fb0a0d40b9875"
    },
    {
      "sha": "e0a25d14a8",
      "message": "(feat): Support Toleration Configuration for ValkeyCluster (#30) (#61)",
      "date": "2026-01-30",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/61",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/e0a25d14a8e30a8c01b2926c3503119d533da516"
    },
    {
      "sha": "37ce76e172",
      "message": "(feat): Support Affinity Configuration for ValkeyCluster (#32) (#38)",
      "date": "2026-01-23",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/38",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/37ce76e172803030eea3fccbaccb8273bdcbad7c"
    },
    {
      "sha": "589930be46",
      "message": " (feat): Support Resources Configuration for ValkeyCluster (#29) (#41)",
      "date": "2026-01-16",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/41",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/589930be46f81a62572ffd7e0ccfb93cd2e823ce"
    },
    {
      "sha": "d877fd95eb",
      "message": "fixed e2e tests failing intermittently & review comments from past PR  (#54)",
      "date": "2026-01-15",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/54",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/d877fd95eb8f0d961586c3abd9b54fc167283af0"
    },
    {
      "sha": "be52c44841",
      "message": "(feat): Status Conditions for ValkeyCluster (#33)",
      "date": "2025-12-25",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/33",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/be52c44841cfc7ef84d3c26b879306b576ad3c7d"
    },
    {
      "sha": "4e3ccccada",
      "message": "Add CI coverage for Solaris DeveloperStudio compiler",
      "date": "2025-12-09",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/270",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/4e3ccccadacdf923e6039ad3b3e395eec3d24610"
    },
    {
      "sha": "4e3ccccada",
      "message": "Add CI coverage for Solaris DeveloperStudio compiler",
      "date": "2025-12-09",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/270",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/4e3ccccadacdf923e6039ad3b3e395eec3d24610"
    },
    {
      "sha": "a87338fcf0",
      "message": "Fix compilation warnings from Solaris Developer Studio",
      "date": "2025-12-08",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/267",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/a87338fcf0fc3be17f7b833158b8310ded705ff0"
    },
    {
      "sha": "38191079c6",
      "message": "Fix compilation on Solaris with Sun/Solaris Studio",
      "date": "2025-12-04",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/266",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/38191079c6bd524cabf981f8ab0cd55c26cf414a"
    },
    {
      "sha": "ef5de03121",
      "message": "Make libvalkey initialization thread-safe",
      "date": "2025-12-03",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/264",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/ef5de03121bad5e2bf99269c3595a5a7a49df9b3"
    },
    {
      "sha": "cf41247730",
      "message": "Add CONTRIBUTING.md (#8)",
      "date": "2025-10-31",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/8",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/cf41247730bbd8b8ce1cb18afa52c30220246285"
    },
    {
      "sha": "b857dabf1b",
      "message": "Fix DISCUSSION_TEMPLATE directory (#13)",
      "date": "2025-10-31",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/13",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/b857dabf1b2a66f7fa43965dfde337273153434a"
    },
    {
      "sha": "90b757ea5b",
      "message": "Add Github DISCUSSION_TEMPLATE (#11)",
      "date": "2025-10-31",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/11",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/90b757ea5b5532ad36ffa27555b19bcc2b215fb5"
    },
    {
      "sha": "a62a46f81a",
      "message": "Add SUPPORT.md (#9)",
      "date": "2025-10-31",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/9",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/a62a46f81a05f38869ef183390c3076981740534"
    },
    {
      "sha": "cc8e48fb9b",
      "message": "Update README (#12)",
      "date": "2025-10-31",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/12",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/cc8e48fb9bac8cabca8fd8a62d3ea483c1b4eb15"
    },
    {
      "sha": "eea6904195",
      "message": "feat(operator): flush out v1alpha1 CRDs (#5)",
      "date": "2025-10-24",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/5",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/eea6904195727b2b52baf439ddf90c4580b7ec51"
    },
    {
      "sha": "36f6e2292e",
      "message": "Fix the long-blocking read for Valkey RDMA. (#233)",
      "date": "2025-10-23",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/233",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/36f6e2292e4748a3d3f4e1653974b8ee0f55d00a"
    },
    {
      "sha": "c090c28bea",
      "message": "Use a uintptr_t hop for casting pointers to ints",
      "date": "2025-10-17",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/252",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/c090c28bea418b0840ae842fd33410f4993f6589"
    },
    {
      "sha": "ebece9346d",
      "message": "Bump taiki-e/install-action in the github-actions group",
      "date": "2025-09-29",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/243",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/ebece9346dc22c192ac3d194fe0a9e71546b5e66"
    },
    {
      "sha": "af3a6aff3e",
      "message": "Merge pull request #2 from valkey-io/kubebuilder",
      "date": "2025-09-29",
      "repo": "valkey-operator",
      "pr_url": "https://github.com/valkey-io/valkey-operator/pull/2",
      "commit_url": "https://github.com/valkey-io/valkey-operator/commit/af3a6aff3e5cc593fa624e16fdbbf4a0c22bff6b"
    },
    {
      "sha": "10fc487d38",
      "message": "Bump the github-actions group across 1 directory with 2 updates",
      "date": "2025-09-08",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/238",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/10fc487d38a77dace065037e0eb69a9c15fef7a3"
    },
    {
      "sha": "9e10acbf7f",
      "message": "Fix duplicate Acks for RDMA events. (#229)",
      "date": "2025-08-13",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/229",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/9e10acbf7fddd83245cde01a35256e0290be16ce"
    },
    {
      "sha": "1eadedf487",
      "message": "Remove the unused value duplicate API from dict",
      "date": "2025-08-05",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/226",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/1eadedf4873ad77918b361a48a402b40dded8351"
    },
    {
      "sha": "3c738f08a4",
      "message": "Remove the unused value duplicate API from dict of libvalkey (#2387)",
      "date": "2025-08-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2387",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3c738f08a4c29cd779c116a89286055a81c61f03"
    },
    {
      "sha": "d861469dca",
      "message": "Bump taiki-e/install-action in the github-actions group",
      "date": "2025-07-29",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/224",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/d861469dca71fd68aaf8736967ccae5292eb254d"
    },
    {
      "sha": "279125e220",
      "message": "Spelling (#213)",
      "date": "2025-06-02",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/213",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/279125e22053311586e3837800c37e9ca08aae33"
    },
    {
      "sha": "4804c8dfbb",
      "message": "Fix windows build when TLS enabled (#203)",
      "date": "2025-05-12",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/203",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/4804c8dfbb1e161d32c14051111f9048cd961c25"
    },
    {
      "sha": "88b214d372",
      "message": "Support SSUBSCRIBE command (#178)",
      "date": "2025-04-25",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/178",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/88b214d372005aa046adac8b1cafd10f76e89f58"
    },
    {
      "sha": "c2ed4933c9",
      "message": "Introduce MPTCP (#189)",
      "date": "2025-04-17",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/189",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/c2ed4933c9f9067b1c91cae5d134e19efc578137"
    },
    {
      "sha": "ac48ff3124",
      "message": "Bump the github-actions group with 3 updates",
      "date": "2025-04-07",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/188",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/ac48ff31245bf0487c6a133c5f6cae0f774d8a57"
    },
    {
      "sha": "7ed4603a0b",
      "message": "Bump taiki-e/install-action in the github-actions group",
      "date": "2025-03-31",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/186",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/7ed4603a0bf26cc68424d5e405095d61be7ee720"
    },
    {
      "sha": "53b07f1b72",
      "message": "Bump the github-actions group across 1 directory with 2 updates",
      "date": "2025-03-06",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/175",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/53b07f1b7295414e5072ead6ad107481040cdc3b"
    },
    {
      "sha": "80e8735412",
      "message": "Add tags into .gitignore",
      "date": "2025-03-04",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/172",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/80e8735412952ef8c65d615dd0fcf065b29d3ab1"
    },
    {
      "sha": "8b736dd732",
      "message": "Rework library naming on `macOS`.",
      "date": "2025-02-19",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/169",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/8b736dd7326939ced9f02a230a46e2cc02e51390"
    },
    {
      "sha": "4e4160848b",
      "message": "SSL_library_init() is deprecated as of openssl v1.1.0",
      "date": "2025-02-06",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/166",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/4e4160848bd458e61671163a3a68c3a5d77b1719"
    },
    {
      "sha": "c9a7b53782",
      "message": "Bump vmactions/freebsd-vm from 1.1.4 to 1.1.5",
      "date": "2024-11-04",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/128",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/c9a7b537829173edef5f589a7b919133957c657d"
    },
    {
      "sha": "9d51a4b845",
      "message": "Remove protected-mode from RDMA test",
      "date": "2024-10-30",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/127",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/9d51a4b8456eb2a3ecd324d5eb885fea2e89643c"
    },
    {
      "sha": "445defeb25",
      "message": "Bump taiki-e/install-action from 2.44.35 to 2.44.44",
      "date": "2024-10-21",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/121",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/445defeb25b955a826bd83cb9220ba7268686712"
    },
    {
      "sha": "297e432b7d",
      "message": "Bump vmactions/freebsd-vm from 1.1.0 to 1.1.1",
      "date": "2024-09-20",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/96",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/297e432b7df804ca038d6edeb64d19ad8e45f4c7"
    },
    {
      "sha": "f888a144b7",
      "message": "Bump vmactions/freebsd-vm from 1.0.8 to 1.1.0",
      "date": "2024-09-09",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/90",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/f888a144b7d5863c1efac033f912a7ca2963b707"
    },
    {
      "sha": "1c64aa4edd",
      "message": "Bump aminya/setup-cpp from 0.39.0 to 0.41.0",
      "date": "2024-09-09",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/89",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/1c64aa4edd2c94a719a2ddf209ab610c901d3ee7"
    },
    {
      "sha": "9b30bed41e",
      "message": "Bump aminya/setup-cpp from 0.38.3 to 0.39.0",
      "date": "2024-08-26",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/77",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/9b30bed41ee19eeb6c2ac08ab31437ecd5b6e0c6"
    },
    {
      "sha": "53f8f0ff41",
      "message": "Bump rojopolis/spellcheck-github-actions from 0.40.0 to 0.41.0",
      "date": "2024-08-19",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/69",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/53f8f0ff41427ef9d67f5c25b5168fd7d10409bf"
    },
    {
      "sha": "260fc68c27",
      "message": "Bump aminya/setup-cpp from 0.38.1 to 0.38.3",
      "date": "2024-08-19",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/68",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/260fc68c27dbed1f0d423f1e3190804823031bad"
    },
    {
      "sha": "9188dbdb60",
      "message": "Fix timing based macOS CI failure.",
      "date": "2024-08-13",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/66",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/9188dbdb60be8968abfa465e1e4e70de2c5e2791"
    },
    {
      "sha": "80ceb19115",
      "message": "Whitelist a few words for spellcheck.",
      "date": "2024-08-13",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/65",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/80ceb1911522e4a0f7adfb586c61b8b2ddb9449d"
    },
    {
      "sha": "3fde85aea1",
      "message": "Initial project readme.",
      "date": "2024-08-12",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/61",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/3fde85aea19be1d6520241d8251c868547938d12"
    },
    {
      "sha": "51aeaa90ba",
      "message": "Bump aminya/setup-cpp from 0.37.0 to 0.38.1",
      "date": "2024-08-12",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/64",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/51aeaa90ba5288985f09635c86b5340148b9c256"
    },
    {
      "sha": "c535911d35",
      "message": "Import updated license header for macos adapter and example.",
      "date": "2024-08-09",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/63",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/c535911d35f30ff370f0185c26a01c95ba45a966"
    },
    {
      "sha": "cd52909119",
      "message": "Bump rojopolis/spellcheck-github-actions from 0.38.0 to 0.40.0",
      "date": "2024-08-01",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/54",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/cd529091196790f25fd3f5e809ae7a295112d434"
    },
    {
      "sha": "1f36dd2e0f",
      "message": "Bump vmactions/freebsd-vm from 1.0.7 to 1.0.8",
      "date": "2024-07-10",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/46",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/1f36dd2e0f57173103504eea96fcaddcedcd158b"
    },
    {
      "sha": "90f6b97c63",
      "message": "Minor Makefile cleanup",
      "date": "2024-07-01",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/40",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/90f6b97c63c69a58e97ed5854a363e3f8ba736b1"
    },
    {
      "sha": "8519d8bf54",
      "message": "Bump jidicula/clang-format-action from 4.11.0 to 4.13.0",
      "date": "2024-06-27",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/7",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/8519d8bf5452d8f155d5ec909edf89f4476de44a"
    },
    {
      "sha": "b3713d3a55",
      "message": "Fix Windows builds and CI",
      "date": "2024-06-27",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/31",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/b3713d3a55fd7bfd2924b215d83e97c5f83c3620"
    },
    {
      "sha": "75da159aa4",
      "message": "Minor makefile update",
      "date": "2024-06-26",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/27",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/75da159aa40d015b3398a7a2e2e76cc239a2c4b1"
    },
    {
      "sha": "e28f811f5a",
      "message": "Build and CI fixes.",
      "date": "2024-06-24",
      "repo": "libvalkey",
      "pr_url": "https://github.com/valkey-io/libvalkey/pull/24",
      "commit_url": "https://github.com/valkey-io/libvalkey/commit/e28f811f5a7ab39ac1e48acbabd46cfefdae0d28"
    }
  ]
}
