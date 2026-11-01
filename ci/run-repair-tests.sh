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
  planner-*)
    sections="$(node - "$1" <<'NODE'
const fs = require('node:fs');
const shards = {
  'planner-core': ['static', 'usage', 'lib', 'repair', 'nonce-confirm'],
  'planner-pipeline': ['pipeline', 'g-safety', 'exec-safety'],
  'planner-c-variants': ['c-variants'],
  'planner-boundary': ['boundary', 'mergearb'],
  'planner-wake': ['wake'],
  'planner-ramp': ['ramp'],
  'planner-recovery': ['recovery'],
  'planner-cap': ['cap'],
};
// A future section must be assigned explicitly; a green partial suite is not full coverage.
const source = fs.readFileSync('planner.test.cjs', 'utf8');
const selectors = [...source.matchAll(/\bwant\(\s*(['"])([^'"]+)\1\s*\)/g)];
if (selectors.length !== [...source.matchAll(/\bwant\s*\(/g)].length) {
  throw new Error('planner selectors are no longer literal; review shard coverage');
}
const declared = new Set(selectors.map(m => m[2]));
const assigned = Object.values(shards).flat();
if (assigned.length !== new Set(assigned).size ||
    declared.size !== assigned.length || assigned.some(s => !declared.has(s))) {
  throw new Error('planner section coverage changed; update every shard mapping before testing');
}
const selected = shards[process.argv[2]];
if (!selected) throw new Error('unknown planner shard');
console.log(selected.join(','));
NODE
    )"
    printf 'Planner selectors: %s\n' "$sections"
    node planner.test.cjs --only "$sections" --dir "/tmp/$1-tests"
    ;;
  routine) node routine.test.cjs --ethers-from /deps/node_modules --dir /tmp/routine-tests ;;
  helper) node chain-helper.test.cjs --offline ;;
  signer) node signer.test.cjs --dir /tmp/signer-tests ;;
  nonce-regression) node planner.test.cjs --only nonce-confirm --dir /tmp/nonce-tests ;;
  *) printf 'Unknown suite: %s\n' "$1" >&2; exit 2 ;;
esac
