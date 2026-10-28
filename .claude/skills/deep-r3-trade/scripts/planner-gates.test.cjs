'use strict';

// Offline authorization regression checks. No signer, RPC or wallet is invoked.
const test = require('node:test');
const assert = require('node:assert/strict');
const { gateProblems } = require('./planner/exec-core.cjs');

function authorizedCloudSetup() {
  return {
    autonomy: {
      enabled: true,
      authorized_at: '2026-10-28T00:00:00Z',
      signer_selftest_passed_at: '2026-10-28T00:00:00Z',
    },
    schedule: { signer_allow_rule_added_at: '2026-10-28T00:00:00Z' },
  };
}

test('cloud setup can pass authorization without a previous live run', () => {
  assert.deepEqual(gateProblems(authorizedCloudSetup()), []);
});

test('legacy first-run history neither blocks cloud setup nor grants authority', () => {
  assert.deepEqual(gateProblems({ ...authorizedCloudSetup(), first_successful_run: null }), []);
  const revoked = { ...authorizedCloudSetup(), first_successful_run: { run_id: 'legacy' } };
  revoked.autonomy.enabled = false;
  assert.deepEqual(gateProblems(revoked), ['autonomy.enabled is not true']);
});

test('missing setup still blocks autonomous operation', () => {
  assert.deepEqual(gateProblems(null), ['run/setup.deep-r3-trade.json does not exist']);
});

for (const [section, field, expected] of [
  ['autonomy', 'enabled', 'autonomy.enabled is not true'],
  ['autonomy', 'authorized_at', 'autonomy.authorized_at is null'],
  ['autonomy', 'signer_selftest_passed_at', 'autonomy.signer_selftest_passed_at is null'],
  ['schedule', 'signer_allow_rule_added_at', 'schedule.signer_allow_rule_added_at is null'],
]) {
  test(`cloud setup still requires ${section}.${field}`, () => {
    const setup = authorizedCloudSetup();
    delete setup[section][field];
    assert.deepEqual(gateProblems(setup), [expected]);
  });
}
