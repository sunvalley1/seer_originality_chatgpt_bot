# G gate print - run 2026-11-01T0359Z-clearance

**Optimism mainnet, holder 0x2AD670e5953a85C998cDf1C2f6D74386aB735d4a. Built, simulated and verified: nothing has been signed or sent.** Pending nonce 4363; head at G's read 158953458 (blocks are reported, never compared between reads). Every group below is an ordered sequence of single transactions, one signer call each.

## 1. The numbers

| | |
|---|---|
| **Allocation input** | `run/2026-11-01T0359Z-clearance/allocation.json` (sha256 `c43f670fb3b6348e0c5fc6709c778630ec162b9df018074274dd4875ded72665`), generated 2026-11-01T04:01:26Z, 71 rows; 61 markets traded, 0 rows skipped (section 5e) |
| **Counts per route** | pair (`dual-buy`) **4** markets (8 rows); `simple-buy` **12**; `complex-buy` **45** (43 single-side markets with spot sum > 1, plus 2 on a market whose `set-sell` runs first); `set-sell` **2**; `merge-arb` (`buy-and-merge`) **4**; mint groups **0**; PSM3 ramp: none |
| **Total sUSDS staked** | **0 sUSDS** = `totals.staked` = the new mint `M` (no parent split: the rows spend repo tokens the holder already holds). Middles split: none. Each traded market's budget is its held repo tokens plus m_X; the rows' stakes sum to 1201.0255 repo tokens of 61 different tokens (12.2554 sUSDS-equivalent at the labelled 1/98) |
| **Expected value** | **0.423046 sUSDS** at the labelled 1/N = 1/98 (F's `totals.expected_value`; 41.4585 repo tokens summed over heterogeneous markets, / 98; 0 for any repo that is not evaluated) |
| **Worst case** | `correlated_worst_case` **0.000000 sUSDS** (F's definition); a `set-sell` row's gain is locked only if its whole group lands |
| **Number of transactions** | **350** in **67** keep-whole groups (complex-buy 270, merge-arb 28, dual-buy 16, simple-buy 24, set-sell 12), nonces 4363 to 4712 |
| **Estimated gas** | **50,345,201 gas used** (mints 0; complex-buy 40,924,028; merge-arb 4,036,754; dual-buy 1,451,174; simple-buy 2,091,308; set-sell 1,841,937); sum of the gas limits 68,756,640, largest limit 880,875 (2^24 = 16,777,216). In ETH: **0.000050590081243548 ETH** at `eth_gasPrice` 1000355 wei (execution 0.000050363073546355 + L1 data fee 0.000000227007697193 from `GasPriceOracle.getL1Fee`), at most 0.000100953154789903 ETH at the signer's ceiling (2 x gas price); about **0.1022 sUSDS** (2251.73 USD/ETH from QuoterV2 WETH/USDC fee 500, / 1.114790 USD per sUSDS from PSM3) |
| **Simulation** | 1 `eth_simulateV1` request(s) (helper `simulate`, one `blockStateCalls` entry per keep-whole group), no state overrides: `all_success` **true**, `failed_count` 0, `clamped_count` 0, `over_cap_count` 0, pending nonce 4363 |

## 2. ETH for gas

The holder holds **0.005193493505401782 ETH**; `eth_gasPrice` 1000355 wei (base fee 355 wei). The simulation runs with `validation: false` and does not see ETH, so it is walked here: the signer refuses a transaction unless the balance covers `gasLimit x maxFeePerGas` (execution only), and before each group G section 8 asks for ETH >= 0.002 ETH + the group's `gas_limit x 2 x eth_gasPrice`. The executor makes that check fresh before each group; this is a projection.

| price assumption | effective price | cost of all 350 transactions (execution + L1 data fee) | starting balance the walk needs | first transaction the signer would refuse | first group failing the affordability gate | lowest balance at a group start |
|---|---|---|---|---|---|---|
| effective price = eth_gasPrice (what the node suggests) | 1000355 wei | 0.000050590081243548 ETH | 0.000051034188185629 ETH | none | none | 0.005143082045497301 ETH (group 66) |
| effective price = the signer's ceiling maxFeePerGas = 2 x eth_gasPrice | 2000710 wei | 0.000100953154789903 ETH | 0.000101021955530503 ETH | none | none | 0.005092896207847361 ETH (group 66) |

Result: **no ETH shortfall** under either assumption.

## 3. Drift, the simulation, and what was checked

- **Pool drift since F sized the plan** (`run/2026-11-01T0359Z-clearance/planner/g-drift.json`): 0 of 122 pools moved, on 0 market(s). A moved pool is reported, never stale by itself; each call carries its own floor and the pre-send re-check decides. Fresh quotes vs F's `quoted_fill`: largest relative gap 7.12e-15 (drift, not a check).
- **Simulation**: one request: the whole ordered sequence. 67 entries and 350 calls in all, from the holder, in send order.
- **Gas limits** are the helper's `gas_limit` per call, copied, never computed by hand: `ceil(maxUsedGas x 1.2)` on every call; the largest is 880,875.
- **Calldata**: all 350 calldatas re-encoded by the helper's `encode` equal the ethers encoding (bytes and keccak256); the signer's policy-only `check` **allowed all 350** signer-input files (`run/2026-11-01T0359Z-clearance/g-tx/tx-NNN.json`, each `{"calls":[one call],"gasLimit":"<helper gas_limit>"}`).
- **End state**: the simulated end state equals the prediction on **231 of 231** probed balances.
- **Independent read**: requested (`run/2026-11-01T0359Z-clearance/g-indep-request.json`, 601 reads): run each with a second tool against a second RPC at its block and compare; the helper pins one RPC, so the planner does not make this read itself.
- **Trading boundary at build**: 61 of 61 children clear at block 158953461 (timestamp 1793505699); parent and 3 middles payoutDenominator 0/0/0/0. Re-read immediately before every group at send time.
- **Route of a market with a `set` row** (paulmillr/noble-curves): fresh spot sum 0.858694 -> dual-buy; sum after its own set-sell 0.960869 -> dual-buy: they agree.
- **Route of a market with a `set` row** (shazow/whatsabi): fresh spot sum 0.943632 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (Commit-Boost/commit-boost-client): fresh spot sum 1.064402 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.
- **Route of a market with a `set` row** (holiman/goevmlab): fresh spot sum 0.937219 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (OffchainLabs/stylus-sdk-rs): fresh spot sum 1.061774 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.
- **Route of a market with a `set` row** (argotorg/fe): fresh spot sum 0.947634 -> simple-buy; sum after its own set-sell 0.992169 -> simple-buy: they agree.

## 4. Mints (0 groups at the head of the sequence, each `[approve, split]`)

- none: M = 0 and no bundle token is held for a bundle with a position, so no split is emitted (G section 1).

## 5. Per-market print (units: the row's own repo token; sUSDS equivalent at the labelled 1/98 in brackets)

### 5a. Pairs: `dual-buy`, "pair (sum < 1 - f)", f = 0.0001 (4 markets)

- **paulmillr/noble-curves** pair (sum < 1 - f): q = 16.8421; the pair-cost quote at q failed (print only)
- **dappnode/DAppNode** pair (sum < 1 - f): q = 15.2625 repo tokens; spot sum 0.95784; locked-in sum = cost/q = 14.9364/15.2625 = 0.97864; cost 14.9364 [0.152413 sUSDS]
  - outcome: +(1 - sum)*q = 0.3260 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 14.9364 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +9.3487 tokens for 6.4962 repo tokens (UP leg total 24.6111 tokens at stake 16.8998)
  - legs: UP count 24.6111 (stake 16.8998, inMax 16.9843), DOWN count 15.2625 (stake 4.5328, inMax 4.5555); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **alloy-rs/alloy** pair (sum < 1 - f): q = 14.5042 repo tokens; spot sum 0.96041; locked-in sum = cost/q = 14.2124/14.5042 = 0.97989; cost 14.2124 [0.145025 sUSDS]
  - outcome: +(1 - sum)*q = 0.2917 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 14.2124 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +23.9408 tokens for 19.9586 repo tokens (UP leg total 38.4450 tokens at stake 31.6812)
  - legs: UP count 38.4450 (stake 31.6812, inMax 31.8397), DOWN count 14.5042 (stake 2.4898, inMax 2.5022); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **foundry-rs/foundry** pair (sum < 1 - f): q = 16.4152 repo tokens; spot sum 0.96309; locked-in sum = cost/q = 16.1089/16.4152 = 0.98134; cost 16.1089 [0.164376 sUSDS]
  - outcome: +(1 - sum)*q = 0.3063 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 16.1089 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +9.0942 tokens for 1.3241 repo tokens (DOWN leg total 25.5094 tokens at stake 3.5276)
  - legs: UP count 16.4152 (stake 13.9054, inMax 13.9749), DOWN count 25.5094 (stake 3.5276, inMax 3.5452); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions

Pairs in total: cost 45.2577 repo tokens, locked gain 0.9241 repo tokens if every repo is evaluated and every child resolves to a score (heterogeneous tokens, informational).

### 5b. Set rows: set-sell and merge-arb (6 markets)

- **paulmillr/noble-curves** merge-arb: 52.2974 pairs, cost ~ 47.4749, gain ~ 4.8226 repo tokens now, consumes 52.2974 child Invalid held from earlier runs (I_j 52.2974; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 41.621624520099962536, DOWN 6.090603106669238366 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **shazow/whatsabi** merge-arb: 20.2635 pairs, cost ~ 19.6778, gain ~ 0.5857 repo tokens now, consumes 20.2635 child Invalid held from earlier runs (I_j 47.1776; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 16.137029543865763336, DOWN 3.639173127572620462 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **holiman/goevmlab** merge-arb: 20.2626 pairs, cost ~ 19.6074, gain ~ 0.6552 repo tokens now, consumes 20.2626 child Invalid held from earlier runs (I_j 29.0239; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 15.419760350769843673, DOWN 4.285642357981665919 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **argotorg/fe** merge-arb: 17.1646 pairs, cost ~ 16.6417, gain ~ 0.5228 repo tokens now, consumes 17.1646 child Invalid held from earlier runs (I_j 17.1646; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 13.865488672881730675, DOWN 2.859466257611097999 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **Commit-Boost/commit-boost-client** set-sell: 15.6025 sets, proceeds ~ 16.0883, gain ~ 0.4858 repo tokens, keeps 15.6025 child Invalid [0.164166 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 11.691913207861688695, DOWN leg >= 4.315940129493970308. Fresh spot sum 1.064402.
- **OffchainLabs/stylus-sdk-rs** set-sell: 21.4787 sets, proceeds ~ 22.1254, gain ~ 0.6468 repo tokens, keeps 21.4787 child Invalid [0.225770 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 16.850699926848837261, DOWN leg >= 5.164109130687663811. Fresh spot sum 1.061774.

### 5c. Complex-buy (45 groups: split `x = stake`, sell the other leg, buy the own leg with the proceeds; keeps `x` child Invalid; the last two transactions are rebuilt at send time with the realised proceeds)

- **ethereum/py_ecc** complex-buy UP: split x = 13.9189 repo tokens [0.142030 sUSDS-eq], sell x DOWN for P = 2.4307 repo tokens, buy 2.9301 UP -> **16.8491 UP + 13.9189 child Invalid** (quoted total; F's simple-route count 16.5952; complex 1.530% vs the simple route); spot sum 1.01554 > 1; p_win 0.8500
- **blockscout/blockscout** complex-buy UP: split x = 7.2940 repo tokens [0.074428 sUSDS-eq], sell x DOWN for P = 2.3026 repo tokens, buy 3.3352 UP -> **10.6291 UP + 7.2940 child Invalid** (quoted total; F's simple-route count 10.5058; complex 1.174% vs the simple route); spot sum 1.01144 > 1; p_win 0.7000
- **herumi/mcl** complex-buy UP: split x = 39.3089 repo tokens [0.401111 sUSDS-eq], sell x DOWN for P = 6.3374 repo tokens, buy 7.5580 UP -> **46.8669 UP + 39.3089 child Invalid** (quoted total; F's simple-route count 45.3931; complex 3.247% vs the simple route); spot sum 1.01305 > 1; p_win 0.9000
- **flashbots/rbuilder** complex-buy UP: split x = 8.3158 repo tokens [0.084856 sUSDS-eq], sell x DOWN for P = 2.2331 repo tokens, buy 3.0245 UP -> **11.3403 UP + 8.3158 child Invalid** (quoted total; F's simple-route count 11.1888; complex 1.355% vs the simple route); spot sum 1.01129 > 1; p_win 0.7500
- **Consensys/gnark-crypto** complex-buy UP: split x = 23.2754 repo tokens [0.237504 sUSDS-eq], sell x DOWN for P = 3.7494 repo tokens, buy 4.3373 UP -> **27.6126 UP + 23.2754 child Invalid** (quoted total; F's simple-route count 26.4348; complex 4.456% vs the simple route); spot sum 1.03965 > 1; p_win 0.9000
- **taikoxyz/taiko-mono** complex-buy UP: split x = 10.9896 repo tokens [0.112139 sUSDS-eq], sell x DOWN for P = 2.9534 repo tokens, buy 4.0185 UP -> **15.0082 UP + 10.9896 child Invalid** (quoted total; F's simple-route count 14.8257; complex 1.231% vs the simple route); spot sum 1.01141 > 1; p_win 0.7500
- **ethereum/js-ethereum-cryptography** complex-buy DOWN: split x = 9.0334 repo tokens [0.092177 sUSDS-eq], sell x UP for P = 4.9327 repo tokens, buy 10.1774 DOWN -> **19.2107 DOWN + 9.0334 child Invalid** (quoted total; F's simple-route count 17.9282; complex 7.154% vs the simple route); spot sum 1.01100 > 1; p_win 0.5500
- **wighawag/hardhat-deploy** complex-buy UP: split x = 8.6143 repo tokens [0.087901 sUSDS-eq], sell x DOWN for P = 2.3484 repo tokens, buy 3.1849 UP -> **11.7993 UP + 8.6143 child Invalid** (quoted total; F's simple-route count 11.5996; complex 1.721% vs the simple route); spot sum 1.01295 > 1; p_win 0.7500
- **intellij-solidity/intellij-solidity** complex-buy UP: split x = 7.2701 repo tokens [0.074185 sUSDS-eq], sell x DOWN for P = 1.6378 repo tokens, buy 2.0747 UP -> **9.3448 UP + 7.2701 child Invalid** (quoted total; F's simple-route count 9.1561; complex 2.061% vs the simple route); spot sum 1.01833 > 1; p_win 0.8000
- **wealdtech/ethdo** complex-buy UP: split x = 7.0874 repo tokens [0.072320 sUSDS-eq], sell x DOWN for P = 1.8941 repo tokens, buy 2.5589 UP -> **9.6462 UP + 7.0874 child Invalid** (quoted total; F's simple-route count 9.5219; complex 1.306% vs the simple route); spot sum 1.01194 > 1; p_win 0.7500
- **lambdaclass/lambdaworks** complex-buy UP: split x = 15.7226 repo tokens [0.160435 sUSDS-eq], sell x DOWN for P = 2.7949 repo tokens, buy 3.3808 UP -> **19.1034 UP + 15.7226 child Invalid** (quoted total; F's simple-route count 18.7816; complex 1.713% vs the simple route); spot sum 1.01444 > 1; p_win 0.8500
- **smartcontracts/simple-optimism-node** complex-buy UP: split x = 16.3933 repo tokens [0.167278 sUSDS-eq], sell x DOWN for P = 7.6422 repo tokens, buy 14.4396 UP -> **30.8328 UP + 16.3933 child Invalid** (quoted total; F's simple-route count 30.5641; complex 0.879% vs the simple route); spot sum 1.00295 > 1; p_win 0.5500
- **skalenetwork/libBLS** complex-buy UP: split x = 8.0048 repo tokens [0.081682 sUSDS-eq], sell x DOWN for P = 2.1580 repo tokens, buy 2.9203 UP -> **10.9251 UP + 8.0048 child Invalid** (quoted total; F's simple-route count 10.7650; complex 1.488% vs the simple route); spot sum 1.01384 > 1; p_win 0.7500
- **succinctlabs/sp1** complex-buy UP: split x = 11.2198 repo tokens [0.114488 sUSDS-eq], sell x DOWN for P = 3.0430 repo tokens, buy 4.1482 UP -> **15.3680 UP + 11.2198 child Invalid** (quoted total; F's simple-route count 15.1527; complex 1.421% vs the simple route); spot sum 1.00873 > 1; p_win 0.7500
- **otterscan/otterscan** complex-buy DOWN: split x = 3.2536 repo tokens [0.033200 sUSDS-eq], sell x UP for P = 2.3754 repo tokens, buy 8.2650 DOWN -> **11.5185 DOWN + 3.2536 child Invalid** (quoted total; F's simple-route count 11.2187; complex 2.672% vs the simple route); spot sum 1.01240 > 1; p_win 0.3000
- **lambdaclass/ethrex** complex-buy UP: split x = 15.1103 repo tokens [0.154187 sUSDS-eq], sell x DOWN for P = 3.2759 repo tokens, buy 4.2083 UP -> **19.3186 UP + 15.1103 child Invalid** (quoted total; F's simple-route count 19.1799; complex 0.724% vs the simple route); spot sum 1.00530 > 1; p_win 0.8000
- **Commit-Boost/commit-boost-client** complex-buy UP: split x = 35.7215 repo tokens [0.364505 sUSDS-eq], sell x DOWN for P = 7.7308 repo tokens, buy 10.3050 UP -> **46.0265 UP + 35.7215 child Invalid** (quoted total; F's simple-route count 46.2932, on the post-set-sell book; complex -0.576% vs the simple route); spot sum 1.06440 > 1; p_win 0.8000
- **Cyfrin/aderyn** complex-buy UP: split x = 10.6952 repo tokens [0.109135 sUSDS-eq], sell x DOWN for P = 3.2370 repo tokens, buy 4.7166 UP -> **15.4118 UP + 10.6952 child Invalid** (quoted total; F's simple-route count 15.4581; complex -0.299% vs the simple route); spot sum 1.00003 > 1; p_win 0.7000
- **0xMiden/miden-vm** complex-buy UP: split x = 29.4643 repo tokens [0.300657 sUSDS-eq], sell x DOWN for P = 5.7372 repo tokens, buy 7.1099 UP -> **36.5743 UP + 29.4643 child Invalid** (quoted total; F's simple-route count 35.6784; complex 2.511% vs the simple route); spot sum 1.02324 > 1; p_win 0.8500
- **edb-rs/edb** complex-buy UP: split x = 36.8961 repo tokens [0.376491 sUSDS-eq], sell x DOWN for P = 9.3008 repo tokens, buy 12.4559 UP -> **49.3520 UP + 36.8961 child Invalid** (quoted total; F's simple-route count 47.9797; complex 2.860% vs the simple route); spot sum 1.01762 > 1; p_win 0.8000
- **succinctlabs/rsp** complex-buy DOWN: split x = 2.7435 repo tokens [0.027995 sUSDS-eq], sell x UP for P = 1.8124 repo tokens, buy 4.7214 DOWN -> **7.4649 DOWN + 2.7435 child Invalid** (quoted total; F's simple-route count 7.0735; complex 5.534% vs the simple route); spot sum 1.03806 > 1; p_win 0.4000
- **OffchainLabs/stylus-sdk-rs** complex-buy UP: split x = 15.3934 repo tokens [0.157075 sUSDS-eq], sell x DOWN for P = 3.3050 repo tokens, buy 4.2500 UP -> **19.6434 UP + 15.3934 child Invalid** (quoted total; F's simple-route count 19.5499, on the post-set-sell book; complex 0.478% vs the simple route); spot sum 1.06177 > 1; p_win 0.8000
- **ethstaker/ethstaker-deposit-cli** complex-buy DOWN: split x = 6.5158 repo tokens [0.066488 sUSDS-eq], sell x UP for P = 3.8692 repo tokens, buy 9.1274 DOWN -> **15.6432 DOWN + 6.5158 child Invalid** (quoted total; F's simple-route count 15.1102; complex 3.528% vs the simple route); spot sum 1.00998 > 1; p_win 0.4500
- **dl-solarity/solidity-lib** complex-buy UP: split x = 17.3975 repo tokens [0.177526 sUSDS-eq], sell x DOWN for P = 5.1546 repo tokens, buy 7.0960 UP -> **24.4935 UP + 17.3975 child Invalid** (quoted total; F's simple-route count 23.6365; complex 3.626% vs the simple route); spot sum 1.03611 > 1; p_win 0.7500
- **powdr-labs/powdr** complex-buy UP: split x = 33.7005 repo tokens [0.343882 sUSDS-eq], sell x DOWN for P = 7.0425 repo tokens, buy 8.8093 UP -> **42.5097 UP + 33.7005 child Invalid** (quoted total; F's simple-route count 41.0308; complex 3.604% vs the simple route); spot sum 1.02373 > 1; p_win 0.8500
- **axiom-crypto/snark-verifier** complex-buy DOWN: split x = 2.4320 repo tokens [0.024816 sUSDS-eq], sell x UP for P = 1.6429 repo tokens, buy 4.8300 DOWN -> **7.2620 DOWN + 2.4320 child Invalid** (quoted total; F's simple-route count 7.1002; complex 2.278% vs the simple route); spot sum 1.01205 > 1; p_win 0.3500
- **swiss-knife-xyz/swiss-knife** complex-buy DOWN: split x = 4.1093 repo tokens [0.041932 sUSDS-eq], sell x UP for P = 3.1002 repo tokens, buy 11.1810 DOWN -> **15.2903 DOWN + 4.1093 child Invalid** (quoted total; F's simple-route count 14.5963; complex 4.755% vs the simple route); spot sum 1.02111 > 1; p_win 0.3000
- **a16z/helios** complex-buy UP: split x = 11.1497 repo tokens [0.113772 sUSDS-eq], sell x DOWN for P = 2.3780 repo tokens, buy 3.0357 UP -> **14.1854 UP + 11.1497 child Invalid** (quoted total; F's simple-route count 14.1025; complex 0.588% vs the simple route); spot sum 1.00050 > 1; p_win 0.8000
- **apeworx/ape** complex-buy UP: split x = 12.1983 repo tokens [0.124472 sUSDS-eq], sell x DOWN for P = 3.3086 repo tokens, buy 4.5125 UP -> **16.7107 UP + 12.1983 child Invalid** (quoted total; F's simple-route count 16.4789; complex 1.407% vs the simple route); spot sum 1.01256 > 1; p_win 0.7500
- **consensys/teku** complex-buy UP: split x = 11.8101 repo tokens [0.120511 sUSDS-eq], sell x DOWN for P = 2.6234 repo tokens, buy 3.3487 UP -> **15.1588 UP + 11.8101 child Invalid** (quoted total; F's simple-route count 14.9378; complex 1.480% vs the simple route); spot sum 1.01625 > 1; p_win 0.8000
- **erigontech/erigon** complex-buy UP: split x = 11.7506 repo tokens [0.119904 sUSDS-eq], sell x DOWN for P = 3.1889 repo tokens, buy 4.3454 UP -> **16.0959 UP + 11.7506 child Invalid** (quoted total; F's simple-route count 15.8661; complex 1.449% vs the simple route); spot sum 1.01323 > 1; p_win 0.7500
- **ethereum-lists/chains** complex-buy UP: split x = 15.4152 repo tokens [0.157298 sUSDS-eq], sell x DOWN for P = 4.1999 repo tokens, buy 5.7714 UP -> **21.1866 UP + 15.4152 child Invalid** (quoted total; F's simple-route count 20.9161; complex 1.293% vs the simple route); spot sum 1.00617 > 1; p_win 0.7500
- **ethers-io/ethers.js** complex-buy DOWN: split x = 1.2036 repo tokens [0.012281 sUSDS-eq], sell x UP for P = 1.0636 repo tokens, buy 7.5079 DOWN -> **8.7114 DOWN + 1.2036 child Invalid** (quoted total; F's simple-route count 8.4463; complex 3.138% vs the simple route); spot sum 1.02003 > 1; p_win 0.1500
- **grandinetech/grandine** complex-buy UP: split x = 9.1484 repo tokens [0.093351 sUSDS-eq], sell x DOWN for P = 2.0718 repo tokens, buy 2.6329 UP -> **11.7814 UP + 9.1484 child Invalid** (quoted total; F's simple-route count 11.5426; complex 2.069% vs the simple route); spot sum 1.01914 > 1; p_win 0.8000
- **hyperledger-web3j/web3j** complex-buy UP: split x = 7.3422 repo tokens [0.074921 sUSDS-eq], sell x DOWN for P = 1.9657 repo tokens, buy 2.6569 UP -> **9.9991 UP + 7.3422 child Invalid** (quoted total; F's simple-route count 9.8670; complex 1.338% vs the simple route); spot sum 1.01219 > 1; p_win 0.7500
- **nethereum/nethereum** complex-buy UP: split x = 9.5455 repo tokens [0.097403 sUSDS-eq], sell x DOWN for P = 1.5818 repo tokens, buy 1.8926 UP -> **11.4382 UP + 9.5455 child Invalid** (quoted total; F's simple-route count 11.3338; complex 0.921% vs the simple route); spot sum 1.00730 > 1; p_win 0.8500
- **openzeppelin/openzeppelin-contracts** complex-buy UP: split x = 14.0024 repo tokens [0.142882 sUSDS-eq], sell x DOWN for P = 2.5134 repo tokens, buy 3.0311 UP -> **17.0336 UP + 14.0024 child Invalid** (quoted total; F's simple-route count 16.6992; complex 2.002% vs the simple route); spot sum 1.01715 > 1; p_win 0.8500
- **safe-global/safe-smart-account** complex-buy UP: split x = 58.4780 repo tokens [0.596714 sUSDS-eq], sell x DOWN for P = 14.9362 repo tokens, buy 19.9267 UP -> **78.4048 UP + 58.4780 child Invalid** (quoted total; F's simple-route count 73.9614; complex 6.008% vs the simple route); spot sum 1.01164 > 1; p_win 0.8500
- **sigp/lighthouse** complex-buy UP: split x = 7.1774 repo tokens [0.073239 sUSDS-eq], sell x DOWN for P = 1.2582 repo tokens, buy 1.4988 UP -> **8.6763 UP + 7.1774 child Invalid** (quoted total; F's simple-route count 8.5020; complex 2.050% vs the simple route); spot sum 1.02092 > 1; p_win 0.8500
- **status-im/nimbus-eth2** complex-buy UP: split x = 9.7700 repo tokens [0.099694 sUSDS-eq], sell x DOWN for P = 1.2258 repo tokens, buy 1.3849 UP -> **11.1550 UP + 9.7700 child Invalid** (quoted total; F's simple-route count 10.9528; complex 1.846% vs the simple route); spot sum 1.02011 > 1; p_win 0.9000
- **vyperlang/titanoboa** complex-buy UP: split x = 9.9434 repo tokens [0.101463 sUSDS-eq], sell x DOWN for P = 2.8832 repo tokens, buy 3.9145 UP -> **13.8579 UP + 9.9434 child Invalid** (quoted total; F's simple-route count 13.3990; complex 3.425% vs the simple route); spot sum 1.03464 > 1; p_win 0.7500
- **ethdebug/format** complex-buy UP: split x = 28.5774 repo tokens [0.291607 sUSDS-eq], sell x DOWN for P = 5.1771 repo tokens, buy 6.4159 UP -> **34.9933 UP + 28.5774 child Invalid** (quoted total; F's simple-route count 34.5971; complex 1.145% vs the simple route); spot sum 1.00016 > 1; p_win 0.8500
- **ethpandaops/ethereum-helm-charts** complex-buy UP: split x = 14.6438 repo tokens [0.149427 sUSDS-eq], sell x DOWN for P = 6.1726 repo tokens, buy 10.6297 UP -> **25.2736 UP + 14.6438 child Invalid** (quoted total; F's simple-route count 24.9184; complex 1.426% vs the simple route); spot sum 1.00826 > 1; p_win 0.6000
- **ethpandaops/checkpointz** complex-buy UP: split x = 49.1389 repo tokens [0.501418 sUSDS-eq], sell x DOWN for P = 20.7181 repo tokens, buy 35.9251 UP -> **85.0641 UP + 49.1389 child Invalid** (quoted total; F's simple-route count 81.5885; complex 4.260% vs the simple route); spot sum 1.00978 > 1; p_win 0.6500
- **lambdaclass/lambda_ethereum_consensus** complex-buy UP: split x = 16.3117 repo tokens [0.166446 sUSDS-eq], sell x DOWN for P = 3.5893 repo tokens, buy 4.6219 UP -> **20.9336 UP + 16.3117 child Invalid** (quoted total; F's simple-route count 20.7329; complex 0.968% vs the simple route); spot sum 1.00647 > 1; p_win 0.8000

### 5d. Simple-buy (12 groups: one approve and one `exactInputSingle`, min 99.5% of the quote)

- **DefiLlama/chainlist** simple-buy DOWN: stake 8.7314 repo tokens [0.089096 sUSDS-eq], quoted out 31.4420 DOWN (F count 31.4420), floor 31.2848; spot sum 0.97928 < 1; p_win 0.3000
- **ChainSafe/bls** simple-buy DOWN: stake 16.8990 repo tokens [0.172438 sUSDS-eq], quoted out 36.3319 DOWN (F count 36.3319), floor 36.1502; spot sum 0.99992 < 1; p_win 0.5000
- **shazow/whatsabi** simple-buy UP: stake 27.7437 repo tokens [0.283099 sUSDS-eq], quoted out 33.5356 UP (F count 33.5356), floor 33.3680; spot sum 0.94363 (quoted on the post-set-sell state); p_win 0.8500
- **holiman/goevmlab** simple-buy UP: stake 19.5896 repo tokens [0.199894 sUSDS-eq], quoted out 24.9729 UP (F count 24.9729), floor 24.8481; spot sum 0.93722 (quoted on the post-set-sell state); p_win 0.8000
- **eth-infinitism/account-abstraction** simple-buy UP: stake 29.2519 repo tokens [0.298489 sUSDS-eq], quoted out 43.2859 UP (F count 43.2859), floor 43.0694; spot sum 0.99624 < 1; p_win 0.7000
- **ethereum/consensus-specs** simple-buy UP: stake 11.8368 repo tokens [0.120784 sUSDS-eq], quoted out 13.2939 UP (F count 13.2939), floor 13.2275; spot sum 0.97797 < 1; p_win 0.9000
- **ipsilon/evmone** simple-buy UP: stake 34.4617 repo tokens [0.351650 sUSDS-eq], quoted out 42.0009 UP (F count 42.0009), floor 41.7909; spot sum 0.98734 < 1; p_win 0.8500
- **argotorg/fe** simple-buy UP: stake 21.6387 repo tokens [0.220803 sUSDS-eq], quoted out 26.0004 UP (F count 26.0004), floor 25.8704; spot sum 0.94763 (quoted on the post-set-sell state); p_win 0.8500
- **nomicfoundation/hardhat** simple-buy UP: stake 15.4789 repo tokens [0.157948 sUSDS-eq], quoted out 19.6506 UP (F count 19.6506), floor 19.5523; spot sum 0.99139 < 1; p_win 0.8000
- **OffchainLabs/prysm** simple-buy UP: stake 15.8377 repo tokens [0.161609 sUSDS-eq], quoted out 20.1141 UP (F count 20.1141), floor 20.0135; spot sum 0.97605 < 1; p_win 0.8000
- **argotorg/hevm** simple-buy UP: stake 19.4902 repo tokens [0.198880 sUSDS-eq], quoted out 24.8565 UP (F count 24.8565), floor 24.7322; spot sum 0.99997 < 1; p_win 0.8000
- **erigontech/silkworm** simple-buy UP: stake 51.7935 repo tokens [0.528505 sUSDS-eq], quoted out 68.3081 UP (F count 68.3081), floor 67.9666; spot sum 0.99999 < 1; p_win 0.8000

### 5e. Skipped rows (0: never sent; the executor writes each `status: "skipped"` with its reason)

- none

## 6. Group order and gas (send order)

| # | group | tx | gas used |
|---|---|---|---|
| 0 | `complex-buy:ethereum/py_ecc:UP` | 0-5 | 969,233 |
| 1 | `complex-buy:blockscout/blockscout:UP` | 6-11 | 874,417 |
| 2 | `complex-buy:herumi/mcl:UP` | 12-17 | 912,392 |
| 3 | `merge-arb:paulmillr/noble-curves` | 18-24 | 1,119,476 |
| 4 | `dual-buy:paulmillr/noble-curves` | 25-28 | 353,393 |
| 5 | `complex-buy:flashbots/rbuilder:UP` | 29-34 | 921,019 |
| 6 | `complex-buy:Consensys/gnark-crypto:UP` | 35-40 | 918,877 |
| 7 | `complex-buy:taikoxyz/taiko-mono:UP` | 41-46 | 877,532 |
| 8 | `complex-buy:ethereum/js-ethereum-cryptography:DOWN` | 47-52 | 910,705 |
| 9 | `complex-buy:wighawag/hardhat-deploy:UP` | 53-58 | 897,348 |
| 10 | `simple-buy:DefiLlama/chainlist:DOWN` | 59-60 | 209,690 |
| 11 | `simple-buy:ChainSafe/bls:DOWN` | 61-62 | 184,603 |
| 12 | `complex-buy:intellij-solidity/intellij-solidity:UP` | 63-68 | 886,204 |
| 13 | `dual-buy:dappnode/DAppNode` | 69-72 | 369,837 |
| 14 | `complex-buy:wealdtech/ethdo:UP` | 73-78 | 874,332 |
| 15 | `complex-buy:lambdaclass/lambdaworks:UP` | 79-84 | 939,919 |
| 16 | `complex-buy:smartcontracts/simple-optimism-node:UP` | 85-90 | 889,030 |
| 17 | `complex-buy:skalenetwork/libBLS:UP` | 91-96 | 884,768 |
| 18 | `merge-arb:shazow/whatsabi` | 97-103 | 975,902 |
| 19 | `simple-buy:shazow/whatsabi:UP` | 104-105 | 163,192 |
| 20 | `complex-buy:succinctlabs/sp1:UP` | 106-111 | 921,963 |
| 21 | `complex-buy:otterscan/otterscan:DOWN` | 112-117 | 887,031 |
| 22 | `complex-buy:lambdaclass/ethrex:UP` | 118-123 | 900,585 |
| 23 | `set-sell:Commit-Boost/commit-boost-client` | 124-129 | 917,982 |
| 24 | `complex-buy:Commit-Boost/commit-boost-client:UP` | 130-135 | 964,060 |
| 25 | `complex-buy:Cyfrin/aderyn:UP` | 136-141 | 908,009 |
| 26 | `complex-buy:0xMiden/miden-vm:UP` | 142-147 | 969,587 |
| 27 | `merge-arb:holiman/goevmlab` | 148-154 | 963,462 |
| 28 | `simple-buy:holiman/goevmlab:UP` | 155-156 | 163,182 |
| 29 | `complex-buy:edb-rs/edb:UP` | 157-162 | 919,555 |
| 30 | `complex-buy:succinctlabs/rsp:DOWN` | 163-168 | 921,833 |
| 31 | `set-sell:OffchainLabs/stylus-sdk-rs` | 169-174 | 923,955 |
| 32 | `complex-buy:OffchainLabs/stylus-sdk-rs:UP` | 175-180 | 893,857 |
| 33 | `complex-buy:ethstaker/ethstaker-deposit-cli:DOWN` | 181-186 | 874,678 |
| 34 | `complex-buy:dl-solarity/solidity-lib:UP` | 187-192 | 877,968 |
| 35 | `complex-buy:powdr-labs/powdr:UP` | 193-198 | 942,966 |
| 36 | `complex-buy:axiom-crypto/snark-verifier:DOWN` | 199-204 | 901,754 |
| 37 | `complex-buy:swiss-knife-xyz/swiss-knife:DOWN` | 205-210 | 955,190 |
| 38 | `complex-buy:a16z/helios:UP` | 211-216 | 906,762 |
| 39 | `dual-buy:alloy-rs/alloy` | 217-220 | 360,418 |
| 40 | `complex-buy:apeworx/ape:UP` | 221-226 | 913,254 |
| 41 | `complex-buy:consensys/teku:UP` | 227-232 | 911,732 |
| 42 | `complex-buy:erigontech/erigon:UP` | 233-238 | 924,681 |
| 43 | `simple-buy:eth-infinitism/account-abstraction:UP` | 239-240 | 169,946 |
| 44 | `complex-buy:ethereum-lists/chains:UP` | 241-246 | 905,990 |
| 45 | `simple-buy:ethereum/consensus-specs:UP` | 247-248 | 165,587 |
| 46 | `simple-buy:ipsilon/evmone:UP` | 249-250 | 186,976 |
| 47 | `merge-arb:argotorg/fe` | 251-257 | 977,914 |
| 48 | `simple-buy:argotorg/fe:UP` | 258-259 | 163,216 |
| 49 | `complex-buy:ethers-io/ethers.js:DOWN` | 260-265 | 895,998 |
| 50 | `dual-buy:foundry-rs/foundry` | 266-269 | 367,526 |
| 51 | `complex-buy:grandinetech/grandine:UP` | 270-275 | 851,995 |
| 52 | `complex-buy:hyperledger-web3j/web3j:UP` | 276-281 | 863,665 |
| 53 | `complex-buy:nethereum/nethereum:UP` | 282-287 | 889,834 |
| 54 | `simple-buy:nomicfoundation/hardhat:UP` | 288-289 | 172,940 |
| 55 | `complex-buy:openzeppelin/openzeppelin-contracts:UP` | 290-295 | 884,645 |
| 56 | `simple-buy:OffchainLabs/prysm:UP` | 296-297 | 172,295 |
| 57 | `complex-buy:safe-global/safe-smart-account:UP` | 298-303 | 965,896 |
| 58 | `complex-buy:sigp/lighthouse:UP` | 304-309 | 904,327 |
| 59 | `complex-buy:status-im/nimbus-eth2:UP` | 310-315 | 922,076 |
| 60 | `complex-buy:vyperlang/titanoboa:UP` | 316-321 | 912,532 |
| 61 | `simple-buy:argotorg/hevm:UP` | 322-323 | 162,508 |
| 62 | `complex-buy:ethdebug/format:UP` | 324-329 | 935,530 |
| 63 | `complex-buy:ethpandaops/ethereum-helm-charts:UP` | 330-335 | 906,206 |
| 64 | `complex-buy:ethpandaops/checkpointz:UP` | 336-341 | 934,556 |
| 65 | `complex-buy:lambdaclass/lambda_ethereum_consensus:UP` | 342-347 | 899,537 |
| 66 | `simple-buy:erigontech/silkworm:UP` | 348-349 | 177,173 |

## 7. Risks the human is told before any "yes" (supervised mode)

- **One transaction per signer call.** Every group above is an ordered sequence of single transactions and **can be left half-done between transactions** (one pair leg bought, a split without its sales, a `set-sell` whose gain is locked only if its whole group lands). A stopped group goes to the recovery rule (G section 8 step 4). EIP-7702 removes this risk and is recommended.
- **Residual risks (a) and (b)** of every pair and of the folded directional rows (section 5a): (a) the repo is evaluated but its child question resolves INVALID, UP + DOWN pay 0; (b) the parent's `n_X` and the middle's `k_X` disagree, a repo token pays `(n_X/N)/k_X`.
- **Complex-buy is chosen on the spot sum.** At size it can quote slightly below the simple route (section 5c); G section 3 keeps the rule as written.
- **Sequence order and mints are not re-sized**; any send-time disagreement (balance, boundary flip, floor) makes the plan stale.

## 8. At send time (the executor's duties; they do not change this plan)

- before every group: the trading-boundary read and fresh slot0 of the market (G section 3); a flip makes the plan stale
- before every group: the affordability gate, ETH >= 0.002 ETH + the sum over the group of gas_limit x 2 x eth_gasPrice (G section 8, Affordability)
- before every transaction: the holder nonce latest == pending == nonce_expected; the signer-input file equal to the plan (calldata, to, gasLimit) and its keccak256 equal to calldata_keccak256
- before every transaction: the signer's own simulate passes, and the pre-send gas check holds: gas_limit >= the fresh gas_used x 1.2, gas_limit >= the peak this plan measured (max_used_gas, else gas_used), and the fresh gas_used at most 10% above this plan's (G section 8)
- before every swap: its floor (amountOutMinimum) or bound (amountInMaximum) against a fresh quote
- write inflight.json and the nonce attempt before every broadcast; one call per send, never re-run once it printed its broadcast line (G section 8; a throttle answered before signing is re-run: I-setup.md I.2 section 7, Rate limits)
- before a merge-arb group: its child Invalid read fresh at the holder; below q the plan is stale (G section 1)
- rebuild the last two transactions of every complex-buy after the sale's receipt, with P = the realised proceeds and a fresh quote at P (rebuild_at_send, G section 3)
- a revert, a floor breach or a stale check stops sending; the group in progress goes to the recovery rule, the groups not started are skipped (G section 8 step 4)

Files: `g-plan.json` (groups, every call with calldata, keccak256, gas limit, floors and expected effects), `g-tx/tx-NNN.json` (one signer-input file per transaction), `g-sim-main.json` (the helper simulate input), `planner/g-drift.json` (the drift report).

## 9. Audit of the written plan (run after `g-plan.json` was written)

- calldata audit: 67 groups, 350 transactions decoded and re-derived from allocation.json (71 rows: 71 in groups, 0 skipped), kinds {"complex-buy":45,"merge-arb":4,"dual-buy":4,"simple-buy":12,"set-sell":2}, every approval exact (none near 2^256), every swap recipient the holder, every tier the candidates.json tier, dual-buy inMax = min(stake x 1.005, remaining); failures 0
- fresh re-simulation of run/2026-11-01T0359Z-clearance/g-sim-main.json (sha256 e892afdf9d8ad0ee74cdd73c8ae724bb0689f414e86c73ec584b2124573acb65): {"entries":67,"count":350,"all_success":true,"failed_count":0,"over_cap_count":0,"clamped_count":0,"pending_nonce":4363,"overrides_active":"absent","no_max_used_gas_count":0}
- holder nonce latest/pending before 4363/4363, after 4363/4363 (the plan's 4363); per-call rows of the fresh simulation: 350 checked, every status 0x1 and every fresh peak within the plan's gas_limit; gasUsed equal to the build's on all
- AUDIT PASSED: every acceptance check holds
