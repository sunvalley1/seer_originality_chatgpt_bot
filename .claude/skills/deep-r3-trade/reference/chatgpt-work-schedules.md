# ChatGPT Work web schedules — optional route, validation pending

Use this reference when the operator chooses ChatGPT Work web schedules. The proposed integration uses cloud
execution and the operator's approved GitHub repository for forecasts and all durable run state. The operator
supplies the forecast CSV; the bot does not invent or revise its scores. Setup and execution start in the chosen
cloud workspace. This document routes setup and validation only: it is not a live trading prompt, and it does not
authorize a send or enable a schedule. Preserve an existing choice; do not make this route the default for everyone.

Claude cloud routines are the other supported setup choice in [SETUP.md](../../../../SETUP.md) and
[I-setup.md](../steps/I-setup.md). The trading safeguards apply to both cloud choices; Claude's commands and
settings are not evidence that ChatGPT Work supports the same interface.

## What has actually been checked

On 2026-10-28, a harmless diagnostic in a regular ChatGPT Work web chat successfully ran `node --version`,
`git --version`, and `pwd`, each with exit code 0. It reported Node v24.22.1, Git 2.51.1 and a cloud workspace
directory. That proves shell access in that ordinary chat, not in a scheduled bot run.

The same ordinary-chat diagnostic successfully read HEAD from the public source repository with Git credential
helpers and interactive authentication disabled. This establishes public GitHub network/read access for that
chat. It does not establish access to a private repository or permission to push, and needs repeating in the
actual scheduled execution context.

The web schedule interface was observed with instructions, repeat, time, time zone and start-new-chat controls.
No selector for a named, published Codex Cloud environment was shown in that interface. Do not equate a ChatGPT
Work web chat or schedule with a selected Codex Cloud environment, and do not infer that a missing selector makes
all cloud scheduling impossible.

The bot targets Node 22. Verify that runtime on the actual scheduled execution host; the successful Node 24
diagnostic above does not validate the bot. Cloud preparation uses signer checks and simulated clearance that
send no transactions. A completed live trading run is not a prerequisite. Keep the planner's guard against
supervised sends when cloud key environment variables are present; the setup flow never needs to bypass it.

## Storage contract

Keep the original CSV draft under `inputs/`. Supply and accept it through D's matching report and `--continue`
flow in [csv.md](../steps/D-methods/csv.md). Preserve `run/csv/current.json`, every immutable CSV version, the
setup record and all durable run artifacts in the approved records repository. Keeping only transaction hashes
or the latest report is insufficient for recovery, merges, redemption and scoring.

Recommend a private repository by default. An operator may explicitly choose a named public destination for
nonsecret code, forecasts and run records, making those records publicly readable. Preserve an already approved
choice; do not ask for the same disclosure approval again. Verify that the push remote is that exact destination.

Use the existing reviewed record selection from SETUP.md step 5. Exclude transient locks, scratch directories and
live-session markers. Never commit or upload keys, keystores, passwords, `.env` files or environment contents.
Never push `run/` or `inputs/` to the upstream source repository; the remote named `public` is for that source,
not the operator's chosen records destination. Check that each push contains only the approved nonsecret content.

Each scheduled execution must obtain the latest approved code, CSV and records before starting, then durably save
new records. The existing `--push` option can save records to GitHub, but it does not by itself configure GitHub
credentials, retrieve the starting state, select the execution environment or prevent two independent cloud
workspaces from sending concurrently. Those pieces require a verified adapter before live use.

## Next check: a scheduled test that sends nothing

The agent performs authorized capability checks through available tools and the permitted UI. The operator does
website sign-ins and all credential entry privately. Ask only for information or human-only actions that remain
unavailable after those checks; do not hand routine UI inspection back to the operator.

1. Use the chosen schedule interface for a bounded diagnostic. Confirm the saved instructions, repeat, time zone
   and whether it starts a new chat. Keep the diagnostic separate from any eventual live trading schedule.
2. Run only harmless runtime and filesystem checks, read-only network checks to the required hosts, and a
   nonsecret probe-file write. No bot trading entry point, signer invocation, `cast`, `allowlist-init`, key access,
   environment dump or wallet transaction belongs in this capability diagnostic. Verify Node 22 and the working directory in the
   scheduled run itself; success in a regular chat is not sufficient.
3. Verify GitHub read access to the chosen records repository and authenticated identity without printing tokens.
   Read access does not establish write access. If authorized, test saving a clearly identified nonsecret probe
   to that repository and retrieving it in a subsequent execution. No secret or real trading record is needed for this test.
4. Establish the platform's supported credential-entry mechanism, which values its child commands can use, its
   network/tool boundaries, command-duration limit, and how a task resumes or reports interruption. The operator
   alone enters secrets in private settings after the mechanism is understood; never put them in chat, prompts,
   repository files or diagnostic output. Do not substitute HTTP-header secrets for values a signer must read.
5. Verify how the next scheduled run gets the latest repository state and how one sender per wallet is enforced
   across executions. A lock file in one disposable workspace does not lock a different workspace. Inspect both
   the scheduled result and the retrieved probe, then report evidence and remaining gaps.

After the capability diagnostic passes, use SETUP.md's cloud preparation to accept the CSV, build the documented
non-sending signer check cases, run the signer self-test and chain-helper checks, and obtain nonempty simulated
clearance. Verify a supported human-controlled cloud interface for the operator's `allowlist-init`; it remains
operator-run. Credential entry also remains private and human-controlled. A missing interface is an adapter gap,
not permission for the agent to take over key handling or operator-only actions.

This test grants no trading authority. No verified adapter or live schedule is supplied by this documentation
change. Until the gaps are resolved, report the cloud route as pending and leave trading disabled.

## Gates that remain required

After platform validation, require separate standing authorization, signer self-test, installed signer/planner
path and hash pins, chain-helper checks and nonempty simulated clearance. Use the actual cloud execution host's
paths and results, without assuming Claude's `/root/` paths. Review the adapter's exact commands and permission
boundaries before any authorization applies to it. Record only genuine `autonomy.authorized_at`,
`autonomy.signer_selftest_passed_at` and `schedule.signer_allow_rule_added_at`, and set `autonomy.enabled` only
with permission. No live first-run timestamp is required. Leave `nonce_pinning` false unless actually verified;
setup requires no nonce transaction.

Later manual batches and sending commands, if requested, still require their explicit approvals. The operator
handles keys, passwords, funding and `allowlist-init`. Keep one sender per wallet and pause the scheduler before
any separately authorized manual send. Preserve the code pin as the first command of any eventual trading run,
and stop on mismatch. No setup check grants standing trading authority.

## Official platform documentation

The current [Scheduled tasks documentation](https://learn.chatgpt.com/docs/automations) describes web tasks using
uploaded context and connected tools; it does not promise a persistent project folder between cloud runs.

[Codex Cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environments) describes separate
workspaces for new tasks and saved files when an existing task resumes. Its default VM-state recovery window is
up to seven days after the last turn starts or the task resumes. That is not a permanent shared transaction store,
and ordinary task changes do not update the reusable environment. GitHub is the proposed durable record store
for this integration. Recheck official guidance when validating a new platform capability; documentation and observed UI are
evidence, not proof that this particular bot has passed its checks.
