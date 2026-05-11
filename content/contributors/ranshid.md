{
  "title": "ranshid",
  "login": "ranshid",
  "avatar_url": "https://avatars.githubusercontent.com/u/88133677?v=4",
  "score": 272,
  "commit_count": 88,
  "review_count": 184,
  "repos": [
    "valkey",
    "valkey-container",
    "valkey-doc",
    "valkey-glide",
    "valkey-hashes",
    "valkey-io.github.io",
    "valkey-perf-benchmark"
  ],
  "commit_list": [
    {
      "sha": "7803996f54",
      "message": "Fix TCP deadlock in MultiplexedConnection with large payloads (#5892)",
      "date": "2026-05-08",
      "repo": "valkey-glide",
      "pr_url": "https://github.com/valkey-io/valkey-glide/pull/5892",
      "commit_url": "https://github.com/valkey-io/valkey-glide/commit/7803996f54825265f8fecff8a644001aa93ad79a"
    },
    {
      "sha": "1d7224f389",
      "message": "Fix UAF in unblockClientOnKey when reprocessed command frees the client (CVE-2026-23479) (#3613)",
      "date": "2026-05-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3613",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1d7224f3894c8e6db39a9e86c040270b3122c064"
    },
    {
      "sha": "fea0b4064c",
      "message": "Fix invalid memory access in RESTORE with malformed zipmap (CVE-2026-25243) (#3619)",
      "date": "2026-05-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3619",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fea0b4064cf612d1c365b032326832bff0946bd9"
    },
    {
      "sha": "c7c92db43b",
      "message": "Delay full sync during yielding Lua scripts to prevent use-after-free (CVE-2026-23631) (#3625)",
      "date": "2026-05-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3625",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c7c92db43b63be0599a076590f012ed35d279a47"
    },
    {
      "sha": "0c81b53d6a",
      "message": "Avoid having server.h being included by cli and benchmark (#3420)",
      "date": "2026-04-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3420",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0c81b53d6af3bcffecbcbadf50639e5969178333"
    },
    {
      "sha": "cf05c0d28e",
      "message": "fix test_entry to consider diffrerent allocator size classes (#3416)",
      "date": "2026-03-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3416",
      "commit_url": "https://github.com/valkey-io/valkey/commit/cf05c0d28ebe8964ad9d92d73fd6cd7b94ef2f1d"
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
      "sha": "b358c3af51",
      "message": "Change read commands for SET and ZSET (#7)",
      "date": "2026-03-17",
      "repo": "valkey-perf-benchmark",
      "pr_url": "https://github.com/valkey-io/valkey-perf-benchmark/pull/7",
      "commit_url": "https://github.com/valkey-io/valkey-perf-benchmark/commit/b358c3af5132f72cfedd1ea2b00f884c4db786f9"
    },
    {
      "sha": "dcfb9269f5",
      "message": "Fix zset to operate defrag scan lexicographically (#3316)",
      "date": "2026-03-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3316",
      "commit_url": "https://github.com/valkey-io/valkey/commit/dcfb9269f5ba4cf2f851e75fba77dc189c4a15aa"
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
      "sha": "b00c9367ff",
      "message": "Always untrack initialized safe iterator (#3223)",
      "date": "2026-02-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3223",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b00c9367fff999188361aebba32c8732729e1178"
    },
    {
      "sha": "fd14380639",
      "message": "HSETEX - Always issue keyspace notifications after validation (#3001)",
      "date": "2026-01-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3001",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fd1438063927d0d3d2d8c9018011d8f7bcda47c3"
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
      "sha": "928e912617",
      "message": "remove unneeded include of expire.h (#3117)",
      "date": "2026-01-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3117",
      "commit_url": "https://github.com/valkey-io/valkey/commit/928e9126172dfdfdbf4ce6ebdc65aae854c6e79e"
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
      "sha": "4b5a48a36e",
      "message": "Fix HRANDFIELD to return null response when no field could be found (#3022)",
      "date": "2026-01-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3022",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4b5a48a36e22a885dad2140cf72fda7b64c5eb03"
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
      "sha": "6865f0a6e9",
      "message": "Fix HEXPIRE should not delete items when GT rule is used and expiration is in the past (#3023)",
      "date": "2026-01-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3023",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6865f0a6e929948aa73560b2ab20e3058d584e65"
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
      "sha": "75707ac432",
      "message": "Avoid hgetall deferred response (#2966)",
      "date": "2025-12-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2966",
      "commit_url": "https://github.com/valkey-io/valkey/commit/75707ac4323b30f112e862b734e3436fa03b620c"
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
      "sha": "8182f4a0b9",
      "message": "HSETEX with FXX should not create an object if it does not exist (#2716)",
      "date": "2025-10-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2716",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8182f4a0b9c92639f7528f4ae412e957c7600bb4"
    },
    {
      "sha": "0152420fb5",
      "message": "Blog Post: Hash field expiration in Valkey (#354)",
      "date": "2025-09-30",
      "repo": "valkey-io.github.io",
      "pr_url": "https://github.com/valkey-io/valkey-io.github.io/pull/354",
      "commit_url": "https://github.com/valkey-io/valkey-io.github.io/commit/0152420fb59f081f95e9e0e1046aca89e3ec5df5"
    },
    {
      "sha": "f39a809711",
      "message": "Fix module key memory usage accounting (#2661)",
      "date": "2025-09-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2661",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f39a809711ded971fb7abfc36dd294ea6183e34d"
    },
    {
      "sha": "3213f48fd6",
      "message": "Increase frequency of time check during fields active expiration (#2595)",
      "date": "2025-09-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2595",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3213f48fd694c201a1ba974bcad0ad7703b44510"
    },
    {
      "sha": "eb68ad8ce3",
      "message": "Add documentation for Hash Fields Expiration (#347)",
      "date": "2025-09-05",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/347",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/eb68ad8ce3043c6c484c5821906e2ee1962a4cd3"
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
      "sha": "bb81f8d14f",
      "message": "fix hash ignore ttl management during active expiry (#2505)",
      "date": "2025-08-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2505",
      "commit_url": "https://github.com/valkey-io/valkey/commit/bb81f8d14f6b32df7b4798dd8e35f45f257f6968"
    },
    {
      "sha": "e364c57e3d",
      "message": "simplify COPY Preserves TTLs hashexpire test (#2495)",
      "date": "2025-08-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2495",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e364c57e3dd10c908aa98926c4a58148d1fe5bff"
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
      "sha": "ba7334c7c6",
      "message": "Fix hfe no malloc size unit (#2436)",
      "date": "2025-08-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2436",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ba7334c7c61abd854109f1d19f807098e5f22cb1"
    },
    {
      "sha": "33a43f2a8a",
      "message": "bump the RDB version for Valkey 9.0(#2422)",
      "date": "2025-08-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2422",
      "commit_url": "https://github.com/valkey-io/valkey/commit/33a43f2a8a66d751b88bce83f5f6bc9921b9dcb7"
    },
    {
      "sha": "822362986c",
      "message": "update build-debian-old to use Bullseye instead of EOL buster (#2345)",
      "date": "2025-07-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2345",
      "commit_url": "https://github.com/valkey-io/valkey/commit/822362986c31cbe6fe8512be5e2cfac9d210a50d"
    },
    {
      "sha": "c35a6f3515",
      "message": "use regular client in test \"Auto-authenticate using tls-auth-clients-user\" (#2346)",
      "date": "2025-07-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2346",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c35a6f35157e0f65819f97fe0b9e0394e693d2f4"
    },
    {
      "sha": "cb10d9d78f",
      "message": "retry accept on transient errors (CVE-2025-48367) (#2315)",
      "date": "2025-07-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2315",
      "commit_url": "https://github.com/valkey-io/valkey/commit/cb10d9d78f35945b667e46967b3980e89954d73b"
    },
    {
      "sha": "20f5199d96",
      "message": "Apply fixed for CVE-2025-32023 (#2314)",
      "date": "2025-07-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2314",
      "commit_url": "https://github.com/valkey-io/valkey/commit/20f5199d96baf0c64bd4e7d042b6274c4e773bcb"
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
      "sha": "30e9109d19",
      "message": "Add output buffer limiting for unauthenticated clients (#2006)",
      "date": "2025-04-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2006",
      "commit_url": "https://github.com/valkey-io/valkey/commit/30e9109d19b0cd38c384560abdbd23e9e5719361"
    },
    {
      "sha": "7af3ff3f31",
      "message": "Valkey 8.1.0 GA release (#231)",
      "date": "2025-04-02",
      "repo": "valkey-io.github.io",
      "pr_url": "https://github.com/valkey-io/valkey-io.github.io/pull/231",
      "commit_url": "https://github.com/valkey-io/valkey-io.github.io/commit/7af3ff3f31dcb5bb120b0ab47fcddc725263baae"
    },
    {
      "sha": "e4036172f5",
      "message": "Align docs version to 8.1.0 (#256)",
      "date": "2025-03-31",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/256",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/e4036172f59174051e89d600b081eb31406f67a2"
    },
    {
      "sha": "5557ba04a9",
      "message": "Valkey release stage documentation (#252)",
      "date": "2025-03-25",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/252",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/5557ba04a96b78177b2cb54bf7ea926fa7916f16"
    },
    {
      "sha": "47295243b8",
      "message": "Add capa in example client-info (#253)",
      "date": "2025-03-25",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/253",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/47295243b807e3d53d3bf4b603b93d57d454642b"
    },
    {
      "sha": "e5a5c1af0f",
      "message": "Update the 8.1.0 rc2 release link in the website (#225)",
      "date": "2025-03-20",
      "repo": "valkey-io.github.io",
      "pr_url": "https://github.com/valkey-io/valkey-io.github.io/pull/225",
      "commit_url": "https://github.com/valkey-io/valkey-io.github.io/commit/e5a5c1af0fb9397a57391576181c10bddbd32e73"
    },
    {
      "sha": "2c9db1a775",
      "message": "Enable large-memory tests solo runs in daily workflow (#1816)",
      "date": "2025-03-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1816",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2c9db1a7751418b490bf799de5fb2fbba6884af5"
    },
    {
      "sha": "0ca3974d3a",
      "message": "Add large memory flag for asan tests (#1767)",
      "date": "2025-02-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1767",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0ca3974d3ac8edec21994add5d2c7cbb7175f9eb"
    },
    {
      "sha": "58c9230489",
      "message": "Divide release tags according to release stage (#52)",
      "date": "2025-02-25",
      "repo": "valkey-container",
      "pr_url": "https://github.com/valkey-io/valkey-container/pull/52",
      "commit_url": "https://github.com/valkey-io/valkey-container/commit/58c923048945c7b532914396508cbf061bd43ac7"
    },
    {
      "sha": "457dbc593f",
      "message": "Add 8.1.0-rc1 release (#209)",
      "date": "2025-02-18",
      "repo": "valkey-io.github.io",
      "pr_url": "https://github.com/valkey-io/valkey-io.github.io/pull/209",
      "commit_url": "https://github.com/valkey-io/valkey-io.github.io/commit/457dbc593f57643b1bc58c5a072279ccaaa2bc5f"
    },
    {
      "sha": "796eef76df",
      "message": "Adds 8.1.0-rc1 and updates docker hub descriptions with new tags (#51)",
      "date": "2025-02-17",
      "repo": "valkey-container",
      "pr_url": "https://github.com/valkey-io/valkey-container/pull/51",
      "commit_url": "https://github.com/valkey-io/valkey-container/commit/796eef76df6747fcf3c5ecb5d84ff55fbd259d87"
    },
    {
      "sha": "21677c19eb",
      "message": "Add hash for 8.1.0-rc1 (#9)",
      "date": "2025-02-17",
      "repo": "valkey-hashes",
      "pr_url": "https://github.com/valkey-io/valkey-hashes/pull/9",
      "commit_url": "https://github.com/valkey-io/valkey-hashes/commit/21677c19ebb6683c68d75c64b369f79b82d7cb5b"
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
      "sha": "c5ae37f223",
      "message": "Add spellchecker ignore section (#1730)",
      "date": "2025-02-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1730",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c5ae37f223cc00ce9f1ea0633693eba64566dfa1"
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
      "sha": "230efa4fbf",
      "message": "deflake tracking-redir-broken test (#1628)",
      "date": "2025-01-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1628",
      "commit_url": "https://github.com/valkey-io/valkey/commit/230efa4fbf4f90828c211924c0e02fe3495bd727"
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
      "sha": "dd92d079dc",
      "message": "Fix Protocol desync regression test (#1590)",
      "date": "2025-01-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1590",
      "commit_url": "https://github.com/valkey-io/valkey/commit/dd92d079dcb15a984493def7f53746669e7cd693"
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
      "sha": "0f273bb648",
      "message": "Align rejected unblocked commands to update the correct error statistic (#577)",
      "date": "2025-01-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/577",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0f273bb648bf06557f8d06ee8cb346668b741ba0"
    },
    {
      "sha": "ba25b586d5",
      "message": "Introduce FORCE_DEFRAG compilation option to allow activedefrag run when allocator is not jemalloc (#1303)",
      "date": "2024-12-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1303",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ba25b586d5744e315864790e6920a26830a54c09"
    },
    {
      "sha": "2d92404522",
      "message": "Avoid defragging scripts during EVAL command execution (#1414)",
      "date": "2024-12-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1414",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2d924045223a9f2396b6a08a939b66e2fe5c5d65"
    },
    {
      "sha": "5be4ce6d27",
      "message": "Optimize ZRANK to avoid path comparisons (#1389)",
      "date": "2024-12-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1389",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5be4ce6d27c0fb8c046508ff04016a1395ca9d5e"
    },
    {
      "sha": "66ae8b7135",
      "message": "change the container image to ubuntu:plucky (#1359)",
      "date": "2024-11-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1359",
      "commit_url": "https://github.com/valkey-io/valkey/commit/66ae8b71352853ee90a0a9d4cddbbb406c189416"
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
      "sha": "c873287d16",
      "message": "avoid double close on replica main channel (#1097)",
      "date": "2024-09-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1097",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c873287d16eabb9e0470f5e21259a0e7f2cbf223"
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
      "sha": "e2ab7ffd89",
      "message": "Make use of a single listNode pointer for blocking utility lists (#919)",
      "date": "2024-08-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/919",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e2ab7ffd894a44d836019c62710c20c7ef5852b3"
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
      "sha": "752b6ee8ff",
      "message": "Avoid compilation error oin valkey-cli (#721)",
      "date": "2024-07-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/721",
      "commit_url": "https://github.com/valkey-io/valkey/commit/752b6ee8ff75a72c364feca8b667f9e723df0c4c"
    },
    {
      "sha": "24208812a6",
      "message": "Increase ping and cluster timeout for cluster-slots test (#717)",
      "date": "2024-06-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/717",
      "commit_url": "https://github.com/valkey-io/valkey/commit/24208812a658c5dbb843dc20f9615e801be37d46"
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
      "sha": "be2c321682",
      "message": "Support RDB compatability with Redis 7.2.4 RDB format (#665)",
      "date": "2024-06-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/665",
      "commit_url": "https://github.com/valkey-io/valkey/commit/be2c3216824207613cf00b1e5579ee510b7fadc2"
    },
    {
      "sha": "b2a397366b",
      "message": "Change ascii logo with temporal valkey logo (#77)",
      "date": "2024-03-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/77",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b2a397366b1704b03f5042395ff620cd2096f598"
    }
  ],
  "review_list": [
    {
      "sha": "ca9dee353d",
      "message": "Add optional REPLACE argument to MOVE (#2993)",
      "date": "2026-05-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2993",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ca9dee353d2f0c1f48f4471fd191d5583043407d"
    },
    {
      "sha": "a07828f235",
      "message": "Update website for version 7.2.13 (#535)",
      "date": "2026-05-07",
      "repo": "valkey-io.github.io",
      "pr_url": "https://github.com/valkey-io/valkey-io.github.io/pull/535",
      "commit_url": "https://github.com/valkey-io/valkey-io.github.io/commit/a07828f2356651c7c455abe955b52824f07b95ed"
    },
    {
      "sha": "96763ade54",
      "message": "Fix Deferred Reply Placeholders in Active Deferred Buffers (#3578)",
      "date": "2026-05-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3578",
      "commit_url": "https://github.com/valkey-io/valkey/commit/96763ade54998de6002b76a6fc574f050cd0490c"
    },
    {
      "sha": "682d67ab00",
      "message": "Update website for version 8.1.7 (#536)",
      "date": "2026-05-06",
      "repo": "valkey-io.github.io",
      "pr_url": "https://github.com/valkey-io/valkey-io.github.io/pull/536",
      "commit_url": "https://github.com/valkey-io/valkey-io.github.io/commit/682d67ab001461d7bacb8df1c55c1ea9595cba18"
    },
    {
      "sha": "f413bd3348",
      "message": "Update website for version 9.0.4 (#537)",
      "date": "2026-05-06",
      "repo": "valkey-io.github.io",
      "pr_url": "https://github.com/valkey-io/valkey-io.github.io/pull/537",
      "commit_url": "https://github.com/valkey-io/valkey-io.github.io/commit/f413bd33487fa339395696171681e3cf998fd908"
    },
    {
      "sha": "ad0c99a4c0",
      "message": "Update website for version 8.0.9 (#538)",
      "date": "2026-05-06",
      "repo": "valkey-io.github.io",
      "pr_url": "https://github.com/valkey-io/valkey-io.github.io/pull/538",
      "commit_url": "https://github.com/valkey-io/valkey-io.github.io/commit/ad0c99a4c09c235e481431004f8bac4fa76065e1"
    },
    {
      "sha": "797c626046",
      "message": "Fix SIGSEGV in VM_GetLRU/SetLRU/GetLFU/SetLFU on NULL key (#3610)",
      "date": "2026-05-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3610",
      "commit_url": "https://github.com/valkey-io/valkey/commit/797c62604698408653b2f3653c4b9f861572d1b5"
    },
    {
      "sha": "7e2a2f7c4a",
      "message": "fix(cluster): Remove per-call srand in clusterManagerNodePrimaryRandom (#3586)",
      "date": "2026-04-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3586",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7e2a2f7c4a394cf27ebaa3dc7106a8337a8ddf72"
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
      "sha": "0327c27131",
      "message": "Add Static Module Support (#3392)",
      "date": "2026-04-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3392",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0327c271316daa952e6c9a41cc922ea8a9548827"
    },
    {
      "sha": "269b1c5eda",
      "message": "Improve COB memory tracking with copy avoidance (#3306)",
      "date": "2026-04-20",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3306",
      "commit_url": "https://github.com/valkey-io/valkey/commit/269b1c5eda9347fb7d4d485ac9d375d11d467edd"
    },
    {
      "sha": "60c1b0b86b",
      "message": "ARM NEON SIMD optimization for pvFind() in vset.c (#3033)",
      "date": "2026-03-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3033",
      "commit_url": "https://github.com/valkey-io/valkey/commit/60c1b0b86bdbab4e80af38db6dd98928aa3909bf"
    },
    {
      "sha": "f7a64c5509",
      "message": "Fix EntryTest.entryUpdate failure on macOS due to allocator differences (#3398)",
      "date": "2026-03-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3398",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f7a64c55099efb4ee3885a2df473ab89c3948abe"
    },
    {
      "sha": "543a6b83df",
      "message": "Ensure the daily workflow uses gtest-parallel to run unit tests in isolation (#3375)",
      "date": "2026-03-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3375",
      "commit_url": "https://github.com/valkey-io/valkey/commit/543a6b83dffff9d35da046ad2067a94b60cf3f38"
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
      "sha": "3d8a1b55ed",
      "message": "Replace long long timestamp references with more specific mstime_t/ustime_t (#3252)",
      "date": "2026-03-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3252",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3d8a1b55ed072380655f18b0868a1edb20b08a64"
    },
    {
      "sha": "9f0106755b",
      "message": "Changed LUA module dependency (#3325)",
      "date": "2026-03-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3325",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9f0106755b177f8eea3d62eed6f28f20fb54d459"
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
      "sha": "501b3153f2",
      "message": "Skip expired hash fields when loading non-preamble RDB on primary (#3091)",
      "date": "2026-02-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3091",
      "commit_url": "https://github.com/valkey-io/valkey/commit/501b3153f26e4d8e5f9764d04abed624e2e655cf"
    },
    {
      "sha": "2565d445ad",
      "message": "Reset request type after handling empty requests",
      "date": "2026-02-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3250",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2565d445adf3f256e7f124cc2387d9e15dd3bc39"
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
      "sha": "130befc812",
      "message": "Dual-channel-replication announces itself at replica-announce-ip if configured (#2846)",
      "date": "2026-02-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2846",
      "commit_url": "https://github.com/valkey-io/valkey/commit/130befc8123b0cb98e3c2c87f604aca0e50755be"
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
      "sha": "eabfe235d2",
      "message": "Check expiration time first before lookup the key in GETEX command (#3116)",
      "date": "2026-02-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3116",
      "commit_url": "https://github.com/valkey-io/valkey/commit/eabfe235d2b522f0aded9a6139f16c4f5deeed93"
    },
    {
      "sha": "920bf128b6",
      "message": "Optimize skiplist query efficiency by embedding the skiplist header (#2867)",
      "date": "2026-01-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2867",
      "commit_url": "https://github.com/valkey-io/valkey/commit/920bf128b6c41caa1a2badeaccf9e5c58a3e86e8"
    },
    {
      "sha": "1fd6d7156f",
      "message": "decouple lru/lfu from server.h (#2928)",
      "date": "2026-01-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2928",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1fd6d7156fbf438f471a680fbc7e5b6b087167be"
    },
    {
      "sha": "f5d7dc8d05",
      "message": "Fix potential memory leaks when a writable replica is promoted to primary after direct writes of keys with expiration (#2953)",
      "date": "2026-01-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2953",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f5d7dc8d057df8431d9d23f80b35c83b424b4d2c"
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
      "sha": "8e462d4ae2",
      "message": "Fix typo in HSETEX command documentation (#400)",
      "date": "2026-01-20",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/400",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/8e462d4ae2fbc61e3222e21b93a32a1a15691fb9"
    },
    {
      "sha": "69bde6a827",
      "message": "Reset maxmemory after OOM scripting tests (#3047)",
      "date": "2026-01-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3047",
      "commit_url": "https://github.com/valkey-io/valkey/commit/69bde6a827df77af6c09862f5360eecaf26397ec"
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
      "sha": "5a3fb0454c",
      "message": "HFE make zero a valid ttl during import mode and data loading  (#3006)",
      "date": "2026-01-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3006",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5a3fb0454c866cdf46729694e24e2ecf792df97b"
    },
    {
      "sha": "0ee4234506",
      "message": "Remove internal server object pointer overhead in small strings (#2516)",
      "date": "2026-01-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2516",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0ee4234506ba5b37095160047daf75b857171c12"
    },
    {
      "sha": "dbe07b7c98",
      "message": "Untrack key based on old->hasembkey (#3007)",
      "date": "2026-01-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3007",
      "commit_url": "https://github.com/valkey-io/valkey/commit/dbe07b7c98790400dc0f895deac2c277aa378175"
    },
    {
      "sha": "dbe07b7c98",
      "message": "Untrack key based on old->hasembkey (#3007)",
      "date": "2026-01-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3007",
      "commit_url": "https://github.com/valkey-io/valkey/commit/dbe07b7c98790400dc0f895deac2c277aa378175"
    },
    {
      "sha": "e4a3e9f0a2",
      "message": "fix(hash): Untrack hash with volatile fields when it is overwritten  (#3003)",
      "date": "2026-01-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3003",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e4a3e9f0a298fbaa7320e76dbdd4b790425c148e"
    },
    {
      "sha": "fd56b21df0",
      "message": "Add sdsnsplitargs to reduce sds allocation. (#2975)",
      "date": "2026-01-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2975",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fd56b21df0c5130e11647e907a4ef31d5fd81584"
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
      "sha": "9a8f1c8c1b",
      "message": "fix(HSETEX): replace strcmp with strcasecmp (#3000)",
      "date": "2026-01-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/3000",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9a8f1c8c1b194eff17f937b569f1b15b8efbc202"
    },
    {
      "sha": "15e79ef00a",
      "message": "Add FIFO and mutexQueue with bio.c refactored (#2895)",
      "date": "2026-01-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2895",
      "commit_url": "https://github.com/valkey-io/valkey/commit/15e79ef00a5e98a062776e7656ed34f834dd2d8a"
    },
    {
      "sha": "e843c18f1e",
      "message": "Valkey Fuzzer (#2340)",
      "date": "2026-01-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2340",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e843c18f1e42dbb96860eed171d13eddad93a0ab"
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
      "sha": "e9014fd02b",
      "message": "Adding support for sharing memory between the module and the engine (#2472)",
      "date": "2025-12-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2472",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e9014fd02b6e378ea647013097452558c20f0540"
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
      "sha": "2e0c55c1c3",
      "message": "test improvements",
      "date": "2025-12-14",
      "repo": "valkey-try-me",
      "pr_url": "https://github.com/valkey-io/valkey-try-me/pull/3",
      "commit_url": "https://github.com/valkey-io/valkey-try-me/commit/2e0c55c1c3145ace47baef38379857007b2e9580"
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
      "sha": "5940dbfb0b",
      "message": "Revert \"Allow partial sync after loading AOF with preamble (#2366)\" (#2925)",
      "date": "2025-12-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2925",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5940dbfb0b601dfc565ca7f349a3a62f67d7e5ed"
    },
    {
      "sha": "44dc58181d",
      "message": "Fix a typo in aof-multi-part.tcl (#2922)",
      "date": "2025-12-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2922",
      "commit_url": "https://github.com/valkey-io/valkey/commit/44dc58181d7f8ef9d39503ec6522d5fcbeb01a79"
    },
    {
      "sha": "04d0bba398",
      "message": "support whole cluster info for INFO command in cluster section (#2876)",
      "date": "2025-12-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2876",
      "commit_url": "https://github.com/valkey-io/valkey/commit/04d0bba398afe056a7a269ae46a81da574020ada"
    },
    {
      "sha": "3d65a4aecd",
      "message": "Fix deadlock in IO thread shutdown during panic (#2898)",
      "date": "2025-12-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2898",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3d65a4aecdcfdd72ff1657317657a4cd665bba5f"
    },
    {
      "sha": "1b5f245eae",
      "message": "Refactor of LFU/LRU code for modularity (#2857)",
      "date": "2025-12-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2857",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1b5f245eaecf274f655763f20e30ed4f1966ff41"
    },
    {
      "sha": "faac14ab9c",
      "message": "Cluster: Optimize slot bitmap iteration from per-bit to 64-bit word scan (#2781)",
      "date": "2025-11-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2781",
      "commit_url": "https://github.com/valkey-io/valkey/commit/faac14ab9c8430057490f64ca979492057bb4d40"
    },
    {
      "sha": "56ab3c4a81",
      "message": "Adds HGETDEL Support to Valkey (#2851)",
      "date": "2025-11-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2851",
      "commit_url": "https://github.com/valkey-io/valkey/commit/56ab3c4a813564e50a00cb2fd80e1beaea4af506"
    },
    {
      "sha": "e19ceb7a6d",
      "message": "deflake \"Hash field TTL and active expiry propagates correctly\" (#2856)",
      "date": "2025-11-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2856",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e19ceb7a6de207d049378a29406cb1763a6e1844"
    },
    {
      "sha": "33bfac37ba",
      "message": "Optimize zset memory usage by embedding element in skiplist (#2508)",
      "date": "2025-11-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2508",
      "commit_url": "https://github.com/valkey-io/valkey/commit/33bfac37bab7b754604c3fd8a5563aa1398c651d"
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
      "sha": "1b0b5c0cfd",
      "message": "New module API to perform prefix\u2011aware ACL permission check (#2796)",
      "date": "2025-11-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2796",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1b0b5c0cfd7fb31d7c957cbe533d95ad693499c0"
    },
    {
      "sha": "65ab07dde7",
      "message": "Leverage zfree_with_size for client reply blocks (#2624)",
      "date": "2025-11-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2624",
      "commit_url": "https://github.com/valkey-io/valkey/commit/65ab07dde7a18e22f9f65e7c3d6dedd3a8727793"
    },
    {
      "sha": "a49d469f48",
      "message": "Reverts hashHashtableTypeValidate signature (#2799)",
      "date": "2025-11-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2799",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a49d469f483b2d8f0624790a0a40ec876b6bfa95"
    },
    {
      "sha": "a99c636321",
      "message": "Improve header comment and strengthen type checking for entry (#2794)",
      "date": "2025-11-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2794",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a99c63632109d17bb06f1153f195658ae3ba2e2c"
    },
    {
      "sha": "4d78d36bff",
      "message": "HSETEX: Support NX/XX Flags (#2668)",
      "date": "2025-11-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2668",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4d78d36bff27c6345be7127cc50776b2fb34a745"
    },
    {
      "sha": "4d78d36bff",
      "message": "HSETEX: Support NX/XX Flags (#2668)",
      "date": "2025-11-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2668",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4d78d36bff27c6345be7127cc50776b2fb34a745"
    },
    {
      "sha": "f3b2dee3b7",
      "message": "Add monotonic clock calibration handling if clock speed is not found (#2776)",
      "date": "2025-10-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2776",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f3b2dee3b7c99d0753d4fb02783be4ec9f086344"
    },
    {
      "sha": "623dbe9f19",
      "message": "Update version to 9.0.0 (#373)",
      "date": "2025-10-22",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/373",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/623dbe9f1949269431c16a5c37e16238948646b9"
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
      "sha": "3390b1e608",
      "message": "Allow TCL 9.0 for tests (#1673)",
      "date": "2025-10-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1673",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3390b1e608f2cf39c00cf66a2e975b756c5e8b02"
    },
    {
      "sha": "ae58b3d5be",
      "message": "Redirect blocked clients after failover (#2329)",
      "date": "2025-09-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2329",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ae58b3d5bee7c8bc4de529da3d89dd07a29a6e0a"
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
      "sha": "d21d529851",
      "message": "Optimize skiplist random level generation logic (#2631)",
      "date": "2025-09-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2631",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d21d529851bef718ed666ab87d975b32a9c7ac5c"
    },
    {
      "sha": "298f7dae60",
      "message": "Adding unit tests for sha256 (#2632)",
      "date": "2025-09-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2632",
      "commit_url": "https://github.com/valkey-io/valkey/commit/298f7dae60386df154d272a496c7e9ac7dcfbd6c"
    },
    {
      "sha": "298f7dae60",
      "message": "Adding unit tests for sha256 (#2632)",
      "date": "2025-09-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2632",
      "commit_url": "https://github.com/valkey-io/valkey/commit/298f7dae60386df154d272a496c7e9ac7dcfbd6c"
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
      "sha": "93d7ccab03",
      "message": "Fix accounting for dual channel RDB bytes in replication stats (#2602)",
      "date": "2025-09-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2602",
      "commit_url": "https://github.com/valkey-io/valkey/commit/93d7ccab03779afe70762740129bd34b840e663f"
    },
    {
      "sha": "9b11d3d9ed",
      "message": "Evict client only when limit is breached (#2596)",
      "date": "2025-09-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2596",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9b11d3d9edf6b1f1f18976305c0923c5aad60297"
    },
    {
      "sha": "d9382bd9f3",
      "message": "ARM Neon SIMD optimization for hashtable findBucket() (#2573)",
      "date": "2025-09-07",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2573",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d9382bd9f3cec97a57815e1ad9216aac08b47fbb"
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
      "sha": "9d10abfbde",
      "message": "Relaxed RDB check for foreign RDB formats (#2543)",
      "date": "2025-09-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2543",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9d10abfbded4ed9633ac50c8c09a9a9965dd6740"
    },
    {
      "sha": "5d2f1e2143",
      "message": "Add CI job to check internal links (#355)",
      "date": "2025-09-04",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/355",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/5d2f1e2143b06e807c9f0d47e668de67cb6131fd"
    },
    {
      "sha": "971cdb7836",
      "message": "Don't use AVX2 instructions if the CPU don't support it (#2571)",
      "date": "2025-09-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2571",
      "commit_url": "https://github.com/valkey-io/valkey/commit/971cdb78363ba19306bb610efa9eca44543f6b70"
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
      "sha": "40fe422899",
      "message": "deflake test: relax time requirement in hash ttl test (#2537)",
      "date": "2025-08-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2537",
      "commit_url": "https://github.com/valkey-io/valkey/commit/40fe4228992f39e31f1481f052ed6bc5c090353d"
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
      "sha": "9d682bad0b",
      "message": "bio.c: Organize all worker data in a struct (#2530)",
      "date": "2025-08-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2530",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9d682bad0bb731de8e21e15e4a1795c73aee9d0d"
    },
    {
      "sha": "b8357e5be8",
      "message": "Fix slot range lists overlap to rewind the nested list again  (#2527)",
      "date": "2025-08-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2527",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b8357e5be83dd19411c77a4e5f1052a3f863e8c9"
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
      "sha": "58f5562d22",
      "message": "Fix duplicate Acks for RDMA events and fix extremely large max latency for RDMA benchmark. (#2430)",
      "date": "2025-08-13",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2430",
      "commit_url": "https://github.com/valkey-io/valkey/commit/58f5562d221d74ab85624a11ac330d9c5f69ae78"
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
      "sha": "d32f9be04a",
      "message": "Use bool for return types in hashtable functions (#2432)",
      "date": "2025-08-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2432",
      "commit_url": "https://github.com/valkey-io/valkey/commit/d32f9be04ab85eddf5c627ddf789cc950a1c6ef4"
    },
    {
      "sha": "e606fcbaff",
      "message": "Fix AOF rewrite behavior for hashes with expirations (#2454)",
      "date": "2025-08-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2454",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e606fcbaffd16760a758de631867ae6b92737bd2"
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
      "sha": "fd8270a0aa",
      "message": "[CRASH] Fix missing check for executing client (#2347)",
      "date": "2025-08-06",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2347",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fd8270a0aab6c15058997a0e8436c9682dac2036"
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
      "sha": "3b12132ac0",
      "message": "Rename trace bgsave type to rdb and aof (#2400)",
      "date": "2025-08-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2400",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3b12132ac0be654abaf1cd04fa9fdf8f44314327"
    },
    {
      "sha": "025f416b74",
      "message": "Save to Disk in Bio Thread and refactor readSyncBulkPayload (#1784)",
      "date": "2025-07-31",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1784",
      "commit_url": "https://github.com/valkey-io/valkey/commit/025f416b74eaafed546c881560ead625242e34b0"
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
      "sha": "04353aea38",
      "message": "Ensure empty error tables in scripts don't crash Valkey (#2229)",
      "date": "2025-06-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2229",
      "commit_url": "https://github.com/valkey-io/valkey/commit/04353aea381f8c93dcb323839b4dc4821fcbd042"
    },
    {
      "sha": "92c154980f",
      "message": "Stabilize dual channel test: Split scenarios and set RDB loading interval (#2200)",
      "date": "2025-06-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2200",
      "commit_url": "https://github.com/valkey-io/valkey/commit/92c154980fe4be123e533b7cd01fcc072666e687"
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
      "sha": "0039adcc7e",
      "message": "Remove dead conditions around the multi/exec check (#2168)",
      "date": "2025-06-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2168",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0039adcc7eea28a4c3ea9d93380edfda72d16956"
    },
    {
      "sha": "3789b29e92",
      "message": "Offload slot calculation and cross-slot detection to I/O threads (#2165)",
      "date": "2025-06-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2165",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3789b29e92d4997252352bd9748bffaf7d8f712b"
    },
    {
      "sha": "3789b29e92",
      "message": "Offload slot calculation and cross-slot detection to I/O threads (#2165)",
      "date": "2025-06-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2165",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3789b29e92d4997252352bd9748bffaf7d8f712b"
    },
    {
      "sha": "5699c8c05a",
      "message": "Combine range element ranks calculation with range elements search to improve zcount performance (#2129)",
      "date": "2025-06-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2129",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5699c8c05a207dd2590aa37843a60b2131f3a2da"
    },
    {
      "sha": "5699c8c05a",
      "message": "Combine range element ranks calculation with range elements search to improve zcount performance (#2129)",
      "date": "2025-06-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2129",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5699c8c05a207dd2590aa37843a60b2131f3a2da"
    },
    {
      "sha": "36312085e7",
      "message": "Have threads gracefully exit instead of killing them when checking thread count (#2156)",
      "date": "2025-06-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2156",
      "commit_url": "https://github.com/valkey-io/valkey/commit/36312085e785304a71467ff555081a4576687f26"
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
      "sha": "bf95710ecf",
      "message": "\"replaced test cdn with production cdn\"",
      "date": "2025-05-28",
      "repo": "valkey-try-me",
      "pr_url": "https://github.com/valkey-io/valkey-try-me/pull/1",
      "commit_url": "https://github.com/valkey-io/valkey-try-me/commit/bf95710ecfd9fa9127be4a338355704e2b89010e"
    },
    {
      "sha": "374718b2a3",
      "message": "Fix unsigned difference expression compared to zero (#2101)",
      "date": "2025-05-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2101",
      "commit_url": "https://github.com/valkey-io/valkey/commit/374718b2a365ca69f715d542709b7d71540b1387"
    },
    {
      "sha": "bd5dcb2819",
      "message": "Fix bad slot used in sharded pubsub unsubscribe (#2137)",
      "date": "2025-05-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2137",
      "commit_url": "https://github.com/valkey-io/valkey/commit/bd5dcb2819cd35f2e346f94ed26a8e1182f5c245"
    },
    {
      "sha": "bd5dcb2819",
      "message": "Fix bad slot used in sharded pubsub unsubscribe (#2137)",
      "date": "2025-05-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2137",
      "commit_url": "https://github.com/valkey-io/valkey/commit/bd5dcb2819cd35f2e346f94ed26a8e1182f5c245"
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
      "sha": "11a2b6c4c6",
      "message": "Fix string embedding decision with keys (#2087)",
      "date": "2025-05-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2087",
      "commit_url": "https://github.com/valkey-io/valkey/commit/11a2b6c4c64048c75aafdb57747d7c3ceba5f1d7"
    },
    {
      "sha": "fe97ba419d",
      "message": "valkey-benchmark: Arbitrary command sequence (#2057)",
      "date": "2025-05-12",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2057",
      "commit_url": "https://github.com/valkey-io/valkey/commit/fe97ba419df86b2face579ef04b109069d36958e"
    },
    {
      "sha": "dec68a9123",
      "message": "Docs for valkey-benchmark custom command sequence (#276)",
      "date": "2025-05-12",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/276",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/dec68a9123c0eb3801002ef5d918ee2ca2d96820"
    },
    {
      "sha": "2205bf99cb",
      "message": "move statement in if condition for zremrangeGenericCommand function (#2060)",
      "date": "2025-05-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2060",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2205bf99cb867fb8c5612d58e24027f1837cf65a"
    },
    {
      "sha": "a2001a3872",
      "message": "Fixed minor grammatical error (#2061)",
      "date": "2025-05-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2061",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a2001a38729fa643fb735b7d931890d807f1d514"
    },
    {
      "sha": "249495a3ff",
      "message": "Convert pubsub dicts to hashtables (#2007)",
      "date": "2025-04-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2007",
      "commit_url": "https://github.com/valkey-io/valkey/commit/249495a3ff364f3fb66096223a98efde72e37b7a"
    },
    {
      "sha": "2399f10772",
      "message": "Fix crash during TLS handshake with I/O threads (#1955)",
      "date": "2025-04-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1955",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2399f107729171f9e8e35c9997b19d3e8c9c58ef"
    },
    {
      "sha": "0410436179",
      "message": "Replaced the use of sdsReplyDictType and hashDictType. (#1793)",
      "date": "2025-04-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1793",
      "commit_url": "https://github.com/valkey-io/valkey/commit/04104361791be789f514d3731ea7cca353d0292b"
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
      "sha": "50a63ec983",
      "message": "Fixes to the blog posts about 8.1.0 release and hash table (#232)",
      "date": "2025-04-02",
      "repo": "valkey-io.github.io",
      "pr_url": "https://github.com/valkey-io/valkey-io.github.io/pull/232",
      "commit_url": "https://github.com/valkey-io/valkey-io.github.io/commit/50a63ec98317a75f7165958c73a75927af56b676"
    },
    {
      "sha": "09f9630171",
      "message": "Redact protocol error log when hide-user-data-from-log enabled (#1889)",
      "date": "2025-03-31",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1889",
      "commit_url": "https://github.com/valkey-io/valkey/commit/09f9630171501d1d62536045984220cad73588ba"
    },
    {
      "sha": "b8ccd9151d",
      "message": "Add description about benchmark option '--rfr' (#254)",
      "date": "2025-03-26",
      "repo": "valkey-doc",
      "pr_url": "https://github.com/valkey-io/valkey-doc/pull/254",
      "commit_url": "https://github.com/valkey-io/valkey-doc/commit/b8ccd9151d47b0a5a4341ea22c05eb94b799403e"
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
      "sha": "3efe8419ec",
      "message": "Fix timing issue in the module propagate test (#1815)",
      "date": "2025-03-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1815",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3efe8419ec98aeb41abf5897501e5fb24100e126"
    },
    {
      "sha": "f31cf189c2",
      "message": "Fixed build error with CMake (#1806)",
      "date": "2025-03-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1806",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f31cf189c21a20f428a0b4714a8495885b04a370"
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
      "sha": "7db01d88c2",
      "message": "Fix undefined behaviour in bitops unit test (#1786)",
      "date": "2025-02-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1786",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7db01d88c271d4fa483d5b8e9e968bbbf979cb35"
    },
    {
      "sha": "aea3eadab5",
      "message": "Enable TCP_NODELAY by default in incoming and outgoing connections (#1763)",
      "date": "2025-02-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1763",
      "commit_url": "https://github.com/valkey-io/valkey/commit/aea3eadab53a14549e6a039a1d4635704637c0cc"
    },
    {
      "sha": "421b2a40e6",
      "message": "Embed hash value in hash type entry (#1579)",
      "date": "2025-02-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1579",
      "commit_url": "https://github.com/valkey-io/valkey/commit/421b2a40e6ac850c097f7b91763b2e30917135fd"
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
      "sha": "be9d9487bd",
      "message": "Fix murmur32 on large strings (#1748)",
      "date": "2025-02-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1748",
      "commit_url": "https://github.com/valkey-io/valkey/commit/be9d9487bd6ba5d5c5d6d6ca351e020fb33268a1"
    },
    {
      "sha": "3a64260e41",
      "message": "Fix error \"SSL routines::bad length\" when connTLSWrite is called second time with smaller buffer (#1737)",
      "date": "2025-02-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1737",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3a64260e415d4c1ae3e0eb7ebe6359ea53d841ca"
    },
    {
      "sha": "f85c93301c",
      "message": "Comment out assert in kvstore for overhead lut (#1745)",
      "date": "2025-02-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1745",
      "commit_url": "https://github.com/valkey-io/valkey/commit/f85c93301ca63f070164b307c6a7371a9ab5ac7b"
    },
    {
      "sha": "83abb13a1c",
      "message": "Fix memory error in networking unittest (#1697)",
      "date": "2025-02-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1697",
      "commit_url": "https://github.com/valkey-io/valkey/commit/83abb13a1ce371e37826bcbfaa1a4198a12457e2"
    },
    {
      "sha": "e8ae5b1852",
      "message": "Fix log message \"DB 9: 100 keys (0 volatile) in 16 slots HT\" (#1691)",
      "date": "2025-02-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1691",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e8ae5b1852474ff89cfe23d4485a88dc59b5c0a3"
    },
    {
      "sha": "de3672a7ff",
      "message": "Offload replication writes to IO threads (#1485)",
      "date": "2025-02-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1485",
      "commit_url": "https://github.com/valkey-io/valkey/commit/de3672a7ffba8773871bebda0553f370906a7ae3"
    },
    {
      "sha": "8d8ce19da8",
      "message": "Embed keys and hash fields as SDS type 5 (#1613)",
      "date": "2025-02-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1613",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8d8ce19da80e5c51d470870e7fdf7e5b3926f47a"
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
      "sha": "2eac2ccd2f",
      "message": "skip CRC checksumming during diskless full sync with TLS enabled. (#1479)",
      "date": "2025-02-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1479",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2eac2ccd2f89e9e15f3e794e1d05e7ffb043f599"
    },
    {
      "sha": "ad60d6b7b3",
      "message": "Initialize one variable in struct to avoid risk (#1606)",
      "date": "2025-01-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1606",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ad60d6b7b36e0599dba8f817c6fcd9bb69c30f37"
    },
    {
      "sha": "88a68303c0",
      "message": "Make sure to disable pause after fork for dual channel test (#1612)",
      "date": "2025-01-27",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1612",
      "commit_url": "https://github.com/valkey-io/valkey/commit/88a68303c034fcb61a04969f6ac6eeb3fdeca1ee"
    },
    {
      "sha": "b2e4155f54",
      "message": "Lower latenct-monitor-threashold in expire-cycle test case (#1584)",
      "date": "2025-01-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1584",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b2e4155f54d335d7a6b0764ef963eaf5ef863f8f"
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
      "sha": "2a1a65b4c7",
      "message": "Introduce const_sds for const-content sds (#1553)",
      "date": "2025-01-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1553",
      "commit_url": "https://github.com/valkey-io/valkey/commit/2a1a65b4c73cd238f37283759a292ac6477f169e"
    },
    {
      "sha": "6be1c77b1e",
      "message": "Fix valgrind test (#1555)",
      "date": "2025-01-14",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1555",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6be1c77b1eb54141041198ded92894e93ac575e2"
    },
    {
      "sha": "ab627d6721",
      "message": "Replace dict with new hashtable: sorted set datatype (#1427)",
      "date": "2025-01-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1427",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ab627d6721af65f999ae6a3fac55f6f458b9ee5e"
    },
    {
      "sha": "6c09eea2bc",
      "message": "client struct: lazy init components and optimize struct layout (#1405)",
      "date": "2025-01-08",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1405",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6c09eea2bcb996d70aeda9f78f4304c6309cf475"
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
      "sha": "ae70c5459b",
      "message": "replication: fix io-threads possible race by moving waitForClientIO (#1422)",
      "date": "2025-01-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1422",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ae70c5459b13d426e8e48d85e7f48120d69eeebb"
    },
    {
      "sha": "9f4503ca50",
      "message": "Add scoped RDB loading context and immediate abort flag (#1173)",
      "date": "2024-12-24",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1173",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9f4503ca500fe2b668decb6fb94c377fbce5d0a0"
    },
    {
      "sha": "e9a1fe0b32",
      "message": "Support for reading from replicas in valkey-benchmark (#1392)",
      "date": "2024-12-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1392",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e9a1fe0b320c2f1f262ffa2200321348c08f8849"
    },
    {
      "sha": "8060c86d20",
      "message": "Offload TLS negotiation to I/O threads (#1338)",
      "date": "2024-12-18",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1338",
      "commit_url": "https://github.com/valkey-io/valkey/commit/8060c86d2015ea9fdb0afcb4efc88fbf3951b78d"
    },
    {
      "sha": "7892bf808b",
      "message": "Fix test_reclaimFilePageCache to avoid tmpfs (#1379)",
      "date": "2024-12-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1379",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7892bf808b6f748684af7defa0c0a8611cc4be50"
    },
    {
      "sha": "0c8ad5cd34",
      "message": "defrag: allow defrag to start during AOF loading (#1420)",
      "date": "2024-12-11",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1420",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0c8ad5cd34129bacf5a3dda30b37b156e7cdfb98"
    },
    {
      "sha": "b4c2a1804a",
      "message": "Fix flaky init_test proc in maxmemory test suite (#1419)",
      "date": "2024-12-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1419",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b4c2a1804a20211a0cca634393d689e5bc96ddf7"
    },
    {
      "sha": "9f8b174c2e",
      "message": "Optimize IO thread offload for modified argv (#1360)",
      "date": "2024-12-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1360",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9f8b174c2eec4be1b6bc15745ac479c95dbd3a6b"
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
      "sha": "a939cb88ee",
      "message": "Handle keyIsExpiredWithDictIndex to make it check for import mode (#1368)",
      "date": "2024-11-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1368",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a939cb88ee0c0512c003106be483b7c6968b3e7f"
    },
    {
      "sha": "9305b49145",
      "message": "Add tag for dual-channel logs (#999)",
      "date": "2024-11-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/999",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9305b49145172da781b8af2b5b96f9643e4367ec"
    },
    {
      "sha": "33f42d7fb5",
      "message": "CMake fixes + README update (#1276)",
      "date": "2024-11-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1276",
      "commit_url": "https://github.com/valkey-io/valkey/commit/33f42d7fb597ce28040f184ee57ed86d6f6ffbd8"
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
      "sha": "b486a41500",
      "message": "Preserve original fd blocking state in TLS I/O operations (#1298)",
      "date": "2024-11-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1298",
      "commit_url": "https://github.com/valkey-io/valkey/commit/b486a415009660f355d0a8eb9fd67a9c9cb9cc6e"
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
      "sha": "4986310945",
      "message": "Import-mode: Avoid expiration and eviction during data syncing (#1185)",
      "date": "2024-11-19",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1185",
      "commit_url": "https://github.com/valkey-io/valkey/commit/49863109453faa907ce2c8b1158e60a6777d28ab"
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
      "sha": "4e2493e5c9",
      "message": "Kill diskless fork child asap when the last replica drop (#1227)",
      "date": "2024-11-15",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1227",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4e2493e5c961b36e6832e8d6ea259939b0cf0fde"
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
      "sha": "5885dc56bd",
      "message": "Fix BGSAVE CANCEL since and history fields (#1200)",
      "date": "2024-10-21",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1200",
      "commit_url": "https://github.com/valkey-io/valkey/commit/5885dc56bdb40b3e0ea9b3d20a8bb08c7f2c3157"
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
      "sha": "9f0c80187e",
      "message": "Fix crash in async IO threads with TLS (#1011)",
      "date": "2024-09-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1011",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9f0c80187e55517a8ee23f4ad31a65622e45fb84"
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
      "sha": "39f8bcb91b",
      "message": "Skip tracking clients OOM test when I/O threads are enabled (#764)",
      "date": "2024-08-22",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/764",
      "commit_url": "https://github.com/valkey-io/valkey/commit/39f8bcb91b3bcc031c67ba71f5352d05fc7d6dca"
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
      "sha": "1d18842074",
      "message": "Fix bug in writeToClient (#834)",
      "date": "2024-07-31",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/834",
      "commit_url": "https://github.com/valkey-io/valkey/commit/1d188420741d4453615f776574f97984334a9939"
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
      "sha": "9211aed72e",
      "message": "Improve reliability of dual-channel-replication pause resume tests (#835)",
      "date": "2024-07-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/835",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9211aed72e335ecf8923bd87f955bd019e731519"
    },
    {
      "sha": "ff6b780fe6",
      "message": "Dual channel replication (#60)",
      "date": "2024-07-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/60",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ff6b780fe616536c233c1440997d49e7276aee0e"
    },
    {
      "sha": "ab3873011a",
      "message": "Replacing REDIS_STATIC with static (#691)",
      "date": "2024-06-26",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/691",
      "commit_url": "https://github.com/valkey-io/valkey/commit/ab3873011a6c208fab4005f7ace87df03850cf03"
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
      "sha": "417660449f",
      "message": "Adjust sds types (#502)",
      "date": "2024-06-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/502",
      "commit_url": "https://github.com/valkey-io/valkey/commit/417660449f9c1fce998e1563f30f7bfd9cb5197f"
    },
    {
      "sha": "6fb90adf4b",
      "message": "Fix crash where command duration is not reset when client is blocked \u2026 (#526)",
      "date": "2024-05-30",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/526",
      "commit_url": "https://github.com/valkey-io/valkey/commit/6fb90adf4be1c3b703040c9f744bc9cf17d3d577"
    }
  ]
}
