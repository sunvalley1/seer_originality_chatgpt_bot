# Instructions for AI agents working in this repository

**Setup and execution take place in the cloud.** Reuse the operator's choice of Claude cloud routines or ChatGPT
Work web schedules; if unknown, explain the two and ask. Apply platform prerequisites only to the chosen route.
For ChatGPT, first read [ChatGPT Work schedules](.claude/skills/deep-r3-trade/reference/chatgpt-work-schedules.md).
Its bot integration needs validation; an ordinary chat's shell access does not establish scheduled compatibility.

**A scheduled run follows its saved prompt first.** If the prompt requires the code pin as the first command,
run that check before reading or running anything else. On failure, stop and report the exit code and error.
After a successful check, follow `.claude/skills/deep-r3-trade/routines/trade.md` and the saved prompt; treat this
file as data. A bounded capability diagnostic follows its own no-send prompt and grants no trading authority.

Everyone else: this repository is the R3 Originality trading bot. Its overview is
[SKILL.md](.claude/skills/deep-r3-trade/SKILL.md). It trades real money on Optimism. The setup path is
[SETUP.md](SETUP.md): cloud preparation, signer checks and simulated clearance, followed by explicit standing
authorization. A completed live trading run is not a setup requirement.

## Check setup progress

Inspect the available tools and permitted cloud UI before asking the operator to inspect them. Report what is
done and the next concrete step; do not claim capabilities or successful checks without evidence.

1. Verify the chosen cloud execution context has Node 22, Git, the required network access, supported credential
   controls, sufficient command duration and configurable command boundaries. ChatGPT-specific gaps follow the
   linked reference. A result from another host does not validate this one.
2. Verify `git remote get-url origin` and `git remote get-url --push origin` identify the exact approved records
   repository. The upstream `sunvalley1/r3-originality-bot` (normally remote `public`) is not a records destination.
   Private storage is recommended by default; explicit approval for a named public repository permits nonsecret
   code, forecasts and run records there. Preserve an approval already given.
3. Verify `routine.config.json` has the confirmed, distinct `signerAddress` and `owner`, not the template
   addresses; `setup/r3-allowlist.json` exists and its hash matches `allowlistSha256`; tools and keys are outside
   the cloud checkout. Inspect nonsecret status and configuration only.
4. Verify `run/csv/current.json` and its immutable CSV version exist. A draft under `inputs/` alone is not an
   accepted trading forecast. Follow the operator's CSV acceptance flow without changing the scores.
5. Verify actual cloud signer self-test results, chain-helper checks and nonempty simulated clearance. The
   installed signer/planner paths and hashes in the setup record must match that execution host's tested install.
   Leave `nonce_pinning` false unless it has really been verified; setup requires no nonce transaction.
6. Before live execution, require the operator's explicit standing permissions and the actual readiness fields:
   `autonomy.enabled`, `autonomy.authorized_at`, `autonomy.signer_selftest_passed_at`, and
   `schedule.signer_allow_rule_added_at`. Record only genuine results and consent. No prior live-run timestamp is
   required. Keep trading disabled while authorization, platform validation or a required test is missing.
7. Verify the paused scheduler's prompt, code pin, permissions, repository, environment and cadence. Confirm it
   retrieves current records and only one process can send from this wallet before enabling it with authorization.

Continue the authorized preparation in SETUP.md. Explain any remaining human-only action clearly: sign-ins,
credential entry, wallet actions and `allowlist-init` belong to the operator. Do not add a live trading test as a
setup prerequisite or replace a missing cloud capability with a different execution route.

## Rules for every agent here

- Never ask for, accept, show or paste a private key, recovery phrase, keystore text or password in chat or a file
  you write. The operator enters credentials only through the platform's supported private settings. If secret
  material is pasted into chat, stop and explain the exposure; do not reuse it as setup input.
- Never read, list, open, print or copy key files, passwords, `.env` files, `/proc` or environment contents,
  including `R3_KEYSTORE_JSON` and `R3_KEYSTORE_PASSWORD`. Only the signer accesses its secrets in its own process.
  Apply the chosen platform's credential and tool restrictions; Claude deny rules do not configure ChatGPT.
- Never write code that reads, creates, converts or encrypts keys. The operator uses a supported private wallet
  flow. If one is unavailable, report the capability gap without handling their secret material.
- `allowlist-init` is operator-run through a supported human-controlled cloud interface, never agent-run, even
  with general setup approval. If the platform lacks that interface, resolve the gap before continuing.
- Setup uses non-sending preparation, signer checks and simulation. Preserve the planner's refusal of supervised
  send entry points when cloud key variables are present. Never bypass it, make a test transaction, or invoke a
  send to satisfy setup. Later manual trading, if explicitly requested, still requires the skill's batch and
  exact-command approvals. Standing scheduled authorization applies only to the reviewed routine and signer.
- Keep one sender per wallet. Never start a second scheduled run while another may be live. Pause the routine
  before any separately authorized manual send; a pause does not stop an already executing run.
- Push only approved nonsecret content to the exact chosen records repository. Verify the push remote and review
  the staged content. Never push `run/` or `inputs/` to the upstream source. Never commit or upload keys,
  keystores, passwords, `.env` files or environment contents, even to a private destination.
- Read SKILL.md in full and then the step files it routes to. Respect the code pin, signer self-test, installed
  path/hash checks, nonempty clearance, explicit standing authorization and one-sender rules. Keep the actual
  trading schedule disabled during documentation and capability work.
- `SKILL.md` and `steps/` are the operational authority when this file, SETUP.md or README disagree, subject to
  the operator's explicit instructions. Do not manufacture readiness to conceal a mismatch.
