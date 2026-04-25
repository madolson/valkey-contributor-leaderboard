---
{
  "title": "zhulipeng",
  "login": "zhulipeng",
  "avatar_url": "https://avatars.githubusercontent.com/u/698621?v=4",
  "score": 26,
  "commit_count": 20,
  "review_count": 6,
  "repos": [
    "valkey"
  ],
  "commit_list": [
    {
      "sha": "9dd5a02cec",
      "message": "Fix the GNU IFUNC error in alpine (non-glibc) environment (#2133)",
      "date": "2025-05-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2133",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9dd5a02cec8db8b7c16ac11092340bd15ec65fc6"
    },
    {
      "sha": "4092c9c8e0",
      "message": "Optimize string2ll with load-time CPU feature check using IFUNC resolver (#2099)",
      "date": "2025-05-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2099",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4092c9c8e091058e3103007b8dc05ae8ae00c1fc"
    },
    {
      "sha": "22c219124f",
      "message": "Optimize findBucket performance using SIMD (#2030)",
      "date": "2025-05-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2030",
      "commit_url": "https://github.com/valkey-io/valkey/commit/22c219124ff6c13bfce757080d41ae243407e476"
    },
    {
      "sha": "70f2057614",
      "message": "Optimize string2ll performance using AVX512 (#1944)",
      "date": "2025-04-29",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1944",
      "commit_url": "https://github.com/valkey-io/valkey/commit/70f205761499854e429e5dd3862d6245b12d1b24"
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
      "sha": "c21f1dc084",
      "message": "Increase the IO_THREADS_MAX_NUM. (#1220)",
      "date": "2024-10-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1220",
      "commit_url": "https://github.com/valkey-io/valkey/commit/c21f1dc084d49ea74883ba93583bf957f7636635"
    },
    {
      "sha": "9c60fcdae2",
      "message": "Do security attack check only when command not found to reduce the critical path (#1212)",
      "date": "2024-10-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1212",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9c60fcdae241a7e1dedc2f51d19491d168d66b9b"
    },
    {
      "sha": "a62d1f177b",
      "message": "Fix false sharing issue between main thread and io-threads when access `used_memory_thread`. (#1179)",
      "date": "2024-10-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1179",
      "commit_url": "https://github.com/valkey-io/valkey/commit/a62d1f177b7888ec88035a0a1ce600fbc2280ce7"
    },
    {
      "sha": "58fe9c0138",
      "message": "Use hashtable as the default type of temp set object during sunion/sdiff (#996)",
      "date": "2024-09-10",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/996",
      "commit_url": "https://github.com/valkey-io/valkey/commit/58fe9c0138af8a45dfcb906a3d5c631a6d6e9a30"
    },
    {
      "sha": "076bf6605f",
      "message": "Move prepareClientToWrite out of loop for lrange command to reduce the redundant call. (#860)",
      "date": "2024-08-28",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/860",
      "commit_url": "https://github.com/valkey-io/valkey/commit/076bf6605fbf2b4b95637bdd4b14a9571139c2fc"
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
      "sha": "4d3d6c06a1",
      "message": "Reduce redundant call of prepareClientToWrite when call addReply* continuously. (#670)",
      "date": "2024-06-25",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/670",
      "commit_url": "https://github.com/valkey-io/valkey/commit/4d3d6c06a15fc5a1a2f9e17b6341cc46850a30f4"
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
      "sha": "7a9951fb80",
      "message": "Correct the actual allocated size from allocator when call sdsRedize to align the logic with sdsnewlen function. (#476)",
      "date": "2024-05-16",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/476",
      "commit_url": "https://github.com/valkey-io/valkey/commit/7a9951fb8093c96ceb75da2f7245a1110b614794"
    },
    {
      "sha": "0342a81b7c",
      "message": "Migrate sds.c unit tests to new test framework. (#478)",
      "date": "2024-05-09",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/478",
      "commit_url": "https://github.com/valkey-io/valkey/commit/0342a81b7c20d8a5360b18ef751c299e7303caf2"
    },
    {
      "sha": "44f273d13b",
      "message": "Delete unused declaration (#400)",
      "date": "2024-05-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/400",
      "commit_url": "https://github.com/valkey-io/valkey/commit/44f273d13bb506550c2473ac41ca00f5ca95b156"
    },
    {
      "sha": "393c8fde29",
      "message": "Rename macros in config.h (#257)",
      "date": "2024-04-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/257",
      "commit_url": "https://github.com/valkey-io/valkey/commit/393c8fde29ef848d43a9bf432d01691098fbad61"
    },
    {
      "sha": "87a5bfc002",
      "message": "Support connection schemes valkey:// and valkeys:// (#199)",
      "date": "2024-04-23",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/199",
      "commit_url": "https://github.com/valkey-io/valkey/commit/87a5bfc002ba2d97e3f74e76fe2f014332383bb9"
    },
    {
      "sha": "9c5e2bb226",
      "message": "Changes references to redis binaries in output of \"--help\", \"--version\" (#113)",
      "date": "2024-04-04",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/113",
      "commit_url": "https://github.com/valkey-io/valkey/commit/9c5e2bb226c797d1eb815cddc342d4ed19a05e1e"
    },
    {
      "sha": "e1cb4c8a8b",
      "message": "Rename #include guards (#167)",
      "date": "2024-04-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/167",
      "commit_url": "https://github.com/valkey-io/valkey/commit/e1cb4c8a8bccfd62cdf76c40a7804110d336d039"
    }
  ],
  "review_list": [
    {
      "sha": "3b25c4d6b8",
      "message": "Optimize scan/sscan/hscan/zscan commands by replacing list with vector (#2160)",
      "date": "2025-06-17",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2160",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3b25c4d6b88a9050166ec6e040088ddb87fd1563"
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
      "sha": "91f6c97379",
      "message": "Compile with -Wundef (#2025)",
      "date": "2025-05-05",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/2025",
      "commit_url": "https://github.com/valkey-io/valkey/commit/91f6c973797c61e932206434e6527c22355aee4b"
    },
    {
      "sha": "dd772c490e",
      "message": "Hyperloglog ARM NEON SIMD optimization (#1859)",
      "date": "2025-05-01",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1859",
      "commit_url": "https://github.com/valkey-io/valkey/commit/dd772c490ed7798e2ec95b8ec973c69d961c8ad0"
    },
    {
      "sha": "3df609ef06",
      "message": "Optimize PFCOUNT, PFMERGE command by SIMD acceleration (#1293)",
      "date": "2024-12-02",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/1293",
      "commit_url": "https://github.com/valkey-io/valkey/commit/3df609ef06f71c37a45049ec1df9611b9f763d55"
    },
    {
      "sha": "417660449f",
      "message": "Adjust sds types (#502)",
      "date": "2024-06-03",
      "repo": "valkey",
      "pr_url": "https://github.com/valkey-io/valkey/pull/502",
      "commit_url": "https://github.com/valkey-io/valkey/commit/417660449f9c1fce998e1563f30f7bfd9cb5197f"
    }
  ]
}
---
