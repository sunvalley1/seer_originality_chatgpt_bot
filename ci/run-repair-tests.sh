#!/usr/bin/env bash
# Runs only inside the workflow's secret-free, network-isolated test container.
set -euo pipefail

test "$(node --version)" = v22.22.0
node -e 'if (require("ethers").version !== "6.17.0") throw new Error("wrong ethers version")'
test "${R3_KEYSTORE_JSON+x}" != x
test "${R3_KEYSTORE_PASSWORD+x}" != x
test ! -e /repo/run
test ! -e /repo/.git
node -e 'if (Object.values(require("node:os").networkInterfaces()).flat().some(a => !a.internal)) throw new Error("test container has external network access")'

case "${1:?suite required}" in
  gates) node --test planner-gates.test.cjs ;;
  planner) node planner.test.cjs --dir /tmp/planner-tests ;;
  routine) node routine.test.cjs --ethers-from /deps/node_modules --dir /tmp/routine-tests ;;
  helper) node chain-helper.test.cjs --offline ;;
  signer) node signer.test.cjs --dir /tmp/signer-tests ;;
  nonce-regression) node planner.test.cjs --only nonce-confirm --dir /tmp/nonce-tests ;;
  *) printf 'Unknown suite: %s\n' "$1" >&2; exit 2 ;;
esac
