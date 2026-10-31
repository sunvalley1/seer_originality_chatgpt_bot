# G gate print - run 2026-10-31T0904Z

**Optimism mainnet, holder 0x2AD670e5953a85C998cDf1C2f6D74386aB735d4a. Built, simulated and verified: nothing has been signed or sent.** Pending nonce 4350; head at G's read 158919419 (blocks are reported, never compared between reads). Every group below is an ordered sequence of single transactions, one signer call each.

## 1. The numbers

| | |
|---|---|
| **Allocation input** | `run/2026-10-31T0904Z/allocation.json` (sha256 `3f4c00ba96f71897df1154bb597e56c1409bed4fcb9b37df30f06d062dd71813`), generated 2026-10-31T09:06:48Z, 72 rows; 64 markets traded, 0 rows skipped (section 5e) |
| **Counts per route** | pair (`dual-buy`) **1** markets (2 rows); `simple-buy` **10**; `complex-buy` **53** (46 single-side markets with spot sum > 1, plus 7 on a market whose `set-sell` runs first); `set-sell` **7**; `merge-arb` (`buy-and-merge`) **0**; mint groups **3** (mint-middle-A, mint-middle-B, mint-middle-C); PSM3 ramp: none |
| **Total sUSDS staked** | **0 sUSDS** = `totals.staked` = the new mint `M` (no parent split: the rows spend repo tokens the holder already holds). Middles split: A by m_X = 14.8564242378734, B by m_X = 247.327090411513132242, C by m_X = 58.478013859262. Each traded market's budget is its held repo tokens plus m_X; the rows' stakes sum to 1347.3302 repo tokens of 64 different tokens (13.7483 sUSDS-equivalent at the labelled 1/98) |
| **Expected value** | **0.505792 sUSDS** at the labelled 1/N = 1/98 (F's `totals.expected_value`; 49.5676 repo tokens summed over heterogeneous markets, / 98; 0 for any repo that is not evaluated) |
| **Worst case** | `correlated_worst_case` **0.000000 sUSDS** (F's definition); a `set-sell` row's gain is locked only if its whole group lands |
| **Number of transactions** | **390** in **74** keep-whole groups (mint 6, complex-buy 318, simple-buy 20, set-sell 42, dual-buy 4), nonces 4350 to 4739 |
| **Estimated gas** | **69,570,830 gas used** (mints 12,418,453; complex-buy 48,627,445; simple-buy 1,740,564; set-sell 6,427,978; dual-buy 356,390); sum of the gas limits 96,901,586, largest limit 6,247,748 (2^24 = 16,777,216). In ETH: **0.0000699211911949 ETH** at `eth_gasPrice` 1000274 wei (execution 0.00006958989240742 + L1 data fee 0.00000033129878748 from `GasPriceOracle.getL1Fee`), at most 0.00013951108360232 ETH at the signer's ceiling (2 x gas price); about **0.1398 sUSDS** (2229.02 USD/ETH from QuoterV2 WETH/USDC fee 500, / 1.114700 USD per sUSDS from PSM3) |
| **Simulation** | 1 `eth_simulateV1` request(s) (helper `simulate`, one `blockStateCalls` entry per keep-whole group), no state overrides: `all_success` **true**, `failed_count` 0, `clamped_count` 0, `over_cap_count` 0, pending nonce 4350 |

## 2. ETH for gas

The holder holds **0.005207427018966937 ETH**; `eth_gasPrice` 1000274 wei (base fee 274 wei). The simulation runs with `validation: false` and does not see ETH, so it is walked here: the signer refuses a transaction unless the balance covers `gasLimit x maxFeePerGas` (execution only), and before each group G section 8 asks for ETH >= 0.002 ETH + the group's `gas_limit x 2 x eth_gasPrice`. The executor makes that check fresh before each group; this is a projection.

| price assumption | effective price | cost of all 390 transactions (execution + L1 data fee) | starting balance the walk needs | first transaction the signer would refuse | first group failing the affordability gate | lowest balance at a group start |
|---|---|---|---|---|---|---|
| effective price = eth_gasPrice (what the node suggests) | 1000274 wei | 0.0000699211911949 ETH | 0.000070363783459225 ETH | none | none | 0.005137684869741353 ETH (group 73) |
| effective price = the signer's ceiling maxFeePerGas = 2 x eth_gasPrice | 2000548 wei | 0.00013951108360232 ETH | 0.000139579610583203 ETH | none | none | 0.005068272198879335 ETH (group 73) |

Result: **no ETH shortfall** under either assumption.

## 3. Drift, the simulation, and what was checked

- **Pool drift since F sized the plan** (`run/2026-10-31T0904Z/planner/g-drift.json`): 0 of 128 pools moved, on 0 market(s). A moved pool is reported, never stale by itself; each call carries its own floor and the pre-send re-check decides. Fresh quotes vs F's `quoted_fill`: largest relative gap 8.45e-15 (drift, not a check).
- **Simulation**: one request: the whole ordered sequence. 74 entries and 390 calls in all, from the holder, in send order.
- **Gas limits** are the helper's `gas_limit` per call, copied, never computed by hand: `ceil(maxUsedGas x 1.2)` on every call; the largest is 6,247,748.
- **Calldata**: all 390 calldatas re-encoded by the helper's `encode` equal the ethers encoding (bytes and keccak256); the signer's policy-only `check` **allowed all 390** signer-input files (`run/2026-10-31T0904Z/g-tx/tx-NNN.json`, each `{"calls":[one call],"gasLimit":"<helper gas_limit>"}`).
- **End state**: the simulated end state equals the prediction on **243 of 243** probed balances.
- **Independent read**: not run (`--indep` not given; it is supervised-only, because the helper pins one RPC).
- **Trading boundary at build**: 64 of 64 children clear at block 158919425 (timestamp 1793437627); parent and 3 middles payoutDenominator 0/0/0/0. Re-read immediately before every group at send time.
- **Route of a market with a `set` row** (dappnode/DAppNode): fresh spot sum 1.057417 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.
- **Route of a market with a `set` row** (shazow/whatsabi): fresh spot sum 1.084973 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.
- **Route of a market with a `set` row** (Commit-Boost/commit-boost-client): fresh spot sum 1.065289 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.
- **Route of a market with a `set` row** (holiman/goevmlab): fresh spot sum 1.077659 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.
- **Route of a market with a `set` row** (OffchainLabs/stylus-sdk-rs): fresh spot sum 1.061787 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.
- **Route of a market with a `set` row** (alloy-rs/alloy): fresh spot sum 1.075461 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.
- **Route of a market with a `set` row** (argotorg/fe): fresh spot sum 1.054775 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.

## 4. Mints (3 groups at the head of the sequence, each `[approve, split]`)

- `mint-middle-A`: approve bundle A -> Router (m_X) ; Router.splitPosition(sUSDS, middle A, m_X) (gas used 29,089 + 4,044,628)
- `mint-middle-B`: approve bundle B -> Router (m_X) ; Router.splitPosition(sUSDS, middle B, m_X) (gas used 49,001 + 4,165,165)
- `mint-middle-C`: approve bundle C -> Router (m_X) ; Router.splitPosition(sUSDS, middle C, m_X) (gas used 49,001 + 4,081,569)

## 5. Per-market print (units: the row's own repo token; sUSDS equivalent at the labelled 1/98 in brackets)

### 5a. Pairs: `dual-buy`, "pair (sum < 1 - f)", f = 0.0001 (1 markets)

- **OffchainLabs/prysm** pair (sum < 1 - f): q = 7.8274 repo tokens; spot sum 0.97596; locked-in sum = cost/q = 7.7326/7.8274 = 0.98789; cost 7.7326 [0.078905 sUSDS]
  - outcome: +(1 - sum)*q = 0.0948 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 7.7326 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +12.2867 tokens for 9.7341 repo tokens (UP leg total 20.1141 tokens at stake 15.8377)
  - legs: UP count 20.1141 (stake 15.8377, inMax 15.9168), DOWN count 7.8274 (stake 1.6291, inMax 1.6373); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions

Pairs in total: cost 7.7326 repo tokens, locked gain 0.0948 repo tokens if every repo is evaluated and every child resolves to a score (heterogeneous tokens, informational).

### 5b. Set rows: set-sell and merge-arb (7 markets)

- **dappnode/DAppNode** set-sell: 17.2804 sets, proceeds ~ 17.7652, gain ~ 0.4848 repo tokens, keeps 17.2804 child Invalid [0.181278 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 11.427032885205643741, DOWN leg >= 6.249359228040212057. Fresh spot sum 1.057417.
- **shazow/whatsabi** set-sell: 20.7975 sets, proceeds ~ 21.6437, gain ~ 0.8462 repo tokens, keeps 20.7975 child Invalid [0.220854 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 15.877349403693805325, DOWN leg >= 5.658124886823708444. Fresh spot sum 1.084973.
- **Commit-Boost/commit-boost-client** set-sell: 15.7931 sets, proceeds ~ 16.2914, gain ~ 0.4983 repo tokens, keeps 15.7931 child Invalid [0.166239 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 11.835110680413810786, DOWN leg >= 4.374865810947331857. Fresh spot sum 1.065289.
- **holiman/goevmlab** set-sell: 17.5316 sets, proceeds ~ 18.1860, gain ~ 0.6544 repo tokens, keeps 17.5316 child Invalid [0.185572 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 12.830234082642468554, DOWN leg >= 5.264848843080095197. Fresh spot sum 1.077659.
- **OffchainLabs/stylus-sdk-rs** set-sell: 21.4833 sets, proceeds ~ 22.1304, gain ~ 0.6470 repo tokens, keeps 21.4833 child Invalid [0.225820 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 16.854572081761135897, DOWN leg >= 5.165154771881594867. Fresh spot sum 1.061787.
- **alloy-rs/alloy** set-sell: 20.0571 sets, proceeds ~ 20.7853, gain ~ 0.7282 repo tokens, keeps 20.0571 child Invalid [0.212094 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 15.693506529280767153, DOWN leg >= 4.987819432148790265. Fresh spot sum 1.075461.
- **argotorg/fe** set-sell: 15.3170 sets, proceeds ~ 15.7248, gain ~ 0.4078 repo tokens, keeps 15.3170 child Invalid [0.160457 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 11.936218647400645784, DOWN leg >= 3.709928914319002262. Fresh spot sum 1.054775.

### 5c. Complex-buy (53 groups: split `x = stake`, sell the other leg, buy the own leg with the proceeds; keeps `x` child Invalid; the last two transactions are rebuilt at send time with the realised proceeds)

- **ethereum/py_ecc** complex-buy UP: split x = 13.9107 repo tokens [0.141945 sUSDS-eq], sell x DOWN for P = 2.8433 repo tokens, buy 3.4261 UP -> **17.3368 UP + 13.9107 child Invalid** (quoted total; F's simple-route count 16.5852; complex 4.531% vs the simple route); spot sum 1.04893 > 1; p_win 0.8500
- **blockscout/blockscout** complex-buy UP: split x = 7.3040 repo tokens [0.074530 sUSDS-eq], sell x DOWN for P = 2.3057 repo tokens, buy 3.3397 UP -> **10.6437 UP + 7.3040 child Invalid** (quoted total; F's simple-route count 10.5203; complex 1.173% vs the simple route); spot sum 1.01143 > 1; p_win 0.7000
- **herumi/mcl** complex-buy UP: split x = 39.3089 repo tokens [0.401111 sUSDS-eq], sell x DOWN for P = 6.3354 repo tokens, buy 7.5557 UP -> **46.8645 UP + 39.3089 child Invalid** (quoted total; F's simple-route count 45.3931; complex 3.242% vs the simple route); spot sum 1.01299 > 1; p_win 0.9000
- **paulmillr/noble-curves** complex-buy UP: split x = 56.2795 repo tokens [0.574280 sUSDS-eq], sell x DOWN for P = 11.5999 repo tokens, buy 15.0922 UP -> **71.3717 UP + 56.2795 child Invalid** (quoted total; F's simple-route count 70.0430; complex 1.897% vs the simple route); spot sum 1.01697 > 1; p_win 0.8500
- **flashbots/rbuilder** complex-buy UP: split x = 8.3158 repo tokens [0.084856 sUSDS-eq], sell x DOWN for P = 2.2326 repo tokens, buy 3.0239 UP -> **11.3397 UP + 8.3158 child Invalid** (quoted total; F's simple-route count 11.1888; complex 1.349% vs the simple route); spot sum 1.01123 > 1; p_win 0.7500
- **l2beat/l2beat** complex-buy UP: split x = 6.8180 repo tokens [0.069571 sUSDS-eq], sell x DOWN for P = 1.5097 repo tokens, buy 1.9103 UP -> **8.7283 UP + 6.8180 child Invalid** (quoted total; F's simple-route count 8.5813; complex 1.713% vs the simple route); spot sum 1.01647 > 1; p_win 0.8000
- **Consensys/gnark-crypto** complex-buy UP: split x = 23.2027 repo tokens [0.236762 sUSDS-eq], sell x DOWN for P = 3.7553 repo tokens, buy 4.3434 UP -> **27.5461 UP + 23.2027 child Invalid** (quoted total; F's simple-route count 26.3505; complex 4.538% vs the simple route); spot sum 1.04060 > 1; p_win 0.9000
- **taikoxyz/taiko-mono** complex-buy UP: split x = 11.0002 repo tokens [0.112247 sUSDS-eq], sell x DOWN for P = 2.9589 repo tokens, buy 4.0261 UP -> **15.0263 UP + 11.0002 child Invalid** (quoted total; F's simple-route count 14.8402; complex 1.254% vs the simple route); spot sum 1.01166 > 1; p_win 0.7500
- **ethereum/js-ethereum-cryptography** complex-buy DOWN: split x = 9.0334 repo tokens [0.092177 sUSDS-eq], sell x UP for P = 4.9326 repo tokens, buy 10.1771 DOWN -> **19.2105 DOWN + 9.0334 child Invalid** (quoted total; F's simple-route count 17.9282; complex 7.152% vs the simple route); spot sum 1.01099 > 1; p_win 0.5500
- **wighawag/hardhat-deploy** complex-buy UP: split x = 8.6143 repo tokens [0.087901 sUSDS-eq], sell x DOWN for P = 2.3480 repo tokens, buy 3.1844 UP -> **11.7988 UP + 8.6143 child Invalid** (quoted total; F's simple-route count 11.5996; complex 1.717% vs the simple route); spot sum 1.01290 > 1; p_win 0.7500
- **Plonky3/Plonky3** complex-buy UP: split x = 6.8006 repo tokens [0.069394 sUSDS-eq], sell x DOWN for P = 1.4880 repo tokens, buy 1.8832 UP -> **8.6838 UP + 6.8006 child Invalid** (quoted total; F's simple-route count 8.5600; complex 1.445% vs the simple route); spot sum 1.01267 > 1; p_win 0.8000
- **intellij-solidity/intellij-solidity** complex-buy UP: split x = 7.2701 repo tokens [0.074185 sUSDS-eq], sell x DOWN for P = 1.6374 repo tokens, buy 2.0742 UP -> **9.3443 UP + 7.2701 child Invalid** (quoted total; F's simple-route count 9.1561; complex 2.055% vs the simple route); spot sum 1.01826 > 1; p_win 0.8000
- **dappnode/DAppNode** complex-buy UP: split x = 28.3787 repo tokens [0.289579 sUSDS-eq], sell x DOWN for P = 8.9841 repo tokens, buy 13.5543 UP -> **41.9330 UP + 28.3787 child Invalid** (quoted total; F's simple-route count 41.8798, on the post-set-sell book; complex 0.127% vs the simple route); spot sum 1.05742 > 1; p_win 0.7000
- **wealdtech/ethdo** complex-buy UP: split x = 7.0874 repo tokens [0.072320 sUSDS-eq], sell x DOWN for P = 1.8936 repo tokens, buy 2.5583 UP -> **9.6456 UP + 7.0874 child Invalid** (quoted total; F's simple-route count 9.5219; complex 1.300% vs the simple route); spot sum 1.01187 > 1; p_win 0.7500
- **lambdaclass/lambdaworks** complex-buy UP: split x = 15.7226 repo tokens [0.160435 sUSDS-eq], sell x DOWN for P = 2.7937 repo tokens, buy 3.3792 UP -> **19.1019 UP + 15.7226 child Invalid** (quoted total; F's simple-route count 18.7816; complex 1.705% vs the simple route); spot sum 1.01436 > 1; p_win 0.8500
- **smartcontracts/simple-optimism-node** complex-buy UP: split x = 16.4033 repo tokens [0.167380 sUSDS-eq], sell x DOWN for P = 7.6467 repo tokens, buy 14.4485 UP -> **30.8517 UP + 16.4033 child Invalid** (quoted total; F's simple-route count 30.5832; complex 0.878% vs the simple route); spot sum 1.00294 > 1; p_win 0.5500
- **skalenetwork/libBLS** complex-buy UP: split x = 8.0048 repo tokens [0.081682 sUSDS-eq], sell x DOWN for P = 2.1575 repo tokens, buy 2.9196 UP -> **10.9244 UP + 8.0048 child Invalid** (quoted total; F's simple-route count 10.7650; complex 1.481% vs the simple route); spot sum 1.01377 > 1; p_win 0.7500
- **shazow/whatsabi** complex-buy UP: split x = 59.6817 repo tokens [0.608997 sUSDS-eq], sell x DOWN for P = 11.2685 repo tokens, buy 14.7532 UP -> **74.4349 UP + 59.6817 child Invalid** (quoted total; F's simple-route count 74.4952, on the post-set-sell book; complex -0.081% vs the simple route); spot sum 1.08497 > 1; p_win 0.8500
- **succinctlabs/sp1** complex-buy UP: split x = 11.2298 repo tokens [0.114590 sUSDS-eq], sell x DOWN for P = 3.0457 repo tokens, buy 4.1519 UP -> **15.3817 UP + 11.2298 child Invalid** (quoted total; F's simple-route count 15.1664; complex 1.420% vs the simple route); spot sum 1.00871 > 1; p_win 0.7500
- **otterscan/otterscan** complex-buy DOWN: split x = 3.2636 repo tokens [0.033302 sUSDS-eq], sell x UP for P = 2.3827 repo tokens, buy 8.2914 DOWN -> **11.5550 DOWN + 3.2636 child Invalid** (quoted total; F's simple-route count 11.2544; complex 2.671% vs the simple route); spot sum 1.01234 > 1; p_win 0.3000
- **lambdaclass/ethrex** complex-buy UP: split x = 15.1103 repo tokens [0.154187 sUSDS-eq], sell x DOWN for P = 3.2748 repo tokens, buy 4.2069 UP -> **19.3173 UP + 15.1103 child Invalid** (quoted total; F's simple-route count 19.1799; complex 0.716% vs the simple route); spot sum 1.00522 > 1; p_win 0.8000
- **Commit-Boost/commit-boost-client** complex-buy UP: split x = 35.7789 repo tokens [0.365091 sUSDS-eq], sell x DOWN for P = 7.7437 repo tokens, buy 10.3233 UP -> **46.1023 UP + 35.7789 child Invalid** (quoted total; F's simple-route count 46.3704, on the post-set-sell book; complex -0.578% vs the simple route); spot sum 1.06529 > 1; p_win 0.8000
- **0xMiden/miden-vm** complex-buy UP: split x = 29.4563 repo tokens [0.300575 sUSDS-eq], sell x DOWN for P = 5.7363 repo tokens, buy 7.1087 UP -> **36.5650 UP + 29.4563 child Invalid** (quoted total; F's simple-route count 35.6684; complex 2.514% vs the simple route); spot sum 1.02328 > 1; p_win 0.8500
- **holiman/goevmlab** complex-buy UP: split x = 47.7564 repo tokens [0.487310 sUSDS-eq], sell x DOWN for P = 10.4880 repo tokens, buy 14.2920 UP -> **62.0484 UP + 47.7564 child Invalid** (quoted total; F's simple-route count 62.6685, on the post-set-sell book; complex -0.990% vs the simple route); spot sum 1.07766 > 1; p_win 0.8000
- **edb-rs/edb** complex-buy UP: split x = 36.8961 repo tokens [0.376491 sUSDS-eq], sell x DOWN for P = 9.2990 repo tokens, buy 12.4535 UP -> **49.3496 UP + 36.8961 child Invalid** (quoted total; F's simple-route count 47.9797; complex 2.855% vs the simple route); spot sum 1.01756 > 1; p_win 0.8000
- **succinctlabs/rsp** complex-buy DOWN: split x = 2.7397 repo tokens [0.027957 sUSDS-eq], sell x UP for P = 1.8099 repo tokens, buy 4.7147 DOWN -> **7.4545 DOWN + 2.7397 child Invalid** (quoted total; F's simple-route count 7.0635; complex 5.535% vs the simple route); spot sum 1.03810 > 1; p_win 0.4000
- **OffchainLabs/stylus-sdk-rs** complex-buy UP: split x = 15.3892 repo tokens [0.157033 sUSDS-eq], sell x DOWN for P = 3.3041 repo tokens, buy 4.2488 UP -> **19.6380 UP + 15.3892 child Invalid** (quoted total; F's simple-route count 19.5446, on the post-set-sell book; complex 0.478% vs the simple route); spot sum 1.06179 > 1; p_win 0.8000
- **ethstaker/ethstaker-deposit-cli** complex-buy DOWN: split x = 6.5258 repo tokens [0.066590 sUSDS-eq], sell x UP for P = 3.8751 repo tokens, buy 9.1422 DOWN -> **15.6680 DOWN + 6.5258 child Invalid** (quoted total; F's simple-route count 15.1344; complex 3.526% vs the simple route); spot sum 1.00993 > 1; p_win 0.4500
- **dl-solarity/solidity-lib** complex-buy UP: split x = 17.3975 repo tokens [0.177526 sUSDS-eq], sell x DOWN for P = 5.1593 repo tokens, buy 7.1025 UP -> **24.5000 UP + 17.3975 child Invalid** (quoted total; F's simple-route count 23.6365; complex 3.653% vs the simple route); spot sum 1.03641 > 1; p_win 0.7500
- **powdr-labs/powdr** complex-buy UP: split x = 33.6925 repo tokens [0.343801 sUSDS-eq], sell x DOWN for P = 7.0410 repo tokens, buy 8.8072 UP -> **42.4998 UP + 33.6925 child Invalid** (quoted total; F's simple-route count 41.0208; complex 3.605% vs the simple route); spot sum 1.02374 > 1; p_win 0.8500
- **axiom-crypto/snark-verifier** complex-buy DOWN: split x = 2.4286 repo tokens [0.024782 sUSDS-eq], sell x UP for P = 1.6407 repo tokens, buy 4.8232 DOWN -> **7.2519 DOWN + 2.4286 child Invalid** (quoted total; F's simple-route count 7.0902; complex 2.279% vs the simple route); spot sum 1.01209 > 1; p_win 0.3500
- **swiss-knife-xyz/swiss-knife** complex-buy DOWN: split x = 4.1067 repo tokens [0.041905 sUSDS-eq], sell x UP for P = 3.0983 repo tokens, buy 11.1734 DOWN -> **15.2801 DOWN + 4.1067 child Invalid** (quoted total; F's simple-route count 14.5863; complex 4.756% vs the simple route); spot sum 1.02115 > 1; p_win 0.3000
- **a16z/helios** complex-buy UP: split x = 11.1497 repo tokens [0.113772 sUSDS-eq], sell x DOWN for P = 2.3775 repo tokens, buy 3.0351 UP -> **14.1848 UP + 11.1497 child Invalid** (quoted total; F's simple-route count 14.1025; complex 0.584% vs the simple route); spot sum 1.00045 > 1; p_win 0.8000
- **alloy-rs/alloy** complex-buy UP: split x = 47.3755 repo tokens [0.483424 sUSDS-eq], sell x DOWN for P = 8.7262 repo tokens, buy 11.1728 UP -> **58.5483 UP + 47.3755 child Invalid** (quoted total; F's simple-route count 58.4004, on the post-set-sell book; complex 0.253% vs the simple route); spot sum 1.07546 > 1; p_win 0.8500
- **apeworx/ape** complex-buy UP: split x = 12.1983 repo tokens [0.124472 sUSDS-eq], sell x DOWN for P = 3.3078 repo tokens, buy 4.5114 UP -> **16.7097 UP + 12.1983 child Invalid** (quoted total; F's simple-route count 16.4789; complex 1.401% vs the simple route); spot sum 1.01250 > 1; p_win 0.7500
- **consensys/teku** complex-buy UP: split x = 11.8201 repo tokens [0.120614 sUSDS-eq], sell x DOWN for P = 2.6255 repo tokens, buy 3.3514 UP -> **15.1715 UP + 11.8201 child Invalid** (quoted total; F's simple-route count 14.9506; complex 1.478% vs the simple route); spot sum 1.01624 > 1; p_win 0.8000
- **erigontech/erigon** complex-buy UP: split x = 11.7606 repo tokens [0.120006 sUSDS-eq], sell x DOWN for P = 3.1915 repo tokens, buy 4.3490 UP -> **16.1096 UP + 11.7606 child Invalid** (quoted total; F's simple-route count 15.8797; complex 1.447% vs the simple route); spot sum 1.01322 > 1; p_win 0.7500
- **ethereum-lists/chains** complex-buy UP: split x = 15.4152 repo tokens [0.157298 sUSDS-eq], sell x DOWN for P = 4.1992 repo tokens, buy 5.7705 UP -> **21.1857 UP + 15.4152 child Invalid** (quoted total; F's simple-route count 20.9161; complex 1.289% vs the simple route); spot sum 1.00613 > 1; p_win 0.7500
- **ethereum/execution-apis** complex-buy UP: split x = 6.9737 repo tokens [0.071160 sUSDS-eq], sell x DOWN for P = 1.4802 repo tokens, buy 1.8727 UP -> **8.8463 UP + 6.9737 child Invalid** (quoted total; F's simple-route count 8.7761; complex 0.800% vs the simple route); spot sum 1.01834 > 1; p_win 0.8000
- **argotorg/fe** complex-buy UP: split x = 47.4247 repo tokens [0.483926 sUSDS-eq], sell x DOWN for P = 8.7990 repo tokens, buy 11.2685 UP -> **58.6932 UP + 47.4247 child Invalid** (quoted total; F's simple-route count 58.4705, on the post-set-sell book; complex 0.381% vs the simple route); spot sum 1.05477 > 1; p_win 0.8500
- **ethers-io/ethers.js** complex-buy DOWN: split x = 1.2136 repo tokens [0.012383 sUSDS-eq], sell x UP for P = 1.0724 repo tokens, buy 7.5739 DOWN -> **8.7874 DOWN + 1.2136 child Invalid** (quoted total; F's simple-route count 8.5202; complex 3.136% vs the simple route); spot sum 1.01991 > 1; p_win 0.1500
- **grandinetech/grandine** complex-buy UP: split x = 9.1484 repo tokens [0.093351 sUSDS-eq], sell x DOWN for P = 2.0712 repo tokens, buy 2.6321 UP -> **11.7806 UP + 9.1484 child Invalid** (quoted total; F's simple-route count 11.5426; complex 2.062% vs the simple route); spot sum 1.01907 > 1; p_win 0.8000
- **hyperledger-web3j/web3j** complex-buy UP: split x = 7.3422 repo tokens [0.074921 sUSDS-eq], sell x DOWN for P = 1.9652 repo tokens, buy 2.6563 UP -> **9.9985 UP + 7.3422 child Invalid** (quoted total; F's simple-route count 9.8670; complex 1.332% vs the simple route); spot sum 1.01212 > 1; p_win 0.7500
- **nethereum/nethereum** complex-buy UP: split x = 9.5455 repo tokens [0.097403 sUSDS-eq], sell x DOWN for P = 1.5810 repo tokens, buy 1.8917 UP -> **11.4372 UP + 9.5455 child Invalid** (quoted total; F's simple-route count 11.3338; complex 0.912% vs the simple route); spot sum 1.00721 > 1; p_win 0.8500
- **openzeppelin/openzeppelin-contracts** complex-buy UP: split x = 14.0024 repo tokens [0.142882 sUSDS-eq], sell x DOWN for P = 2.5124 repo tokens, buy 3.0299 UP -> **17.0323 UP + 14.0024 child Invalid** (quoted total; F's simple-route count 16.6992; complex 1.994% vs the simple route); spot sum 1.01707 > 1; p_win 0.8500
- **safe-global/safe-smart-account** complex-buy UP: split x = 58.4780 repo tokens [0.596714 sUSDS-eq], sell x DOWN for P = 14.9347 repo tokens, buy 19.9248 UP -> **78.4029 UP + 58.4780 child Invalid** (quoted total; F's simple-route count 73.9614; complex 6.005% vs the simple route); spot sum 1.01161 > 1; p_win 0.8500
- **sigp/lighthouse** complex-buy UP: split x = 7.1690 repo tokens [0.073154 sUSDS-eq], sell x DOWN for P = 1.2568 repo tokens, buy 1.4971 UP -> **8.6662 UP + 7.1690 child Invalid** (quoted total; F's simple-route count 8.4920; complex 2.051% vs the simple route); spot sum 1.02094 > 1; p_win 0.8500
- **status-im/nimbus-eth2** complex-buy UP: split x = 9.7612 repo tokens [0.099604 sUSDS-eq], sell x DOWN for P = 1.2347 repo tokens, buy 1.3950 UP -> **11.1562 UP + 9.7612 child Invalid** (quoted total; F's simple-route count 10.9428; complex 1.950% vs the simple route); spot sum 1.02128 > 1; p_win 0.9000
- **vyperlang/titanoboa** complex-buy UP: split x = 9.9360 repo tokens [0.101388 sUSDS-eq], sell x DOWN for P = 2.8814 repo tokens, buy 3.9119 UP -> **13.8479 UP + 9.9360 child Invalid** (quoted total; F's simple-route count 13.3890; complex 3.428% vs the simple route); spot sum 1.03467 > 1; p_win 0.7500
- **ethdebug/format** complex-buy UP: split x = 28.5774 repo tokens [0.291607 sUSDS-eq], sell x DOWN for P = 5.1755 repo tokens, buy 6.4139 UP -> **34.9914 UP + 28.5774 child Invalid** (quoted total; F's simple-route count 34.5971; complex 1.140% vs the simple route); spot sum 1.00010 > 1; p_win 0.8500
- **ethpandaops/ethereum-helm-charts** complex-buy UP: split x = 14.6438 repo tokens [0.149427 sUSDS-eq], sell x DOWN for P = 6.1721 repo tokens, buy 10.6289 UP -> **25.2727 UP + 14.6438 child Invalid** (quoted total; F's simple-route count 24.9184; complex 1.422% vs the simple route); spot sum 1.00823 > 1; p_win 0.6000
- **ethpandaops/checkpointz** complex-buy UP: split x = 49.1489 repo tokens [0.501520 sUSDS-eq], sell x DOWN for P = 20.7220 repo tokens, buy 35.9329 UP -> **85.0818 UP + 49.1489 child Invalid** (quoted total; F's simple-route count 81.6064; complex 4.259% vs the simple route); spot sum 1.00976 > 1; p_win 0.6500
- **lambdaclass/lambda_ethereum_consensus** complex-buy UP: split x = 16.3117 repo tokens [0.166446 sUSDS-eq], sell x DOWN for P = 3.5882 repo tokens, buy 4.6205 UP -> **20.9322 UP + 16.3117 child Invalid** (quoted total; F's simple-route count 20.7329; complex 0.961% vs the simple route); spot sum 1.00640 > 1; p_win 0.8000

### 5d. Simple-buy (10 groups: one approve and one `exactInputSingle`, min 99.5% of the quote)

- **DefiLlama/chainlist** simple-buy DOWN: stake 8.7414 repo tokens [0.089198 sUSDS-eq], quoted out 31.4809 DOWN (F count 31.4809), floor 31.3235; spot sum 0.97923 < 1; p_win 0.3000
- **ChainSafe/bls** simple-buy DOWN: stake 16.8990 repo tokens [0.172438 sUSDS-eq], quoted out 36.3319 DOWN (F count 36.3319), floor 36.1502; spot sum 0.99990 < 1; p_win 0.5000
- **Cyfrin/aderyn** simple-buy UP: stake 10.6453 repo tokens [0.108626 sUSDS-eq], quoted out 15.3852 UP (F count 15.3852), floor 15.3082; spot sum 0.99990 < 1; p_win 0.7000
- **eth-infinitism/account-abstraction** simple-buy UP: stake 29.2619 repo tokens [0.298591 sUSDS-eq], quoted out 43.3012 UP (F count 43.3012), floor 43.0847; spot sum 0.99755 < 1; p_win 0.7000
- **ethereum/consensus-specs** simple-buy UP: stake 11.8368 repo tokens [0.120784 sUSDS-eq], quoted out 13.2939 UP (F count 13.2939), floor 13.2275; spot sum 0.97797 < 1; p_win 0.9000
- **ipsilon/evmone** simple-buy UP: stake 34.4617 repo tokens [0.351650 sUSDS-eq], quoted out 42.0009 UP (F count 42.0009), floor 41.7909; spot sum 0.98729 < 1; p_win 0.8500
- **foundry-rs/foundry** simple-buy UP: stake 8.6802 repo tokens [0.088574 sUSDS-eq], quoted out 10.2990 UP (F count 10.2990), floor 10.2475; spot sum 0.98179 < 1; p_win 0.8500
- **nomicfoundation/hardhat** simple-buy UP: stake 15.4789 repo tokens [0.157948 sUSDS-eq], quoted out 19.6506 UP (F count 19.6506), floor 19.5523; spot sum 0.99139 < 1; p_win 0.8000
- **argotorg/hevm** simple-buy UP: stake 19.4902 repo tokens [0.198880 sUSDS-eq], quoted out 24.8565 UP (F count 24.8565), floor 24.7322; spot sum 0.99990 < 1; p_win 0.8000
- **erigontech/silkworm** simple-buy UP: stake 51.8035 repo tokens [0.528608 sUSDS-eq], quoted out 68.3220 UP (F count 68.3220), floor 67.9804; spot sum 0.99998 < 1; p_win 0.8000

### 5e. Skipped rows (0: never sent; the executor writes each `status: "skipped"` with its reason)

- none

## 6. Group order and gas (send order)

| # | group | tx | gas used |
|---|---|---|---|
| 0 | `mint-middle-A` | 0-1 | 4,073,717 |
| 1 | `mint-middle-B` | 2-3 | 4,214,166 |
| 2 | `mint-middle-C` | 4-5 | 4,130,570 |
| 3 | `complex-buy:ethereum/py_ecc:UP` | 6-11 | 976,787 |
| 4 | `complex-buy:blockscout/blockscout:UP` | 12-17 | 875,415 |
| 5 | `complex-buy:herumi/mcl:UP` | 18-23 | 913,372 |
| 6 | `complex-buy:paulmillr/noble-curves:UP` | 24-29 | 1,077,448 |
| 7 | `complex-buy:flashbots/rbuilder:UP` | 30-35 | 921,001 |
| 8 | `complex-buy:l2beat/l2beat:UP` | 36-41 | 933,518 |
| 9 | `complex-buy:Consensys/gnark-crypto:UP` | 42-47 | 918,827 |
| 10 | `complex-buy:taikoxyz/taiko-mono:UP` | 48-53 | 877,586 |
| 11 | `complex-buy:ethereum/js-ethereum-cryptography:DOWN` | 54-59 | 910,705 |
| 12 | `complex-buy:wighawag/hardhat-deploy:UP` | 60-65 | 898,316 |
| 13 | `simple-buy:DefiLlama/chainlist:DOWN` | 66-67 | 209,690 |
| 14 | `complex-buy:Plonky3/Plonky3:UP` | 68-73 | 857,154 |
| 15 | `simple-buy:ChainSafe/bls:DOWN` | 74-75 | 184,603 |
| 16 | `complex-buy:intellij-solidity/intellij-solidity:UP` | 76-81 | 885,248 |
| 17 | `set-sell:dappnode/DAppNode` | 82-87 | 895,654 |
| 18 | `complex-buy:dappnode/DAppNode:UP` | 88-93 | 919,397 |
| 19 | `complex-buy:wealdtech/ethdo:UP` | 94-99 | 873,336 |
| 20 | `complex-buy:lambdaclass/lambdaworks:UP` | 100-105 | 939,939 |
| 21 | `complex-buy:smartcontracts/simple-optimism-node:UP` | 106-111 | 889,024 |
| 22 | `complex-buy:skalenetwork/libBLS:UP` | 112-117 | 885,734 |
| 23 | `set-sell:shazow/whatsabi` | 118-123 | 925,607 |
| 24 | `complex-buy:shazow/whatsabi:UP` | 124-129 | 998,155 |
| 25 | `complex-buy:succinctlabs/sp1:UP` | 130-135 | 921,953 |
| 26 | `complex-buy:otterscan/otterscan:DOWN` | 136-141 | 885,979 |
| 27 | `complex-buy:lambdaclass/ethrex:UP` | 142-147 | 901,597 |
| 28 | `set-sell:Commit-Boost/commit-boost-client` | 148-153 | 919,045 |
| 29 | `complex-buy:Commit-Boost/commit-boost-client:UP` | 154-159 | 964,068 |
| 30 | `simple-buy:Cyfrin/aderyn:UP` | 160-161 | 155,914 |
| 31 | `complex-buy:0xMiden/miden-vm:UP` | 162-167 | 968,601 |
| 32 | `set-sell:holiman/goevmlab` | 168-173 | 907,142 |
| 33 | `complex-buy:holiman/goevmlab:UP` | 174-179 | 964,774 |
| 34 | `complex-buy:edb-rs/edb:UP` | 180-185 | 919,541 |
| 35 | `complex-buy:succinctlabs/rsp:DOWN` | 186-191 | 921,761 |
| 36 | `set-sell:OffchainLabs/stylus-sdk-rs` | 192-197 | 923,981 |
| 37 | `complex-buy:OffchainLabs/stylus-sdk-rs:UP` | 198-203 | 893,812 |
| 38 | `complex-buy:ethstaker/ethstaker-deposit-cli:DOWN` | 204-209 | 874,672 |
| 39 | `complex-buy:dl-solarity/solidity-lib:UP` | 210-215 | 877,972 |
| 40 | `complex-buy:powdr-labs/powdr:UP` | 216-221 | 942,940 |
| 41 | `complex-buy:axiom-crypto/snark-verifier:DOWN` | 222-227 | 901,754 |
| 42 | `complex-buy:swiss-knife-xyz/swiss-knife:DOWN` | 228-233 | 948,746 |
| 43 | `complex-buy:a16z/helios:UP` | 234-239 | 906,760 |
| 44 | `set-sell:alloy-rs/alloy` | 240-245 | 945,937 |
| 45 | `complex-buy:alloy-rs/alloy:UP` | 246-251 | 971,782 |
| 46 | `complex-buy:apeworx/ape:UP` | 252-257 | 913,258 |
| 47 | `complex-buy:consensys/teku:UP` | 258-263 | 912,738 |
| 48 | `complex-buy:erigontech/erigon:UP` | 264-269 | 924,677 |
| 49 | `simple-buy:eth-infinitism/account-abstraction:UP` | 270-271 | 169,946 |
| 50 | `complex-buy:ethereum-lists/chains:UP` | 272-277 | 905,990 |
| 51 | `simple-buy:ethereum/consensus-specs:UP` | 278-279 | 165,587 |
| 52 | `simple-buy:ipsilon/evmone:UP` | 280-281 | 186,976 |
| 53 | `complex-buy:ethereum/execution-apis:UP` | 282-287 | 915,810 |
| 54 | `set-sell:argotorg/fe` | 288-293 | 910,612 |
| 55 | `complex-buy:argotorg/fe:UP` | 294-299 | 978,696 |
| 56 | `complex-buy:ethers-io/ethers.js:DOWN` | 300-305 | 895,982 |
| 57 | `simple-buy:foundry-rs/foundry:UP` | 306-307 | 155,227 |
| 58 | `complex-buy:grandinetech/grandine:UP` | 308-313 | 852,955 |
| 59 | `complex-buy:hyperledger-web3j/web3j:UP` | 314-319 | 862,737 |
| 60 | `complex-buy:nethereum/nethereum:UP` | 320-325 | 889,796 |
| 61 | `simple-buy:nomicfoundation/hardhat:UP` | 326-327 | 172,940 |
| 62 | `complex-buy:openzeppelin/openzeppelin-contracts:UP` | 328-333 | 883,673 |
| 63 | `dual-buy:OffchainLabs/prysm` | 334-337 | 356,390 |
| 64 | `complex-buy:safe-global/safe-smart-account:UP` | 338-343 | 965,880 |
| 65 | `complex-buy:sigp/lighthouse:UP` | 344-349 | 904,383 |
| 66 | `complex-buy:status-im/nimbus-eth2:UP` | 350-355 | 914,773 |
| 67 | `complex-buy:vyperlang/titanoboa:UP` | 356-361 | 912,560 |
| 68 | `simple-buy:argotorg/hevm:UP` | 362-363 | 162,508 |
| 69 | `complex-buy:ethdebug/format:UP` | 364-369 | 935,508 |
| 70 | `complex-buy:ethpandaops/ethereum-helm-charts:UP` | 370-375 | 906,216 |
| 71 | `complex-buy:ethpandaops/checkpointz:UP` | 376-381 | 934,606 |
| 72 | `complex-buy:lambdaclass/lambda_ethereum_consensus:UP` | 382-387 | 899,533 |
| 73 | `simple-buy:erigontech/silkworm:UP` | 388-389 | 177,173 |

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
