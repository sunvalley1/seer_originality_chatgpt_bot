# R3 Originality trading bot

A bot that trades the 98 **Deep Funding Round 3 "Originality"** prediction markets on
[deep.seer.pm](https://deep.seer.pm) (Seer, on the Optimism chain). Each market asks for one GitHub repo's average
originality score (0 to 100), and you can buy UP or DOWN on each one.

**Setup and scheduled runs take place in the cloud.** The skill lives in
`.claude/skills/deep-r3-trade/`. Choose **Claude Code cloud routines** or **ChatGPT Work web schedules**;
neither route requires the other. [SETUP.md](SETUP.md) covers the cloud setup and its checks. This workflow has no
laptop installation, local scheduler or required first live trading run. The first setup run performs the signer
policy self-test, planning checks and simulations without sending transactions. Live operation still requires
explicit standing authorization after those checks pass.

The ChatGPT route needs [bot compatibility validation](.claude/skills/deep-r3-trade/reference/chatgpt-work-schedules.md)
before live use. A regular ChatGPT chat has demonstrated a shell with Node.js 24.22.1, Git 2.51.1 and public GitHub
read access. That does not verify scheduled execution, authenticated repository writes, key provisioning, command
duration, or this bot's compatibility with that runtime. No complete ChatGPT trading integration is claimed.

**The forecast is a CSV you provide** (`steps/D-forecast.md`, `steps/D-methods/csv.md`), in the format of
deep.seer.pm's upload: trading through the bot is then trading through the interface, every day. Other ways to
forecast, such as an AI researching each repo, a model or a pool of forecasters, are yours to build as a change to
step D; the bot does not include them.

> **Strategy write-ups wanted.** Seer will open write-ups on trading strategies built on this bot, with **$1,000 for
> the best one**. Running the base bot unchanged doesn't qualify: change a step (`.claude/skills/deep-r3-trade/steps/`)
> and show what it did.

Each run does the following:

1. **Forecast.** It takes your stored CSV. A market with no forecast gets no directional trade.
2. **Compare and size.** It takes the forecast at face value and buys wherever it beats the pool price, until the
   edge or your treasury runs out. Thin pools mean small trades: runs so far moved between about 15 and 100 sUSDS.
3. **Trade.** It mints, trades, merges and redeems through a **signer that only signs calls on its allowlist**.
4. **Report.** It writes everything under `run/<run-id>/`, including `report.md`.

> Real money, experimental software. Use a wallet made only for this bot, and fund it with what you can afford to lose.

## What's in this repo

| Path | What it is |
|---|---|
| `.claude/skills/deep-r3-trade/` | The skill: `SKILL.md` (overview), `steps/` (steps C to I), `routines/` (what the trading routine's agent does), `scripts/` (planner, chain helper, signer, the routine runner, and their tests) |
| `.claude/skills/seer-trade/`, `seer-protocol/`, `evm-onchain/`, `wallet-setup/` | Supporting skills: the reasoned arm for other Seer markets, how Seer works onchain, Optimism addresses and gas, the encrypted-wallet tool |
| `r3.cjs` | The cloud runner: `node r3.cjs install`, `trade`, `clearance`, `selftest`, `status`, and `planner <subcommand>` for interactive setup checks |
| `routine.config.example.json` | The template of `routine.config.json`: your wallet, your own address, the signer's allowlist |
| `tools/` | Read-only helpers: book status, an independent second-RPC check, who swapped in our pools |
| `scope/r3-originality.json` | A human-readable list of the 98 markets |
| `setup/signer.config.json` | The original machine's signer config, kept as an example |

**Not in the upstream source repo:** `run/` (trade records, stored CSVs, the setup record), `inputs/` (your CSV drafts),
and any key or password. Keep records in **your own trading repository**. Private visibility is recommended;
an explicitly chosen public records repository is also supported, with forecasts and records visible to everyone.
Keys, keystores, passwords and environment dumps never belong in either kind of repository.

## Your forecast

Two columns, the same format as deep.seer.pm's upload:

```csv
repo,originality
https://github.com/ethereum/py_ecc,0.62
https://github.com/paradigmxyz/reth,
```

- The repo is its GitHub URL (or `owner/repo`), spelled exactly as on deep.seer.pm.
- `originality` is the score you expect divided by 100, from 0 to 1. A blank cell means you have no view: that market
  gets no directional trade, while the forecast-free arbitrage still runs.
- Make it however you like: by hand, in a spreadsheet, with your own research or with an AI. The bot only reads it.

Supply it, or a new version, to the chosen cloud setup session. Put the provided file under `inputs/` in its
trading checkout after syncing the approved repository state. Git ignores drafts in `inputs/`:

```bash
node r3.cjs planner c <run-id>
node r3.cjs planner d <run-id> --supply inputs/my-forecast.csv
node r3.cjs planner d <run-id> --supply inputs/my-forecast.csv --continue
```

The second command reports how many rows matched a market, which did not, and which markets have no forecast, and
stores nothing. The third stores it as the next version under `run/csv/` (a version is never overwritten), and every
later run uses it, once pushed, until you supply another. A run-id is any new name in the form `2026-10-23T0300Z`
(UTC). A new file replaces the old one whole: a market missing from it gets no new trades.

The trading routine works on a fresh clone of your trading repository, so it only sees a new version once you push
it (if the push is rejected because a run pushed meanwhile: `git pull --rebase`, then `git push`):

```bash
git add -f -- run/csv
git commit -m "csv: new version"
git push
```

**Another way to forecast** is a change to step D, and yours to build. Keep D's contract (`steps/D-forecast.md`: what
it reads, the `base-forecast.json` it writes, its checks and rules), and the rest of the bot runs unchanged on it.
Change one thing per run, dry-run it first (`node r3.cjs clearance`, which sends nothing), and run anything that reads
web pages outside your trading repository.

## How it fits together

Three tools are installed **outside** the project folder, and each one refuses to run from inside it:

- **Chain helper** (`chain-helper.cjs`): reads the chain and the Seer data function, and simulates transactions. It never signs.
- **Signer** (`signer.cjs`): the only one of the three tools that signs. It decrypts the wallet only inside its own process, only for
  calls on its allowlist (the Seer Router, Uniswap's SwapRouter02 for these markets' pools, and PSM3), and can sweep
  funds only to your `owner` address.
- **Planner** (`planner.cjs` and `planner/`): runs steps C to H, calling the helper for every read and the signer for every send.

`node r3.cjs install` lays all three down from this repo, with their configs, and reports whether the planner and the
signer match the paths and hashes your setup record pins. `node r3.cjs trade` refuses to run (exit 4) unless the
setup record pins exactly the planner and signer `install` laid down; it never runs a path the record names instead.

A scheduled run is the **trading routine**. Its agent first checks that the code is still the commit its prompt pins
(below), then runs `node r3.cjs install`, then `node r3.cjs trade --push`, which:
1. reads the setup record, takes the lock and checks the planner's and signer's paths and hashes against the record;
2. runs the planner's `wake`, which repairs anything an earlier run left unfinished; selects the markets (C); takes the
   forecast (D) and sets it beside the prices unchanged (E); converts any USDC to sUSDS (PSM3); sizes the positions (F),
   builds the plan (G) and sends it (exec); merges and redeems settled positions (Half B), then scores them (H);
3. writes `run/<run-id>/report.md`, and commits and pushes the run's records (`run/` only) to the trading repository.

**Your trading copy.** You keep one copy of this repo, the **trading repository** (private by default, or public
when you explicitly choose to publish forecasts and records): the code,
`routine.config.json`, `setup/r3-allowlist.json` and the run records in `run/`. Only you and the trading routine (with
its one-off setup run) use it, and the routine pushes `run/` only. The trading routine attaches it alone, and its
session starts inside that clone.

Why only you and the routine push to it: when a session starts, before the agent's first command, Claude Code loads
what the repository holds: the clone's `.claude/settings.json` (permission rules, hooks, environment) and `.mcp.json`,
and its `CLAUDE.md`, `.claude/rules/`, `.claude/skills/`, `.claude/agents/` and `.claude/commands/`. The code pin
(below) cannot cover any of it. A hook pushed into the trading repository would run where the key is, before any
check, and a `CLAUDE.md` or a skill reaches the agent as instructions. So whoever can push to the trading repository
controls the key.

**The code pin.** The trading routine's prompt, stored in the chosen scheduler and not in the repo, pins the code of one commit by
its tree fingerprint: the git tree of everything outside `run/`, which `git ls-tree <commit> | awk -F '\t' '$2 != "run"' |
git mktree` prints in a POSIX shell on the cloud worker. The agent's first command, in the
trading clone, is:

```bash
test "$(git ls-tree HEAD | awk -F '\t' '$2 != "run"' | git mktree)" = <pinned tree>
```

Exit 1 means the fingerprint does not match: either the code differs from the pinned tree, or git could not compute
it (git then prints an error, for example outside the trading clone). Either way the agent stops, reports the exit
code and any error, and reads and runs nothing else. The check needs no history: the routine's
clone is shallow, and every run pushes its records as about two hundred commits (a checkpoint every 20 seconds), so a check
that looks up the pinned commit itself (`git diff <commit> HEAD`) fails with "bad object" a run or two later.
Everything outside `run/` is pinned: the code, `routine.config.json`, `setup/` with the allowlist, `routines/*.md` and
the skill's steps. The pin cannot cover what Claude Code loads at session start (above): that is why only you and the
trading routine push to that repository. `run/` is not pinned: it holds the records, the stored CSVs and the setup
record, whose consent fields and pins steer the run. After any change outside `run/`, clear the new commit and update
the pin (*Running and checking it*).

## Setting it up

**Follow [SETUP.md](SETUP.md), step by step, in the chosen cloud environment.** The agent performs the approved
setup checks; you control account logins, wallet funding, secret entry and trading authorization.

0. Choose Claude cloud or ChatGPT Work web. Verify that route can execute the bot, use its required Node/Git
   runtime, receive credentials without exposing them to chat, persist records to GitHub and run long enough.
1. Connect your **trading copy** of this repository to that route. Use private visibility unless you explicitly
   choose public forecasts and records. The Claude GitHub app is needed only for the Claude route.
2. Configure the platform's key protections. You supply the dedicated wallet's encrypted keystore and password
   through its protected settings; never through chat or Git. Confirm the public bot and owner addresses.
3. Configure and install the tools in the cloud. Initialize and verify the signer's allowlist through the
   operator-controlled setup path, record its sha256, and verify the actual cloud install's paths and hashes.
4. Supply and approve the CSV. Run the signer policy self-test and the no-send planner clearance, including
   simulation. **No previous live trade or supervised trading run is required.** Failed or empty checks do not
   count as passed; fix their cause before proceeding.
5. Persist the approved configuration, forecast store and setup evidence to the chosen trading repository.
   Exclude keys, passwords, environment dumps and the active lock.
6. Configure the chosen cloud environment's network and credentials. If that platform cannot provide the required
   controls, leave it unconfigured rather than substituting the other route or a laptop workflow.
7. Create a paused schedule using a supported management surface for the chosen route. Verify its fixed prompt,
   exact code pin, tool permissions, repository access, timeout and prevention of overlapping runs. An ordinary
   chat's shell test does not prove a scheduled task has the same capabilities.
8. Record the passing cloud self-test and clearance against that install's exact paths and hashes. Explain the
   full-balance strategy and obtain the explicit standing trading and signer authorizations before enabling the
   schedule. These checks and authorizations replace a required first live run; they do not prove future trades
   will succeed or earn money.
9. Inspect the first authorized scheduled run's report and saved records. Confirm what happened from the report,
   rather than the scheduler's success indicator alone.

`steps/I-setup.md` defines the wallet, signer, authorization and setup checks. The ChatGPT route's current evidence
and remaining integration checks are in [its reference](.claude/skills/deep-r3-trade/reference/chatgpt-work-schedules.md).

## Running and checking it

- **What happened:** each run's session is listed under the routine, with the agent's report as its last message.
  In your trading repository, read the newest `run/<run-id>/report.md` and `wake-status.json`, or `node r3.cjs status`.
- **Change your forecast:** supply a new CSV version (*Your forecast*, above).
- **Change the code or the config:** anything outside `run/` (a step, `routine.config.json`, the allowlist) is
  pinned. Review the new commit, including any `.claude/`, `CLAUDE.md` or `.mcp.json` file it adds or changes (the pin
  cannot stop those at session start), and push it. Make a setup run with the new commit's tree fingerprint in its prompt (SETUP.md step 6). If
  `planner.cjs` or `signer.cjs` changed, record the new paths and hashes its `install` printed in the setup record; a
  changed signer also needs the self-test's pass and the second question again (`steps/I-setup.md` I.2 §1). Commit
  `run/`, then put the new commit's tree fingerprint in the trading routine's prompt and in its pin-check tool entry
  through the chosen route's supported management surface. Verify that it updates tool permissions as well as
  the prompt. Until you do, the trading run stops at its pin check.
- **Update from an install made before 25 Oct 2026:** delete `forecastImport`, `planner.forecastMethod` and
  `planner.forecastMaxAgeHours` from your `routine.config.json`. The forecast-file method and its research routine
  were removed from the base skill; `install`, `trade` and `clearance` refuse a config that still holds those keys and
  name the one to delete.
- **Pause:** turn the routine off in the chosen cloud scheduler, and set `autonomy.enabled` to false in `run/setup.deep-r3-trade.json`
  and push it. Neither stops a run already in progress. Removing the two key variables from the trading environment
  stops new runs from getting the key. It does not reach a past run: its VM pauses with its files saved, the key files
  `install` wrote among them, and continuing its session can restore it. Never continue a trading run's session.
- **One sender at a time:** pause the schedule and confirm no run is live before any other authorized cloud run
  can send. `r3.cjs`'s lock lives in one clone, so it does not stop separate cloud sessions from sending at once.
  Never Run now while a scheduled run is live.
- **Status of the book** (read-only): `node tools/r3-status.cjs run/<run-id> <from-block>`.
- **Tests**, from `.claude/skills/deep-r3-trade/scripts/`, with `NODE_PATH` pointing at a `node_modules` folder that
  holds `ethers` 6.17.0. The planner suite takes 50 to 120 minutes. The signer and chain helper suites are
  `signer.test.cjs` and `chain-helper.test.cjs`.

  ```bash
  node planner.test.cjs --dir <scratch folder>
  ```

`tools/*.cjs` carry the original machine's `ethers` path and wallet in their first lines; change them to yours.

## Safety rules

- Never put a private key, keystore or password in any repository or a chat. The operator configures the chosen
  cloud platform's credential mechanism; `install` writes the signer's key files outside the project. Verify that
  route's protections before using it. For Claude routines, auto mode sends commands on neither tool list to a
  classifier, and a `Read` deny rule does not cover shell reads. Do not assume ChatGPT has the same controls.
  A network allowlist does not stop a leaked key from being used: an allowed RPC can broadcast a transfer signed
  with it. Restrict repository writers and what loads at session start, pin reviewed code, retain the runner's
  gates and signer allowlist, and protect the chosen platform and GitHub accounts. The signer also loads `ethers`
  6.17.0 and its npm dependencies. Its allowlist bounds signer calls, not a leaked key. Keep in the bot wallet only
  what you accept to lose.
- Use the trading environment for the trading routine alone. Start no other session in it, and never continue a
  trading run's session.
- Never give anything that reads web pages push access to the trading repository.
- Use a wallet made only for this bot, and fund it with what you can afford to lose.
- Run one copy of the bot per wallet. Two machines or routines sending from the same wallet clash on nonces, and
  `r3.cjs`'s lock covers one machine only: turn off any other scheduler or machine first.
- Keep `run/` and `inputs/` out of the upstream source repository: they hold your trade history and forecasts.
  Push them only to the exact trading repository you selected, including a public one only after your explicit
  choice to publish those records. Check the remote before every upload.
- The skill text (`.claude/skills/deep-r3-trade/SKILL.md` and `steps/`) is the authority whenever this README and the skill disagree.
