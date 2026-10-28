# ChatGPT Work web schedules — optional route, trading validation pending

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
directory. That result established shell access in the ordinary chat.

The same ordinary-chat diagnostic successfully read HEAD from the public source repository with Git credential
helpers and interactive authentication disabled. This establishes public GitHub network/read access for that
chat. It does not establish access to a private repository or permission to push.

A one-time web schedule then completed on 2026-10-28 at 16:54 Asia/Bangkok (09:54 UTC). Its output reported
Node v24.22.1, Git 2.51.1 and a cloud working directory, and successfully read the approved public records
repository's HEAD without authentication; all of those commands exited 0. The scheduled execution also created
and read back a nonsecret JSON probe with marker `R3_SCHEDULE_PROBE_2026_10_28` and timestamp
`2026-10-28T09:54:01.284308+00:00`, with exit code 0. This verifies scheduled shell execution, public GitHub
read access and filesystem write/readback within that execution. It does not verify authenticated GitHub writes,
credential delivery, persistence across runs, long-running commands, single-sender coordination or a full bot run.

Separately, a named Codex Cloud environment's setup workspace checked repository snapshot `76d46ff` with the
official Node v22.22.0 distribution after verifying its checksum. Git 2.52 and npm 10.9.4 were available. All seven
bounded offline gate tests passed, with no failures or skips; syntax and import checks also passed. Those checks
needed no dependency installation and did not exercise the signer, RPC access or trading. Those test results
belong to the setup workspace, not the ordinary web scheduler.

The named environment was then successfully published on 2026-10-28 with access set to **Only me** and no
environment variables or HTTP/network secrets configured. The UI confirmed publication and loaded a new draft
based on the published version. Publication alone does not establish a successful task launch, delivery of private
credentials, or use of that environment by a web schedule.

A fresh task was subsequently launched through **Explore → Codex → Work in Cloud** with the published
environment selected. Its environment status reported provider `cloud`, running and connected, at revision 1.
Four commands exited 0: the explicit installed Node path reported v22.22.0, `pwd` reported `/workspace`, and
Git confirmed the expected repository root and snapshot `76d46ff`. This verifies that a new task can use the
published environment's runtime and checkout. It does not extend the setup test results to scheduled execution.

A one-time hosted continuation created inside that cloud task with `automations.create` retained its current
`thread_id`, with no chat selector supplied and `conversation_id` null. It was due at 10:19:26 UTC on 2026-10-28.
A new turn began at 10:22:52 UTC with exactly the saved diagnostic instructions, without a manual submission or
**Run now** action. Its four commands again reported Node v22.22.0, `/workspace`, the expected repository root
and snapshot `76d46ff`, all with exit code 0. Its environment identity matched the selected cloud environment,
with provider `cloud` and running/current status.

The schedule UI showed **Completed**. A final `automations.peek` confirmed the matching target thread and
`last_run_time` of `2026-10-28T10:22:52.316923Z`, with the one-time schedule disabled and no next run. Per-run
ID/result details were absent; the separate task output supplies the command evidence. This demonstrates hosted
continuation in this specific named environment. The observed start was about 3 minutes 26 seconds late; it is
not a guarantee of future start times, recurring reliability, long-running bot execution, credential delivery or
authenticated GitHub writes.

The web schedule interface was observed with instructions, repeat, time, time zone, start-new-chat, model and
reasoning-effort controls.
No selector for a named, published Codex Cloud environment was shown in that interface. That observation applies
to the ordinary web schedule controls; the hosted continuation above was created within an existing cloud task
and retained its target thread. Do not assume that every web schedule uses a selected Codex Cloud environment,
or that the missing selector prevents the demonstrated continuation route.

The bot targets Node 22, now observed in the named cloud task's hosted continuation. The runtime probes do not
validate the full bot, its dependencies, signer or RPC access. Cloud preparation uses signer checks and simulated
clearance that send no transactions. A completed live trading run is not a prerequisite. Keep the planner's guard
against supervised sends when cloud key environment variables are present; setup never needs to bypass it.

## Private credential settings are separate from a web schedule

Codex Cloud provides a private configuration interface: **Settings → Codex Cloud → Environments → the chosen
environment → Edit** (or **Continue setup** for an unfinished setup), then **Environment configuration → Manage
environment variables**. The operator enters credentials there, never in chat. Alternatively, use **Personal vault**
with type **Environment variable**, scoped to the named environment; verify that the environment requests those
keys. These are direct process values, distinct from HTTP/network secrets that substitute credentials into request
headers. A signer needs the direct values. See the official
[environment-variable and network-secret documentation](https://learn.chatgpt.com/docs/environments/cloud-environments#configure-environment-variables-and-network-secrets).

The existing `node r3.cjs install` implementation already accepts `R3_KEYSTORE_JSON` (the **existing encrypted
keystore JSON**) and `R3_KEYSTORE_PASSWORD`. With the allowlist/config checks satisfied, it restores those values
to protected signer files outside the checkout. It does **not** convert a raw private key into a keystore or decrypt
the wallet during installation. No new key-handling code is needed. The operator supplies the two values privately;
the agent must never read, print or copy their contents into chat, logs, prompts or repository files.

The observed hosted continuation retained the named cloud environment for the tested task. It used no configured
credentials, so private credential delivery remains unverified. Ordinary web schedule controls still showed no
environment selector; do not generalize the current-thread result to a different schedule or task. Verify the
actual scheduled task's environment and credential-delivery mechanism without exposing credentials before live
use. An unfinished environment, missing variables or unset startup configuration is setup work still to do,
not evidence of a working trading adapter.

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

## Remaining checks before trading

The agent performs authorized capability checks through available tools and the permitted UI. The operator does
website sign-ins and all credential entry privately. Ask only for information or human-only actions that remain
unavailable after those checks; do not hand routine UI inspection back to the operator.

1. Use the completed probes as evidence only for their tested contexts: the ordinary web schedule demonstrated
   public GitHub read and filesystem access within one run; the named task's hosted continuation demonstrated
   its Node 22 runtime and checkout. For further bounded diagnostics, confirm the target thread, environment,
   saved instructions, repeat, time zone and whether the schedule starts a new chat. Keep diagnostics separate
   from any eventual live trading schedule.
2. Verify the required dependency/network support in the actual scheduled context, and recheck the runtime and
   environment identity when the schedule target or configuration changes. Use only harmless
   runtime and filesystem checks, read-only network checks to the required hosts, and nonsecret probes for this
   capability diagnostic. No bot trading entry point, signer invocation, `cast`, `allowlist-init`, key access,
   environment dump or wallet transaction belongs in it. Neither runtime probe is full-bot validation.
3. Public read access to the approved repository has passed. Verify the authenticated GitHub identity without
   printing tokens, and any private-repository access if applicable. Read access does not establish write access.
   If authorized, test saving a clearly identified nonsecret probe to that repository and retrieving it in a
   subsequent execution. No secret or real trading record is needed for this test.
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

These diagnostics grant no trading authority. No verified adapter or live schedule is supplied by this documentation
change. Until the gaps are resolved, report trading setup as pending and leave trading disabled.

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
