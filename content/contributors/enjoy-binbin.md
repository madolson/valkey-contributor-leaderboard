{
  "title": "enjoy-binbin",
  "login": "enjoy-binbin",
  "avatar_url": "https://avatars.githubusercontent.com/u/22811481?v=4",
  "score": 824,
  "commit_count": 316,
  "review_count": 508,
  "repos": [
    "valkey",
    "valkey-bloom",
    "valkey-doc",
    "valkey-io.github.io",
    "valkey-json"
  ],
  "commit_list": [
    {
      "sha": "bef46dacc1",
      "message": "Skip cluster resharding test under valgrind (#3574)",
      "date": "2026-04-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3574",
      "commit_url": "https://github.com/valkey-io/valkey/commit/bef46dacc1a4ffbd1c983d75b1a5eee00982fd6c"
    },
    {
      "sha": "a3e44a55d3",
      "message": "Fix lua-enable-insecure-api default value cannot be changed to yes (#3548)",
      "date": "2026-04-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3548",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a3e44a55d3da5bc590b5ee596f195e56f187f70e"
    },
    {
      "sha": "ac9ca9de3d",
      "message": "Fix rdmaServer leaks when create listen cm id error (#3557)",
      "date": "2026-04-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3557",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ac9ca9de3d1feff4a40358935b0f2e2acdcdc789"
    },
    {
      "sha": "c403eecd5b",
      "message": "Fix double free in stream consumer PEL loading with corrupt RDB data (#3498)",
      "date": "2026-04-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3498",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c403eecd5b7dbfdf737e8c6aae8e1d022727ba50"
    },
    {
      "sha": "087280e3f8",
      "message": "Rewrite the faster failover test case (#3495)",
      "date": "2026-04-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3495",
      "commit_url": "https://github.com/valkey-io/valkey/commit/087280e3f87ccbdc13714bf94f8288de8888c08f"
    },
    {
      "sha": "a34f125d8e",
      "message": "Change rdbSaveStreamConsumers return type from size_t to ssize_t (#3499)",
      "date": "2026-04-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3499",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a34f125d8e18201bc51878e2848c6b6187a8a3cb"
    },
    {
      "sha": "2871efd436",
      "message": "Add cluster-config-save-behavior option to control nodes.conf save behavior (#3372)",
      "date": "2026-04-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3372",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2871efd43644f9bf222dca882a184e36f3e28d4a"
    },
    {
      "sha": "890b82ac33",
      "message": "Fix config rewrite producing negative values for unsigned memory configs (#3440)",
      "date": "2026-04-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3440",
      "commit_url": "https://github.com/valkey-io/valkey/commit/890b82ac335672cb545f38ee6ebc4fb6cafd6e31"
    },
    {
      "sha": "dba128f13b",
      "message": "Fix slot-migration-max-failover-repl-bytes unable to accept -1 (#3443)",
      "date": "2026-04-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3443",
      "commit_url": "https://github.com/valkey-io/valkey/commit/dba128f13b7486322fe3b52a8358bd9188ec613a"
    },
    {
      "sha": "95860937d5",
      "message": "Optimize WATCH duplicate key check from O(N) to O(1) using per-db hashtable (#3360)",
      "date": "2026-03-31",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3360",
      "commit_url": "https://github.com/valkey-io/valkey/commit/95860937d555ce13b6cad32b7c3510fceb809861"
    },
    {
      "sha": "2cde059da1",
      "message": "Handle EAGAIN in clusterWriteHandler (#3421)",
      "date": "2026-03-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3421",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2cde059da1b746eb7917147b16412678a9e5e12f"
    },
    {
      "sha": "6822a676fe",
      "message": "Do the failover immediately if the replica is the best ranked replica (#2227)",
      "date": "2026-03-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2227",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6822a676fe8f9100dbc722d2a65995c135af1b0f"
    },
    {
      "sha": "c921cb5aa5",
      "message": "Fix incorrect memory overhead calculation for watched keys (#3359)",
      "date": "2026-03-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3359",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c921cb5aa5619cb4ae5cd4affb43a3a441e297b3"
    },
    {
      "sha": "26522fc527",
      "message": "Add availability-zone to the reply schema for CLUSTER SHARDS/SLOTS (#3352)",
      "date": "2026-03-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3352",
      "commit_url": "https://github.com/valkey-io/valkey/commit/26522fc527d1f474d39bbd74482541aa54715bfb"
    },
    {
      "sha": "a7d919a5bb",
      "message": "Optimize SET key value EX/PX/EXAT ttl to reduce calls of rewriteClientCommandVector (#3279)",
      "date": "2026-03-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3279",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a7d919a5bbb311e04221ea29c460b5c40fc70169"
    },
    {
      "sha": "5157255b82",
      "message": "Fix timing issue in RDB abort test (#3343)",
      "date": "2026-03-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3343",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5157255b82002a79fd212de9d9ba0fe08812849f"
    },
    {
      "sha": "ba58546369",
      "message": "New MSETEX command allows to set an expiration time with MSET (#3121)",
      "date": "2026-03-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3121",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ba58546369965d8b0d5d14ef87d41531f4fe5bc2"
    },
    {
      "sha": "fc217fca2d",
      "message": "Update cluster config file when NOFAILOVER changes (#3280)",
      "date": "2026-03-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3280",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fc217fca2d7de246ab8494d9d8619b7348235f47"
    },
    {
      "sha": "d1734415bf",
      "message": "Fix timing issue in LATENCY GRAPH test (#3265)",
      "date": "2026-03-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3265",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d1734415bf9fed2472e9e31be20d0cf8544129b1"
    },
    {
      "sha": "a59b1feb49",
      "message": "Add new INFO field mem_total_replication_buffers and new replicas.repl.buffer MEMORY STATS field (#416)",
      "date": "2026-03-03",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/416",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/a59b1feb49013b0ddfe0ce04c8921bd4fc775277"
    },
    {
      "sha": "2937911003",
      "message": "Show replica dual-channel replication buffer memory in INFO MEMORY and MEMORY STATS (#2924)",
      "date": "2026-03-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2924",
      "commit_url": "https://github.com/valkey-io/valkey/commit/293791100325d4d472d65ab005726771c238ad21"
    },
    {
      "sha": "f23f093b78",
      "message": "Add the new remaining_repl_size field in CLUSTER GETSLOTMIGRATIONS (#406)",
      "date": "2026-03-01",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/406",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/f23f093b78175b89fb7ebee21817fe9554a7292c"
    },
    {
      "sha": "262b371da0",
      "message": "Abort and swap the tables if ht1 is very full during the hashtable shrink rehashing (#3175)",
      "date": "2026-02-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3175",
      "commit_url": "https://github.com/valkey-io/valkey/commit/262b371da0d2454130dd487db34b388f50697c02"
    },
    {
      "sha": "537cb07942",
      "message": "Logging fix or improvement around new shard ID generation (#3192)",
      "date": "2026-02-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3192",
      "commit_url": "https://github.com/valkey-io/valkey/commit/537cb07942f1e4233e9e8a60a5015a6b3dee6e2d"
    },
    {
      "sha": "1f473323c8",
      "message": "Fix getKeysUsingKeySpecs keynum case ignoring keystep when calc the last key (#3197)",
      "date": "2026-02-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3197",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1f473323c8b6d51dcf5955125ba723437f2a8287"
    },
    {
      "sha": "556180dc8f",
      "message": "Fix flaky cluster automatic failover test (#3206)",
      "date": "2026-02-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3206",
      "commit_url": "https://github.com/valkey-io/valkey/commit/556180dc8f52d85a41717f5bf45ecfc804425429"
    },
    {
      "sha": "223bfa840b",
      "message": "Added comment to maxmemory-clients conf to mention the performance issue (#1840)",
      "date": "2026-02-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1840",
      "commit_url": "https://github.com/valkey-io/valkey/commit/223bfa840b31918c1aa4931846e3408c57b6e4a5"
    },
    {
      "sha": "06ccdf9904",
      "message": "Fix remaining_repl_size should be in CLUSTER GETSLOTMIGRATIONS in conf (#3180)",
      "date": "2026-02-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3180",
      "commit_url": "https://github.com/valkey-io/valkey/commit/06ccdf99049d938b6a6cabc0d69bf4ecc4fa506f"
    },
    {
      "sha": "751a099643",
      "message": "Add remaining_repl_size field in CLUSTER MIGRATESLOTS output (#3135)",
      "date": "2026-02-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3135",
      "commit_url": "https://github.com/valkey-io/valkey/commit/751a099643f9a4397a91cef2316468e7eed5bfeb"
    },
    {
      "sha": "746c4d0372",
      "message": "Revert \"Extend test helper wait_for_cluster_propagation to support ignoring certain node (#3069)\" (#3176)",
      "date": "2026-02-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3176",
      "commit_url": "https://github.com/valkey-io/valkey/commit/746c4d0372b3c479893ef250a8c8a9e9e18761eb"
    },
    {
      "sha": "346c11dde9",
      "message": "Rehashing more empty buckets to optimize the rehashing speed (#3150)",
      "date": "2026-02-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3150",
      "commit_url": "https://github.com/valkey-io/valkey/commit/346c11dde9928bbc9aacd0f0c63594ec31967959"
    },
    {
      "sha": "8ed270f443",
      "message": "Optimize SREM/ZREM/HDEL to pause auto shrink when deleting multiple items (#3144)",
      "date": "2026-02-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3144",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8ed270f443701b0a737d37c3ecb026d7559ecaaa"
    },
    {
      "sha": "79c8948edc",
      "message": "Optimize rehash completion check for empty hash table (#3141)",
      "date": "2026-02-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3141",
      "commit_url": "https://github.com/valkey-io/valkey/commit/79c8948edcdbc4e2deb887e0e3fbb54067432fd7"
    },
    {
      "sha": "cfbe0937fb",
      "message": "Extend hashtableGetStatsMsg to always show empty table and rehash index (#3142)",
      "date": "2026-02-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3142",
      "commit_url": "https://github.com/valkey-io/valkey/commit/cfbe0937fb3b275e735a061c811f07482cdf7904"
    },
    {
      "sha": "eabfe235d2",
      "message": "Check expiration time first before lookup the key in GETEX command (#3116)",
      "date": "2026-02-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3116",
      "commit_url": "https://github.com/valkey-io/valkey/commit/eabfe235d2b522f0aded9a6139f16c4f5deeed93"
    },
    {
      "sha": "851eaafe61",
      "message": "Free replica local buffer in async way in dual channel replication (#2948)",
      "date": "2026-01-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2948",
      "commit_url": "https://github.com/valkey-io/valkey/commit/851eaafe61dada5ba075def06d5a839f8980d4bb"
    },
    {
      "sha": "73838a0ddb",
      "message": "Remove empty list dead code condition in lmoveGenericCommand code (#3128)",
      "date": "2026-01-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3128",
      "commit_url": "https://github.com/valkey-io/valkey/commit/73838a0ddb485ba0c5cbd8c2a430037876127128"
    },
    {
      "sha": "8a9c3717d1",
      "message": "Don't exit the process when locale-collate fails to be set from env during startup (#3067)",
      "date": "2026-01-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3067",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8a9c3717d13e7857b19a792058f9075f045868f4"
    },
    {
      "sha": "e7d004be0b",
      "message": "Comment cleanup around entry.c file (#3107)",
      "date": "2026-01-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3107",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e7d004be0b8221af1e6b07ef7598b901e2d45382"
    },
    {
      "sha": "0b1f99d49b",
      "message": "Fix race condition in TIME overflow test (#3074)",
      "date": "2026-01-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3074",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0b1f99d49bf3a3891d8c1732907b911ceb2c8f03"
    },
    {
      "sha": "5e65bad9cc",
      "message": "Cleanup and break the while loop in clusterPrimariesHaveReplicas (#3075)",
      "date": "2026-01-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3075",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5e65bad9cc53e46fdfce5f55b429dc89dff9273e"
    },
    {
      "sha": "9735bac65b",
      "message": "Update dual channel replication conf to mention primary should also enable repl-diskless-sync (#3051)",
      "date": "2026-01-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3051",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9735bac65b29984c138127e859dd5b6a74fe034c"
    },
    {
      "sha": "b7b11d77d6",
      "message": "Avoid duplicate calculations of network-bytes-out in slot stats with copy-avoidance (#3046)",
      "date": "2026-01-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3046",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b7b11d77d621d8d5fed0f77faed676e4ecee5854"
    },
    {
      "sha": "f0d981014c",
      "message": "Don't stop the dirty scripts when an OOM occurs midway through execution (#3030)",
      "date": "2026-01-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3030",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f0d981014c208b6d80badf3a814cff016b3f117d"
    },
    {
      "sha": "4c3f1d94d1",
      "message": "Update maxclients example in clients.md (#390)",
      "date": "2026-01-05",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/390",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/4c3f1d94d1b1079d3f364852bdcddd3520424e60"
    },
    {
      "sha": "8362031c5a",
      "message": "Update Keyspace event 2025 Beijing page with presentation slides (#433)",
      "date": "2026-01-03",
      "repo": "valkey-io.github.io",
      "pr_url": "https://github.com/valkey-io/valkey-io.github.io/pull/433",
      "commit_url": "https://github.com/valkey-io/valkey-io.github.io/commit/8362031c5ab4ed3d624884ad115473189e6c4757"
    },
    {
      "sha": "9c5d004bfe",
      "message": "Fix chained replica crash when doing dual channel replication (#2983)",
      "date": "2025-12-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2983",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9c5d004bfebe44d8ec6d3e616dd380d70df708e9"
    },
    {
      "sha": "82d7b7e40c",
      "message": "Fail to save the cluster config file will not exit the process (#1032)",
      "date": "2025-12-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1032",
      "commit_url": "https://github.com/valkey-io/valkey/commit/82d7b7e40c18d6f18ddf59d6759e9cfde16067ac"
    },
    {
      "sha": "8ab0152bef",
      "message": "Check for duplicate nodeids when loading nodes.conf (#2852)",
      "date": "2025-12-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2852",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8ab0152bef7c273c0f44dec08fe06d6affbbe141"
    },
    {
      "sha": "148c86d2b5",
      "message": "Update README to fix 8.0 build and update build.sh to support 9.0 (#76)",
      "date": "2025-12-16",
      "repo": "valkey-bloom",
      "pr_url": "https://github.com/valkey-io/valkey-bloom/pull/76",
      "commit_url": "https://github.com/valkey-io/valkey-bloom/commit/148c86d2b595857ac05001e59f1886f394b35aa3"
    },
    {
      "sha": "3a29d8a429",
      "message": "Fix typo in tst/integration/README.md (#90)",
      "date": "2025-12-15",
      "repo": "valkey-json",
      "pr_url": "https://github.com/valkey-io/valkey-json/pull/90",
      "commit_url": "https://github.com/valkey-io/valkey-json/commit/3a29d8a429ac5ce6d5d5ca18b4d36af0eb03c477"
    },
    {
      "sha": "51f871ae52",
      "message": "Strictly check CRLF when parsing querybuf (#2872)",
      "date": "2025-12-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2872",
      "commit_url": "https://github.com/valkey-io/valkey/commit/51f871ae52e3ed17899a2ed23439aac5c6c03547"
    },
    {
      "sha": "48e0cbbb41",
      "message": "Fix commandlog large-reply when using reply copy avoidance (#2652)",
      "date": "2025-12-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2652",
      "commit_url": "https://github.com/valkey-io/valkey/commit/48e0cbbb415a56c88ec3e3359a3054b0995fdd45"
    },
    {
      "sha": "29d3244937",
      "message": "Make the COB soft limit also use repl-backlog-size when its value is smaller (#2866)",
      "date": "2025-12-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2866",
      "commit_url": "https://github.com/valkey-io/valkey/commit/29d3244937767bcafd586b96638847c5dc537c77"
    },
    {
      "sha": "95f2adffa5",
      "message": "Add acl_access_denied_tls_cert info field to INFO command (#387)",
      "date": "2025-12-04",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/387",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/95f2adffa5df819f22f28d506e6a009a23f628ec"
    },
    {
      "sha": "e4acbe7b84",
      "message": "Update cluster-migrateslots doc to mention cluster-cancelslotmigrations (#388)",
      "date": "2025-12-03",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/388",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/e4acbe7b84b1a8a2435cb0baed3983f4e0093b91"
    },
    {
      "sha": "4a0e20bbc9",
      "message": "Handle failed psync log when there is no replication backlog (#2886)",
      "date": "2025-12-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2886",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4a0e20bbc91da1e776c619df741e0e9377193602"
    },
    {
      "sha": "a087cc1132",
      "message": "Add psync offset range information to the failed psync log (#2877)",
      "date": "2025-11-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2877",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a087cc1132cbe2ae17d6063a32c1543f8a31c39e"
    },
    {
      "sha": "4e652bf0bf",
      "message": "Improve the doc of replication backlog fields (#383)",
      "date": "2025-11-28",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/383",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/4e652bf0bf1d166c193946730446ad7f187bbf81"
    },
    {
      "sha": "d16788e52d",
      "message": "Fix discarded-qualifiers warnings reported by fedorarawhide (#2874)",
      "date": "2025-11-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2874",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d16788e52dfe1c80627975bb503d5e9ba6ae58ae"
    },
    {
      "sha": "a6372c38c3",
      "message": "Update ROLE command documentation (#386)",
      "date": "2025-11-27",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/386",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/a6372c38c3b3765eb31d4af3491dcb7d7078f2d2"
    },
    {
      "sha": "1b2151c7c2",
      "message": "Update and add more INFO fields about replication in INFO command (#385)",
      "date": "2025-11-26",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/385",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/1b2151c7c205e61494adae19a8cf6e33b86f123b"
    },
    {
      "sha": "8ea7f1330c",
      "message": "Update dual channel replication conf to mention the local buffer is imited by COB (#2824)",
      "date": "2025-11-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2824",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8ea7f1330cbc80fe016fc5110ec91efe2369ecee"
    },
    {
      "sha": "8189fe5c42",
      "message": "Add rdb_transmitted to replstateToString so that we can see it in INFO (#2833)",
      "date": "2025-11-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2833",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8189fe5c42573f96229bea7d427b650a4354be31"
    },
    {
      "sha": "aef56e52f5",
      "message": "Fix timing issue in dual channel replication COB test (#2847)",
      "date": "2025-11-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2847",
      "commit_url": "https://github.com/valkey-io/valkey/commit/aef56e52f5e9a32aa115475118c9aca1bb27609f"
    },
    {
      "sha": "a06cf15b20",
      "message": "Allow dual channel full sync in plain failover (#2659)",
      "date": "2025-11-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2659",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a06cf15b20cdbd7ba91b03f826b0d512d56d618b"
    },
    {
      "sha": "331a852821",
      "message": "Change DEFAULT_WAIT_BEFORE_RDB_CLIENT_FREE from 60s to 5s (#2829)",
      "date": "2025-11-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2829",
      "commit_url": "https://github.com/valkey-io/valkey/commit/331a85282152070113353fa3b287c3b9186b2871"
    },
    {
      "sha": "7ffe4dcec4",
      "message": "Remove the EXAT and PXAT from some HFE notifications tests (#2831)",
      "date": "2025-11-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2831",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7ffe4dcec4e9d03d484e61b106b43000f841d246"
    },
    {
      "sha": "9acea36841",
      "message": "Fix outdated comment around clusterLink->flags (#2752)",
      "date": "2025-10-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2752",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9acea36841903eb08fb9e12a5febbf112ab8200d"
    },
    {
      "sha": "5d3cb3d04c",
      "message": "Initialize the lua attributes of the luaFunction script (#2750)",
      "date": "2025-10-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2750",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5d3cb3d04c100c938f5859f12bdc3a76dc86900f"
    },
    {
      "sha": "b4c93cc9c2",
      "message": "FUNCTION FLUSH re-create lua VM, fix flush not gc, fix flush async + load crash (#1826)",
      "date": "2025-10-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1826",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b4c93cc9c25e08d2da9c12cb7e109a176e3e885c"
    },
    {
      "sha": "af45feea12",
      "message": "Remove the outupdated unknown key/value pairs comment in CLUSTER SYNCSLOTS ESTABLISH (#2498)",
      "date": "2025-10-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2498",
      "commit_url": "https://github.com/valkey-io/valkey/commit/af45feea12bb7ec852f2265582dd4e9250724ec1"
    },
    {
      "sha": "ccf6fca5f4",
      "message": "Add `Slot migration is ok when the replicas are down test` back (#2727)",
      "date": "2025-10-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2727",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ccf6fca5f426d3deebbcd45b3c48b11c09a66a72"
    },
    {
      "sha": "b1edacb45a",
      "message": "Update active expire doc to remove the potentially ambiguous - (#367)",
      "date": "2025-10-09",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/367",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/b1edacb45acfccd76a3eeb58d4652fbfaffa199f"
    },
    {
      "sha": "80cec0a184",
      "message": "Minor fix for dual rdb channel connection conn error log (#2658)",
      "date": "2025-09-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2658",
      "commit_url": "https://github.com/valkey-io/valkey/commit/80cec0a18459af92cf0f613e5bbe4a52892ce15d"
    },
    {
      "sha": "f6a0f8cfc0",
      "message": "Separate RDB snapshotting from atomic slot migration (#2533)",
      "date": "2025-09-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2533",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f6a0f8cfc0079407d9df05ec50cedac8f9c684b6"
    },
    {
      "sha": "5a9ee5b944",
      "message": "Skip codeql-analysis ci on documentation changes as well (#2567)",
      "date": "2025-09-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2567",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5a9ee5b944c6e7dac813e5f0eef6edf51d105317"
    },
    {
      "sha": "eebed88429",
      "message": "Remove deny_blocking check in moduleBlockClient, cleanup code and doc (#2215)",
      "date": "2025-09-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2215",
      "commit_url": "https://github.com/valkey-io/valkey/commit/eebed884294c31c6a9040e5da4fd7f2830e2bf31"
    },
    {
      "sha": "e19fc4d1e6",
      "message": "Add jacob as a commiter (#2566)",
      "date": "2025-08-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2566",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e19fc4d1e6d1262531ddb77fb62087d91223394d"
    },
    {
      "sha": "88cd2086ae",
      "message": "Split SLOT_EXPORT_AUTHENTICATING into SEND and READ to avoid synchronous reading of auth response (#2494)",
      "date": "2025-08-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2494",
      "commit_url": "https://github.com/valkey-io/valkey/commit/88cd2086aef25183ae0c5fb8bc154d8206dd07f1"
    },
    {
      "sha": "39fade42d1",
      "message": "Do not migrate function in new atomic slot migration (#2547)",
      "date": "2025-08-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2547",
      "commit_url": "https://github.com/valkey-io/valkey/commit/39fade42d11a22d4a13beb98d6e36adaa12ecba3"
    },
    {
      "sha": "682fc0b419",
      "message": "Remove the trailing chars of the --cluster reshard log message in valkey-cli (#2560)",
      "date": "2025-08-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2560",
      "commit_url": "https://github.com/valkey-io/valkey/commit/682fc0b4197311a2bc0ea2512151ee29a2b1d327"
    },
    {
      "sha": "1ba622bad5",
      "message": "Update tests/xxx/tmp/.gitignore to ignore everything (#2542)",
      "date": "2025-08-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2542",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1ba622bad5369ece4e88946e7a9b1d65541bc8db"
    },
    {
      "sha": "8c55547999",
      "message": "Don't allow slot migration to myself node (#2497)",
      "date": "2025-08-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2497",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8c55547999a980680997a2c0c2bd292a7112da9c"
    },
    {
      "sha": "ac515159a1",
      "message": "Remove debug logging from cluster-flush-slot.tcl (#2535)",
      "date": "2025-08-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2535",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ac515159a1e79ada6e43ed49c9ed9cb11178c50d"
    },
    {
      "sha": "a97d584cc2",
      "message": "Fix slot-info expand not working, kvstoreHashtableExpand always creat\u2026 (#2466)",
      "date": "2025-08-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2466",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a97d584cc20013c6797843a30633f0f268874d28"
    },
    {
      "sha": "fb9503bfd1",
      "message": "CLUSTER SYNCSLOTS ESTABLISH added source node == myself check (#2500)",
      "date": "2025-08-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2500",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fb9503bfd12bf8331647b151c3af0b28fa4d7e7a"
    },
    {
      "sha": "7a5c0d0ebf",
      "message": "Fix memory leak in saveSnapshotToConnectionSockets (#2503)",
      "date": "2025-08-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2503",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7a5c0d0ebf72354f122c64cd52788c671ae04064"
    },
    {
      "sha": "4a12021707",
      "message": "Fix memory leak in rdbLoadObject when loading a wrong HFE (#2502)",
      "date": "2025-08-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2502",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4a120217075c5ca4bacbeb13db6fdfe9df9e321e"
    },
    {
      "sha": "aefed3d363",
      "message": "Don't allow resize hashtable if rehashing is ongoing (#2465)",
      "date": "2025-08-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2465",
      "commit_url": "https://github.com/valkey-io/valkey/commit/aefed3d363d1c7d7cb391d3f605484c78c9a88f2"
    },
    {
      "sha": "3d1ff2a38c",
      "message": "Remove if condition and disable the new failover test (#2477)",
      "date": "2025-08-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2477",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3d1ff2a38c3a17644afa4b64f086ea110df5fa86"
    },
    {
      "sha": "7a9ef29f1a",
      "message": "Change the same shard failover assert to if condition to avoid crash (#2431)",
      "date": "2025-08-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2431",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7a9ef29f1ae6baa571a1ca30e68eed1fa0304fa2"
    },
    {
      "sha": "8131c2b07b",
      "message": "Add test for failover sub-replica replication loop case (#2456)",
      "date": "2025-08-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2456",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8131c2b07bcff0dd62c79f8495e45563eacadec1"
    },
    {
      "sha": "094c80b9ce",
      "message": "Print error context when test fails (#2437)",
      "date": "2025-08-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2437",
      "commit_url": "https://github.com/valkey-io/valkey/commit/094c80b9cedac7a63cb10ed7ec0ebdf439132b8c"
    },
    {
      "sha": "db11e41dfc",
      "message": "Add STALE command flag to SCRIPT-EXISTS, SCRIPT-SHOW and SCRIPT-FLUSH (#2419)",
      "date": "2025-08-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2419",
      "commit_url": "https://github.com/valkey-io/valkey/commit/db11e41dfcc391501e3d9955d472c0983ffe7ddc"
    },
    {
      "sha": "fa8659d309",
      "message": "Print the complete log instead of just the crash log in log_crashes (#2428)",
      "date": "2025-08-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2428",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fa8659d3099d01206cc8db310cfd28201c26e69e"
    },
    {
      "sha": "dceb9f3b22",
      "message": "Make ./runtest --dump-logs dump logs on valgrind / sanitizer errors (#2427)",
      "date": "2025-08-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2427",
      "commit_url": "https://github.com/valkey-io/valkey/commit/dceb9f3b229d232744ee68d12eb2c9edd83e856f"
    },
    {
      "sha": "a50690f02c",
      "message": "Update swapdb command comment to mention why cluster mode is not allowed (#2391)",
      "date": "2025-08-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2391",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a50690f02c08e4e67b8b472f81587b05c405b6f7"
    },
    {
      "sha": "36bd5bf926",
      "message": "Cleanup and rename isExpiryTableValidForSamplingCb to expiryTableShouldSkipForSamplingCb (#2395)",
      "date": "2025-08-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2395",
      "commit_url": "https://github.com/valkey-io/valkey/commit/36bd5bf926055882b10a65bf277327e5caa96871"
    },
    {
      "sha": "82acd7a57b",
      "message": "Mention WAITAOF will be blocked in CLIENT PAUSE WRITE as well just like WAIT (#336)",
      "date": "2025-08-05",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/336",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/82acd7a57b8013a577629b6064f70819b6026ad4"
    },
    {
      "sha": "34480ac35e",
      "message": "Initialize rdbstate.key_type to -1 at the beginning (#2381)",
      "date": "2025-08-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2381",
      "commit_url": "https://github.com/valkey-io/valkey/commit/34480ac35eaab8e08afecf68a53238a553098b93"
    },
    {
      "sha": "e16fc8d8c8",
      "message": "Fix check-rdb --stats crash with empty RDB (#2382)",
      "date": "2025-08-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2382",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e16fc8d8c8afc474f9a275276d75d42f6162177c"
    },
    {
      "sha": "43c4af0b0e",
      "message": "Remove obsolete BLOCKED_WAITAOF comment (#2374)",
      "date": "2025-08-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2374",
      "commit_url": "https://github.com/valkey-io/valkey/commit/43c4af0b0e1b19868fbbf940d479a9f0e02f1baa"
    },
    {
      "sha": "3b12132ac0",
      "message": "Rename trace bgsave type to rdb and aof (#2400)",
      "date": "2025-08-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2400",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3b12132ac0be654abaf1cd04fa9fdf8f44314327"
    },
    {
      "sha": "ee5b72b184",
      "message": "Fix dual-channel-replication test due to typo error and stabilize it (#2386)",
      "date": "2025-07-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2386",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ee5b72b18481bb975ae7b2813515df3b5d100b2b"
    },
    {
      "sha": "a481fe228c",
      "message": "Update clusterMoveNodeSlots to also move importing slots and migrating slots (#2370)",
      "date": "2025-07-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2370",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a481fe228c16c4e33e35f3c2fc1770b34db3737b"
    },
    {
      "sha": "f21beaf4f7",
      "message": "Defrag should only skip non-existent dbs, not empty dbs (#2379)",
      "date": "2025-07-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2379",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f21beaf4f7be1c5be37f1183e7d4c250f8fe3498"
    },
    {
      "sha": "e5956d0c23",
      "message": "Fix client tracking memory overhead calculation (#2360)",
      "date": "2025-07-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2360",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e5956d0c23863fef127202e06021c171b688c78a"
    },
    {
      "sha": "0999007f5c",
      "message": "Include command fullname in error message when returning NO_MULTI error (#2286)",
      "date": "2025-07-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2286",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0999007f5c631b74e0eef58322086477c2a100b7"
    },
    {
      "sha": "78e7208b03",
      "message": "Add extensions supported to cluster link layer to propagate extension faster during handshake (#2310)",
      "date": "2025-07-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2310",
      "commit_url": "https://github.com/valkey-io/valkey/commit/78e7208b030d31149aceddad8048da4d1b0d9df2"
    },
    {
      "sha": "507042df96",
      "message": "Fix replica (the old primary) claims to sitll have slots after manual failover (#2301)",
      "date": "2025-07-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2301",
      "commit_url": "https://github.com/valkey-io/valkey/commit/507042df9642a0f70f991d87003ffaab2246ceea"
    },
    {
      "sha": "c782b5aeac",
      "message": "Fix DEBUG CLUSTERLINK KILL args check to avoid crash (#2333)",
      "date": "2025-07-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2333",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c782b5aeac9b25b3b6e84930f067497ec2e1a384"
    },
    {
      "sha": "e279b00f85",
      "message": "Generate a new shard_id when the replica executes CLUSTER RESET SOFT (#2283)",
      "date": "2025-07-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2283",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e279b00f854b7b4cfe06f8a3eb7c89fd7ce25bdc"
    },
    {
      "sha": "a62f83db8f",
      "message": "Make valkey-server --help/-h output to stdout and exit with 0 (#2296)",
      "date": "2025-07-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2296",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a62f83db8f639883f214cdcebd343263565bda73"
    },
    {
      "sha": "fc7c04e4f8",
      "message": "Fix missing response when AUTH is errored inside a transaction (#2287)",
      "date": "2025-07-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2287",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fc7c04e4f8ba86dfbac1ec059db457fb44ed0a2d"
    },
    {
      "sha": "1e05724f59",
      "message": "Add SAFE option to SHUTDOWN to reject shutdown in unsafe situations (#2195)",
      "date": "2025-07-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2195",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1e05724f592025535d4e53a700d65486e715a2a8"
    },
    {
      "sha": "fef4dbf046",
      "message": "Move auth check to the front, before command exist/arity/protected check (#1475)",
      "date": "2025-07-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1475",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fef4dbf046d60b52b116135c08d73a20195072fa"
    },
    {
      "sha": "5a83d613f2",
      "message": "Add SAFE option to SHUTDOWN to reject shutdown in unsafe situations (#325)",
      "date": "2025-07-01",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/325",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/5a83d613f2272982fa0bf4ae6fa03822d214b6c7"
    },
    {
      "sha": "d37dc527d0",
      "message": "Use objectGetExpire instead of getExpire to reduce expire hashtable lookup (#2280)",
      "date": "2025-06-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2280",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d37dc527d0b4865cf38ef9939551bd2b5cc16c72"
    },
    {
      "sha": "23fb9f2b51",
      "message": "Start failover without waiting for the next cluster cron cycle (#2209)",
      "date": "2025-06-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2209",
      "commit_url": "https://github.com/valkey-io/valkey/commit/23fb9f2b5162752fbf42d892c6ff311a346565b8"
    },
    {
      "sha": "a0b8d5e378",
      "message": "Save config file after replica migration and brocast a PONG when role changed (#1677)",
      "date": "2025-06-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1677",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a0b8d5e378cdd999aaca2cafdb5c0b4d0aaed581"
    },
    {
      "sha": "db639c99f7",
      "message": "Check module NO_FAILOVER flag before calling clusterHandleReplicaFailover (#2269)",
      "date": "2025-06-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2269",
      "commit_url": "https://github.com/valkey-io/valkey/commit/db639c99f7f8cd530405a991b24b61e945b3f281"
    },
    {
      "sha": "94a95cd368",
      "message": "Cleanup aof temp files in sigShutdownHandler before exiting (#1482)",
      "date": "2025-06-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1482",
      "commit_url": "https://github.com/valkey-io/valkey/commit/94a95cd3680eec33481563e5a45a3756b14b3e5d"
    },
    {
      "sha": "3a01c7f7e3",
      "message": "Fix unixsocket too long cause addr / laddr being truncated in CLIENT INFO / LIST and logging (#2216)",
      "date": "2025-06-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2216",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3a01c7f7e3c5af06ef53241efe3601525c3eb6d0"
    },
    {
      "sha": "ceb09b0a9d",
      "message": "Reset failover failed primary rank when doing a manual failover (#2226)",
      "date": "2025-06-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2226",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ceb09b0a9df8a72e544d4837cf6c27221c6f15c8"
    },
    {
      "sha": "22872611fa",
      "message": "Updates for lttng daily CI to be able to skip it or notify it (#2197)",
      "date": "2025-06-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2197",
      "commit_url": "https://github.com/valkey-io/valkey/commit/22872611fa0c999f05392df037075faf9e2e5edd"
    },
    {
      "sha": "5b368352bf",
      "message": "Remove unused repl_offset_time field in clusterNode (#2198)",
      "date": "2025-06-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2198",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5b368352bf830581e317a9fbf59a88ec5d80ae34"
    },
    {
      "sha": "2019337e74",
      "message": "Add packet-drop to fix the new flaky failover test (#2196)",
      "date": "2025-06-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2196",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2019337e7442a1421955716bb7663801a2f29c8d"
    },
    {
      "sha": "1b531e560b",
      "message": "Call makeObjectShared to normalize a shared object into a true shared object (#1566)",
      "date": "2025-06-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1566",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1b531e560b6256a26692382ad622fc975a683f36"
    },
    {
      "sha": "4771660689",
      "message": "Update extended-redis-compatibility conf to remove the specific words (#2192)",
      "date": "2025-06-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2192",
      "commit_url": "https://github.com/valkey-io/valkey/commit/47716606896c9c6ea4f7aa024957fb946f5b0e9f"
    },
    {
      "sha": "767302e3ae",
      "message": "Update commandlog parameters conf text to mention special value settings (#2074)",
      "date": "2025-06-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2074",
      "commit_url": "https://github.com/valkey-io/valkey/commit/767302e3ae6ebb535c3ce49279485e135f0e23d7"
    },
    {
      "sha": "5cc2b25753",
      "message": "Fix cluster myself CLUSTER SLOTS/NODES wrong port after updating port/tls-port (#2186)",
      "date": "2025-06-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2186",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5cc2b2575300f09c004bf73f0a5f69ed1775c00c"
    },
    {
      "sha": "3bc40be6cd",
      "message": "CLIENT UNBLOCK should't be able to unpause paused clients (#2117)",
      "date": "2025-06-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2117",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3bc40be6cdef24f9db8a30e5f8659ea5c404027a"
    },
    {
      "sha": "476671be19",
      "message": "Fix replica can't finish failover when config epoch is outdated (#2178)",
      "date": "2025-06-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2178",
      "commit_url": "https://github.com/valkey-io/valkey/commit/476671be194e4296b9100663560193069fa46453"
    },
    {
      "sha": "0039adcc7e",
      "message": "Remove dead conditions around the multi/exec check (#2168)",
      "date": "2025-06-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2168",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0039adcc7eea28a4c3ea9d93380edfda72d16956"
    },
    {
      "sha": "831220a30b",
      "message": "Skip empty db when doing FLUSHALL to reduce some NOP (#2151)",
      "date": "2025-05-31",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2151",
      "commit_url": "https://github.com/valkey-io/valkey/commit/831220a30b5973fcd4b999e3f541ba53e057850e"
    },
    {
      "sha": "28f48ff638",
      "message": "Changes and fixes for the new DELIFEQ command (#2120)",
      "date": "2025-05-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2120",
      "commit_url": "https://github.com/valkey-io/valkey/commit/28f48ff638ec00409a1a2b5ddae979c90ed2bb1c"
    },
    {
      "sha": "1119765df9",
      "message": "Fix CLUSTER RESET to use lazyfree-lazy-user-flush to do the lazyfree (#1931)",
      "date": "2025-04-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1931",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1119765df9511936d8bee80b7d1769a4bf5dc28b"
    },
    {
      "sha": "d1053ac319",
      "message": "Ignore stale gossip packets that arrive out of order (#1777)",
      "date": "2025-04-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1777",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d1053ac3198795a6e913b1cf143f06f3d8631734"
    },
    {
      "sha": "44dafba2ce",
      "message": "Trigger manual failover on SIGTERM / shutdown to cluster primary (#1091)",
      "date": "2025-04-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1091",
      "commit_url": "https://github.com/valkey-io/valkey/commit/44dafba2ce5635c5945c52bc6d2aa798e3537448"
    },
    {
      "sha": "ea2e48a807",
      "message": "Fix TCL tmp dir leak in the ACL load test (#1895)",
      "date": "2025-03-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1895",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ea2e48a807e1d4a1a5a684a2a699eda1934a0c6f"
    },
    {
      "sha": "4de8cf3567",
      "message": "Add missing close_replication_stream on multi test (#1841)",
      "date": "2025-03-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1841",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4de8cf3567b4dfd3a541219462b22d46c730c4b4"
    },
    {
      "sha": "bcd2f952de",
      "message": "Save config file and brocast the PONG when configEpoch changed (#1813)",
      "date": "2025-03-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1813",
      "commit_url": "https://github.com/valkey-io/valkey/commit/bcd2f952dead1da28b61e79184d8bd0bb9042dea"
    },
    {
      "sha": "3efe8419ec",
      "message": "Fix timing issue in the module propagate test (#1815)",
      "date": "2025-03-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1815",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3efe8419ec98aeb41abf5897501e5fb24100e126"
    },
    {
      "sha": "e03b3f1fc8",
      "message": "Add cluster-manual-failover-timeout to configure the timeout for manual failover (#1690)",
      "date": "2025-02-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1690",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e03b3f1fc87911e6a7404cf357df47f9a1b6037c"
    },
    {
      "sha": "bc1b3ba65a",
      "message": "Add cluster-manual-failover-timeout desc in CLUSTER FAILOVER command page (#238)",
      "date": "2025-02-27",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/238",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/bc1b3ba65a3420df2d2140ae811814dc91455f9a"
    },
    {
      "sha": "b360f96a7d",
      "message": "Fix temp file leak druing replication error handling (#1721)",
      "date": "2025-02-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1721",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b360f96a7d658e89af8575fd37f121c6705339fa"
    },
    {
      "sha": "99ec47a784",
      "message": "Simplify isNodeAvailable function and add comments (#994)",
      "date": "2025-02-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/994",
      "commit_url": "https://github.com/valkey-io/valkey/commit/99ec47a784b47f9d21d59eb30dcb18a39ac968ef"
    },
    {
      "sha": "eeda8ae748",
      "message": "Reset failover auth time when myself won the failover (#1711)",
      "date": "2025-02-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1711",
      "commit_url": "https://github.com/valkey-io/valkey/commit/eeda8ae748622f96abf68e13b576cdfcb0cc8ef8"
    },
    {
      "sha": "4e0149a381",
      "message": "Fix new benchmark test under the TLS (#1710)",
      "date": "2025-02-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1710",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4e0149a381ac5e030537712f046c235110168b60"
    },
    {
      "sha": "8fc37a0e0b",
      "message": "Fix undefined behavior warning in UBSAN (#1709)",
      "date": "2025-02-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1709",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8fc37a0e0b32974450592303b612df09bb64821e"
    },
    {
      "sha": "8988a6135d",
      "message": "Update availability-zone conf comment to mention hello command (#1695)",
      "date": "2025-02-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1695",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8988a6135d8568c9834b490096492de5b1c153bf"
    },
    {
      "sha": "3828936fe5",
      "message": "Fix outdated slot info comments in clusterGenNodesSlotsInfo (#1696)",
      "date": "2025-02-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1696",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3828936fe54d4c77030c5db98ce4521ad6aaaf7b"
    },
    {
      "sha": "b716fe72d2",
      "message": "Add paused_reason field for INFO CLIENTS (#227)",
      "date": "2025-02-10",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/227",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/b716fe72d24a898b30b8f6a15e527108da6a9891"
    },
    {
      "sha": "dfff87bb99",
      "message": "Add availability_zone filed to INFO command  (#228)",
      "date": "2025-02-10",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/228",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/dfff87bb998983bb33d7c359af4dbb2be4f42674"
    },
    {
      "sha": "e9ed53c862",
      "message": "Improved failover pause stats test stability (#1682)",
      "date": "2025-02-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1682",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e9ed53c862af5b38e99c15670b9f0e382196b213"
    },
    {
      "sha": "da3f1c6144",
      "message": "Add paused_reason to INFO CLIENTS (#1564)",
      "date": "2025-02-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1564",
      "commit_url": "https://github.com/valkey-io/valkey/commit/da3f1c6144cf3e748545adc13fe607bcdf96609f"
    },
    {
      "sha": "0579103aef",
      "message": "Add reply schema for LATENCY-LATESTS new fields (#1678)",
      "date": "2025-02-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1678",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0579103aefcfc4797ef9ead4cdbea67bfc57a58a"
    },
    {
      "sha": "f875fceea7",
      "message": "Fix client querybuf resize test by skipping the clientsCron (#1667)",
      "date": "2025-02-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1667",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f875fceea7812af9c554cb1f742d4987017b9168"
    },
    {
      "sha": "6eaf0887cc",
      "message": "Extend LATENCY LATEST to add sum / cnt stats (#1570)",
      "date": "2025-02-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1570",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6eaf0887cc91d43b37b9bc3e9349ea639134a1ed"
    },
    {
      "sha": "511b975a20",
      "message": "Add sum and cnt stats in LATENCY LATEST (#224)",
      "date": "2025-02-04",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/224",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/511b975a20adfd15882cb5da9c2b0a7fe4b7299d"
    },
    {
      "sha": "4b8f3ed9ac",
      "message": "Do command existence and arity checks when loading AOF to avoid crash (#1614)",
      "date": "2025-01-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1614",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4b8f3ed9acf3103349b6368407fc48bef55b3327"
    },
    {
      "sha": "cda9eee8c9",
      "message": "Allow clang-format to be triggered in push events (#1565)",
      "date": "2025-01-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1565",
      "commit_url": "https://github.com/valkey-io/valkey/commit/cda9eee8c9161a418be8dbd399909aa64d3fb487"
    },
    {
      "sha": "11cb8ee27c",
      "message": "Add latency stats around cluster config file operations (#1534)",
      "date": "2025-01-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1534",
      "commit_url": "https://github.com/valkey-io/valkey/commit/11cb8ee27cf0ef7a1ebce524cfe5afac3b92fc84"
    },
    {
      "sha": "10357ceda5",
      "message": "Mark the node as FAIL when the node is marked as NOADDR and broadcast the FAIL (#1191)",
      "date": "2025-01-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1191",
      "commit_url": "https://github.com/valkey-io/valkey/commit/10357ceda5dce8baf42a4a585b913d490f11e56f"
    },
    {
      "sha": "211b250aad",
      "message": "Do election in order based on failed primary rank to avoid voting conflicts (#1018)",
      "date": "2025-01-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1018",
      "commit_url": "https://github.com/valkey-io/valkey/commit/211b250aad1db6e7a9480fd3c896786d25210fb2"
    },
    {
      "sha": "d6bdd9e7d7",
      "message": "Fix module LatencyAddSample still work when latency-monitor-threshold is 0 (#1541)",
      "date": "2025-01-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1541",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d6bdd9e7d7f901c98d86a2f5ec79450130d0f5e7"
    },
    {
      "sha": "e60990e579",
      "message": "Fix crash when freeing newly created node when nodeIp2String fail (#1535)",
      "date": "2025-01-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1535",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e60990e5798a4a9a943aa444dba24855d59674c0"
    },
    {
      "sha": "b207b421bc",
      "message": "Fix new cli subscribed mode test in cluster mode (#1533)",
      "date": "2025-01-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1533",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b207b421bca51e49f510abaa6c5ffaa54c4eb5bb"
    },
    {
      "sha": "c0014ef15e",
      "message": "Check whether to switch to fail when setting the node to pfail in cron (#1061)",
      "date": "2025-01-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1061",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c0014ef15e2b09ce6aaf2184aacd20a041e19018"
    },
    {
      "sha": "33b824137e",
      "message": "Explicitly check C_ERR condition to improve readability in clusterSaveConfig (#1505)",
      "date": "2025-01-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1505",
      "commit_url": "https://github.com/valkey-io/valkey/commit/33b824137e4d86e69e50cd7843695af8bec8dff1"
    },
    {
      "sha": "da92c1d6c8",
      "message": "Document all command flags near serverCommand (#1474)",
      "date": "2024-12-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1474",
      "commit_url": "https://github.com/valkey-io/valkey/commit/da92c1d6c8f3dd58f3b03da3c468a5fab162fd8f"
    },
    {
      "sha": "d00c856448",
      "message": "Fix switch case compilation error in the new helloscripting (#1472)",
      "date": "2024-12-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1472",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d00c856448e918feb6bff47cf3fbd62dc0f861f5"
    },
    {
      "sha": "ca0b0c662a",
      "message": "Clear outdated failure reports more accurately (#1184)",
      "date": "2024-12-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1184",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ca0b0c662a991f84d8e11a0d433e06fdeae6980b"
    },
    {
      "sha": "97029953a0",
      "message": "Minor log fixes when failover auth denied due to slot epoch (#1341)",
      "date": "2024-12-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1341",
      "commit_url": "https://github.com/valkey-io/valkey/commit/97029953a094a2ed27382bd9fed3d55c784834d0"
    },
    {
      "sha": "e024b4bd27",
      "message": "Drop the MEET packet if the link node is in handshake state (#1436)",
      "date": "2024-12-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1436",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e024b4bd27645a33c5f317792051c5ae3a97fa56"
    },
    {
      "sha": "ad24220681",
      "message": "Automatic failover vote is not limited by two times the node timeout (#1356)",
      "date": "2024-12-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1356",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ad242206819059937244eb519fa612936aee4143"
    },
    {
      "sha": "7d72fada2c",
      "message": "Fix wrong file name in build-release-packages.yml (#1437)",
      "date": "2024-12-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1437",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7d72fada2c349eb5b91c7e33099adc167abb0e99"
    },
    {
      "sha": "d588bb4406",
      "message": "Skip build-release-packages CI job in forks (#1438)",
      "date": "2024-12-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1438",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d588bb440668056a5bc64251739b9349dbe719b3"
    },
    {
      "sha": "1acf7f71c0",
      "message": "Fix memory leak in the new hashtable unittest (#1421)",
      "date": "2024-12-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1421",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1acf7f71c0324747de6b0ed9118f065dde0a5a92"
    },
    {
      "sha": "7e564887b9",
      "message": "Set HIDDEN_CONFIG flag on events-per-io-thread (#1408)",
      "date": "2024-12-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1408",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7e564887b93ea3d1008cd2ea2d2bb82c4a4b0a04"
    },
    {
      "sha": "1ba85d002a",
      "message": "Use binary representation in assert crash log, cleanup in crash log (#1410)",
      "date": "2024-12-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1410",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1ba85d002a824a12b0107bdd2b493a3a0516cec9"
    },
    {
      "sha": "924729eb16",
      "message": "Fix the election was reset wrongly before failover epoch was obtained (#1339)",
      "date": "2024-12-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1339",
      "commit_url": "https://github.com/valkey-io/valkey/commit/924729eb1695a8a5913fe32531a8d520560fe70b"
    },
    {
      "sha": "176fafcaf7",
      "message": "Add a note to conf about the dangers of modifying dir at runtime (#887)",
      "date": "2024-12-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/887",
      "commit_url": "https://github.com/valkey-io/valkey/commit/176fafcaf71793efdadefba8e49ef711748b0c20"
    },
    {
      "sha": "fbbfe5d3d3",
      "message": "Print logs when the cluster state changes to fail or the fail reason changes (#1188)",
      "date": "2024-12-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1188",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fbbfe5d3d3833c74d86c324ca9ffee8b97856724"
    },
    {
      "sha": "9c48f56790",
      "message": "Reset repl_down_since to zero only on state change (#1149)",
      "date": "2024-12-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1149",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9c48f567907087637e19bf30a5a137d8b50e0df3"
    },
    {
      "sha": "a939cb88ee",
      "message": "Handle keyIsExpiredWithDictIndex to make it check for import mode (#1368)",
      "date": "2024-11-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1368",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a939cb88ee0c0512c003106be483b7c6968b3e7f"
    },
    {
      "sha": "db7b7396ff",
      "message": "Make KEYS can visit expired key in import-source state (#1326)",
      "date": "2024-11-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1326",
      "commit_url": "https://github.com/valkey-io/valkey/commit/db7b7396ff1cc98832396a57e8d3e76e0eebd5fa"
    },
    {
      "sha": "5d08149e72",
      "message": "Use fake client flag to replace not conn check (#1198)",
      "date": "2024-11-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1198",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5d08149e726bb7d393d76401c7be683ceaf67b7b"
    },
    {
      "sha": "469d41fb37",
      "message": "Avoid double close on repl_transfer_fd (#1349)",
      "date": "2024-11-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1349",
      "commit_url": "https://github.com/valkey-io/valkey/commit/469d41fb37d7c88d508b0a8c7ac495a8f00c717f"
    },
    {
      "sha": "2d48a39c27",
      "message": "Save open's errno when opening temp rdb fails to prevent it from being modified (#1347)",
      "date": "2024-11-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1347",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2d48a39c2781e72200b2e360ef250009c6701711"
    },
    {
      "sha": "653d5f7fe3",
      "message": "Support empty callback on function and free temp function in async way (#1334)",
      "date": "2024-11-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1334",
      "commit_url": "https://github.com/valkey-io/valkey/commit/653d5f7fe3d44adfb2a2e10c9110a3efacd3f0da"
    },
    {
      "sha": "9851006d6d",
      "message": "Add short client info log to CLUSTER MEET / FORGET / RESET commands (#1249)",
      "date": "2024-11-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1249",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9851006d6d7af570d7f38025f4b1de68f12c7731"
    },
    {
      "sha": "b9d224097a",
      "message": "Brocast a PONG to all node in cluster when role changed (#1295)",
      "date": "2024-11-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1295",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b9d224097a46dbe62ec0857cb91e7c67505a200e"
    },
    {
      "sha": "979f4c1ceb",
      "message": "Add cmake-build-debug and cmake-build-release to gitignore (#1340)",
      "date": "2024-11-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1340",
      "commit_url": "https://github.com/valkey-io/valkey/commit/979f4c1ceba9eecc0f984101775b101ab87b58fc"
    },
    {
      "sha": "50aae13b0a",
      "message": "Skip reclaim file page cache test in valgrind (#1327)",
      "date": "2024-11-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1327",
      "commit_url": "https://github.com/valkey-io/valkey/commit/50aae13b0a7fffc6591ee2842d1ef4f2e59096dd"
    },
    {
      "sha": "c4be326c32",
      "message": "Make manual failover reset the on-going election to promote failover (#1274)",
      "date": "2024-11-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1274",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c4be326c3225ca4323ad7c21ccafee7197d0d539"
    },
    {
      "sha": "6038eda010",
      "message": "Make FUNCTION RESTORE FLUSH flush async based on lazyfree-lazy-user-flush (#1254)",
      "date": "2024-11-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1254",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6038eda010dfb99eff908cf0839cc41004383acd"
    },
    {
      "sha": "f553ccbda6",
      "message": "Use goto to cleanup error handling in readSyncBulkPayload (#1332)",
      "date": "2024-11-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1332",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f553ccbda674caa13d3cfa6e8096c5f19cb3a9c1"
    },
    {
      "sha": "ee386c92ff",
      "message": "Manual failover vote is not limited by two times the node timeout (#1305)",
      "date": "2024-11-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1305",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ee386c92ffa9724771e4980064fa279655e46f90"
    },
    {
      "sha": "132798b57d",
      "message": "Receipt of REPLCONF VERSION reply should be triggered by event (#1320)",
      "date": "2024-11-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1320",
      "commit_url": "https://github.com/valkey-io/valkey/commit/132798b57d7f95ad5901495d566578bf8ba71390"
    },
    {
      "sha": "d07674fc01",
      "message": "Fix sds unittest tests to check for zmalloc_usable_size (#1314)",
      "date": "2024-11-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1314",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d07674fc01fd9b3b4fdd8c13de74d3d28697ddc5"
    },
    {
      "sha": "aa2dd3ecb8",
      "message": "Stabilize replica migration test to make sure cluster config is consistent (#1311)",
      "date": "2024-11-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1311",
      "commit_url": "https://github.com/valkey-io/valkey/commit/aa2dd3ecb82bce5d76f7796c5e6df3e5c6e55203"
    },
    {
      "sha": "86f33ea2b0",
      "message": "Unprotect rdb channel when bgsave child fails in dual channel replication (#1297)",
      "date": "2024-11-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1297",
      "commit_url": "https://github.com/valkey-io/valkey/commit/86f33ea2b05e0f14391942c635a87974eb103937"
    },
    {
      "sha": "92181b6797",
      "message": "Fix primary crash when processing dirty slots during shutdown wait / failover wait / client pause (#1131)",
      "date": "2024-11-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1131",
      "commit_url": "https://github.com/valkey-io/valkey/commit/92181b67970efad6df82ea2319ccd4a266dfec5e"
    },
    {
      "sha": "4e2493e5c9",
      "message": "Kill diskless fork child asap when the last replica drop (#1227)",
      "date": "2024-11-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1227",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4e2493e5c961b36e6832e8d6ea259939b0cf0fde"
    },
    {
      "sha": "d3f3b9cc3a",
      "message": "Fix daily valgrind build with unit tests (#1309)",
      "date": "2024-11-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1309",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d3f3b9cc3a452b6d18e9e862dcae5a923952c8da"
    },
    {
      "sha": "6fba747c39",
      "message": "Fix log printing always shows the role as child under daemonize (#1301)",
      "date": "2024-11-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1301",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6fba747c39bee10e27942afabd2c46be4b4fae39"
    },
    {
      "sha": "2df56d87c0",
      "message": "Fix empty primary may have dirty slots data due to bad migration (#1285)",
      "date": "2024-11-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1285",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2df56d87c0ebe802f38e8922bb2ea1e4ca9cfa76"
    },
    {
      "sha": "a2d22c63c0",
      "message": "Fix replica not able to initate election in time when epoch fails (#1009)",
      "date": "2024-11-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1009",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a2d22c63c007eee1709ca71d9bf1e912fadb4f87"
    },
    {
      "sha": "167e8ab8de",
      "message": "Trigger the election immediately when doing a manual failover (#1081)",
      "date": "2024-11-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1081",
      "commit_url": "https://github.com/valkey-io/valkey/commit/167e8ab8de4c26a41222d94fcf0ccbd1864a9774"
    },
    {
      "sha": "4aacffa32d",
      "message": "Stabilize dual replication test to avoid getting LOADING error (#1288)",
      "date": "2024-11-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1288",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4aacffa32da07eb09b271c7c3dfbd58c7a2cb8d1"
    },
    {
      "sha": "1c18c80844",
      "message": "Fix incorrect cache_memory reset in functionsLibCtxClear (#1255)",
      "date": "2024-11-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1255",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1c18c8084451153c468e3224f31da43ff6fbd615"
    },
    {
      "sha": "22bc49c4a6",
      "message": "Try to stabilize the failover call in the slot migration test (#1078)",
      "date": "2024-11-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1078",
      "commit_url": "https://github.com/valkey-io/valkey/commit/22bc49c4a62894694f7977bb9047e1da27599c25"
    },
    {
      "sha": "a0b1cbad83",
      "message": "Change errno from EEXIST to EALREADY in serverFork if child process exists (#1258)",
      "date": "2024-11-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1258",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a0b1cbad83012b93f1e04f77cb3a067a9f37dd97"
    },
    {
      "sha": "12c5af03b8",
      "message": "Remove empty DB check branch in KEYS command (#1259)",
      "date": "2024-11-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1259",
      "commit_url": "https://github.com/valkey-io/valkey/commit/12c5af03b8b2d868fd35f4c1142162695f8dd41c"
    },
    {
      "sha": "a102852d5e",
      "message": "Fix timing issue in cluster-shards tests (#1243)",
      "date": "2024-11-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1243",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a102852d5ed5316063d680362f910e725070b9ee"
    },
    {
      "sha": "789a73b0d0",
      "message": "Minor fix to debug logging in replicationFeedStreamFromPrimaryStream (#1235)",
      "date": "2024-10-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1235",
      "commit_url": "https://github.com/valkey-io/valkey/commit/789a73b0d0fc9e2b754adbb39ed3ca92e9c30669"
    },
    {
      "sha": "5d2ff853a3",
      "message": "Fix minor repldbfd leak in updateReplicasWaitingBgsave if fstat fails (#1226)",
      "date": "2024-10-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1226",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5d2ff853a335af2bc2c1527da126b3e947269ad2"
    },
    {
      "sha": "2956367731",
      "message": "Maintain return value of rdbSaveDb after writing slot-info aux (#1222)",
      "date": "2024-10-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1222",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2956367731305f73005b44b26d6f665564731de3"
    },
    {
      "sha": "a21fe718f4",
      "message": "Limit CLUSTER_CANT_FAILOVER_DATA_AGE log to 10 times period (#1189)",
      "date": "2024-10-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1189",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a21fe718f46e5987dd9cf1ca698dce6d0d060795"
    },
    {
      "sha": "b803f7aeff",
      "message": "Cleaned up getSlotOrReply is return -1 instead of C_ERR (#1211)",
      "date": "2024-10-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1211",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b803f7aeff4ffe43c866a52d9ea830add33b5834"
    },
    {
      "sha": "5d70ccd70e",
      "message": "Make replica CLUSTER RESET flush async based on lazyfree-lazy-user-flush (#1190)",
      "date": "2024-10-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1190",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5d70ccd70eb42db718e0176987891f91d21d29c8"
    },
    {
      "sha": "2743b7e04b",
      "message": "Fix SORT GET to ignore special pattern # in cluster slot check (#1182)",
      "date": "2024-10-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1182",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2743b7e04beecc3128b696e2b90a4916f45dc1c4"
    },
    {
      "sha": "701ab72429",
      "message": "Remove the restriction that cli --cluster create requires at least 3 primary nodes (#1075)",
      "date": "2024-10-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1075",
      "commit_url": "https://github.com/valkey-io/valkey/commit/701ab724291a26da358ca828768388f278508ac2"
    },
    {
      "sha": "247a8f23c5",
      "message": "Fix FUNCTION KILL error message being displayed as SCRIPT KILL (#1171)",
      "date": "2024-10-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1171",
      "commit_url": "https://github.com/valkey-io/valkey/commit/247a8f23c54242dbc029107cf3c0c1f449a6dd79"
    },
    {
      "sha": "dc05a327f9",
      "message": "Take hz into account in activerehashing to avoid CPU spikes (#977)",
      "date": "2024-10-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/977",
      "commit_url": "https://github.com/valkey-io/valkey/commit/dc05a327f962d94319d4ae4b93ad10c7661700f1"
    },
    {
      "sha": "416defdc0e",
      "message": "Minor cleanups in acl-v2 tests (#1166)",
      "date": "2024-10-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1166",
      "commit_url": "https://github.com/valkey-io/valkey/commit/416defdc0ecd7134ceaeeb07d0a729540c4934c3"
    },
    {
      "sha": "87b5e13465",
      "message": "Use listLast to replace listIndex -1 (#1163)",
      "date": "2024-10-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1163",
      "commit_url": "https://github.com/valkey-io/valkey/commit/87b5e13465752d5e42b97a910d23426565ded4d9"
    },
    {
      "sha": "9c20c84251",
      "message": "Set fail-fast to false in daily CI (#1162)",
      "date": "2024-10-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1162",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9c20c84251571fcf2212543866f1d5ac094ba978"
    },
    {
      "sha": "1a5c80fe90",
      "message": "Minor comments cleanup around replication.c (#1154)",
      "date": "2024-10-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1154",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1a5c80fe905023e8bab874e67e23e8205ff92a60"
    },
    {
      "sha": "e50f31ef3a",
      "message": "Fix aof race in shutdown nosave timedout script test (#1156)",
      "date": "2024-10-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1156",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e50f31ef3a7e604236e178a737b8e28590faf1c9"
    },
    {
      "sha": "014219879d",
      "message": "Fix typo last_procssed -> last_processed (#1142)",
      "date": "2024-10-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1142",
      "commit_url": "https://github.com/valkey-io/valkey/commit/014219879d4c4f355d335a20d578672c99e0c56e"
    },
    {
      "sha": "1892f8a731",
      "message": "Add server log when module load fails with busy name (#1084)",
      "date": "2024-10-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1084",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1892f8a7315f272e36afdabb8dc0e806ed104633"
    },
    {
      "sha": "9827eef4d0",
      "message": "Avoid timing issue in diskless-load-swapdb test (#1077)",
      "date": "2024-10-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1077",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9827eef4d0c8635993224d7068afdf730d843eab"
    },
    {
      "sha": "bf8183d065",
      "message": "Add --cluster option to runtest to run only cluster tests (#1052)",
      "date": "2024-09-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1052",
      "commit_url": "https://github.com/valkey-io/valkey/commit/bf8183d065f07b40d465cca818a51689036b7488"
    },
    {
      "sha": "80fcbd3fec",
      "message": "Fix module / script call CLUSTER SLOTS / SHARDS fake client check crash (#1063)",
      "date": "2024-09-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1063",
      "commit_url": "https://github.com/valkey-io/valkey/commit/80fcbd3fece6decb6195dc1a4289ebb675b5d45d"
    },
    {
      "sha": "6e0216471d",
      "message": "Trigger the election as soon as possible when doing a forced manual failover (#1067)",
      "date": "2024-09-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1067",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6e0216471d5365882a042cd8f7531f5a277243e6"
    },
    {
      "sha": "6ce75cdea8",
      "message": "Fix replica online timing issue in failover test (#1044)",
      "date": "2024-09-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1044",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6ce75cdea8ca7dc0d70c9ee7131b9d82778d1973"
    },
    {
      "sha": "56fba564b6",
      "message": "Print an empty primary log when primary lost its last slot (#1064)",
      "date": "2024-09-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1064",
      "commit_url": "https://github.com/valkey-io/valkey/commit/56fba564b609d389fdd8f64e1234f46a052a6ed7"
    },
    {
      "sha": "d07c29791a",
      "message": "Use _Thread_local to solve threads.h build issue (#1053)",
      "date": "2024-09-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1053",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d07c29791a4cecd8bce76b05d046981f39fe5fcd"
    },
    {
      "sha": "ea7a7995ed",
      "message": "Fix default value of primary-reboot-down-after-period in sentinel.conf (#1040)",
      "date": "2024-09-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1040",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ea7a7995ed072dcf836e6e38076305295d4abd15"
    },
    {
      "sha": "d9c41e9ef9",
      "message": "Fix timing issue in the new tot-net-out replica test (#1060)",
      "date": "2024-09-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1060",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d9c41e9ef9b787e4cbf27b14548de179267d9380"
    },
    {
      "sha": "7fab15795f",
      "message": "Add log about old primary after myself failover (#1058)",
      "date": "2024-09-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1058",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7fab15795f5d419acc284e002119190b00718881"
    },
    {
      "sha": "f89ff3137d",
      "message": "Add --moduleapi option to better use runtest-moduleapi (#1007)",
      "date": "2024-09-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1007",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f89ff3137d437e7c43d910e4d28ed8fbed44decc"
    },
    {
      "sha": "17390383b5",
      "message": "Replica flush the old data after RDB file is ok in disk-based replication (#926)",
      "date": "2024-09-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/926",
      "commit_url": "https://github.com/valkey-io/valkey/commit/17390383b58e7e894e9a754132509def2ce0d913"
    },
    {
      "sha": "dcc7678fc4",
      "message": "Fix replica unable trigger migration when it received CLUSTER SETSLOT in advance (#981)",
      "date": "2024-09-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/981",
      "commit_url": "https://github.com/valkey-io/valkey/commit/dcc7678fc4d4b7b26e79b76489d37a93064420c3"
    },
    {
      "sha": "f7c5b40183",
      "message": "Avoid false positive in election tests (#984)",
      "date": "2024-09-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/984",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f7c5b401830616652fa9a97c916f40a45166ade2"
    },
    {
      "sha": "38457b7320",
      "message": "Trigger a save of the cluster configuration file before shutting down (#822)",
      "date": "2024-09-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/822",
      "commit_url": "https://github.com/valkey-io/valkey/commit/38457b73208d9edadbdeb64dda8b18f57099475a"
    },
    {
      "sha": "4033c99ef5",
      "message": "Fix module RdbLoad wrongly disable the AOF (#1001)",
      "date": "2024-09-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1001",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4033c99ef522cd66150878dee8a97dc057b05a25"
    },
    {
      "sha": "50c1fe59f7",
      "message": "Add missing moduleapi getchannels test and fix tests (#1002)",
      "date": "2024-09-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1002",
      "commit_url": "https://github.com/valkey-io/valkey/commit/50c1fe59f7634b9b4658d4fdf9ce52d3468ed8ce"
    },
    {
      "sha": "c642cf0134",
      "message": "Add client info to SHUTDOWN / CLUSTER FAILOVER logs (#875)",
      "date": "2024-09-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/875",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c642cf0134cf03ca9a5aff8ce126b982fcc48324"
    },
    {
      "sha": "6478526597",
      "message": "Fix aof base suffix when modifying aof-use-rdb-preamble during rewrite (#886)",
      "date": "2024-09-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/886",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6478526597601b23455fef75a3a87f030bd12bd2"
    },
    {
      "sha": "9b51949abe",
      "message": "Fix missing replication link re-connection when primary's IP/port is updated in `clusterProcessGossipSection` (#965)",
      "date": "2024-09-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/965",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9b51949abe3616148437a914eab49c1a6a53c599"
    },
    {
      "sha": "9033734b6b",
      "message": "Add newline to argv in crash report when doing redact (#993)",
      "date": "2024-09-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/993",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9033734b6b0df062fa70b5d6579769b6f9c38896"
    },
    {
      "sha": "5693fe4664",
      "message": "Fix set expire test due to the new lazyfree configs changes (#980)",
      "date": "2024-09-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/980",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5693fe466481a9d40ace3b14dd81c688df3e0c64"
    },
    {
      "sha": "70624ea63d",
      "message": "Change all the lazyfree configurations to yes by default (#913)",
      "date": "2024-09-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/913",
      "commit_url": "https://github.com/valkey-io/valkey/commit/70624ea63d472ec05b2697dbdba6bd579d3322b5"
    },
    {
      "sha": "e3af1a30e4",
      "message": "Fast path in SET if the expiration time is expired (#865)",
      "date": "2024-08-31",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/865",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e3af1a30e41087364091f5fe6d9c71f61526fe3f"
    },
    {
      "sha": "fea49bce2c",
      "message": "Fix timing issue in replica migration test (#968)",
      "date": "2024-08-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/968",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fea49bce2c5018efbd564c627e6ceedbbe136cc5"
    },
    {
      "sha": "ecbfb6a7ec",
      "message": "Fix reconfiguring sub-replica causing data loss when myself change shard_id (#944)",
      "date": "2024-08-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/944",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ecbfb6a7ec3b6b0619ede8653effb04055ce7b18"
    },
    {
      "sha": "75b824052d",
      "message": "Revert make KEYS to be an exact match if there is no pattern (#964)",
      "date": "2024-08-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/964",
      "commit_url": "https://github.com/valkey-io/valkey/commit/75b824052d72eec8611a5af5e92ef428877cec1e"
    },
    {
      "sha": "4fe8320711",
      "message": "Add pause path coverage to replica migration tests (#937)",
      "date": "2024-08-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/937",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4fe83207116b3986a2d021d38dfacfe06ba69604"
    },
    {
      "sha": "6a84e06b05",
      "message": "Wait for the role change and fix the timing issue in the new test (#947)",
      "date": "2024-08-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/947",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6a84e06b05dd08c61942cdb254997775ed9b5e00"
    },
    {
      "sha": "694246cfab",
      "message": "Drop the outdated script replication example comments (#951)",
      "date": "2024-08-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/951",
      "commit_url": "https://github.com/valkey-io/valkey/commit/694246cfab971560b02a7cf228f71b9d1cbea87e"
    },
    {
      "sha": "d66a06e818",
      "message": "Make KEYS to be an exact match if there is no pattern (#792)",
      "date": "2024-08-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/792",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d66a06e8183818c035bb78706f46fd62645db07e"
    },
    {
      "sha": "9f4b1adbea",
      "message": "Add explicit assert to ensure thread_shared_qb won't expand (#938)",
      "date": "2024-08-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/938",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9f4b1adbea6aa729c767257495dec23635923a3e"
    },
    {
      "sha": "c7d1daea05",
      "message": "Add epoch information to failover auth denied logs (#816)",
      "date": "2024-08-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/816",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c7d1daea057427bd54c43b9600ecdd475ec6fcdc"
    },
    {
      "sha": "8045994972",
      "message": "valkey-cli make source node ignores NOREPLICAS when doing the last CLUSTER SETSLOT (#928)",
      "date": "2024-08-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/928",
      "commit_url": "https://github.com/valkey-io/valkey/commit/804599497212873710269f7bd589e3a7164f6fdd"
    },
    {
      "sha": "5d97f5133c",
      "message": "Fix CLUSTER SETSLOT block and unblock error when all replicas are down (#879)",
      "date": "2024-08-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/879",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5d97f5133c271313cd5a172617e8af1fe845e0e2"
    },
    {
      "sha": "8d9b8c9d3d",
      "message": "Make runtest-cluster support --io-threads option (#933)",
      "date": "2024-08-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/933",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8d9b8c9d3d5fd9e22e18230a0ff86afba06bcc9a"
    },
    {
      "sha": "08aaeea4b7",
      "message": "Avoid to re-establish replication if node is already myself primary in CLUSTER REPLICATE (#884)",
      "date": "2024-08-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/884",
      "commit_url": "https://github.com/valkey-io/valkey/commit/08aaeea4b7714ffb191e57f105f950cb1924ba4a"
    },
    {
      "sha": "a1ac459ef1",
      "message": "Set repl-backlog-size from 1mb to 10mb by default (#911)",
      "date": "2024-08-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/911",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a1ac459ef1f48e44b2429446243917c67afab401"
    },
    {
      "sha": "e1b3629186",
      "message": "Fix data loss when replica do a failover with a old history repl offset (#885)",
      "date": "2024-08-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/976",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e1b3629186a89ee1aec86c0f512d3faafa62d91c"
    },
    {
      "sha": "829243e76b",
      "message": "Correct RDB_EOF_MARK_SIZE usage where EOF mark is relevant (#925)",
      "date": "2024-08-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/925",
      "commit_url": "https://github.com/valkey-io/valkey/commit/829243e76bb658b9f2379ce47a7a5c302dd360fa"
    },
    {
      "sha": "70b9285802",
      "message": "Optimize linear search of WAIT and WAITAOF when unblocking the client (#787)",
      "date": "2024-08-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/787",
      "commit_url": "https://github.com/valkey-io/valkey/commit/70b92858025b49fae2c73648f9676bfd516932f1"
    },
    {
      "sha": "fc9f291033",
      "message": "Make a light weight version of DEBUG OBJECT, add FAST option (#881)",
      "date": "2024-08-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/881",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fc9f29103396eca37ecd594125bc0b9ae5f9d6e0"
    },
    {
      "sha": "76ad8f7a76",
      "message": "Skip IPv6 tests when TCLSH version is < 8.6 (#910)",
      "date": "2024-08-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/910",
      "commit_url": "https://github.com/valkey-io/valkey/commit/76ad8f7a7603ff3eee68c19d2029a1d393e149b6"
    },
    {
      "sha": "370bdb3e46",
      "message": "Change server.daylight_active to an atomic variable (#876)",
      "date": "2024-08-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/876",
      "commit_url": "https://github.com/valkey-io/valkey/commit/370bdb3e4679c6b4a333301e1854a2a61a818f0d"
    },
    {
      "sha": "f622e375a0",
      "message": "Better messages when valkey-cli cluster --fix meet value check failed (#867)",
      "date": "2024-08-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/867",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f622e375a06bb8a2e700826c1af1af448155ad69"
    },
    {
      "sha": "929283fc6f",
      "message": "Dual channel replication should not update lastbgsave_status when transfer error (#811)",
      "date": "2024-08-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/811",
      "commit_url": "https://github.com/valkey-io/valkey/commit/929283fc6f03b0d3dcc5dcc1847be1c5c6688157"
    },
    {
      "sha": "5166d489da",
      "message": "Correctly recode client infomation to the slowlog when runing script (#805)",
      "date": "2024-08-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/805",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5166d489da1bbf49643dd6b44cd2593e21c09dc3"
    },
    {
      "sha": "380f700816",
      "message": "Improve cluster cant failover log conditions (#780)",
      "date": "2024-08-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/780",
      "commit_url": "https://github.com/valkey-io/valkey/commit/380f70081686d68739536990f5c8535d1382524d"
    },
    {
      "sha": "c8983c43e0",
      "message": "Update to mention PING behavior with RESP2 and subscribe (#160)",
      "date": "2024-08-05",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/160",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/c8983c43e00fa52334c85f212df3a06f878d9c59"
    },
    {
      "sha": "054ffd140f",
      "message": "Fix outdated comment of migrate in valkey-cli --cluster (#864)",
      "date": "2024-08-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/864",
      "commit_url": "https://github.com/valkey-io/valkey/commit/054ffd140f4982850aae147908b968215613641c"
    },
    {
      "sha": "fa238dc049",
      "message": "Update dir in valkey.conf to mention cluster-config-file (#635)",
      "date": "2024-07-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/635",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fa238dc0496e6fbb3c2c031e18718589ea6695d6"
    },
    {
      "sha": "e32518d655",
      "message": "Fix unexpected behavior when turning appendonly on and off within a transaction (#826)",
      "date": "2024-07-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/826",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e32518d6553e4bd9d7742926b65fdc3fb18a0da6"
    },
    {
      "sha": "f00c8f6214",
      "message": "Modify clusterSaveConfig function call to use C_OK / C_ERR return value (#818)",
      "date": "2024-07-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/818",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f00c8f6214b2b3f6eec7af74cdf6485ffbb33ed3"
    },
    {
      "sha": "59aa00823c",
      "message": "Replicas with the same offset queue up for election (#762)",
      "date": "2024-07-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/762",
      "commit_url": "https://github.com/valkey-io/valkey/commit/59aa00823c3691c50da452f2df2c4bc24e46696d"
    },
    {
      "sha": "9a7bf910cb",
      "message": "Fix extra reply in debug sleep-after-fork-seconds error path (#810)",
      "date": "2024-07-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/810",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9a7bf910cbd7795d8a86bee9bec6378c366b9e6b"
    },
    {
      "sha": "14e09e981e",
      "message": "Fix the wrong woff when execute WAIT / WAITAOF in script (#776)",
      "date": "2024-07-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/776",
      "commit_url": "https://github.com/valkey-io/valkey/commit/14e09e981e0039edbf8c41a208a258c18624cbb7"
    },
    {
      "sha": "15a8290231",
      "message": "Optimize failover time when the new primary node is down again (#782)",
      "date": "2024-07-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/782",
      "commit_url": "https://github.com/valkey-io/valkey/commit/15a82902316b59e2cbf8962ac2665e4b6b038f4c"
    },
    {
      "sha": "35a1888333",
      "message": "Fix incorrect usage of process_is_paused in tests (#783)",
      "date": "2024-07-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/783",
      "commit_url": "https://github.com/valkey-io/valkey/commit/35a188833335332980a16239ac2efebf241c8a6a"
    },
    {
      "sha": "36e81d9e79",
      "message": "Fix rdb_child_exit_pipe incorrect close call (#801)",
      "date": "2024-07-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/801",
      "commit_url": "https://github.com/valkey-io/valkey/commit/36e81d9e79ea934b888f133ccee313a5fe0b9297"
    },
    {
      "sha": "c584371506",
      "message": "Fix rdb pipe uninitialized false positive warning (#800)",
      "date": "2024-07-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/800",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c584371506010686087e64af7edc9706e2c38674"
    },
    {
      "sha": "4b96a01dcf",
      "message": "Update rdb save releated fileds to distinguish diskless RDB (#158)",
      "date": "2024-07-17",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/158",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/4b96a01dcf494bb839953b18a2900aceccc6a851"
    },
    {
      "sha": "b4ac2c406c",
      "message": "Update gitignore to ignore the cluster-cluster test files (#756)",
      "date": "2024-07-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/756",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b4ac2c406c54dae42f42f56c6f65f134a18cc514"
    },
    {
      "sha": "8c92b2f747",
      "message": "Minor fix for --loops option in normal testing framework (#781)",
      "date": "2024-07-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/781",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8c92b2f7470d2661bd5987d979d4a1fe23b012d4"
    },
    {
      "sha": "a4ee8dada4",
      "message": "Fix WAITAOF test in external test due to appendonly is enabled (#775)",
      "date": "2024-07-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/775",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a4ee8dada4fcff9805cb6820e274fdb0d924ed83"
    },
    {
      "sha": "6bf1d02edf",
      "message": "Nested MULTI or WATCH in MULTI now will abort the transaction (#723)",
      "date": "2024-07-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/723",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6bf1d02edf962674cb32dc2e4f2f13d3d8cece3f"
    },
    {
      "sha": "2d6791bb11",
      "message": "Use clusterNodeIsVotingPrimary function to check the right (#735)",
      "date": "2024-07-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/735",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2d6791bb1157af52e20ffd1fb4ca025c283153d3"
    },
    {
      "sha": "1ea49e5845",
      "message": "Make valkey compatible with redis-sentinel to start sentinel (#731)",
      "date": "2024-07-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/731",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1ea49e5845a11250a13273c725720822c26860f1"
    },
    {
      "sha": "0cc16d0298",
      "message": "Fix wrong reserved bits in ClientFlags (#729)",
      "date": "2024-07-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/729",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0cc16d0298995ae4292b0d317e17fa82c338942a"
    },
    {
      "sha": "2979fe6060",
      "message": "CLUSTER SLOT-STATS ORDERBY when stats are the same, compare by slot in ascending order (#710)",
      "date": "2024-06-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/710",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2979fe606057437b344b08b0758722c64dfe0fd0"
    },
    {
      "sha": "518f0bf79b",
      "message": "Fix limit undefined behavior crash in CLUSTER SLOT-STATS (#709)",
      "date": "2024-06-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/709",
      "commit_url": "https://github.com/valkey-io/valkey/commit/518f0bf79bae984e5b93e03b5b951369419d4ca3"
    },
    {
      "sha": "7f7ef9a3fa",
      "message": "Update availability-zone to use the flag instead of the number 0 (#711)",
      "date": "2024-06-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/711",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7f7ef9a3fac516751ecdf20542753c321a12e0ba"
    },
    {
      "sha": "2b0723957e",
      "message": "Enable protected-configs, debug and module commands in create-cluster script (#701)",
      "date": "2024-06-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/701",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2b0723957e264f042951145a8c64eba65eb5a037"
    },
    {
      "sha": "bf1fb1fd36",
      "message": "Fix copy-paste error in scripts eviction test (#671)",
      "date": "2024-06-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/671",
      "commit_url": "https://github.com/valkey-io/valkey/commit/bf1fb1fd3658f57b3040f4e869c0c906c3fe3d9d"
    },
    {
      "sha": "a2cc2fe26d",
      "message": "Fix memory leak when loading slot migrations states fails (#658)",
      "date": "2024-06-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/658",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a2cc2fe26ddf5fac46476ec1f958dea56e35a513"
    },
    {
      "sha": "495a121f19",
      "message": "Adjust the log level of some logs in the cluster (#633)",
      "date": "2024-06-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/633",
      "commit_url": "https://github.com/valkey-io/valkey/commit/495a121f1938ccba6a249bd44df7d963fd32139a"
    },
    {
      "sha": "db6d3c1138",
      "message": "Only primary with slots has the right to mark a node as failed (#634)",
      "date": "2024-06-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/634",
      "commit_url": "https://github.com/valkey-io/valkey/commit/db6d3c1138695947412a745146ca29dbdf2e91c6"
    },
    {
      "sha": "a18bd47787",
      "message": "Mention that eviction policies use approximated randomized algorithms (#144)",
      "date": "2024-06-17",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/144",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/a18bd477878bb2db660b6d9445ba0b334a4870c7"
    },
    {
      "sha": "d5496e42bc",
      "message": "Lua scripts promoted from eval to script load to avoid evict (#637)",
      "date": "2024-06-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/637",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d5496e42bc601abc76bcd58bd9a4e6f2271a4578"
    },
    {
      "sha": "d309b9b235",
      "message": "Make configs dir/dbfilename/cluster-config-file reject empty string (#636)",
      "date": "2024-06-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/636",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d309b9b23550cd64621bf62f42504bf23838ab15"
    },
    {
      "sha": "6bab2d7968",
      "message": "Make sure clear the CLUSTER SLOTS cache on time when updating hostname (#564)",
      "date": "2024-05-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/564",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6bab2d7968dd9d71f2ce200386ecf4286e333a76"
    },
    {
      "sha": "e7e5a104ec",
      "message": "Revert mmap_rnd bits back to default value in CI (#520)",
      "date": "2024-05-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/520",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e7e5a104ec9b3274577dce9cf1a35ea8b8f8e008"
    },
    {
      "sha": "fdd023ff82",
      "message": "Migrate cluster mode tests to normal framework (#442)",
      "date": "2024-05-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/442",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fdd023ff8239ded21998fc711362759e0ca68bcc"
    }
  ],
  "review_list": [
    {
      "sha": "1d7224f389",
      "message": "Fix UAF in unblockClientOnKey when reprocessed command frees the client (CVE-2026-23479) (#3613)",
      "date": "2026-05-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3613",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1d7224f3894c8e6db39a9e86c040270b3122c064"
    },
    {
      "sha": "ccef347922",
      "message": "Skip deferred_reply test in req/res log validation (#3642)",
      "date": "2026-05-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3642",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ccef34792266961ec63393a8bc09c1552bc83e95"
    },
    {
      "sha": "96a6bc5d27",
      "message": "Fix the memory leak in valkey-benchmark (#3643)",
      "date": "2026-05-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3643",
      "commit_url": "https://github.com/valkey-io/valkey/commit/96a6bc5d2749a2722a91ecff8c094c23a58e9a7a"
    },
    {
      "sha": "89b7baa598",
      "message": "Speed up cluster startup by 10 seconds (#3606)",
      "date": "2026-05-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3606",
      "commit_url": "https://github.com/valkey-io/valkey/commit/89b7baa598b177286572e0784a4391810910f3d2"
    },
    {
      "sha": "89b7baa598",
      "message": "Speed up cluster startup by 10 seconds (#3606)",
      "date": "2026-05-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3606",
      "commit_url": "https://github.com/valkey-io/valkey/commit/89b7baa598b177286572e0784a4391810910f3d2"
    },
    {
      "sha": "f2f4e5dbfc",
      "message": "Run ASan Tests on run-extra-tests label (#3512)",
      "date": "2026-05-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3512",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f2f4e5dbfccdcefbc7d961bb28a1aef44068d3a6"
    },
    {
      "sha": "cea9354b56",
      "message": "Big Endian: add daily workflow UT job and fix UTs (#3330)",
      "date": "2026-05-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3330",
      "commit_url": "https://github.com/valkey-io/valkey/commit/cea9354b56128f4353ef4865e9005c78f5cf8fed"
    },
    {
      "sha": "46d37e4d5e",
      "message": "Fix off-by-one boundary in lpEncodeBacklen() for 3 values (#3601)",
      "date": "2026-05-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3601",
      "commit_url": "https://github.com/valkey-io/valkey/commit/46d37e4d5ee2dfdab263453c90fb64958f92d5de"
    },
    {
      "sha": "54bdf5737b",
      "message": "Handle NULL pointer in streamTrim listpack delta calculation (#3591)",
      "date": "2026-05-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3591",
      "commit_url": "https://github.com/valkey-io/valkey/commit/54bdf5737b3a4d9109d0b7ec6ad37e9adb52cb5a"
    },
    {
      "sha": "cba05103de",
      "message": "Fix: prevent NULL dereference crash in connectSlotExportJob when target node disappears (#3596)",
      "date": "2026-04-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3596",
      "commit_url": "https://github.com/valkey-io/valkey/commit/cba05103de24cd5d49f2f4d80e337646c2c941b4"
    },
    {
      "sha": "72fc5b14b1",
      "message": "Fix compilation error: replace deprecated je_calloc with zcalloc_num (#3592)",
      "date": "2026-04-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3592",
      "commit_url": "https://github.com/valkey-io/valkey/commit/72fc5b14b1f7bf7bd0ca2546bd6e636af151454f"
    },
    {
      "sha": "7817ca8a73",
      "message": "Fix GEOSEARCH BYPOLYGON leak on invalid COUNT (#3568)",
      "date": "2026-04-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3568",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7817ca8a736e70ed1205839d3a701342d348eac9"
    },
    {
      "sha": "8091c6c10a",
      "message": "Remove redundant count division in genericHgetallCommand (#3573)",
      "date": "2026-04-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3573",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8091c6c10a3bd80fcb639a036dde882580f61fcb"
    },
    {
      "sha": "6dbb7f81a9",
      "message": "Fix remove cached eval scripts on engine unregister (#3503)",
      "date": "2026-04-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3503",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6dbb7f81a97f7d687cf7fcc88bdcbe78bf6cf170"
    },
    {
      "sha": "28ecbd204f",
      "message": "Ensure client slot migration pointer is cleared during reset (#3554)",
      "date": "2026-04-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3554",
      "commit_url": "https://github.com/valkey-io/valkey/commit/28ecbd204fceec9f0bf1aa1b2d791b0f7e9fc7e5"
    },
    {
      "sha": "ff80b2d1dc",
      "message": "Migrate the remaining cluster tests to the new framework and remove legacy files (#2297) (#3382)",
      "date": "2026-04-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3382",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ff80b2d1dc7c7858e938ece683d5c3fcb8c9ed31"
    },
    {
      "sha": "7a480bb96c",
      "message": "adds Leadership page with TSC (#510)",
      "date": "2026-04-24",
      "repo": "valkey-io.github.io",
      "pr_url": "https://github.com/valkey-io/valkey-io.github.io/pull/510",
      "commit_url": "https://github.com/valkey-io/valkey-io.github.io/commit/7a480bb96cd42113fd3213663b255591a96b4339"
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
      "sha": "651c40a89e",
      "message": "Fix FD leak in connSocketBlockingConnect on timeout (#3541)",
      "date": "2026-04-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3541",
      "commit_url": "https://github.com/valkey-io/valkey/commit/651c40a89ebe6427e2053bb139a7dedf466821ff"
    },
    {
      "sha": "04896c1e6d",
      "message": "Deflake many-slot-migration under valgrind (#3462)",
      "date": "2026-04-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3462",
      "commit_url": "https://github.com/valkey-io/valkey/commit/04896c1e6dab95f6da6c0cf6c2fa2d3d23330bb8"
    },
    {
      "sha": "4a42c95853",
      "message": "Fix HPERSIST RESP protocol violation on wrong-type key (#3516)",
      "date": "2026-04-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3516",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4a42c95853c0f3978715cb509a774f457edc182b"
    },
    {
      "sha": "8a91a12398",
      "message": "Unique samples in hashtableSampleEntries (#3460)",
      "date": "2026-04-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3460",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8a91a123980bf7715a851792b5f00c45b993aeba"
    },
    {
      "sha": "baa5a48b5a",
      "message": "Env: Read VALKEYCLI_HOST and VALKEYCLI_PORT environment variables (#3402)",
      "date": "2026-04-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3402",
      "commit_url": "https://github.com/valkey-io/valkey/commit/baa5a48b5acb2afebdf463ca5b91f3ad77bdaec6"
    },
    {
      "sha": "b020b03c69",
      "message": "Increase timeouts in faster-failover test for slow CI runners (#3463)",
      "date": "2026-04-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3463",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b020b03c69874bfb0b24dfdb6eb20765f4e2cfba"
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
      "sha": "f6b5461b73",
      "message": "Attempt to deflake 'diskless no replicas drop during rdb pipe' (#3461)",
      "date": "2026-04-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3461",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f6b5461b7348987da65f17a8c072ab46e93baaa4"
    },
    {
      "sha": "c35dbdfc83",
      "message": "Fix some flaky tests using CLIENT REPLY OFF (#3452)",
      "date": "2026-04-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3452",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c35dbdfc83b7860a66d2b88685b1d31739ceb962"
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
      "sha": "e8ca6c07b2",
      "message": "Fix VLA warning in linenoise and enable -Werror (#3439)",
      "date": "2026-04-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3439",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e8ca6c07b22ceb89692c17b7f51c4a8f03a268ba"
    },
    {
      "sha": "1db8bab508",
      "message": "Big endian bitmap byte order mismatch fix (#3401)",
      "date": "2026-04-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3401",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1db8bab50851cc22aa97d91aeccb4b8385be1672"
    },
    {
      "sha": "1db8bab508",
      "message": "Big endian bitmap byte order mismatch fix (#3401)",
      "date": "2026-04-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3401",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1db8bab50851cc22aa97d91aeccb4b8385be1672"
    },
    {
      "sha": "fb655dbf5c",
      "message": "Replace dict with thin wrapper around hashtable (#3366)",
      "date": "2026-04-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3366",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fb655dbf5cfaf254e0b8bb6617f1f734dbebc07d"
    },
    {
      "sha": "f3b6470502",
      "message": "Fix some flaky tests (#3430)",
      "date": "2026-04-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3430",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f3b647050269003cd0ae40c5ec359c62163aff2a"
    },
    {
      "sha": "8bb8d9168f",
      "message": "Enhance cluster stale packet detection to prevent sub-replica and empty primary (#2811)",
      "date": "2026-04-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2811",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8bb8d9168fbab2fbc07a26f744bea06d547925aa"
    },
    {
      "sha": "2e12d27b97",
      "message": "Increase timeout in flaky \"failover immediately\" test case (#3424)",
      "date": "2026-04-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3424",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2e12d27b97f5bda8400275f66ae7838516912544"
    },
    {
      "sha": "0dab0b59c5",
      "message": "Reduce corrupt-dump-fuzzer tests from 10 to 1 minute (#3425)",
      "date": "2026-04-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3425",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0dab0b59c52fd67afce3f1cf69b22f69fbd877aa"
    },
    {
      "sha": "b83209de0a",
      "message": " Fix race condition in diskless swapdb RedisModuleEvent_ReplAsyncLoad tests (#3404)",
      "date": "2026-03-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3404",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b83209de0ab5807b695c780ec6d44e1f49d9140e"
    },
    {
      "sha": "afe6ee11b1",
      "message": "remove duplicated lline (#3379)",
      "date": "2026-03-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3379",
      "commit_url": "https://github.com/valkey-io/valkey/commit/afe6ee11b1ecb2029b09ed9338d22a89a061b3ce"
    },
    {
      "sha": "0027b7d453",
      "message": "Add AGENTS.md file for agentic coding assistant steering (#3371)",
      "date": "2026-03-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3371",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0027b7d4533a90944d6175a83257f874d8ffd2a3"
    },
    {
      "sha": "059a77c429",
      "message": "Add design-docs folder and README. (#3300)",
      "date": "2026-03-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3300",
      "commit_url": "https://github.com/valkey-io/valkey/commit/059a77c4290794c4a729be611208eec5aa080735"
    },
    {
      "sha": "ed9016a2f7",
      "message": "Make macOS leaks check skippable (#3370)",
      "date": "2026-03-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3370",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ed9016a2f79941ffee86e4b52214aacba7dffb29"
    },
    {
      "sha": "6c329dfe2c",
      "message": "Weekly tests branches are not honored on scheduled workflow (#3340)",
      "date": "2026-03-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3340",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6c329dfe2c02d09b276fd5617acdb31e6169ebc1"
    },
    {
      "sha": "c9ce3e0919",
      "message": "Fix OOM aborts in large-memory ASAN tests on GitHub runners (#3263)",
      "date": "2026-03-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3263",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c9ce3e09191305a455139f70b7807ebb0549b951"
    },
    {
      "sha": "2cbb86b076",
      "message": "Add docs for availability-zone field in CLUSTER SHARDS/SLOTS (#420)",
      "date": "2026-03-11",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/420",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/2cbb86b0768ea0d9986f201e1f83092a1abe2a2b"
    },
    {
      "sha": "8051de740d",
      "message": "Inherit LDFLAGS for TLS and RDMA modules (#3344)",
      "date": "2026-03-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3344",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8051de740dd38172476b04e892e5517630e3eaed"
    },
    {
      "sha": "6b384e9a5b",
      "message": "Fix ZDIFF algorithm 2 memory leak on early exit (#3342)",
      "date": "2026-03-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3342",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6b384e9a5b6cd4e4f8198f5df22a74feb1b70e0f"
    },
    {
      "sha": "3741503557",
      "message": "Add availability-zone field support to CLUSTER SHARDS / CLUSTER SLOTS (#3156)",
      "date": "2026-03-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3156",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3741503557b1fff2072216812e61654b7d366409"
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
      "sha": "cb9e7c94e9",
      "message": "Let script continue if busy-reply-threshold is zero (#3307)",
      "date": "2026-03-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3307",
      "commit_url": "https://github.com/valkey-io/valkey/commit/cb9e7c94e98f364e4536cb00483174fe6248e0f5"
    },
    {
      "sha": "cb9e7c94e9",
      "message": "Let script continue if busy-reply-threshold is zero (#3307)",
      "date": "2026-03-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3307",
      "commit_url": "https://github.com/valkey-io/valkey/commit/cb9e7c94e98f364e4536cb00483174fe6248e0f5"
    },
    {
      "sha": "a731e45fd3",
      "message": "Fix compatibility for OpenSSL < 3.0 and Almalinux version mismatch for daily tests (#3303)",
      "date": "2026-03-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3303",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a731e45fd3940bf6e1c61b21b840e7ed5dd499f2"
    },
    {
      "sha": "d49eac9cad",
      "message": "Update the CodeQL action to resolve v3 deprecation warnings (#3310)",
      "date": "2026-03-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3310",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d49eac9cada3b605fd6968e0d7377566ce801c67"
    },
    {
      "sha": "c21689ab4d",
      "message": "[DEFLAKE] Fix flaky block_keyspace_notification pipelining test (#3294)",
      "date": "2026-03-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3294",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c21689ab4d2d80802b8c78a2338dfed3444a0f35"
    },
    {
      "sha": "b1f590f905",
      "message": "Fix TSAN compatibility for module loading (#3257)",
      "date": "2026-03-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3257",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b1f590f90586565a23fdfa1feb2b3b2375c63bc7"
    },
    {
      "sha": "153f495019",
      "message": "Deflake ttl persistence in aof test (#3285)",
      "date": "2026-03-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3285",
      "commit_url": "https://github.com/valkey-io/valkey/commit/153f4950196f905a2d86e91cad511ed8914b6551"
    },
    {
      "sha": "ec5e8fa2b1",
      "message": "Fix use-after-free in generateSyncSlotsEstablishCommand (#3283)",
      "date": "2026-03-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3283",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ec5e8fa2b16aad209b2e586f5e6e40c872b02359"
    },
    {
      "sha": "dab36efd33",
      "message": "Fix use zfree in cli --eval path  (#3281)",
      "date": "2026-03-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3281",
      "commit_url": "https://github.com/valkey-io/valkey/commit/dab36efd33e5b2bbc4dfc780c5fa2cc77b7a0483"
    },
    {
      "sha": "75fb0e6cbb",
      "message": "Deflake Restart target replica during migration (without save) causes success test (#3226)",
      "date": "2026-02-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3226",
      "commit_url": "https://github.com/valkey-io/valkey/commit/75fb0e6cbb7ce7e6762951b6b97083c433e5b4c1"
    },
    {
      "sha": "994d87a0f2",
      "message": "Deflake test 'LATENCY GRAPH can output the event graph' (#3260)",
      "date": "2026-02-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3260",
      "commit_url": "https://github.com/valkey-io/valkey/commit/994d87a0f255f5a261b78c3f792eb7ac81a1ecbe"
    },
    {
      "sha": "c471364910",
      "message": "Fix type of now parameter in rdbLoadObject() to use mstime_t instead of time_t (#3255)",
      "date": "2026-02-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3255",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c471364910e7412b4a46f6cd6cc7d5c70c1dc13b"
    },
    {
      "sha": "4dee322ede",
      "message": "Fix flake dual-channel-replication primary gets cob overrun before established psync test (#3242)",
      "date": "2026-02-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3242",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4dee322edeb9c96029d89cfaf1600abad2afead0"
    },
    {
      "sha": "1ee434e63e",
      "message": "Bugfix for GIL deadlock while unloading script engine, reenable memory test in crash report (#3029)",
      "date": "2026-02-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3029",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1ee434e63e46aeb337ede4b5e91e6336f2067d77"
    },
    {
      "sha": "1ee434e63e",
      "message": "Bugfix for GIL deadlock while unloading script engine, reenable memory test in crash report (#3029)",
      "date": "2026-02-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3029",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1ee434e63e46aeb337ede4b5e91e6336f2067d77"
    },
    {
      "sha": "501b3153f2",
      "message": "Skip expired hash fields when loading non-preamble RDB on primary (#3091)",
      "date": "2026-02-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3091",
      "commit_url": "https://github.com/valkey-io/valkey/commit/501b3153f26e4d8e5f9764d04abed624e2e655cf"
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
      "sha": "d0a32a70f8",
      "message": "Add `ALLOW_BUSY` flag to `SELECT` and various `CLIENT` sub-commands (#3217)",
      "date": "2026-02-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3217",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d0a32a70f858e6950e1606ead2881af09c13f13c"
    },
    {
      "sha": "e30efee802",
      "message": "Cluster shard documentation fix for fail health status (#408)",
      "date": "2026-02-15",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/408",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/e30efee80204960b68669482cec5bd6c71ea79ed"
    },
    {
      "sha": "fde31b08f7",
      "message": "Optimize endian conversion functions (#3201)",
      "date": "2026-02-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3201",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fde31b08f7b00ed0bc1bb153e7a315ff435270f2"
    },
    {
      "sha": "e0a467edab",
      "message": "Optimize ustime() with monotonic delta (#3193)",
      "date": "2026-02-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3193",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e0a467edabad66c75dbfca5e9caaadc3d6848c36"
    },
    {
      "sha": "546020e54c",
      "message": "Add test-tls-only CI job (#3143)",
      "date": "2026-02-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3143",
      "commit_url": "https://github.com/valkey-io/valkey/commit/546020e54c98f4a0c829b9e4470da1410bc26c6e"
    },
    {
      "sha": "83e07389e0",
      "message": "Workflows use actions/checkout for libbacktrace instead of git clone (#3204)",
      "date": "2026-02-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3204",
      "commit_url": "https://github.com/valkey-io/valkey/commit/83e07389e002d6b4cc0f8fb900bf0537b19331a0"
    },
    {
      "sha": "62686985e5",
      "message": "Fix bug causing no response flush sometimes when IO threads are busy (#3205)",
      "date": "2026-02-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3205",
      "commit_url": "https://github.com/valkey-io/valkey/commit/62686985e5d99996c9f9427524daed52e14cbec3"
    },
    {
      "sha": "42fc851b76",
      "message": "Fix pointer-to-int-cast warnings for RDMA address handling (#3186)",
      "date": "2026-02-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3186",
      "commit_url": "https://github.com/valkey-io/valkey/commit/42fc851b76c9eab40a161fc0df03cbe887f8ea34"
    },
    {
      "sha": "c25cae5f9b",
      "message": "COPY returns 0 when the source key does not exist (#404)",
      "date": "2026-02-10",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/404",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/c25cae5f9be7f48cd2aa78f5c0b49e95c89d2a20"
    },
    {
      "sha": "0f5db6a5d1",
      "message": "Steps to run daily workflow in forked repo (#3168)",
      "date": "2026-02-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3168",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0f5db6a5d17d8273d2535aeac2d9eaca23635861"
    },
    {
      "sha": "185d2ad7d9",
      "message": "Allow some tags only on top level to fix `--tags` filtering (#3171)",
      "date": "2026-02-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3171",
      "commit_url": "https://github.com/valkey-io/valkey/commit/185d2ad7d9e8d1c598af544ba623f9383ef6b00f"
    },
    {
      "sha": "ca34cc0b8f",
      "message": "Make TLS disable/enable INFO checks deterministic for module mode (#3167)",
      "date": "2026-02-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3167",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ca34cc0b8f75d83414a88e42f65a8c8623ef6f93"
    },
    {
      "sha": "dbdc3d9c6b",
      "message": "Extend test helper wait_for_cluster_propagation to support ignoring certain node (#3069)",
      "date": "2026-02-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3069",
      "commit_url": "https://github.com/valkey-io/valkey/commit/dbdc3d9c6bce50a4d50396fd672bf43160762db5"
    },
    {
      "sha": "55b846064d",
      "message": "Minor cleanup in memtoull to also check ERANGE when calling strtoull (#3159)",
      "date": "2026-02-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3159",
      "commit_url": "https://github.com/valkey-io/valkey/commit/55b846064d5e9efbb23b013dbff2dc23c2bcf7a9"
    },
    {
      "sha": "980ef57829",
      "message": "make test_empty_buckets_rehashing deterministic across hash seeds (#3174)",
      "date": "2026-02-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3174",
      "commit_url": "https://github.com/valkey-io/valkey/commit/980ef57829a857be46dba08af14efd59e8fcf52d"
    },
    {
      "sha": "839d0c6698",
      "message": "Fix flake replicas different ranks test (#3164)",
      "date": "2026-02-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3164",
      "commit_url": "https://github.com/valkey-io/valkey/commit/839d0c66980f85610869486e467a6b9f3ad1a83f"
    },
    {
      "sha": "d64f2072ef",
      "message": "Skip flaky test cases in client-eviction.tcl when in TLS mode (#3151)",
      "date": "2026-02-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3151",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d64f2072efd80e760e53351e8fab1e1ce1320975"
    },
    {
      "sha": "3ea5cb3989",
      "message": "CI: Stop using symlinks for tests with CMake (#3145)",
      "date": "2026-02-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3145",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3ea5cb39898bce6f8073a2dd2efbc4d43c9dbcaf"
    },
    {
      "sha": "9e0303bc53",
      "message": "Revert #3088 (#3137)",
      "date": "2026-01-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3137",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9e0303bc53c61b9d9e48fe5f14a640287888fe54"
    },
    {
      "sha": "8d509a5d33",
      "message": "deflake HSETEX EXAT single field expires leaving other fields intact (#3120)",
      "date": "2026-01-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3120",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8d509a5d33a9eed7a47d116ff4273e61afb5189c"
    },
    {
      "sha": "985cf836ac",
      "message": "Perf: Track net bytes only if commandlog-request-larger-than != -1 (#3086)",
      "date": "2026-01-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3086",
      "commit_url": "https://github.com/valkey-io/valkey/commit/985cf836ac13e7366f938aa9a4e7a309d83733da"
    },
    {
      "sha": "94edae4b8d",
      "message": "Fix how hash is handling overriding of expired fields overwrite (#3060)",
      "date": "2026-01-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3060",
      "commit_url": "https://github.com/valkey-io/valkey/commit/94edae4b8d81ad683ab225c93a381eae444a0f14"
    },
    {
      "sha": "be561e2b4b",
      "message": "CI: Make CMake test also run tls tests (#3097)",
      "date": "2026-01-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3097",
      "commit_url": "https://github.com/valkey-io/valkey/commit/be561e2b4b824d232a97e3f07290f2333cebb928"
    },
    {
      "sha": "18257cd2e3",
      "message": "Fix unit test for TLS auto reload (#3094)",
      "date": "2026-01-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3094",
      "commit_url": "https://github.com/valkey-io/valkey/commit/18257cd2e32fd98ea630a209336858bd8c3d55c7"
    },
    {
      "sha": "be0a572c8b",
      "message": "Fix minor inconsistency in connFormatAddr size argument (#3098)",
      "date": "2026-01-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3098",
      "commit_url": "https://github.com/valkey-io/valkey/commit/be0a572c8b949538a1947925edf3074b53fbe7c1"
    },
    {
      "sha": "2e2eb418f9",
      "message": "Fix the memory leak in the VM_GetCommandKeysWithFlags function (#3088)",
      "date": "2026-01-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3088",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2e2eb418f97ee8ac0dcccd1d5d790697bd0fa43e"
    },
    {
      "sha": "951d942ab2",
      "message": "Fix weekly workflow to continue after failure in releases branches (#3082)",
      "date": "2026-01-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3082",
      "commit_url": "https://github.com/valkey-io/valkey/commit/951d942ab20178b89c07420f8f4c13ae7a764749"
    },
    {
      "sha": "ff7395a90c",
      "message": "Fix flaky tests related to deferring client timing issues (#3071)",
      "date": "2026-01-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3071",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ff7395a90cf53b1756340c658e4bf8f460981b2e"
    },
    {
      "sha": "bdc62355c6",
      "message": "Add ValkeyModule_ClusterKeySlotC  (#2984)",
      "date": "2026-01-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2984",
      "commit_url": "https://github.com/valkey-io/valkey/commit/bdc62355c642af7ef9f1fa87ffe2aa5df59724e8"
    },
    {
      "sha": "2635377f4d",
      "message": "Fix used_memory_dataset underflow due to miscalculated used_memory_overhead (#3005)",
      "date": "2026-01-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3005",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2635377f4da46a50e66c4cad7c3128129a39279f"
    },
    {
      "sha": "2635377f4d",
      "message": "Fix used_memory_dataset underflow due to miscalculated used_memory_overhead (#3005)",
      "date": "2026-01-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3005",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2635377f4da46a50e66c4cad7c3128129a39279f"
    },
    {
      "sha": "fa59643128",
      "message": "Fix HEXPIRE should not delete items when validation rules fail and expiration is in the past (#3048)",
      "date": "2026-01-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3048",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fa5964312801ec435147ecd0667da03aad229434"
    },
    {
      "sha": "b7f1a6c7d9",
      "message": "Delete large binary junk file valkey-microbench (#3055)",
      "date": "2026-01-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3055",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b7f1a6c7d9ce83d202c128616b4abd28691fa3a1"
    },
    {
      "sha": "6e2fb51371",
      "message": "Initial draft of contributing guide (#1787)",
      "date": "2026-01-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1787",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6e2fb513713396363b8991dc699b767408570ace"
    },
    {
      "sha": "6e2fb51371",
      "message": "Initial draft of contributing guide (#1787)",
      "date": "2026-01-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1787",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6e2fb513713396363b8991dc699b767408570ace"
    },
    {
      "sha": "de00054326",
      "message": "Skip slot cache optimization for AOF client to prevent key duplication and data corruption (#3004)",
      "date": "2026-01-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3004",
      "commit_url": "https://github.com/valkey-io/valkey/commit/de00054326db991c35529dcbe5342470404c3bba"
    },
    {
      "sha": "f85ec7b00f",
      "message": "Add logging helper function to print node's ip:port when nodename not explicitly set (#2777)",
      "date": "2026-01-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2777",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f85ec7b00ff4a9c97ec72c196baf5bec96fb7fb7"
    },
    {
      "sha": "269f6e7083",
      "message": "Adding json support for log-format config (#1791)",
      "date": "2026-01-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1791",
      "commit_url": "https://github.com/valkey-io/valkey/commit/269f6e7083f29528191595584eac1c4cda2542d1"
    },
    {
      "sha": "5a3fb0454c",
      "message": "HFE make zero a valid ttl during import mode and data loading  (#3006)",
      "date": "2026-01-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3006",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5a3fb0454c866cdf46729694e24e2ecf792df97b"
    },
    {
      "sha": "82a312d8a5",
      "message": "replace info cluster info in a dedicated new section (#2964)",
      "date": "2026-01-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2964",
      "commit_url": "https://github.com/valkey-io/valkey/commit/82a312d8a595b71cc818fb045c84121cc13835ec"
    },
    {
      "sha": "263d9ea419",
      "message": "Fix zero length hash creation with HSETEX (#2998)",
      "date": "2026-01-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2998",
      "commit_url": "https://github.com/valkey-io/valkey/commit/263d9ea41972d8005e739324b826efe945549acc"
    },
    {
      "sha": "d10b06009f",
      "message": "Avoid useless seek in xtrim (#2985)",
      "date": "2026-01-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2985",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d10b06009f32dcbcf9473cfdb0ba6d45c5ee2b0f"
    },
    {
      "sha": "b56543285e",
      "message": "avoid memory leak of new argv when hexpire commands target only non-exiting fields (#2973)",
      "date": "2025-12-31",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2973",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b56543285e3d99ff7b2b123f818353e3315647a4"
    },
    {
      "sha": "7cef1e8ee2",
      "message": "fix hincrby* update volatile key tracking (#2974)",
      "date": "2025-12-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2974",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7cef1e8ee21bf67190a48fccdcbe73ba69b42a19"
    },
    {
      "sha": "e179fddcfd",
      "message": "Revert hgetall dynamic deferred response  (#2981)",
      "date": "2025-12-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2981",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e179fddcfdf1ff52e92a5d575196fb9453ae6227"
    },
    {
      "sha": "2a6137be03",
      "message": "Fix compile overflow warnings (#2963)",
      "date": "2025-12-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2963",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2a6137be033b01bff4b99a733c09e56b5c758028"
    },
    {
      "sha": "2a6137be03",
      "message": "Fix compile overflow warnings (#2963)",
      "date": "2025-12-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2963",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2a6137be033b01bff4b99a733c09e56b5c758028"
    },
    {
      "sha": "26162effd4",
      "message": "Restrict ttl from being negative and avoid crash in import-mode (#2944)",
      "date": "2025-12-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2944",
      "commit_url": "https://github.com/valkey-io/valkey/commit/26162effd4be179497843049566f3fa9c40b625d"
    },
    {
      "sha": "75707ac432",
      "message": "Avoid hgetall deferred response (#2966)",
      "date": "2025-12-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2966",
      "commit_url": "https://github.com/valkey-io/valkey/commit/75707ac4323b30f112e862b734e3436fa03b620c"
    },
    {
      "sha": "328b3ce3c8",
      "message": "Add support for Atomic Slot Migration to CLI (#2755)",
      "date": "2025-12-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2755",
      "commit_url": "https://github.com/valkey-io/valkey/commit/328b3ce3c8fd7f48eac6fd301612157bd00bfa90"
    },
    {
      "sha": "992b886260",
      "message": "Fix incorrect comment about STATS_METRIC_* Macro in server.h (#2935)",
      "date": "2025-12-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2935",
      "commit_url": "https://github.com/valkey-io/valkey/commit/992b886260685b9eed669ad8bb5dce74ebc1070c"
    },
    {
      "sha": "a571ac527f",
      "message": "Fix memory allocation size in getClusterNodesList (#2932)",
      "date": "2025-12-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2932",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a571ac527fa8030d5a51c1edaea948c393bb5fbd"
    },
    {
      "sha": "0a9cb985c8",
      "message": "Fix lua module build failure when using CLANG (#2955)",
      "date": "2025-12-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2955",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0a9cb985c8c37c54c5007bc0af2dcd0b6752a529"
    },
    {
      "sha": "d22fcfb032",
      "message": "Respect REPLCONF VERSION in diskless full sync (#2735)",
      "date": "2025-12-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2735",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d22fcfb0328404695f5fecf832f92ce5a28e4065"
    },
    {
      "sha": "6b60e6bfc7",
      "message": "Update MAINTAINERS list and add committee chair section (#2939)",
      "date": "2025-12-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2939",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6b60e6bfc7342cd3e7bc1abcbdf1787f5004d564"
    },
    {
      "sha": "cd6faaa726",
      "message": "Refine major decision process and update TSC composition rules (#2927)",
      "date": "2025-12-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2927",
      "commit_url": "https://github.com/valkey-io/valkey/commit/cd6faaa726791447f7adc196b6c77cc20658112d"
    },
    {
      "sha": "5940dbfb0b",
      "message": "Revert \"Allow partial sync after loading AOF with preamble (#2366)\" (#2925)",
      "date": "2025-12-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2925",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5940dbfb0b601dfc565ca7f349a3a62f67d7e5ed"
    },
    {
      "sha": "2a9a1731ee",
      "message": "Fix CLUSTER SLOTS crash when called from module timer callback (#2915)",
      "date": "2025-12-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2915",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2a9a1731ee8e049495068244822535928e5e0da8"
    },
    {
      "sha": "761fba2e9d",
      "message": "Fix persisting missing make variables (#2881)",
      "date": "2025-11-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2881",
      "commit_url": "https://github.com/valkey-io/valkey/commit/761fba2e9de2b1cf4f9081220565f78f1922b7c9"
    },
    {
      "sha": "9562bdc0ab",
      "message": "Align the complexity description for all multi field HFE commands docs (#2875)",
      "date": "2025-11-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2875",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9562bdc0ab185554d013e9406674aea1918dbc30"
    },
    {
      "sha": "8fdd586fc6",
      "message": "Fix link in CLUSTER SYNCSLOTS  (#377)",
      "date": "2025-11-26",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/377",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/8fdd586fc6c65542f0b279ca3ef3cbc314ab4490"
    },
    {
      "sha": "de414bc461",
      "message": "Add documentation for \"SENTINEL FAILOVER COORDINATED\" (#364)",
      "date": "2025-11-26",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/364",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/de414bc461dd76f4eca8c1517034882b253380ef"
    },
    {
      "sha": "b39df5ab39",
      "message": "Fix two links (#356)",
      "date": "2025-11-26",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/356",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/b39df5ab394262cc14cdfab6c063f53d7384456e"
    },
    {
      "sha": "f0e62eab4f",
      "message": "Fix incorrect topics link in quickstart page (#371)",
      "date": "2025-11-26",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/371",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/f0e62eab4fb41a66b2fd494834583254cfdac5a2"
    },
    {
      "sha": "dd2827a14e",
      "message": "Add support for asynchronous release to replicaKeysWithExpire on writable replica (#2849)",
      "date": "2025-11-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2849",
      "commit_url": "https://github.com/valkey-io/valkey/commit/dd2827a14ea183389e693255c244e1a7cad2acbb"
    },
    {
      "sha": "ed8856bdfc",
      "message": "Fix cluster slot migration flaky test (#2756)",
      "date": "2025-11-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2756",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ed8856bdfce07426b36a75b84cf9ee798024336f"
    },
    {
      "sha": "86db609219",
      "message": "Print node name on a best effort basis if light weight message is received before link stabilization (#2825)",
      "date": "2025-11-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2825",
      "commit_url": "https://github.com/valkey-io/valkey/commit/86db6092198fa42acf75cad2481bd1881cfd3165"
    },
    {
      "sha": "b93cfcc332",
      "message": "Attempt to fix flaky SCAN consistency test (#2834)",
      "date": "2025-11-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2834",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b93cfcc33277327f929c441a0cd98f02343b568e"
    },
    {
      "sha": "1b0b5c0cfd",
      "message": "New module API to perform prefix\u2011aware ACL permission check (#2796)",
      "date": "2025-11-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2796",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1b0b5c0cfd7fb31d7c957cbe533d95ad693499c0"
    },
    {
      "sha": "7f8c5b6f0c",
      "message": "[flaky-failure-fix] Increase the cluster-node-timeout to have longer delay between failover of each shard (#2793)",
      "date": "2025-11-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2793",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7f8c5b6f0c260698a16d18dde1105cdd61e05976"
    },
    {
      "sha": "ea103da5d6",
      "message": "New INFO section for scripting engines (#2738)",
      "date": "2025-10-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2738",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ea103da5d6e1ed8cd9993547a28a69fd26c04ffc"
    },
    {
      "sha": "baf2d572f7",
      "message": "Ensure the server executable exists before running tests (#2762)",
      "date": "2025-10-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2762",
      "commit_url": "https://github.com/valkey-io/valkey/commit/baf2d572f7c3016c25168928c6de039028f1ddcc"
    },
    {
      "sha": "f1270a851f",
      "message": "Adjust test runners to the number of tests to run (#2759)",
      "date": "2025-10-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2759",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f1270a851f6d488081a556a7f098a564c2b6d578"
    },
    {
      "sha": "746d9eca9e",
      "message": "Use the fetched TLS and TCP ports in clusterProcessGossipSection (#2761)",
      "date": "2025-10-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2761",
      "commit_url": "https://github.com/valkey-io/valkey/commit/746d9eca9e139af501f21944f200a707b2c8e394"
    },
    {
      "sha": "35b4e2f1ab",
      "message": "Update module api generation and format module.c (#2757)",
      "date": "2025-10-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2757",
      "commit_url": "https://github.com/valkey-io/valkey/commit/35b4e2f1ab84eb609162cca64bc2d29bd765ae7a"
    },
    {
      "sha": "95154feaa1",
      "message": "Bump old engine version(s) for compatibility test (#2741)",
      "date": "2025-10-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2741",
      "commit_url": "https://github.com/valkey-io/valkey/commit/95154feaa122f867ffd91c65b5ceb0a44dc7c0ef"
    },
    {
      "sha": "981b8fe1bd",
      "message": "Deflakes Primary COB growth with inactive replica (#2715)",
      "date": "2025-10-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2715",
      "commit_url": "https://github.com/valkey-io/valkey/commit/981b8fe1bdd1a58e1a06eb80186cd890b557f98a"
    },
    {
      "sha": "28e5dcce2c",
      "message": "Fix crash that occurs sometimes when aborting a slot migration while child snapshot is active (#2721)",
      "date": "2025-10-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2721",
      "commit_url": "https://github.com/valkey-io/valkey/commit/28e5dcce2caafc7680460810a3daca4df77ca10e"
    },
    {
      "sha": "19474c867a",
      "message": "Deflake atomic slot migration client flag test (#2720)",
      "date": "2025-10-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2720",
      "commit_url": "https://github.com/valkey-io/valkey/commit/19474c867a67bde06e20335872ad9d6e0b2eb83f"
    },
    {
      "sha": "dbcf022480",
      "message": "Stop using DEBUG LOADAOF on replica in ASM tests (#2719)",
      "date": "2025-10-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2719",
      "commit_url": "https://github.com/valkey-io/valkey/commit/dbcf0224806ed36acceb01332fbaa371bd6b185a"
    },
    {
      "sha": "f0f4e52142",
      "message": "Avoid indicating that cluster slots is being replaced by cluster shards (#366)",
      "date": "2025-10-11",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/366",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/f0f4e521424790d6f3431dde542a2a20e2b07eb9"
    },
    {
      "sha": "8182f4a0b9",
      "message": "HSETEX with FXX should not create an object if it does not exist (#2716)",
      "date": "2025-10-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2716",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8182f4a0b9c92639f7528f4ae412e957c7600bb4"
    },
    {
      "sha": "18214be490",
      "message": "Add compatibility test with Valkey 7.2/8.0 (#2342)",
      "date": "2025-10-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2342",
      "commit_url": "https://github.com/valkey-io/valkey/commit/18214be4902cb4c3792d27567a00db5365643fc9"
    },
    {
      "sha": "f598d11a4b",
      "message": "Deflake replica selection test by relaxing cluster configurations (#2672)",
      "date": "2025-10-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2672",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f598d11a4bd3465c6f1b020906054161bef60890"
    },
    {
      "sha": "f7c95277da",
      "message": "Add invalid RDB signature to log statement (#2710)",
      "date": "2025-10-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2710",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f7c95277dac5433af7a9c1c3106b23002e82648f"
    },
    {
      "sha": "155b0bb821",
      "message": "Fix memory leak with CLIENT LIST/KILL duplicate filters (#2362)",
      "date": "2025-10-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2362",
      "commit_url": "https://github.com/valkey-io/valkey/commit/155b0bb82196c8fc70245823856a8e966525d55a"
    },
    {
      "sha": "5bbbc6bd9a",
      "message": "Add shard id field to CLUSTER SHARDS response (#2568)",
      "date": "2025-10-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2568",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5bbbc6bd9a3ec44c9a47b0cbb91219370e798088"
    },
    {
      "sha": "22247f6119",
      "message": "Reduce flakiness of atomic slot migration AOF test (#2705)",
      "date": "2025-10-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2705",
      "commit_url": "https://github.com/valkey-io/valkey/commit/22247f6119526c41cb59890abff3f07e9b4df366"
    },
    {
      "sha": "3390b1e608",
      "message": "Allow TCL 9.0 for tests (#1673)",
      "date": "2025-10-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1673",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3390b1e608f2cf39c00cf66a2e975b756c5e8b02"
    },
    {
      "sha": "d5bb986fd5",
      "message": "Add slot migration client flags and module context flags (#2639)",
      "date": "2025-10-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2639",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d5bb986fd592733330ff4042c011f7c64da543ec"
    },
    {
      "sha": "a9a65abc85",
      "message": "Implement a lolwut for version 9 (#2646)",
      "date": "2025-09-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2646",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a9a65abc85b396e6b1b2ebf68564dabc251bc06e"
    },
    {
      "sha": "6c1bb73a57",
      "message": "Add atomic slot migration test for unblock on migration complete (#2637)",
      "date": "2025-09-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2637",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6c1bb73a57a04bd40ef6091ecaf19473601c57f4"
    },
    {
      "sha": "d21d529851",
      "message": "Optimize skiplist random level generation logic (#2631)",
      "date": "2025-09-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2631",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d21d529851bef718ed666ab87d975b32a9c7ac5c"
    },
    {
      "sha": "8d562d26df",
      "message": "Fix closing slot migration pipe read (#2630)",
      "date": "2025-09-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2630",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8d562d26df25cae9f354e0d447979d4b53f061e9"
    },
    {
      "sha": "ff1d017958",
      "message": "Fix flaky cluster flush slot test (#2626)",
      "date": "2025-09-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2626",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ff1d017958783904169e0b53fd80f76b9f7ef143"
    },
    {
      "sha": "80bbbcf6fe",
      "message": "Fix memory leak in deferred reply buffer (#2615)",
      "date": "2025-09-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2615",
      "commit_url": "https://github.com/valkey-io/valkey/commit/80bbbcf6fe321b513b95d68c15d270de4f18edf6"
    },
    {
      "sha": "fab2a12c51",
      "message": "Increase wait time condition for New Master down consecutively test (#2612)",
      "date": "2025-09-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2612",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fab2a12c510399a70b09ab3215f690e012863e34"
    },
    {
      "sha": "a47e8fa150",
      "message": "Expand wait condition time for slave selection test (#2604)",
      "date": "2025-09-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2604",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a47e8fa1505578d78cef5c5e11da0972c3dae560"
    },
    {
      "sha": "9d10abfbde",
      "message": "Relaxed RDB check for foreign RDB formats (#2543)",
      "date": "2025-09-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2543",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9d10abfbded4ed9633ac50c8c09a9a9965dd6740"
    },
    {
      "sha": "47d2203c1b",
      "message": "Store number of keys with volatile items per slot in RDB aux field and pre-size hashtables on load (#2572)",
      "date": "2025-09-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2572",
      "commit_url": "https://github.com/valkey-io/valkey/commit/47d2203c1bba39dbd5de9da1ba1c7acb4b7316e0"
    },
    {
      "sha": "c039b691c4",
      "message": "Fix module context object re-usage in scripting engines (#2358)",
      "date": "2025-09-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2358",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c039b691c42810a39b08bc8223daba45a665d17f"
    },
    {
      "sha": "d6e011f955",
      "message": "Reduce active defrag test latency by lowering hit threshold (#2553)",
      "date": "2025-08-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2553",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d6e011f955b18f5af46af07569c686a16d82e129"
    },
    {
      "sha": "6774d173c4",
      "message": "Fix the issue of incorrect commandlog metrics in the script (#2565)",
      "date": "2025-08-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2565",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6774d173c4a3b931dae953158beb1f85af43e972"
    },
    {
      "sha": "3db75f5551",
      "message": "Reset cluster related stats in CONFIG RESETSTATS (#2458)",
      "date": "2025-08-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2458",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3db75f5551cdf6da8aa27b719d52cce598fd0b54"
    },
    {
      "sha": "cf90acbc61",
      "message": "Correct path to gen-test-certs.sh in README.md (#2554)",
      "date": "2025-08-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2554",
      "commit_url": "https://github.com/valkey-io/valkey/commit/cf90acbc6137ede7ae17fb1450c8aa19a62d163c"
    },
    {
      "sha": "06cefc181a",
      "message": "Attempt to fix sub-replica getting out of sync (#2548)",
      "date": "2025-08-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2548",
      "commit_url": "https://github.com/valkey-io/valkey/commit/06cefc181abbe458d59a0c4865670810a9cb65d3"
    },
    {
      "sha": "3086e61d4b",
      "message": "Update reply schema for LMOVE and BLMOVE (#2541)",
      "date": "2025-08-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2541",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3086e61d4b06a81602fc74163eb7d4eb6b6bfe41"
    },
    {
      "sha": "9aeab8ccba",
      "message": "Consistently use static_assert across code (#2538)",
      "date": "2025-08-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2538",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9aeab8ccbac0ca4923676c749c98d0de4718c872"
    },
    {
      "sha": "23112fad87",
      "message": "fix hsetex handling of wrong number of fields (#2509)",
      "date": "2025-08-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2509",
      "commit_url": "https://github.com/valkey-io/valkey/commit/23112fad87e65380d4774233fc0fa1edb65c9364"
    },
    {
      "sha": "39d5c6e6ee",
      "message": "Fix vset unittest compilation warning for bad signedness comparison (#2523)",
      "date": "2025-08-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2523",
      "commit_url": "https://github.com/valkey-io/valkey/commit/39d5c6e6ee46b839c935974eb7ff4de7d87399f7"
    },
    {
      "sha": "2ca0dd8781",
      "message": "Make cluster failover delay relative to node timeout (#2449)",
      "date": "2025-08-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2449",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2ca0dd878196033811a69a9a2a3381030e5264dd"
    },
    {
      "sha": "390e0c9555",
      "message": "CONFIG GET command return sorted output (#2493)",
      "date": "2025-08-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2493",
      "commit_url": "https://github.com/valkey-io/valkey/commit/390e0c95551236c863da76fb0675f55b8b53cfcd"
    },
    {
      "sha": "f36cc20836",
      "message": "Fix cluster test module to pass null terminated node-id to SendClusterMessage (#2484)",
      "date": "2025-08-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2484",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f36cc208368c4dd63f8e4a26f56d4ea1daf629f6"
    },
    {
      "sha": "dcbaecddce",
      "message": "Ensures presence of slots on the node before test is run (#2486)",
      "date": "2025-08-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2486",
      "commit_url": "https://github.com/valkey-io/valkey/commit/dcbaecddce5d56076189bcfb514eece917c1297e"
    },
    {
      "sha": "15355124d4",
      "message": "HSETEX 'hset' notification should only be generated if not expired (#2475)",
      "date": "2025-08-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2475",
      "commit_url": "https://github.com/valkey-io/valkey/commit/15355124d42b0b82ca85adbf887b42a4a21b49b6"
    },
    {
      "sha": "c93b2971e6",
      "message": "Increment expired_fields stat when assigned TTL is in the past (#2474)",
      "date": "2025-08-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2474",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c93b2971e6780a8f4c427752b9be1443a0f52d6a"
    },
    {
      "sha": "6c2e4f9553",
      "message": "Deflake hashexpire tests (#2473)",
      "date": "2025-08-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2473",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6c2e4f955310f956b25696fd9d008ea0e13d980e"
    },
    {
      "sha": "a89e529932",
      "message": "Redact user data when hide-user-data-from-log enabled (#2274)",
      "date": "2025-08-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2274",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a89e529932b8106010b1b8faedc974ff3fbc89ad"
    },
    {
      "sha": "ecca213311",
      "message": "Fix out-of-bound memory access when num-fields is not provided (#2464)",
      "date": "2025-08-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2464",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ecca21331117d38c9eadbbccf5c80c34cb11ec53"
    },
    {
      "sha": "bddc9db087",
      "message": "Fix HGETEX to return array response when the hash object is empty (#2462)",
      "date": "2025-08-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2462",
      "commit_url": "https://github.com/valkey-io/valkey/commit/bddc9db087a4540d577049871eb1c37b334994e5"
    },
    {
      "sha": "cc465383c4",
      "message": "Adding backup directory check for valkey-cli --cluster backup (#2452)",
      "date": "2025-08-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2452",
      "commit_url": "https://github.com/valkey-io/valkey/commit/cc465383c419a0cbfdd60a17256b7a0fcffe21c8"
    },
    {
      "sha": "de7bb614f1",
      "message": "Fix expectations for manual failover tests (#2453)",
      "date": "2025-08-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2453",
      "commit_url": "https://github.com/valkey-io/valkey/commit/de7bb614f1843cebd8fdaf49fdaa29de895519e7"
    },
    {
      "sha": "7bbf5233c8",
      "message": "Fix and remove conflicting paths from clang-format workflow (#2455)",
      "date": "2025-08-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2455",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7bbf5233c8cbdb35d020cd7b64849fd2774feb4d"
    },
    {
      "sha": "8d9d642872",
      "message": "Document FAILOVER option to SHUTDOWN command (#344)",
      "date": "2025-08-08",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/344",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/8d9d6428726d19eaead6903aeae62fbf927dd4b5"
    },
    {
      "sha": "ba19ec861a",
      "message": "Fix hashexpire test toggle active expire (#2447)",
      "date": "2025-08-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2447",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ba19ec861a660059ac9e22652166c562cdd75493"
    },
    {
      "sha": "2b9fb7514e",
      "message": "make sure replica and primary are in sync during hfe test Promotion to primary (#2446)",
      "date": "2025-08-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2446",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2b9fb7514ec2feb2be73df58f23e4f93fa507951"
    },
    {
      "sha": "772d12ed02",
      "message": "verify expiration is set on hashexpire active expire test (#2440)",
      "date": "2025-08-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2440",
      "commit_url": "https://github.com/valkey-io/valkey/commit/772d12ed024632da58846bba86979fc5908060d8"
    },
    {
      "sha": "fd8270a0aa",
      "message": "[CRASH] Fix missing check for executing client (#2347)",
      "date": "2025-08-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2347",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fd8270a0aab6c15058997a0e8436c9682dac2036"
    },
    {
      "sha": "ba7334c7c6",
      "message": "Fix hfe no malloc size unit (#2436)",
      "date": "2025-08-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2436",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ba7334c7c61abd854109f1d19f807098e5f22cb1"
    },
    {
      "sha": "52b5519c5a",
      "message": "Use unsigned long for `maxiterations`, fixing undefined behavior in scan with extremely large count (#2414)",
      "date": "2025-08-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2414",
      "commit_url": "https://github.com/valkey-io/valkey/commit/52b5519c5ae5f059023b81681514c978853e39f6"
    },
    {
      "sha": "7d63bc5bab",
      "message": "Increase TID count to accomodate valkey-search reader/writer pools (#2417)",
      "date": "2025-08-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2417",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7d63bc5babc936402573f067ecd36a4e4557f534"
    },
    {
      "sha": "8973cdf014",
      "message": "Make ./runtest --dump-logs dump logs for timeout tests's servers (#2412)",
      "date": "2025-08-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2412",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8973cdf01432c19f9971b0b46ef225b85b4c4b3b"
    },
    {
      "sha": "bcaf918a79",
      "message": "Try to stabilize aof test (#2399)",
      "date": "2025-07-31",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2399",
      "commit_url": "https://github.com/valkey-io/valkey/commit/bcaf918a7933d76fff9dd25c3ea2000c4289b5a3"
    },
    {
      "sha": "8df8c84ffe",
      "message": "Same number of hyphens for summary output (#2397)",
      "date": "2025-07-31",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2397",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8df8c84ffe45194d1763d0262d565c3113c8e40c"
    },
    {
      "sha": "f21015c904",
      "message": "Limiting the new reconnections for failed nodes (#2154)",
      "date": "2025-07-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2154",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f21015c9041463238d2996f6e595c2a00d7e066b"
    },
    {
      "sha": "89e0e64964",
      "message": "Auto-failover on shutdown unified config (#2292)",
      "date": "2025-07-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2292",
      "commit_url": "https://github.com/valkey-io/valkey/commit/89e0e64964ed3a4c58cc73000786462a1f7d9f94"
    },
    {
      "sha": "de765863f0",
      "message": "Fix large allocations crashing Valkey during active defrag (#2353)",
      "date": "2025-07-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2353",
      "commit_url": "https://github.com/valkey-io/valkey/commit/de765863f049ab44e11dceffff7a9b5fc0244f20"
    },
    {
      "sha": "b44e24493b",
      "message": "Add cross engine (Redis OSS) compatible test (#2336)",
      "date": "2025-07-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2336",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b44e24493bf0a1b142fba3ab1c54dab6c0a4cb2a"
    },
    {
      "sha": "b44e24493b",
      "message": "Add cross engine (Redis OSS) compatible test (#2336)",
      "date": "2025-07-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2336",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b44e24493bf0a1b142fba3ab1c54dab6c0a4cb2a"
    },
    {
      "sha": "ba24e0d4f5",
      "message": "Avoid logging sender role on each cluster message (#2337)",
      "date": "2025-07-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2337",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ba24e0d4f536b9c830a4505ee7064c301510dcc6"
    },
    {
      "sha": "30ea139fb4",
      "message": "Disable active expiry until it's needed (#2313)",
      "date": "2025-07-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2313",
      "commit_url": "https://github.com/valkey-io/valkey/commit/30ea139fb49e3d8e0a40833c92d23938165c6ea9"
    },
    {
      "sha": "d4d09d706d",
      "message": "Enable tab completion of test file path for runtest util and allow directory as path (#630)",
      "date": "2025-07-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/630",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d4d09d706dcf8f57e4d3d00f1fd5f91dfa5a9c2b"
    },
    {
      "sha": "9c45cf3342",
      "message": "Make unit test report each memory leak only once (#2304)",
      "date": "2025-07-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2304",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9c45cf33423e2f7c70ccf6adbdb428a1890cb4a5"
    },
    {
      "sha": "e53e048c69",
      "message": "Fix leak when shrinking a hashtable without entries (#2288)",
      "date": "2025-07-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2288",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e53e048c6960a2b821d33ef3f4fb55bf8977dfd5"
    },
    {
      "sha": "ad2c6b049b",
      "message": "Fix hashtablePauseAutoShrink and use it in hashtableScanDefrag (#2257)",
      "date": "2025-06-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2257",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ad2c6b049b01f28dc39e0b39dfc1f463a86056e6"
    },
    {
      "sha": "2aea99b26f",
      "message": "Do not report negative passing test count (#2260)",
      "date": "2025-06-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2260",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2aea99b26f6520ab0ee5068a0a16e66c78c3fc47"
    },
    {
      "sha": "6a259d8e05",
      "message": "Properly account for checking zmalloc_used_memory() (#2263)",
      "date": "2025-06-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2263",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6a259d8e05b7038c5c2149450d850bc2c8f9c45d"
    },
    {
      "sha": "621039d868",
      "message": "Preserve newlines in commands.def reporting (#2259)",
      "date": "2025-06-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2259",
      "commit_url": "https://github.com/valkey-io/valkey/commit/621039d868f4afbc0a4268deb4db46acd4cae6c4"
    },
    {
      "sha": "4a3e713032",
      "message": "Converge divergent shard-id persisted in nodes.conf to primary's shard id (#2174)",
      "date": "2025-06-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2174",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4a3e713032ff73fc652221fef958bae6bb1958f4"
    },
    {
      "sha": "502dd451d1",
      "message": "Fix incorrect laddr field and correct getClientSockname declaration (#2214)",
      "date": "2025-06-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2214",
      "commit_url": "https://github.com/valkey-io/valkey/commit/502dd451d176b805c830291430cd786642a587df"
    },
    {
      "sha": "04353aea38",
      "message": "Ensure empty error tables in scripts don't crash Valkey (#2229)",
      "date": "2025-06-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2229",
      "commit_url": "https://github.com/valkey-io/valkey/commit/04353aea381f8c93dcb323839b4dc4821fcbd042"
    },
    {
      "sha": "7bc34cf876",
      "message": "fix: use replica's last selected db for dual-channel sync (#2188)",
      "date": "2025-06-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2188",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7bc34cf87644733621108199efcdd15ea3500013"
    },
    {
      "sha": "ac2451bf5c",
      "message": "Run external cluster tests with multiple databases (#2176)",
      "date": "2025-06-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2176",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ac2451bf5c7bfec4bd579cfb33b9c7a3c2e0c03f"
    },
    {
      "sha": "c41ffc3401",
      "message": "valkey-check-rdb: Fix truncated long aux fields (#2193)",
      "date": "2025-06-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2193",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c41ffc3401acd3f9b7c2bfc50314626805718dd0"
    },
    {
      "sha": "b5e012a108",
      "message": "Fix invalid functionname processMultibulkBuffer typo in comments. (#2097)",
      "date": "2025-06-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2097",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b5e012a1083cbfda3ab27c6df3fc8d82534d6a80"
    },
    {
      "sha": "988297d19a",
      "message": "Avoid log spam about cluster node failure detection by each primary (#2010)",
      "date": "2025-06-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2010",
      "commit_url": "https://github.com/valkey-io/valkey/commit/988297d19abea59799cdfaedcf7d0b01f0a559d8"
    },
    {
      "sha": "4dae83dba1",
      "message": "Remove unnecessary refcount increment in propagateDelete (#2175)",
      "date": "2025-06-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2175",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4dae83dba19ee06191dcd927e7c9ae20d79f4324"
    },
    {
      "sha": "23ecd7a967",
      "message": "Unify behavior of CLIENT REPLY in multi with other NO_MULTI commands (#2152)",
      "date": "2025-05-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2152",
      "commit_url": "https://github.com/valkey-io/valkey/commit/23ecd7a967efcdb3505196cc2f946b5277859355"
    },
    {
      "sha": "51e96c1df2",
      "message": "Add ricardo as a commiter (#2149)",
      "date": "2025-05-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2149",
      "commit_url": "https://github.com/valkey-io/valkey/commit/51e96c1df2f980d679a33926d3e9dca86929ad27"
    },
    {
      "sha": "92c859de68",
      "message": "Update tests to catch module context leaks if using aux save/load  (#2150)",
      "date": "2025-05-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2150",
      "commit_url": "https://github.com/valkey-io/valkey/commit/92c859de6813d71aa4cb99f6731faefd88c458b8"
    },
    {
      "sha": "689a3b1581",
      "message": "Flip pfail flag while marking node as failed (#2012)",
      "date": "2025-05-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2012",
      "commit_url": "https://github.com/valkey-io/valkey/commit/689a3b15813758cfce0b8699baf5f147093ef215"
    },
    {
      "sha": "17e66863a5",
      "message": "Detect SSL_new() returning NULL in outgoing connections (#2140)",
      "date": "2025-05-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2140",
      "commit_url": "https://github.com/valkey-io/valkey/commit/17e66863a5f9d6065544d0b3d655ba8f40081570"
    },
    {
      "sha": "258213ff7e",
      "message": "Free module context even if there was no content written in auxsave2 (#2132)",
      "date": "2025-05-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2132",
      "commit_url": "https://github.com/valkey-io/valkey/commit/258213ff7e305b7bd77549577712084cd2d9e512"
    },
    {
      "sha": "3ceae81fc4",
      "message": "Fix a case of out of bound read when cluster node ID is provided with wrong length in CLUSTER FORGET (#2108)",
      "date": "2025-05-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2108",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3ceae81fc4cf065dae00888ab92b7aa069fde111"
    },
    {
      "sha": "d00fb8e713",
      "message": "Only mark the client reprocessing flag when unblocked on keys (#2109)",
      "date": "2025-05-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2109",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d00fb8e713d651f7c42a36f052a4fd12a9637e0e"
    },
    {
      "sha": "30599c4936",
      "message": "fix commandlog argument schema to use pure tokens (#2113)",
      "date": "2025-05-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2113",
      "commit_url": "https://github.com/valkey-io/valkey/commit/30599c4936ccee982f7e94c4913e82014ff0d779"
    },
    {
      "sha": "1531b44a15",
      "message": "Respect process umask when creating data files (#1725)",
      "date": "2025-05-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1725",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1531b44a153857b9929f2ed5bedbf1cafb4c07d9"
    },
    {
      "sha": "45d03e6164",
      "message": "Fix random element in skewed sparse hash table (#2085)",
      "date": "2025-05-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2085",
      "commit_url": "https://github.com/valkey-io/valkey/commit/45d03e616421d0a1a303c3d2c84a9f89de9ee1e1"
    },
    {
      "sha": "8d686dd74f",
      "message": "Fix minor memory leak in valkey-cli when command table hint fails due to NOAUTH (#2091)",
      "date": "2025-05-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2091",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8d686dd74fccedcbd612e6e5c82e95cfc9cc3c16"
    },
    {
      "sha": "b7f4b20bc4",
      "message": "Make sure that the same point reports for geo comparisons (#2063)",
      "date": "2025-05-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2063",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b7f4b20bc4966a1a30918ff77d36e3f50bfe45ff"
    },
    {
      "sha": "4ede540e92",
      "message": "Fix variable scope confusion (#2071)",
      "date": "2025-05-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2071",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4ede540e9236430b15100f2e37c4280d2a495c24"
    },
    {
      "sha": "51387ddc99",
      "message": "Update function clusterNodeSetSlotBit() return type to void (#1934)",
      "date": "2025-04-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1934",
      "commit_url": "https://github.com/valkey-io/valkey/commit/51387ddc99404dd4ecb426f43fbe4630659922ea"
    },
    {
      "sha": "5f5ad43ebb",
      "message": "Fix random-key CI failure: key may expire before CLIENT PAUSE (#1932)",
      "date": "2025-04-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1932",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5f5ad43ebbc1075a51143de2429a562f6b82b94a"
    },
    {
      "sha": "74075203d2",
      "message": "Implement: CLUSTER REPLICATE NO ONE (#1674)",
      "date": "2025-04-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1674",
      "commit_url": "https://github.com/valkey-io/valkey/commit/74075203d2b95214af853a9d28f48010bdc76a4c"
    },
    {
      "sha": "204097dac4",
      "message": "Fix the build on less common platforms in zmalloc.c (#1922)",
      "date": "2025-04-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1922",
      "commit_url": "https://github.com/valkey-io/valkey/commit/204097dac46730e9eb125c822c1dc2959c6572c5"
    },
    {
      "sha": "cc31c20a40",
      "message": "Add human node name to log statement with node name (#1918)",
      "date": "2025-04-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1918",
      "commit_url": "https://github.com/valkey-io/valkey/commit/cc31c20a409c738a058e685c5adb41e9761d8332"
    },
    {
      "sha": "add716b7dd",
      "message": "Fix valkey-cli port parse logic for invalid string (#1915)",
      "date": "2025-04-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1915",
      "commit_url": "https://github.com/valkey-io/valkey/commit/add716b7ddce48d4e13ebffe65401c7d0e26b91a"
    },
    {
      "sha": "5cce160315",
      "message": "In LOLWUT's reply, change \"Redis ver.\" to \"Valkey ver.\" (#1559)",
      "date": "2025-04-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1559",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5cce160315e5e1c7ba605bca6874eef08be4faf0"
    },
    {
      "sha": "5cce160315",
      "message": "In LOLWUT's reply, change \"Redis ver.\" to \"Valkey ver.\" (#1559)",
      "date": "2025-04-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1559",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5cce160315e5e1c7ba605bca6874eef08be4faf0"
    },
    {
      "sha": "e5ce98459e",
      "message": "Initialize child process pipe file descriptor to -1 (#1911)",
      "date": "2025-04-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1911",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e5ce98459eae52be89428da3ac9cd60beba28f80"
    },
    {
      "sha": "74b6330f63",
      "message": "Update ACL SETUSER command help message (#1899)",
      "date": "2025-04-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1899",
      "commit_url": "https://github.com/valkey-io/valkey/commit/74b6330f63a577d7c12c6a04c1bf24cd2ae62d9f"
    },
    {
      "sha": "0af8a120d6",
      "message": "Add --sequential to valkey-benchmark (for populating entire keyspace) (#1839)",
      "date": "2025-04-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1839",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0af8a120d6eeed4836b6f0dc1ad970fa078412d1"
    },
    {
      "sha": "da3244352f",
      "message": "Remove TLSCONN_DEBUG dead code in tls.c (#1891)",
      "date": "2025-03-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1891",
      "commit_url": "https://github.com/valkey-io/valkey/commit/da3244352fb20fe3a84d080fe62e9d499faf2231"
    },
    {
      "sha": "d56a1f79b4",
      "message": "[cluster] Add node id to log statement for closing link on first message as lightweight (#1869)",
      "date": "2025-03-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1869",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d56a1f79b451d89904b421dcc94a519b271c16f4"
    },
    {
      "sha": "d9ae08684c",
      "message": "Minor cleanup remove unnecessary cast since slot is int (#1865)",
      "date": "2025-03-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1865",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d9ae08684c0ae4e4cb4e459d06612a67d1ec413e"
    },
    {
      "sha": "89b1f8fb11",
      "message": "Update valkey-benchmark parseURI function name and comment (#1845)",
      "date": "2025-03-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1845",
      "commit_url": "https://github.com/valkey-io/valkey/commit/89b1f8fb11267572d7a3a97a6c21c9d58c96435d"
    },
    {
      "sha": "1a975faf79",
      "message": "Fix ACL LOAD crash on replica since the primary client don't has a user (#1842)",
      "date": "2025-03-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1842",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1a975faf79c35cbbd6c846b118b3060af4ccf559"
    },
    {
      "sha": "8221a15565",
      "message": "Fix bug where invalidation messages were getting sent to closing clients (#1823)",
      "date": "2025-03-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1823",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8221a155657fa2cee72d9043bd145fde6639f9b4"
    },
    {
      "sha": "8221a15565",
      "message": "Fix bug where invalidation messages were getting sent to closing clients (#1823)",
      "date": "2025-03-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1823",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8221a155657fa2cee72d9043bd145fde6639f9b4"
    },
    {
      "sha": "bb944c7860",
      "message": "Adds a memory leak check after running a unit test (#1798)",
      "date": "2025-03-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1798",
      "commit_url": "https://github.com/valkey-io/valkey/commit/bb944c78602cbce2d452e364709c934c1dfe5531"
    },
    {
      "sha": "fe4241586d",
      "message": "Use the wrapper from cli_common instead of hiredis (#1802)",
      "date": "2025-03-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1802",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fe4241586d2aa594110b135a2b66168618c68daa"
    },
    {
      "sha": "cab500cf6a",
      "message": "Fix incorrect assertion in client list operations (#1800)",
      "date": "2025-03-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1800",
      "commit_url": "https://github.com/valkey-io/valkey/commit/cab500cf6a4a5618a73a0142fa5c82c711d4dd78"
    },
    {
      "sha": "185fcec976",
      "message": "Stop running large memory test for address santizer (#1810)",
      "date": "2025-03-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1810",
      "commit_url": "https://github.com/valkey-io/valkey/commit/185fcec976d116e704ef507c9d577f4ccf93b4d5"
    },
    {
      "sha": "0cc0bf7222",
      "message": "make net_input_bytes_curr_cmd more readable (#1756)",
      "date": "2025-03-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1756",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0cc0bf7222d6266bb53feb16c785c67a513cf0d1"
    },
    {
      "sha": "6156590fa7",
      "message": "Fix hashTypeEntryDefrag returning bad pointer (#1799)",
      "date": "2025-02-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1799",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6156590fa7272140dcf798a450f8c5f6003abe91"
    },
    {
      "sha": "089b830479",
      "message": "Consistent look and feel of licenses (#1788)",
      "date": "2025-02-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1788",
      "commit_url": "https://github.com/valkey-io/valkey/commit/089b830479f4984e77e570560f85e37212879740"
    },
    {
      "sha": "f7c6d3192f",
      "message": "Migrate binaries build to ARM github runners (#1790)",
      "date": "2025-02-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1790",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f7c6d3192fc4920e54b6b5d2a27d3e18c647c618"
    },
    {
      "sha": "49663575c0",
      "message": "cmd's out bytes need count deferred reply (#1760)",
      "date": "2025-02-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1760",
      "commit_url": "https://github.com/valkey-io/valkey/commit/49663575c0df441a894578c5c1220ddda83d6b56"
    },
    {
      "sha": "587a6fce12",
      "message": "valkey-cli: ensure output ends with a newline if missing when printing reply (#1782)",
      "date": "2025-02-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1782",
      "commit_url": "https://github.com/valkey-io/valkey/commit/587a6fce12dbbb777bd9487af0e454b06ea69651"
    },
    {
      "sha": "6355d85715",
      "message": "Update I/O threads documentation (#222)",
      "date": "2025-02-27",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/222",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/6355d8571529b2fff0e33a6372deacd567595a01"
    },
    {
      "sha": "7db7cf5839",
      "message": "Fixed function name for ValkeyModule_RegisterCommandFilter (#236)",
      "date": "2025-02-27",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/236",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/7db7cf5839ce0402133443aae53d201354dbe802"
    },
    {
      "sha": "77de3bc545",
      "message": "Update client-list.md and fix a misleading word (#237)",
      "date": "2025-02-26",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/237",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/77de3bc545da0498ce560872663975be2bc31d21"
    },
    {
      "sha": "ee8465ce3b",
      "message": "Fixed active-expire-effort description in conf file (#1773)",
      "date": "2025-02-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1773",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ee8465ce3bf8a7291f6f7e3cb66184064a6a5312"
    },
    {
      "sha": "bd951e694a",
      "message": "Fixed issue with `CONFIG RESETSTAT` in cluster module message callback test (#1768)",
      "date": "2025-02-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1768",
      "commit_url": "https://github.com/valkey-io/valkey/commit/bd951e694abde55520dd967f0520fd9bc848d41e"
    },
    {
      "sha": "df5caa637a",
      "message": "Disable Fedora Fawhide in Daily runs (#1769)",
      "date": "2025-02-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1769",
      "commit_url": "https://github.com/valkey-io/valkey/commit/df5caa637a1d4c833fb9fa994e8a7c7fad1ef022"
    },
    {
      "sha": "54c4bbcec7",
      "message": "Add new module API flag to bypass command validation (#1357)",
      "date": "2025-02-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1357",
      "commit_url": "https://github.com/valkey-io/valkey/commit/54c4bbcec712d1f8ae0aaf1940040fd579abed48"
    },
    {
      "sha": "d588bb3bee",
      "message": "Fix raxRemove crash at memcpy() due to key size exceeds max Rax size (#1722)",
      "date": "2025-02-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1722",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d588bb3bee0122ead9671647c34b7452bee81381"
    },
    {
      "sha": "e6e65c64a3",
      "message": "Explicitly use github arm runners for ARM release (#1742)",
      "date": "2025-02-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1742",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e6e65c64a36aca0dce7ef382ea8ec35d8fa0481f"
    },
    {
      "sha": "0b73968d56",
      "message": "Add a daily test running for ARM (#1738)",
      "date": "2025-02-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1738",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0b73968d56bad01e4395f8049c282bf1307bf600"
    },
    {
      "sha": "c4c9c6db48",
      "message": "Introduce Valkey release stage indication (#1724)",
      "date": "2025-02-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1724",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c4c9c6db48c318c3d9c102eb172af4eacbefa29b"
    },
    {
      "sha": "41a4bc2649",
      "message": "Introduce valkey_version_full info field which includes the release stage (#1723)",
      "date": "2025-02-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1723",
      "commit_url": "https://github.com/valkey-io/valkey/commit/41a4bc264906b8f0119938e5f92a773c575456e2"
    },
    {
      "sha": "a019089ad8",
      "message": "Prevent double writing out of responses and fix reply schema CI (#1715)",
      "date": "2025-02-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1715",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a019089ad8bd42cfdea6b2c9bb27c17d7e985ab5"
    },
    {
      "sha": "44675562b5",
      "message": "Correctly detect address sanitizer with Clang (#1712)",
      "date": "2025-02-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1712",
      "commit_url": "https://github.com/valkey-io/valkey/commit/44675562b536e2b235a4c0f92e256561506d1f71"
    },
    {
      "sha": "86469ab167",
      "message": "Fix: Exclude RTLD_DEEPBIND for Alpine Linux (musl-based systems) (#1707)",
      "date": "2025-02-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1707",
      "commit_url": "https://github.com/valkey-io/valkey/commit/86469ab167f337b18a22a4e0110bb135146d5575"
    },
    {
      "sha": "eec01d75ad",
      "message": "explain capa for client list (#229)",
      "date": "2025-02-11",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/229",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/eec01d75ad9655e895e69ebb21618fd8004fd2fc"
    },
    {
      "sha": "99e2dc9e74",
      "message": "Add support for MustObeyClient Module API (#1582)",
      "date": "2025-02-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1582",
      "commit_url": "https://github.com/valkey-io/valkey/commit/99e2dc9e746ff1d733af922694ca0212769351de"
    },
    {
      "sha": "96857bfeb1",
      "message": "show capa in CLIENT LIST (#1698)",
      "date": "2025-02-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1698",
      "commit_url": "https://github.com/valkey-io/valkey/commit/96857bfeb196ea5fdb1afa00bdbd8ae85889232c"
    },
    {
      "sha": "0e66aaa60e",
      "message": "Run unit tests with ASAN in CI (#1700)",
      "date": "2025-02-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1700",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0e66aaa60e832078ab78c852a76319f91b560d99"
    },
    {
      "sha": "61a854dbbd",
      "message": "Fix client trackinginfo crash when tracking off by default (#1684)",
      "date": "2025-02-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1684",
      "commit_url": "https://github.com/valkey-io/valkey/commit/61a854dbbd14c80e0584bbdfa71f3b5b25d66153"
    },
    {
      "sha": "7fa784a275",
      "message": "Disable mem usage test case for non-jemalloc allocators (#1685)",
      "date": "2025-02-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1685",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7fa784a27562940d2995fc6e3d6938940d81e4b6"
    },
    {
      "sha": "3e12e79e2f",
      "message": "Add paused_actions and paused_timeout_milliseconds fields for info clients (#215)",
      "date": "2025-02-07",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/215",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/3e12e79e2fc672a229e4f5f71e306db51fd40715"
    },
    {
      "sha": "a3c9f67665",
      "message": "Fix kvstore overhead_hashtable_lut (#1676)",
      "date": "2025-02-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1676",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a3c9f6766547ea8664b32a7b2e7a6f27dc8fbbf8"
    },
    {
      "sha": "c75e866176",
      "message": "move clientCron onto a separate timer (#1387)",
      "date": "2025-02-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1387",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c75e8661762d106ead32312fa760b5fbb8446a7a"
    },
    {
      "sha": "d3aabd7f13",
      "message": "Hex encode the data in dump test (#1637)",
      "date": "2025-01-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1637",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d3aabd7f13a8ad4d6b45767cce04dc284dce5b0f"
    },
    {
      "sha": "f695c52acb",
      "message": "Fix timing issue in pause test (#1631)",
      "date": "2025-01-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1631",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f695c52acb82519d8b1362d456b2ec64ae401fd4"
    },
    {
      "sha": "230efa4fbf",
      "message": "deflake tracking-redir-broken test (#1628)",
      "date": "2025-01-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1628",
      "commit_url": "https://github.com/valkey-io/valkey/commit/230efa4fbf4f90828c211924c0e02fe3495bd727"
    },
    {
      "sha": "e9b8970e72",
      "message": "Relaxed RDB version check (#1604)",
      "date": "2025-01-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1604",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e9b8970e72754461d92b8bf22055a58540878d59"
    },
    {
      "sha": "7699a3a94a",
      "message": "Fix use-after-free in hashtableTwoPhasePopDelete (#1626)",
      "date": "2025-01-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1626",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7699a3a94a5d3b2d5f2713893192ba87042fa030"
    },
    {
      "sha": "a18fcdb371",
      "message": "Deflake hashtable random fairness test (#1618)",
      "date": "2025-01-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1618",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a18fcdb371db351b25332ddc0269589e4c5d56c1"
    },
    {
      "sha": "66577573f2",
      "message": "Test coverage for COMMANDLOG HELP (#1617)",
      "date": "2025-01-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1617",
      "commit_url": "https://github.com/valkey-io/valkey/commit/66577573f207313b8998f4e0e81e32740adf5d6b"
    },
    {
      "sha": "9071a5c8e6",
      "message": "Set GH actions job timeout to a day (#1540)",
      "date": "2025-01-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1540",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9071a5c8e627b4a74d810bfc68fcfb70d0db4dcb"
    },
    {
      "sha": "3f21705a6c",
      "message": "Feature COMMANDLOG to record slow execution and large request/reply (#1294)",
      "date": "2025-01-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1294",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3f21705a6c51d7f412f80dd7aabd83dac45b2493"
    },
    {
      "sha": "7fc958da52",
      "message": "fix test Protocol desync regression test with TLS (#1593)",
      "date": "2025-01-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1593",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7fc958da52aab644daf55ba39cc9f0092b063fbd"
    },
    {
      "sha": "3032ccd48a",
      "message": "Change the shared format for dual channel replication logs (#1586)",
      "date": "2025-01-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1586",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3032ccd48a17f9da78799dea0f8f976ee4312531"
    },
    {
      "sha": "2d0b8e3608",
      "message": "Update comments and log message in cluster_legacy.c (#1561)",
      "date": "2025-01-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1561",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2d0b8e360847146fa43a8463773dde8125187fa7"
    },
    {
      "sha": "87cc3d7a71",
      "message": "Fix cluster info sent stats for message with light header (#1563)",
      "date": "2025-01-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1563",
      "commit_url": "https://github.com/valkey-io/valkey/commit/87cc3d7a716f28af33a9c7ab017b81831016ab87"
    },
    {
      "sha": "921ba19acb",
      "message": "Incr expired_keys if the unix-time is already expired for EXPIREAT and other commands(#1517)",
      "date": "2025-01-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1517",
      "commit_url": "https://github.com/valkey-io/valkey/commit/921ba19acbebed63bf49b12b8123a72887e53128"
    },
    {
      "sha": "dc9ca1b98d",
      "message": "Test coverage for ECHO for reply schema validation (#1549)",
      "date": "2025-01-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1549",
      "commit_url": "https://github.com/valkey-io/valkey/commit/dc9ca1b98da657fecfb5bc32b6a57d2b9931007a"
    },
    {
      "sha": "ad592f73d7",
      "message": "Skip CLI tests with reply schema validation (#1545)",
      "date": "2025-01-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1545",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ad592f73d7c245f530f428af786ee39042208784"
    },
    {
      "sha": "d99457c09c",
      "message": "Free the passed in lua context instead of the global (#1536)",
      "date": "2025-01-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1536",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d99457c09cefed8afdc112dbce3d3bee29e555a5"
    },
    {
      "sha": "80c35402bc",
      "message": "Remove legacy SERVER_TEST compiler flag from cmake. (#1530)",
      "date": "2025-01-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1530",
      "commit_url": "https://github.com/valkey-io/valkey/commit/80c35402bce9e4f7c79bb975d43a119fee9ce951"
    },
    {
      "sha": "8af35a1712",
      "message": "Add build folder to gitignore. (#1488)",
      "date": "2025-01-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1488",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8af35a1712534de3b3d508788fff2555bb614350"
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
    },
    {
      "sha": "b3b4bdcda4",
      "message": "CMake: fail on warnings (#1503)",
      "date": "2025-01-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1503",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b3b4bdcda40380048b302c6dd957396340b88d6c"
    },
    {
      "sha": "fe72c784b7",
      "message": "Move coverity back to ubuntu 22 until test failures are fixed (#1504)",
      "date": "2025-01-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1504",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fe72c784b74b88e4b642a1796f235a2f886f23d4"
    },
    {
      "sha": "26a72fa89c",
      "message": "Use the correct command proc for the LOOKUP_NOTOUCH exception in lookupKey (#1499)",
      "date": "2025-01-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1499",
      "commit_url": "https://github.com/valkey-io/valkey/commit/26a72fa89c8da17c6529a645853d6559e5fdcb70"
    },
    {
      "sha": "93b701d8d4",
      "message": "Update Redis legacy keyword and link in utils/whatisdoing.sh (#1495)",
      "date": "2025-01-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1495",
      "commit_url": "https://github.com/valkey-io/valkey/commit/93b701d8d48eaf87077e707dd77eaaed0e66900f"
    },
    {
      "sha": "35abb68b79",
      "message": "Offload reading the replication stream to IO threads (#1449)",
      "date": "2025-01-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1449",
      "commit_url": "https://github.com/valkey-io/valkey/commit/35abb68b798b25333e94186583996efed9667958"
    },
    {
      "sha": "8aff235721",
      "message": "Fix unreliable dual channel Valgrind tests (#1500)",
      "date": "2025-01-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1500",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8aff2357212e2bec0d729f835bd278890aff0e4b"
    },
    {
      "sha": "e4179f1f3b",
      "message": "Only (re-)send MEET packet once every handshake timeout period (#1441)",
      "date": "2024-12-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1441",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e4179f1f3b6b8d8490077860bd438303d302f2b9"
    },
    {
      "sha": "e470735d91",
      "message": "Immediately restart the defrag cycle if we still need to defrag (#1492)",
      "date": "2024-12-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1492",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e470735d911ea5b1ee550a7a7c68beb63c6c812d"
    },
    {
      "sha": "bb325bde35",
      "message": "Fix restore replica output bytes stat update (#1486)",
      "date": "2024-12-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1486",
      "commit_url": "https://github.com/valkey-io/valkey/commit/bb325bde355040a91b6d1237fe6965dd4650b2ec"
    },
    {
      "sha": "f1b7f3072c",
      "message": "Reduce dual channel testing time (#1477)",
      "date": "2024-12-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1477",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f1b7f3072ce0378a181a26f3dfa5e4526b5d813b"
    },
    {
      "sha": "2ee06e7983",
      "message": "Remove readability refactor for failover auth to fix clang warning (#1481)",
      "date": "2024-12-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1481",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2ee06e79837df46389ae2e23348b4c51ab25315f"
    },
    {
      "sha": "1c97317518",
      "message": "Resolve bounds checks on cluster_legacy.c (#1463)",
      "date": "2024-12-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1463",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1c97317518e40efb4c271ae3b0656cc6e43f0110"
    },
    {
      "sha": "b56f4f70d2",
      "message": "Update info.tcl test to revert client output limits sooner (#1462)",
      "date": "2024-12-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1462",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b56f4f70d2cae11988f2f330b8060e21d78b163b"
    },
    {
      "sha": "ffef236dbb",
      "message": "Fix storing the wrong PID in active servers (#1464)",
      "date": "2024-12-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1464",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ffef236dbbfd26383262fa222e869814f5608ce5"
    },
    {
      "sha": "079f4edf2d",
      "message": "Add a hint about the current file for TCL debugging (#1459)",
      "date": "2024-12-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1459",
      "commit_url": "https://github.com/valkey-io/valkey/commit/079f4edf2d7aabd98bd37ffaac608b54dea62b6a"
    },
    {
      "sha": "60197b30e2",
      "message": "Attempt to read secondary error from info test (#1452)",
      "date": "2024-12-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1452",
      "commit_url": "https://github.com/valkey-io/valkey/commit/60197b30e266842fc84eb7ee1eead2d27d87e62f"
    },
    {
      "sha": "0e96bb311e",
      "message": "Synchronously delete data during defrag tests (#1443)",
      "date": "2024-12-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1443",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0e96bb311e35b07b1f85932752cad9b777037441"
    },
    {
      "sha": "3cd176dc39",
      "message": "Avoid importing memory aligned malloc (#1442)",
      "date": "2024-12-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1442",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3cd176dc3908e89b3178d9d031f58339c242325e"
    },
    {
      "sha": "b60097ba07",
      "message": "Check length before reading in `stringmatchlen` (#1431)",
      "date": "2024-12-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1431",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b60097ba073139ca62fdb59d15cc09737d114add"
    },
    {
      "sha": "3a1043a4f0",
      "message": "Fix Valkey binary build workflow, version support changes. (#1429)",
      "date": "2024-12-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1429",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3a1043a4f0fa97daa31f4bd2b3714a07736ac1b6"
    },
    {
      "sha": "ab69a8a55d",
      "message": "Use `configure-aws-credentials` workflow instead of passing `secret_access_key` (#1363)",
      "date": "2024-12-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1363",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ab69a8a55dee8738dc0bf005c4cb37a259b12053"
    },
    {
      "sha": "5f7fe9ef21",
      "message": "Send MEET packet to node if there is no inbound link to fix inconsistency when handshake timedout (#1307)",
      "date": "2024-12-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1307",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5f7fe9ef21f1feae42257ac93ab33d8f8c06e97f"
    },
    {
      "sha": "2dfe25b408",
      "message": "Fix race in test \"CLUSTER SLOT-STATS cpu-usec for blocking commands, unblocked on timeout\" (#1416)",
      "date": "2024-12-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1416",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2dfe25b40839bb7e904d83622b09b999b25fb160"
    },
    {
      "sha": "f951a1ca73",
      "message": "Add new flag in `CLIENT LIST` for import-source client (#1398)",
      "date": "2024-12-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1398",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f951a1ca730c5b00b1c1d8e1590bc7f4c2d7d5c2"
    },
    {
      "sha": "9cfe1b3d81",
      "message": "Set Command with IFEQ Support (#1324)",
      "date": "2024-12-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1324",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9cfe1b3d81466ed324c28e55ba60be66dea0b7c9"
    },
    {
      "sha": "4f61034934",
      "message": "Update governance and maintainers file for Valkey committers (#1390)",
      "date": "2024-12-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1390",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4f61034934cf165163ef272e5795bccadc288b09"
    },
    {
      "sha": "b09db3ef78",
      "message": "Fix typo in streams seen-time / active-time test (#1409)",
      "date": "2024-12-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1409",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b09db3ef788896f7192b068b1089c11b761ed3fe"
    },
    {
      "sha": "e8078b7315",
      "message": "Allow MEMORY MALLOC-STATS and MEMORY PURGE during loading phase (#1317)",
      "date": "2024-12-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1317",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e8078b7315250dc052b4020a4ea73471a8c0e4a9"
    },
    {
      "sha": "f20d629dbe",
      "message": "Fix sanitizer builds with clang (#1402)",
      "date": "2024-12-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1402",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f20d629dbe31d31eb82e360f9da4ef94ba9aabdc"
    },
    {
      "sha": "a2fe6af457",
      "message": "Fix Module Update Args test when other modules are loaded (#1403)",
      "date": "2024-12-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1403",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a2fe6af457e353425d39c858b8cf68f1b4d6a9b7"
    },
    {
      "sha": "90475af594",
      "message": "Free strings during BGSAVE/BGAOFRW to reduce copy-on-write (#905)",
      "date": "2024-12-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/905",
      "commit_url": "https://github.com/valkey-io/valkey/commit/90475af59429583182402ee3b408d7bcb36d56cd"
    },
    {
      "sha": "7043ef0bbb",
      "message": "Split dual-channel COB overrun tests to separate servers (#1374)",
      "date": "2024-12-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1374",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7043ef0bbb627b66bcaa75351b1b141c96852df8"
    },
    {
      "sha": "4695d118dd",
      "message": "RDMA builtin support (#1209)",
      "date": "2024-11-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1209",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4695d118dd6126b9b4f3e3415198df398e8bbb79"
    },
    {
      "sha": "926b6fd6fe",
      "message": "Contributing valkeyJSON module (#1)",
      "date": "2024-11-29",
      "repo": "valkey-json",
      "pr_url": "https://github.com/valkey-io/valkey-json/pull/1",
      "commit_url": "https://github.com/valkey-io/valkey-json/commit/926b6fd6feba583e251383094fedd6f0f1d19712"
    },
    {
      "sha": "f1d08776a0",
      "message": "Add performance tuning section for RDMA (#190)",
      "date": "2024-11-27",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/190",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/f1d08776a07a6fa655debcdbf50404cca4c77274"
    },
    {
      "sha": "109d2dadc0",
      "message": "Add slack link for users (#1273)",
      "date": "2024-11-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1273",
      "commit_url": "https://github.com/valkey-io/valkey/commit/109d2dadc0a23326a71f58c8e312859689d6697c"
    },
    {
      "sha": "3d0c834203",
      "message": "Fix LRU crash when getting too many random lua scripts (#1310)",
      "date": "2024-11-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1310",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3d0c8342030654bdfaf74d08d2d5645ff616c7a7"
    },
    {
      "sha": "f9d0b87622",
      "message": "Upgrade macos-12 to macos-13 in workflows (#1318)",
      "date": "2024-11-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1318",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f9d0b876224beecc8386cce5e11d43e649b82189"
    },
    {
      "sha": "920db68229",
      "message": "Addresses open question for ValkeyJSON rfc (#13)",
      "date": "2024-11-18",
      "repo": "valkey-rfc",
      "pr_url": "https://github.com/valkey-io/valkey-rfc/pull/13",
      "commit_url": "https://github.com/valkey-io/valkey-rfc/commit/920db68229ba1e9be561b3ee33d74561ec58234d"
    },
    {
      "sha": "c5012cc630",
      "message": "Optimize RDB load performance and fix cluster mode resizing on replica side (#1199)",
      "date": "2024-11-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1199",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c5012cc630bb65c07a17ea870630edd8825cde52"
    },
    {
      "sha": "94113fde7f",
      "message": "Improvements for TLS with I/O threads (#1271)",
      "date": "2024-11-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1271",
      "commit_url": "https://github.com/valkey-io/valkey/commit/94113fde7fb251e24911e51ab8cf2a696864ebb6"
    },
    {
      "sha": "b9994030e9",
      "message": "Log clusterbus handshake timeout failures (#1247)",
      "date": "2024-11-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1247",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b9994030e952788c8f736bcd02387dddf2c8b1cb"
    },
    {
      "sha": "863d312803",
      "message": "Fix link-time optimization to work correctly for unit tests (i.e. -flto flag) (#1290) (#1296)",
      "date": "2024-11-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1296",
      "commit_url": "https://github.com/valkey-io/valkey/commit/863d31280369a290c5b51f446a2c018ce3e98da0"
    },
    {
      "sha": "4a9864206f",
      "message": "Migrate quicklist unit test to new framework (#515)",
      "date": "2024-11-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/515",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4a9864206f8aa1b3b33976c0a96b292d3fa4905a"
    },
    {
      "sha": "4a9864206f",
      "message": "Migrate quicklist unit test to new framework (#515)",
      "date": "2024-11-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/515",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4a9864206f8aa1b3b33976c0a96b292d3fa4905a"
    },
    {
      "sha": "9300a7ebc8",
      "message": "Set fields to NULL after free in freeClient() (#1279)",
      "date": "2024-11-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1279",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9300a7ebc856356f1d55df16ddfb845773b5daca"
    },
    {
      "sha": "0b5b2c7484",
      "message": "Log as primary role (M) instead of child process (C) during startup (#1282)",
      "date": "2024-11-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1282",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0b5b2c7484e6d401ce7818571bde09b49f88180e"
    },
    {
      "sha": "7cd3ab0dd1",
      "message": "Document duplicate options in ZUNIONSTORE (#186)",
      "date": "2024-11-11",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/186",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/7cd3ab0dd144ccf8a3bb140fd56d442598e2c6e1"
    },
    {
      "sha": "20f31bd532",
      "message": "Delete utils/__pycache__ added by mistake (#187)",
      "date": "2024-11-11",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/187",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/20f31bd5327c2eb7e0cc31390b98c7364d8d59e5"
    },
    {
      "sha": "07b3e7ae7a",
      "message": "Add CMake build system for valkey (#1196)",
      "date": "2024-11-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1196",
      "commit_url": "https://github.com/valkey-io/valkey/commit/07b3e7ae7a9e08101fa4dd50aebb8fa5fbdd4f1e"
    },
    {
      "sha": "3672f9b2c3",
      "message": "Revert \"Decline unsubscribe related command in non-subscribed mode\" (#1265)",
      "date": "2024-11-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1265",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3672f9b2c322c4c8f073acc5973fffce546bd4e5"
    },
    {
      "sha": "48ebe21ad1",
      "message": "fix: clean up refactoring leftovers (#1264)",
      "date": "2024-11-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1264",
      "commit_url": "https://github.com/valkey-io/valkey/commit/48ebe21ad1a30eee60c22fe8235118f4c6b1aed3"
    },
    {
      "sha": "3c32ee1bda",
      "message": "Add a filter option to drop all cluster packets (#1252)",
      "date": "2024-11-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1252",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3c32ee1bdaddcd5fbe699aa6c8b320e86702d1b6"
    },
    {
      "sha": "5a4c0640ce",
      "message": "Mark main and serverAssert as weak symbols to be overridden (#1232)",
      "date": "2024-10-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1232",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5a4c0640cebe922de563e03ff2a683b89612f522"
    },
    {
      "sha": "8ee7a58025",
      "message": "Document log format configs in valkey.conf (#1233)",
      "date": "2024-10-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1233",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8ee7a580254d5600a2af32ac30ce2a103b7d83fb"
    },
    {
      "sha": "c21f1dc084",
      "message": "Increase the IO_THREADS_MAX_NUM. (#1220)",
      "date": "2024-10-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1220",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c21f1dc084d49ea74883ba93583bf957f7636635"
    },
    {
      "sha": "5885dc56bd",
      "message": "Fix BGSAVE CANCEL since and history fields (#1200)",
      "date": "2024-10-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1200",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5885dc56bdb40b3e0ea9b3d20a8bb08c7f2c3157"
    },
    {
      "sha": "29b83f1ac8",
      "message": "Introduce bgsave cancel (#757)",
      "date": "2024-10-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/757",
      "commit_url": "https://github.com/valkey-io/valkey/commit/29b83f1ac8dd80a9c3214c1e1f0ff3b7730fb612"
    },
    {
      "sha": "29b83f1ac8",
      "message": "Introduce bgsave cancel (#757)",
      "date": "2024-10-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/757",
      "commit_url": "https://github.com/valkey-io/valkey/commit/29b83f1ac8dd80a9c3214c1e1f0ff3b7730fb612"
    },
    {
      "sha": "36d438ba27",
      "message": "Deflake test ync should continue if not all slaves dropped dual-channel-replication (#1164)",
      "date": "2024-10-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1164",
      "commit_url": "https://github.com/valkey-io/valkey/commit/36d438ba2793fefc7d50fb954ce7f7cd01469540"
    },
    {
      "sha": "597aa037cc",
      "message": "Deflake test Primary COB growth with inactive replica (#1165)",
      "date": "2024-10-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1165",
      "commit_url": "https://github.com/valkey-io/valkey/commit/597aa037cc72282e74b5b7591a99490a6166fe65"
    },
    {
      "sha": "9b8a06137c",
      "message": "Fix empty response for ACL CAT category subcommand for module defined categories (#1140)",
      "date": "2024-10-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1140",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9b8a06137c20c6fa112e0ce5830bec51edf39999"
    },
    {
      "sha": "cd8de095c4",
      "message": "Add flush-before-load option for repl-diskless-load (#909)",
      "date": "2024-10-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/909",
      "commit_url": "https://github.com/valkey-io/valkey/commit/cd8de095c4dc6687dabaa194a0fff4473c52299f"
    },
    {
      "sha": "e617bf2ddc",
      "message": "Removing incorrect comment about a warning (#1132)",
      "date": "2024-10-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1132",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e617bf2ddc2106c2a94c3130f3bfb70500e190b8"
    },
    {
      "sha": "b5eb793079",
      "message": "Eliminate hashTypeIterator memory allocation by assigning it on stack (#1105)",
      "date": "2024-10-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1105",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b5eb7930797023f46331d68b964b3871625da79d"
    },
    {
      "sha": "a1cc7c263a",
      "message": "Reuse `obey_client` variable in `processCommand()` function (#1101)",
      "date": "2024-10-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1101",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a1cc7c263abde54a85bd5b58168e1a4069d9671c"
    },
    {
      "sha": "00c97979d9",
      "message": "Make ./runtest --dump-logs dump logs on crash (#1117)",
      "date": "2024-10-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1117",
      "commit_url": "https://github.com/valkey-io/valkey/commit/00c97979d96929619d94acd7f5edd083fa337ab6"
    },
    {
      "sha": "69eddb4874",
      "message": "Speed up AOF rewrite test case (#1093)",
      "date": "2024-09-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1093",
      "commit_url": "https://github.com/valkey-io/valkey/commit/69eddb4874e21479d8eec32bc017359f53b24574"
    },
    {
      "sha": "a7cbca4066",
      "message": "RDMA: Support .is_local method (#1089)",
      "date": "2024-09-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1089",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a7cbca406619eef635b9bb6ca21d15c7e33a79ee"
    },
    {
      "sha": "bb57dfe630",
      "message": "Fix typo in test_helper.tcl (#1080)",
      "date": "2024-09-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1080",
      "commit_url": "https://github.com/valkey-io/valkey/commit/bb57dfe6303ae53259cf7806c696cf56c637b4e7"
    },
    {
      "sha": "99865b197c",
      "message": "Fix bug for CLUSTER SLOTS from EVAL over TLS (#1072)",
      "date": "2024-09-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1072",
      "commit_url": "https://github.com/valkey-io/valkey/commit/99865b197cc5bcf0f9335e5dd2e6bfd5096b7c26"
    },
    {
      "sha": "56fd97733b",
      "message": "Move printver test to info-command file (#1056)",
      "date": "2024-09-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1056",
      "commit_url": "https://github.com/valkey-io/valkey/commit/56fd97733b60d59014c97fbca906ff3e20ef04f5"
    },
    {
      "sha": "4593dc2f05",
      "message": "Fix memory allocation for server databases (#1046)",
      "date": "2024-09-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1046",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4593dc2f059661e1c4eb43bba025f68948344228"
    },
    {
      "sha": "ba71c7e56e",
      "message": "Copy 'errno' and use copied value in the if check of retry in cluster migrate commands socket_err block. (#1042)",
      "date": "2024-09-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1042",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ba71c7e56e40daed2871975b3ff433383a20cd93"
    },
    {
      "sha": "ff69b4be1d",
      "message": "Fix casing in README.md (#1043)",
      "date": "2024-09-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1043",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ff69b4be1db24ea4e3b111e8e865af0df601b907"
    },
    {
      "sha": "9f8185f5c8",
      "message": "Update valkey-benchmark log output to reference 'server' instead of 'Redis' (#1029)",
      "date": "2024-09-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1029",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9f8185f5c80bc98bdbc631b90ccf13929d6a0cbc"
    },
    {
      "sha": "d090fbefde",
      "message": "Add the missing help output for new command: client capa redirect (#1025)",
      "date": "2024-09-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1025",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d090fbefded1c1f67a4450100fe42d0dbdbad564"
    },
    {
      "sha": "8cca11ac54",
      "message": "Fix wrong count for replica's tot-net-out (#1013)",
      "date": "2024-09-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1013",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8cca11ac541012e6bfbe995fb0367e6a058719b6"
    },
    {
      "sha": "2b207ee1b3",
      "message": "Improve stability of hostnames test (#1016)",
      "date": "2024-09-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1016",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2b207ee1b3808c5eb5de6879651104044ca162b2"
    },
    {
      "sha": "1b24168450",
      "message": "Dual Channel Replication - Verify Replica Local Buffer Limit Configuration (#989)",
      "date": "2024-09-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/989",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1b241684508bd6fd63c083c25a9a4195a8e242d9"
    },
    {
      "sha": "affbea5dc1",
      "message": "For MEETs, save the extensions support flag immediately during MEET processing (#778)",
      "date": "2024-09-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/778",
      "commit_url": "https://github.com/valkey-io/valkey/commit/affbea5dc1ae1a0d80019c4f313d2bf1c3fcb7f9"
    },
    {
      "sha": "f504cf233b",
      "message": "add assertion for kvstore's dictType (#1004)",
      "date": "2024-09-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1004",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f504cf233bd08d56b1aa4af6c1ef3a2b4aa0ac60"
    },
    {
      "sha": "20d583f774",
      "message": "Migrate dict.c unit tests to new framework (#946)",
      "date": "2024-09-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/946",
      "commit_url": "https://github.com/valkey-io/valkey/commit/20d583f774efd0de8415f17ed575854414b8ecab"
    },
    {
      "sha": "14016d2df7",
      "message": "Migrate listpack.c unit tests to new framework  (#949)",
      "date": "2024-09-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/949",
      "commit_url": "https://github.com/valkey-io/valkey/commit/14016d2df7ce6e7726012c2b0ec023b2a64ef2d1"
    },
    {
      "sha": "ea58fbf40d",
      "message": "Rewrite lazyfree docs in valkey.conf to reflect that lazy is now default (#983)",
      "date": "2024-09-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/983",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ea58fbf40d175a2a97c6ea7c6bc9df59798e013e"
    },
    {
      "sha": "f143ffd2a5",
      "message": "Fix typo in valkey-cli.c (#979)",
      "date": "2024-09-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/979",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f143ffd2a5b550e3490dbef0679d090dbaf5b416"
    },
    {
      "sha": "5fdb47c2e2",
      "message": "Add configuration hide-user-data-from-log to hide user data from server logs (#877)",
      "date": "2024-09-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/877",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5fdb47c2e262693269b231ebfb38116fc4d2f147"
    },
    {
      "sha": "5d458c6292",
      "message": "Delete unused parts of zipmap (#973)",
      "date": "2024-08-31",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/973",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5d458c62925f4c5d6eba1788447a1bf6d9d6380f"
    },
    {
      "sha": "743f5ac2ae",
      "message": "standalone -REDIRECT handles special case of MULTI context (#895)",
      "date": "2024-08-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/895",
      "commit_url": "https://github.com/valkey-io/valkey/commit/743f5ac2ae18080658a862e483d8247c3b2967df"
    },
    {
      "sha": "743f5ac2ae",
      "message": "standalone -REDIRECT handles special case of MULTI context (#895)",
      "date": "2024-08-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/895",
      "commit_url": "https://github.com/valkey-io/valkey/commit/743f5ac2ae18080658a862e483d8247c3b2967df"
    },
    {
      "sha": "2b76c8fbe2",
      "message": "Migrate zipmap unit test to new framework (#474)",
      "date": "2024-08-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/474",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2b76c8fbe2ccadaee2149e4b9b7c7df7ff0d07b6"
    },
    {
      "sha": "4a9b4f667c",
      "message": "free client's multi state when it becomes dirty (#961)",
      "date": "2024-08-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/961",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4a9b4f667cdf4caf53e5ef3a032801819b2dc9a4"
    },
    {
      "sha": "25dd943087",
      "message": "Delete TLS.md and update README.md about tests (#960)",
      "date": "2024-08-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/960",
      "commit_url": "https://github.com/valkey-io/valkey/commit/25dd943087d0f2bdbea76edd059cf5805d4db7e2"
    },
    {
      "sha": "927c2a8cd1",
      "message": "Delete files MANIFESTO, BUGS and INSTALL (#958)",
      "date": "2024-08-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/958",
      "commit_url": "https://github.com/valkey-io/valkey/commit/927c2a8cd137431d4a6226f0a51ed24c348b2cef"
    },
    {
      "sha": "744b13e302",
      "message": "Using intrinsics to optimize counting HyperLogLog trailing bits (#846)",
      "date": "2024-08-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/846",
      "commit_url": "https://github.com/valkey-io/valkey/commit/744b13e302559fc6da30749df266810882b5df99"
    },
    {
      "sha": "54c0f743dd",
      "message": "Connection minor fixes (#953)",
      "date": "2024-08-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/953",
      "commit_url": "https://github.com/valkey-io/valkey/commit/54c0f743dd6971bf8636c13600a6d4e2ef10106f"
    },
    {
      "sha": "73698fa028",
      "message": "Fix invalid escape sequence in utils, minor cleanup in python script  (#948)",
      "date": "2024-08-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/948",
      "commit_url": "https://github.com/valkey-io/valkey/commit/73698fa028be57ae710940f47f536f6d822a44bb"
    },
    {
      "sha": "b48596a914",
      "message": "Add support for setting the group on a unix domain socket (#901)",
      "date": "2024-08-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/901",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b48596a91421cc3a3ec3f73babe050ba1ae11d2d"
    },
    {
      "sha": "829aa7fe3c",
      "message": "Remove accurate from extra test tag (#935)",
      "date": "2024-08-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/935",
      "commit_url": "https://github.com/valkey-io/valkey/commit/829aa7fe3cdb81f53bd3c1e08e0e4e291357761b"
    },
    {
      "sha": "0a11c4a140",
      "message": "Delete redundant declaration clusterNodeCoversSlot and countKeysInSlot (#930)",
      "date": "2024-08-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/930",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0a11c4a14093ac6486eea2a912a2befdf3ea0fb3"
    },
    {
      "sha": "b8dd4fbbf7",
      "message": "Fix Error in Daily CI -- reply-schemas-validator (#922)",
      "date": "2024-08-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/922",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b8dd4fbbf7e9f052b5d94c27602f616474ed8d41"
    },
    {
      "sha": "e2ab7ffd89",
      "message": "Make use of a single listNode pointer for blocking utility lists (#919)",
      "date": "2024-08-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/919",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e2ab7ffd894a44d836019c62710c20c7ef5852b3"
    },
    {
      "sha": "7795152fff",
      "message": "Fix valgrind timing issue failure in replica-redirect test (#917)",
      "date": "2024-08-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/917",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7795152fff06f8200f5e4239ff612b240f638e14"
    },
    {
      "sha": "adf53c212b",
      "message": "Add lfu support for DEBUG OBJECT command, added lfu_freq and lfu_access_time_minutes fields (#479)",
      "date": "2024-08-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/479",
      "commit_url": "https://github.com/valkey-io/valkey/commit/adf53c212be1b1334c66608e4c60c4ddf8d6db46"
    },
    {
      "sha": "bfdab65791",
      "message": "Fix CI concurrency (#849)",
      "date": "2024-08-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/849",
      "commit_url": "https://github.com/valkey-io/valkey/commit/bfdab65791a72e356b9ad61866a790a8646a4c62"
    },
    {
      "sha": "0fc43edc6c",
      "message": "Update sentinel conf access string to allow hello channel access (#854)",
      "date": "2024-08-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/854",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0fc43edc6cf388854bc824f192647cc59f7019e7"
    },
    {
      "sha": "facd123ce6",
      "message": "Update redis.conf to valkey.conf in log message (#855)",
      "date": "2024-08-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/855",
      "commit_url": "https://github.com/valkey-io/valkey/commit/facd123ce60e8d39cbdfcedd51c72569d755d68a"
    },
    {
      "sha": "e86557fba2",
      "message": "Valkey 8.0 RC1 Blog (#105)",
      "date": "2024-08-02",
      "repo": "valkey-io.github.io",
      "pr_url": "https://github.com/valkey-io/valkey-io.github.io/pull/105",
      "commit_url": "https://github.com/valkey-io/valkey-io.github.io/commit/e86557fba2ecf9d0899c69772f6f9a56b1cf92cb"
    },
    {
      "sha": "1d18842074",
      "message": "Fix bug in writeToClient (#834)",
      "date": "2024-07-31",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/834",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1d188420741d4453615f776574f97984334a9939"
    },
    {
      "sha": "48ca2c9176",
      "message": "Improve dual channel replication stability and fix compatibility issues (#804)",
      "date": "2024-07-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/804",
      "commit_url": "https://github.com/valkey-io/valkey/commit/48ca2c91763ddfc6484f9e06cff3bbddd94f1c89"
    },
    {
      "sha": "da286a599d",
      "message": "Optimize the logic for checking the conversion of zset from listpack to skiplist during the ZADD operation. (#806)",
      "date": "2024-07-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/806",
      "commit_url": "https://github.com/valkey-io/valkey/commit/da286a599d24da71ad353c35e84d3d4b85f9b89c"
    },
    {
      "sha": "5c073a58e4",
      "message": "Increase rioConnsetWrite max chunk size to 16K (#817)",
      "date": "2024-07-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/817",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5c073a58e40973d9996778a705196f2bd876bb05"
    },
    {
      "sha": "816accea76",
      "message": "Generate correct slot information in cluster shards command on primary failure  (#790)",
      "date": "2024-07-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/790",
      "commit_url": "https://github.com/valkey-io/valkey/commit/816accea762271458e89016e3ed6ea27c9c1daff"
    },
    {
      "sha": "8b480310a6",
      "message": "Remove read handler upon RDB connection close (#803)",
      "date": "2024-07-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/803",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8b480310a629300c7cb28576f04df889bda21198"
    },
    {
      "sha": "1a8bd045f3",
      "message": "Replace master-reboot-down-after-period with primary-reboot-down-after-period in sentinel.conf (#647)",
      "date": "2024-07-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/647",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1a8bd045f3037699f2db92a974f1f3be215f11c6"
    },
    {
      "sha": "c1bbdc796d",
      "message": "Skip IPv6 tests on MacOS (daily) (#786)",
      "date": "2024-07-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/786",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c1bbdc796d7159b2f5ae1a8d12391407340d0262"
    },
    {
      "sha": "418901dec4",
      "message": "Limit tracking custom errors (e.g. from LUA) while allowing non custom errors to be tracked normally (#500)",
      "date": "2024-07-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/500",
      "commit_url": "https://github.com/valkey-io/valkey/commit/418901dec4e824c9d165f3437196ba803d3984ab"
    },
    {
      "sha": "34649bd034",
      "message": "Configurable cluster blacklist TTL (#738)",
      "date": "2024-07-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/738",
      "commit_url": "https://github.com/valkey-io/valkey/commit/34649bd034b6780989bf05b97fa9bde2b7cec243"
    },
    {
      "sha": "6a5a11f21c",
      "message": "Fix ULong config boundary checking (#752)",
      "date": "2024-07-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/752",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6a5a11f21c6b6a5c8678c50e96b559919962ba10"
    },
    {
      "sha": "548b4e0ea9",
      "message": "Calculate the actual mask to be removed in the eventloop before aeApiDelEvent (#725)",
      "date": "2024-07-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/725",
      "commit_url": "https://github.com/valkey-io/valkey/commit/548b4e0ea943da765a4fec46e73484b0742f58f8"
    },
    {
      "sha": "5f0ccf1478",
      "message": "Remove duplicate definition of UNUSED(V) (#755)",
      "date": "2024-07-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/755",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5f0ccf1478452598490683be4f78cf3e69ee259f"
    },
    {
      "sha": "f2bbd1ff0f",
      "message": "Fix minor memory leak in clusterLoadConfig (#741)",
      "date": "2024-07-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/741",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f2bbd1ff0f650182e7df1fda1055551389bb79c2"
    },
    {
      "sha": "eff45f5467",
      "message": "Fix flakiness of cluster-multiple-meets and cluster-reliable-meet (#728)",
      "date": "2024-07-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/728",
      "commit_url": "https://github.com/valkey-io/valkey/commit/eff45f546762577bd1877dfeece41c53b39926ad"
    },
    {
      "sha": "3323e422ad",
      "message": "Introduce thread-local storage variable to update thread's own used_memory and sum when reading to reduce atomic contention. (#674)",
      "date": "2024-07-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/674",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3323e422ad0c0dc81859017798cb04a9621d6522"
    },
    {
      "sha": "752b6ee8ff",
      "message": "Avoid compilation error oin valkey-cli (#721)",
      "date": "2024-07-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/721",
      "commit_url": "https://github.com/valkey-io/valkey/commit/752b6ee8ff75a72c364feca8b667f9e723df0c4c"
    },
    {
      "sha": "7415a576a8",
      "message": "Add prompt when Ctrl-C pressed (#702)",
      "date": "2024-06-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/702",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7415a576a8c49fdb946ac45aa66f4a462872d277"
    },
    {
      "sha": "4fbe31ab87",
      "message": "Fix the TLS and REPS issues about CLUSTER SLOTS cache (#581)",
      "date": "2024-06-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/581",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4fbe31ab87ba2a5fd1360328f5e75993986fa0d0"
    },
    {
      "sha": "28c5a17edf",
      "message": "replica redirect read&write to primary in standalone mode (#325)",
      "date": "2024-06-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/325",
      "commit_url": "https://github.com/valkey-io/valkey/commit/28c5a17edfff1c4607b16d3416bb1e021986d138"
    },
    {
      "sha": "dcee122bc0",
      "message": "Added new CLIENT CAPA command along with other related modifications (#151)",
      "date": "2024-06-27",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/151",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/dcee122bc0a739cfd82266cddb3730dd89ca8fb4"
    },
    {
      "sha": "3df9d42794",
      "message": "Fix bad memory accounting for sds when no malloc_size available (#694)",
      "date": "2024-06-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/694",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3df9d4279414bf46a9d85d599d2e60055ddaea1d"
    },
    {
      "sha": "ce79539047",
      "message": "Fail tests immediately if the server is no longer running (#678)",
      "date": "2024-06-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/678",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ce79539047ccecf39951168e5f30e2cd9a3135ec"
    },
    {
      "sha": "c8644e8544",
      "message": "Update release guidance for Valkey (#94)",
      "date": "2024-06-21",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/94",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/c8644e854466f84fb65aa2a35a445fd9831c8e75"
    },
    {
      "sha": "52f2909c04",
      "message": "Delete internals pages (#146)",
      "date": "2024-06-20",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/146",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/52f2909c042b6f631190061fa6d43c50f13f9ec9"
    },
    {
      "sha": "0143b7c9dd",
      "message": "Add zfree_with_size to optimize sdsfree since we can get zmalloc_size from the header (#453)",
      "date": "2024-06-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/453",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0143b7c9dd7ec38fec5469a1055d96e8f4f0984c"
    },
    {
      "sha": "ae2d4217e1",
      "message": "Add new SCRIPT SHOW subcommand to dump script via sha1 (#617)",
      "date": "2024-06-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/617",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ae2d4217e147996bd6c546f559aa564f873f9203"
    },
    {
      "sha": "b33f932c56",
      "message": "Add missing commas from debug command (#662)",
      "date": "2024-06-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/662",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b33f932c5670749bea67933c10578336c67f16e6"
    },
    {
      "sha": "6faa48a358",
      "message": "Don't initialize the key buffer in getKeysResult (#631)",
      "date": "2024-06-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/631",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6faa48a358ead15ea4b86798aa832a4820dfbe4e"
    },
    {
      "sha": "76fc041685",
      "message": "represent cluster node flags with bitwise shift value (#642)",
      "date": "2024-06-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/642",
      "commit_url": "https://github.com/valkey-io/valkey/commit/76fc041685217ad7279c486be892c16f182a3454"
    },
    {
      "sha": "d211078a27",
      "message": "Fix query buffer resized test flakiness (#646)",
      "date": "2024-06-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/646",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d211078a27ba75f1dfdcdaf7d407f3370f914974"
    },
    {
      "sha": "b546dd26e5",
      "message": "Allow CLUSTER NODES/INFO/MYID/MYSHARDID during loading state (#596)",
      "date": "2024-06-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/596",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b546dd26e5f446d86275152af3e8295e07be22a4"
    },
    {
      "sha": "b546dd26e5",
      "message": "Allow CLUSTER NODES/INFO/MYID/MYSHARDID during loading state (#596)",
      "date": "2024-06-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/596",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b546dd26e5f446d86275152af3e8295e07be22a4"
    },
    {
      "sha": "4bb7cc471a",
      "message": "Remove unnecessary clang-format off annotations (#628)",
      "date": "2024-06-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/628",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4bb7cc471a0a4e0948737c99c36aaf7202f4cb4c"
    },
    {
      "sha": "e65b2d235c",
      "message": "Update rewriteConfigSaveOption function code to rewrite multiple save in one line. (#583)",
      "date": "2024-06-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/583",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e65b2d235c300bb86cc7f960883ad919f75162e6"
    },
    {
      "sha": "bce240eab7",
      "message": "Replace masteruser and masterauth with primaryuser and primaryauth (#598)",
      "date": "2024-06-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/598",
      "commit_url": "https://github.com/valkey-io/valkey/commit/bce240eab7aa02ace5ed76f61122647f9ef719d7"
    },
    {
      "sha": "278ce0cae0",
      "message": "Rebrand the Lua debugger (#603)",
      "date": "2024-06-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/603",
      "commit_url": "https://github.com/valkey-io/valkey/commit/278ce0cae04342c392ebb865d155cbecd6672313"
    },
    {
      "sha": "60c10a5a4d",
      "message": "Remove valdup from BenchmarkDictType (#600)",
      "date": "2024-06-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/600",
      "commit_url": "https://github.com/valkey-io/valkey/commit/60c10a5a4daeb60dece86550c47a220fc401bb57"
    },
    {
      "sha": "a5406a0377",
      "message": "Mention ASK and TRYAGAIN for replicas in READONLY command manual (#142)",
      "date": "2024-06-02",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/142",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/a5406a03771416e532daaca4f67dced9d83cafdd"
    },
    {
      "sha": "4e44f5aae9",
      "message": "Fix races in test for tot-net-in, tot-net-out, tot-cmds (#559)",
      "date": "2024-05-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/559",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4e44f5aae934b2d459d0c6d3957ec01d6d2b014a"
    },
    {
      "sha": "045d475a94",
      "message": "Implement REPLCONF VERSION (#554)",
      "date": "2024-05-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/554",
      "commit_url": "https://github.com/valkey-io/valkey/commit/045d475a94f1dceae46170426195d3b9dd4fdf81"
    },
    {
      "sha": "d72ba06dd0",
      "message": "Make cluster replicas return ASK and TRYAGAIN (#495)",
      "date": "2024-05-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/495",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d72ba06dd0519fd0bf578cca2a2f5c457629dc6c"
    },
    {
      "sha": "3dd2f5a586",
      "message": "Undeprecate cluster slots command (#536)",
      "date": "2024-05-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/536",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3dd2f5a586f2c4d5f9cbf984a0565f70547efae7"
    },
    {
      "sha": "5f279b94de",
      "message": "Generate man pages (#92)",
      "date": "2024-05-24",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/92",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/5f279b94de77e52e7f4d4ed3baa3cea80b7617a5"
    },
    {
      "sha": "acb74f8da1",
      "message": "Delete dead code \"zfree_usable\"  (#518)",
      "date": "2024-05-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/518",
      "commit_url": "https://github.com/valkey-io/valkey/commit/acb74f8da1c62fd895e9a4956f484ba44cc2f742"
    },
    {
      "sha": "122cba5103",
      "message": "Quick fix of failure when use libc allocator in daily CI. (#521)",
      "date": "2024-05-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/521",
      "commit_url": "https://github.com/valkey-io/valkey/commit/122cba5103b14314fc56511b447af0e78bd68f1d"
    },
    {
      "sha": "efa8ba519b",
      "message": "Finish postponed SCAN changes (#501)",
      "date": "2024-05-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/501",
      "commit_url": "https://github.com/valkey-io/valkey/commit/efa8ba519b2d54f68fe05d03cac5b0d5352400ad"
    },
    {
      "sha": "9b6232b501",
      "message": "Automatically notify the slack channel when tests fail (#509)",
      "date": "2024-05-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/509",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9b6232b50120ae38537f22617b3ec8efaa625602"
    },
    {
      "sha": "6e4a61093e",
      "message": "Make it to so that unit tests build on mac (#499)",
      "date": "2024-05-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/499",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6e4a61093e9ad9f6e29aa46ace9b10f537437b87"
    },
    {
      "sha": "4e18e326a1",
      "message": "Remove endian coverage from server.c (#492)",
      "date": "2024-05-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/492",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4e18e326a163211ee213b894718d61b0b936b85e"
    },
    {
      "sha": "b166980c8e",
      "message": "Fix UNUSED repetition issue in test sources (#475)",
      "date": "2024-05-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/475",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b166980c8e6618a66aa0ec82e77c40bb305404be"
    },
    {
      "sha": "6af51f5092",
      "message": "Prevent clang-format in certain places (#468)",
      "date": "2024-05-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/468",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6af51f5092785f2367b4d86e3152db132b26b140"
    },
    {
      "sha": "315b7573c4",
      "message": "Update server function's name to valkey (#456)",
      "date": "2024-05-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/456",
      "commit_url": "https://github.com/valkey-io/valkey/commit/315b7573c423a6cddf0a63aba364c57917697756"
    },
    {
      "sha": "ba9dd7b23a",
      "message": "Add noscores option to command ZSCAN. (#324)",
      "date": "2024-05-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/324",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ba9dd7b23a13452cf4aac1420ecffcbab879fbe3"
    },
    {
      "sha": "93f8a19b6f",
      "message": "Change strlcat function name from redis to valkey (#440)",
      "date": "2024-05-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/440",
      "commit_url": "https://github.com/valkey-io/valkey/commit/93f8a19b6f9884f382d24f7650822d99cbb26c6d"
    },
    {
      "sha": "d1de34930a",
      "message": "Document the commands JSON files (#403)",
      "date": "2024-05-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/403",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d1de34930af0fa371dc703b9d8d2852ebd0b8f2b"
    },
    {
      "sha": "7b78e3f1b3",
      "message": "Various corrections and cleanup (#73)",
      "date": "2024-05-02",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/73",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/7b78e3f1b3e8398dc34f5aa2a956544341c88b47"
    },
    {
      "sha": "b283c6b508",
      "message": "Initial PR outlining the governance for the project (#345)",
      "date": "2024-04-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/345",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b283c6b508792892d76b9a4911e3086e37518748"
    },
    {
      "sha": "2e926b2de1",
      "message": "Fix command line formatting in TLS.md (#372)",
      "date": "2024-04-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/372",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2e926b2de17eaf8f62036103eb20bc504ab2e706"
    },
    {
      "sha": "52f9291f79",
      "message": "Rename redis to valkey in test suite logs and test names. (#366)",
      "date": "2024-04-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/366",
      "commit_url": "https://github.com/valkey-io/valkey/commit/52f9291f797a7f24267115bedb396f16310456ed"
    },
    {
      "sha": "74a0486e3d",
      "message": "Update redis* to valkey* in server.c and module.c (#367)",
      "date": "2024-04-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/367",
      "commit_url": "https://github.com/valkey-io/valkey/commit/74a0486e3d84221f1c94c44250ab3e022fc106d0"
    },
    {
      "sha": "2864fffe73",
      "message": "Update redis* to valkey* in syscheck.c (#365)",
      "date": "2024-04-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/365",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2864fffe7371b1031634ba92c68bdb062e8c0894"
    },
    {
      "sha": "8baf322742",
      "message": "Rename remaining test procedures (#355)",
      "date": "2024-04-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/355",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8baf3227429480ba769cfdf85ae3b06758fc552d"
    },
    {
      "sha": "d09a59c3b1",
      "message": "Rename redis_init_script file and its content (#357)",
      "date": "2024-04-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/357",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d09a59c3b10f52d8737768631c110e46cd2c1278"
    },
    {
      "sha": "0be7e71e21",
      "message": "Add new \"history\" page and delete irrelevant pages (#35)",
      "date": "2024-04-24",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/35",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/0be7e71e21c388d97612c78b19e9374afe9acec2"
    },
    {
      "sha": "85647bea36",
      "message": "Rebranding in docs/manual/ (#37)",
      "date": "2024-04-23",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/37",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/85647bea36f2bbf07bbd51518a14385ac46eefcc"
    },
    {
      "sha": "7809df0c93",
      "message": "Remove REDIS tag from test macros. (#333)",
      "date": "2024-04-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/333",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7809df0c93baba93e140bc2764ef57f65ca341a8"
    },
    {
      "sha": "9e2b7838ea",
      "message": "Add 'extended-redis-compatibility' config (#306)",
      "date": "2024-04-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/306",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9e2b7838ea03c87a846bb3d47e60911f6eabba86"
    },
    {
      "sha": "af47cffc83",
      "message": "Update oom_score_adjusted_by_redis to oom_score_adjusted_by_valkey in server.c (#229)",
      "date": "2024-04-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/229",
      "commit_url": "https://github.com/valkey-io/valkey/commit/af47cffc8358c96d5f7a7f388a46b6c02e6fa7e9"
    },
    {
      "sha": "3040c439b8",
      "message": "Remove REDIS tag from REDIS_CONFIG_REWRITE_SIGNATURE. (#331)",
      "date": "2024-04-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/331",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3040c439b845ef19210d9c1f4d050ab28e351ea4"
    },
    {
      "sha": "5d23f8f58a",
      "message": "Complete fields in client list and client info test. (#326)",
      "date": "2024-04-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/326",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5d23f8f58a5196f46d7c24d88bda5ea7151fea85"
    },
    {
      "sha": "8dcc8ebba4",
      "message": "Remove 'Redis' in error replies (#206)",
      "date": "2024-04-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/206",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8dcc8ebba4e83ac5eaddc3628e8b4bea9287edcb"
    },
    {
      "sha": "10d980890c",
      "message": "Update CONTRIBUTING.md and issue templates (#311)",
      "date": "2024-04-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/311",
      "commit_url": "https://github.com/valkey-io/valkey/commit/10d980890c746c2c14d56183086d4aa5bd35d7b0"
    },
    {
      "sha": "c090874ed4",
      "message": "List test files dynamically (#313)",
      "date": "2024-04-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/313",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c090874ed44aceb4aa93cedd4304d3140826d7e8"
    },
    {
      "sha": "6975242529",
      "message": "Update comment in cluster_legacy.h (#277)",
      "date": "2024-04-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/277",
      "commit_url": "https://github.com/valkey-io/valkey/commit/697524252993f849f0ade560fa46625623fa7ed5"
    },
    {
      "sha": "a054862b72",
      "message": "Rename redis_client* procedure to valkey_client* in test environment (#276)",
      "date": "2024-04-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/276",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a054862b72eb1761ba8102f34a60807163beffaa"
    },
    {
      "sha": "05d16579e6",
      "message": "Rename redis in valkey-cli file comments and prints (#222)",
      "date": "2024-04-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/222",
      "commit_url": "https://github.com/valkey-io/valkey/commit/05d16579e612c7670787ce3f2c3f5c91e0914afe"
    },
    {
      "sha": "da831c0d22",
      "message": "rename procedure redis_deferring_client to valkey_deferring_client (#270)",
      "date": "2024-04-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/270",
      "commit_url": "https://github.com/valkey-io/valkey/commit/da831c0d2242251be84a5d7f14f954c6c7fa8ee8"
    },
    {
      "sha": "c0cef48e98",
      "message": "Fix reference to redis-tls module (#273)",
      "date": "2024-04-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/273",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c0cef48e98574acd9840abf1c44c963eb56861ce"
    },
    {
      "sha": "9f03dfc1f6",
      "message": "Fix two typos that were flagged in the 7.2 build (#248)",
      "date": "2024-04-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/248",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9f03dfc1f637aef983118ada00ca3cd5c9829402"
    },
    {
      "sha": "48184ae2db",
      "message": "In CONTIBUTING.md, mention how to link PR to issue (#197)",
      "date": "2024-04-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/197",
      "commit_url": "https://github.com/valkey-io/valkey/commit/48184ae2dbb42e786de13f9ea6c99bfd0e1dbdc7"
    },
    {
      "sha": "def09488aa",
      "message": "Rename redis_member2struct ro  server_member2struct (#166)",
      "date": "2024-04-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/166",
      "commit_url": "https://github.com/valkey-io/valkey/commit/def09488aa2787038a2e8047a836dd2e76763a7c"
    },
    {
      "sha": "69d28be0f1",
      "message": "Rename redis to valkey in create-cluster script (#165)",
      "date": "2024-04-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/165",
      "commit_url": "https://github.com/valkey-io/valkey/commit/69d28be0f1939683d63546ef88ab949ee2e2847d"
    },
    {
      "sha": "730174445b",
      "message": "Rename redisOpArray to serverOpArray (#157)",
      "date": "2024-04-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/157",
      "commit_url": "https://github.com/valkey-io/valkey/commit/730174445b72bb04c446c635d4c34041270b596b"
    },
    {
      "sha": "cbbaf69d1d",
      "message": "Remove unused REDIS_TEST_MAIN dead code in crc64.c (#160)",
      "date": "2024-04-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/160",
      "commit_url": "https://github.com/valkey-io/valkey/commit/cbbaf69d1de08c92c415a64e241ee8d79dac682d"
    },
    {
      "sha": "717dfe8022",
      "message": "Rename redisDb to serverDb (#156)",
      "date": "2024-04-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/156",
      "commit_url": "https://github.com/valkey-io/valkey/commit/717dfe80221463e78cd5033c24ca71c1c582957c"
    },
    {
      "sha": "98892bb5c3",
      "message": "Rename redisMemOverhead to serverMemOverhead (#159)",
      "date": "2024-04-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/159",
      "commit_url": "https://github.com/valkey-io/valkey/commit/98892bb5c37c181199a66ea7cb85d47f87a357cd"
    },
    {
      "sha": "621edbafba",
      "message": "Rename redisassert to serverassert in comment (#142)",
      "date": "2024-04-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/142",
      "commit_url": "https://github.com/valkey-io/valkey/commit/621edbafba74c2d6211bf81d54be8b1da8543d4e"
    },
    {
      "sha": "e35d86f2a2",
      "message": "Fix rename REDIS_TEST to SERVER_TEST to pass the Daily workflow (#131)",
      "date": "2024-04-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/131",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e35d86f2a28bd39fc883132c361a2def7a463094"
    },
    {
      "sha": "4d7fff9aba",
      "message": "Remove unused var desc in luaRegisterFunctionReadPositionalArgs (#130)",
      "date": "2024-04-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/130",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4d7fff9abacab3c8c7618caea419aebeb71f266e"
    }
  ]
}
