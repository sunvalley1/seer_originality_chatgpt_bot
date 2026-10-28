@AGENTS.md

This copy uses cloud setup and cloud scheduling only. The operator chooses Claude Code cloud routines or ChatGPT
Work web schedules; do not force either route, require a laptop installation, or introduce a local scheduler.
Follow [SETUP.md](SETUP.md) and the selected route's verified capabilities. ChatGPT route details and unresolved
checks are in `.claude/skills/deep-r3-trade/reference/chatgpt-work-schedules.md`.

Setup requires the signer policy self-test, no-send clearance and simulations, code pins, allowlist checks and
explicit standing trading and signer authorizations. It does not require a previous live trade or a first
supervised trading run. Keep the schedule paused until the chosen cloud route and all those checks are verified.

For the Claude route, use a supported routine-management surface that can set both the fixed prompt and its exact
allowed/denied tools. Verify those capabilities; do not assume a web chat supports `/schedule` or require an installed
laptop CLI as a workaround. The setup run is a no-send run of that routine before it is enabled. The operator alone
enters key material into the chosen platform's protected settings; never request it in chat or put it in Git.
