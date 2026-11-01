# R3 cloud repair checks

Pushing an actual patch to `r3-repair/<stable-id>` or opening/updating its pull request runs
`.github/workflows/r3-repair-tests.yml` in GitHub Actions. The workflow has read-only repository
permission, no deployment step, no secret inputs and no production wallet or runtime access.

Every job uses the pinned official Node 22.22.0 image and `npm ci --ignore-scripts` with the
committed ethers 6.17.0 dependency lock. Candidate tests run in a separate, read-only Docker
container with `--network none`, no host environment or `.git`, and only temporary scratch
space. Loopback mock RPC servers remain available; the public chain is unreachable.

The required jobs are `gates`, the complete `planner` suite, `routine`, offline `helper`,
offline `signer`, and `nonce-regression`. The last job demonstrates the stale-nonce regression
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
then inspect this workflow's jobs/artifacts. Repeated post-receipt nonce-read mismatches must
trigger evidence-based diagnosis and regression work, not be dismissed indefinitely as merely
an open financial state. Existing pending/uncertain transactions still block sending, and a
repair never permits replaying a confirmed transaction or weakening nonce, price or safety checks.
