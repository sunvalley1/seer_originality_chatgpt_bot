# R3 cloud repair checks

Push an actual patch to `r3-repair/<stable-id>` and open or update its pull request to `main`.
The pull request runs `.github/workflows/r3-repair-tests.yml` in GitHub Actions; a branch push
without a pull request does not trigger it. An explicit workflow dispatch is also supported.
New commits cancel obsolete runs for the same pull request; a canceled run is never a pass.
There is no duplicate push-triggered test matrix. The workflow has read-only repository
permission, no deployment step, no secret inputs and no production wallet or runtime access.

Every job uses the pinned official Node 22.22.0 image and `npm ci --ignore-scripts` with the
committed ethers 6.17.0 dependency lock. Candidate tests run in a separate, read-only Docker
container with `--network none`, no host environment or `.git`, and only temporary scratch
space. Loopback mock RPC servers remain available; the public chain is unreachable.

All 13 jobs below are required. The planner README records full offline runs lasting
3,579-7,091 seconds, so its complete suite runs in eight parallel shards using the existing
`--only` sections. Each job retains the same isolation and 2 CPU/4 GB limits, with a 60-minute
timeout ceiling. Sharding reduces elapsed time; it does not skip or shorten test cases.

| Job (`Offline ` prefix in Actions) | Coverage |
| --- | --- |
| `gates` | All `planner-gates.test.cjs` tests |
| `planner-core` | `static,usage,lib,repair,nonce-confirm` |
| `planner-pipeline` | `pipeline,g-safety,exec-safety` in one job; the latter two require the pipeline snapshot |
| `planner-c-variants` | `c-variants` |
| `planner-boundary` | `boundary,mergearb` |
| `planner-wake` | `wake`, including `wake-afford`, `wake-halfdone`, and `wake-replan` |
| `planner-ramp` | `ramp` |
| `planner-recovery` | `recovery` |
| `planner-cap` | `cap`, including the complete 306-transaction synthetic sequence |
| `routine` | All `routine.test.cjs` sections |
| `helper` | All `chain-helper.test.cjs --offline` tests |
| `signer` | All `signer.test.cjs` tests with throwaway fixture wallets and loopback RPC |
| `nonce-regression` | Original-code failure followed by candidate success for `nonce-confirm` |

The runner checks that its shard mapping covers every selector in `planner.test.cjs` exactly
once. Adding or removing a selector fails that check until the mapping is updated. Each shard
also executes the harness's final JSON/exit contract assertion and maximum-20-flagged-calls
assertion over all calls made by that shard; together those assertions cover the complete suite.
The `wake` section has its own CSV fixture when invoked independently, as supported by the harness.
The standalone nonce regression deliberately repeats the targeted candidate section after
proving that the original implementation fails it.

The `nonce-regression` job demonstrates the stale-nonce regression
against commit `4ea4b38b39b30ffb953510c56847d32d7474d9f1`: the specific assertion must fail on
the original modules and pass on the candidate. A generic setup error does not count as proof.
The original code fixture is retained only for this regression; other fixes need their own
reproducing regression and relevant full-suite coverage.

Each job retains nonsecret logs and a manifest for 14 days, including the exact candidate
commit, tree outside `run/`, source hashes, dependency-lock hash, image digest and test outcome.
An agent must read completed job results for the exact candidate commit, not merely a green
result on an older branch head. Authored tests, queued jobs and missing/skipped jobs are not passes.
Persist the successful workflow URL and exact manifest hashes in the repair record before
artifact expiry. Do not commit generated test wallets, scratch files or their contents.

These checks supply the previously missing secret-free test worker. They do **not** install,
merge, change source pins or authorize a trade. The durable trading task remains the sole
promoter: use its verified maintenance guard, wait for prior senders to exit, review the exact
patch, preserve all run records, refresh every affected validation and pin, and leave the
maintenance occurrence non-trading. A planner/module change still needs genuine nonempty cloud
clearance before the guard can be cleared. Trading stays on the existing 09:00/21:00 UTC schedule.

The hourly monitor should implement a minimal patch and regression on the stable repair branch,
open/update its pull request, then inspect all 13 workflow jobs and their artifacts.
Repeated post-receipt nonce-read mismatches must
trigger evidence-based diagnosis and regression work, not be dismissed indefinitely as merely
an open financial state. Existing pending/uncertain transactions still block sending, and a
repair never permits replaying a confirmed transaction or weakening nonce, price or safety checks.
