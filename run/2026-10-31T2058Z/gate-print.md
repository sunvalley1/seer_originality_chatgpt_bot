# G gate print - run 2026-10-31T2058Z

**Optimism mainnet, holder 0x2AD670e5953a85C998cDf1C2f6D74386aB735d4a. Built, simulated and verified: nothing has been signed or sent.** Pending nonce 4359; head at G's read 158940857 (blocks are reported, never compared between reads). Every group below is an ordered sequence of single transactions, one signer call each.

## 1. The numbers

| | |
|---|---|
| **Allocation input** | `run/2026-10-31T2058Z/allocation.json` (sha256 `3b948575a7e93578434bbe740cd1c3588486aeb9b203aeaea461cae2445ff94d`), generated 2026-10-31T21:01:24Z, 69 rows; 62 markets traded, 0 rows skipped (section 5e) |
| **Counts per route** | pair (`dual-buy`) **0** markets (0 rows); `simple-buy` **10**; `complex-buy` **52** (45 single-side markets with spot sum > 1, plus 7 on a market whose `set-sell` runs first); `set-sell` **7**; `merge-arb` (`buy-and-merge`) **0**; mint groups **0**; PSM3 ramp: none |
| **Total sUSDS staked** | **0 sUSDS** = `totals.staked` = the new mint `M` (no parent split: the rows spend repo tokens the holder already holds). Middles split: none. Each traded market's budget is its held repo tokens plus m_X; the rows' stakes sum to 1330.3512 repo tokens of 62 different tokens (13.5750 sUSDS-equivalent at the labelled 1/98) |
| **Expected value** | **0.504032 sUSDS** at the labelled 1/N = 1/98 (F's `totals.expected_value`; 49.3952 repo tokens summed over heterogeneous markets, / 98; 0 for any repo that is not evaluated) |
| **Worst case** | `correlated_worst_case` **0.000000 sUSDS** (F's definition); a `set-sell` row's gain is locked only if its whole group lands |
| **Number of transactions** | **374** in **69** keep-whole groups (complex-buy 312, simple-buy 20, set-sell 42), nonces 4359 to 4732 |
| **Estimated gas** | **55,851,958 gas used** (mints 0; complex-buy 47,675,398; simple-buy 1,756,945; set-sell 6,419,615); sum of the gas limits 76,578,640, largest limit 861,588 (2^24 = 16,777,216). In ETH: **0.000056187201543448 ETH** at `eth_gasPrice` 1000308 wei (execution 0.000055869160403064 + L1 data fee 0.000000318041140384 from `GasPriceOracle.getL1Fee`), at most 0.000112056361946512 ETH at the signer's ceiling (2 x gas price); about **0.1128 sUSDS** (2238.03 USD/ETH from QuoterV2 WETH/USDC fee 500, / 1.114756 USD per sUSDS from PSM3) |
| **Simulation** | 1 `eth_simulateV1` request(s) (helper `simulate`, one `blockStateCalls` entry per keep-whole group), no state overrides: `all_success` **true**, `failed_count` 0, `clamped_count` 0, `over_cap_count` 0, pending nonce 4359 |

## 2. ETH for gas

The holder holds **0.00519431856602798 ETH**; `eth_gasPrice` 1000308 wei (base fee 308 wei). The simulation runs with `validation: false` and does not see ETH, so it is walked here: the signer refuses a transaction unless the balance covers `gasLimit x maxFeePerGas` (execution only), and before each group G section 8 asks for ETH >= 0.002 ETH + the group's `gas_limit x 2 x eth_gasPrice`. The executor makes that check fresh before each group; this is a projection.

| price assumption | effective price | cost of all 374 transactions (execution + L1 data fee) | starting balance the walk needs | first transaction the signer would refuse | first group failing the affordability gate | lowest balance at a group start |
|---|---|---|---|---|---|---|
| effective price = eth_gasPrice (what the node suggests) | 1000308 wei | 0.000056187201543448 ETH | 0.000056629585710478 ETH | none | none | 0.005138310476844721 ETH (group 68) |
| effective price = the signer's ceiling maxFeePerGas = 2 x eth_gasPrice | 2000616 wei | 0.000112056361946512 ETH | 0.000112124851619411 ETH | none | none | 0.005082618544010941 ETH (group 68) |

Result: **no ETH shortfall** under either assumption.

## 3. Drift, the simulation, and what was checked

- **Pool drift since F sized the plan** (`run/2026-10-31T2058Z/planner/g-drift.json`): 0 of 124 pools moved, on 0 market(s). A moved pool is reported, never stale by itself; each call carries its own floor and the pre-send re-check decides. Fresh quotes vs F's `quoted_fill`: largest relative gap 7.12e-15 (drift, not a check).
- **Simulation**: one request: the whole ordered sequence. 69 entries and 374 calls in all, from the holder, in send order.
- **Gas limits** are the helper's `gas_limit` per call, copied, never computed by hand: `ceil(maxUsedGas x 1.2)` on every call; the largest is 861,588.
- **Calldata**: all 374 calldatas re-encoded by the helper's `encode` equal the ethers encoding (bytes and keccak256); the signer's policy-only `check` **allowed all 374** signer-input files (`run/2026-10-31T2058Z/g-tx/tx-NNN.json`, each `{"calls":[one call],"gasLimit":"<helper gas_limit>"}`).
- **End state**: the simulated end state equals the prediction on **236 of 236** probed balances.
- **Independent read**: not run (`--indep` not given; it is supervised-only, because the helper pins one RPC).
- **Trading boundary at build**: 62 of 62 children clear at block 158940860 (timestamp 1793480497); parent and 3 middles payoutDenominator 0/0/0/0. Re-read immediately before every group at send time.
- **Route of a market with a `set` row** (dappnode/DAppNode): fresh spot sum 1.057406 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.
- **Route of a market with a `set` row** (shazow/whatsabi): fresh spot sum 1.083521 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.
- **Route of a market with a `set` row** (Commit-Boost/commit-boost-client): fresh spot sum 1.064402 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.
- **Route of a market with a `set` row** (holiman/goevmlab): fresh spot sum 1.076185 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.
- **Route of a market with a `set` row** (OffchainLabs/stylus-sdk-rs): fresh spot sum 1.061774 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.
- **Route of a market with a `set` row** (alloy-rs/alloy): fresh spot sum 1.074096 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.
- **Route of a market with a `set` row** (argotorg/fe): fresh spot sum 1.054736 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.

## 4. Mints (0 groups at the head of the sequence, each `[approve, split]`)

- none: M = 0 and no bundle token is held for a bundle with a position, so no split is emitted (G section 1).

## 5. Per-market print (units: the row's own repo token; sUSDS equivalent at the labelled 1/98 in brackets)

### 5a. Pairs: `dual-buy`, "pair (sum < 1 - f)", f = 0.0001 (0 markets)


### 5b. Set rows: set-sell and merge-arb (7 markets)

- **dappnode/DAppNode** set-sell: 17.2772 sets, proceeds ~ 17.7618, gain ~ 0.4846 repo tokens, keeps 17.2772 child Invalid [0.181243 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 11.424760332566897881, DOWN leg >= 6.24825874675538239. Fresh spot sum 1.057406.
- **shazow/whatsabi** set-sell: 20.4993 sets, proceeds ~ 21.3197, gain ~ 0.8204 repo tokens, keeps 20.4993 child Invalid [0.217548 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 15.650918265790284992, DOWN leg >= 5.562207865924688023. Fresh spot sum 1.083521.
- **Commit-Boost/commit-boost-client** set-sell: 15.6025 sets, proceeds ~ 16.0883, gain ~ 0.4858 repo tokens, keeps 15.6025 child Invalid [0.164166 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 11.691913207861688695, DOWN leg >= 4.315940129493970308. Fresh spot sum 1.064402.
- **holiman/goevmlab** set-sell: 17.2454 sets, proceeds ~ 17.8773, gain ~ 0.6319 repo tokens, keeps 17.2454 child Invalid [0.182421 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 12.621614859881043601, DOWN leg >= 5.166284935306548206. Fresh spot sum 1.076185.
- **OffchainLabs/stylus-sdk-rs** set-sell: 21.4787 sets, proceeds ~ 22.1254, gain ~ 0.6468 repo tokens, keeps 21.4787 child Invalid [0.225770 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 16.850699926848837261, DOWN leg >= 5.164109130687663811. Fresh spot sum 1.061774.
- **alloy-rs/alloy** set-sell: 19.7490 sets, proceeds ~ 20.4535, gain ~ 0.7045 repo tokens, keeps 19.7490 child Invalid [0.208709 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 15.453733164232439384, DOWN leg >= 4.897451713065898056. Fresh spot sum 1.074096.
- **argotorg/fe** set-sell: 15.3070 sets, proceeds ~ 15.7142, gain ~ 0.4072 repo tokens, keeps 15.3070 child Invalid [0.160349 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 11.928331347412636997, DOWN leg >= 3.707322448929882142. Fresh spot sum 1.054736.

### 5c. Complex-buy (52 groups: split `x = stake`, sell the other leg, buy the own leg with the proceeds; keeps `x` child Invalid; the last two transactions are rebuilt at send time with the realised proceeds)

- **ethereum/py_ecc** complex-buy UP: split x = 13.9189 repo tokens [0.142030 sUSDS-eq], sell x DOWN for P = 2.8336 repo tokens, buy 3.4145 UP -> **17.3334 UP + 13.9189 child Invalid** (quoted total; F's simple-route count 16.5952; complex 4.448% vs the simple route); spot sum 1.04800 > 1; p_win 0.8500
- **blockscout/blockscout** complex-buy UP: split x = 7.2940 repo tokens [0.074428 sUSDS-eq], sell x DOWN for P = 2.3026 repo tokens, buy 3.3352 UP -> **10.6291 UP + 7.2940 child Invalid** (quoted total; F's simple-route count 10.5058; complex 1.174% vs the simple route); spot sum 1.01144 > 1; p_win 0.7000
- **herumi/mcl** complex-buy UP: split x = 39.3089 repo tokens [0.401111 sUSDS-eq], sell x DOWN for P = 6.3374 repo tokens, buy 7.5580 UP -> **46.8669 UP + 39.3089 child Invalid** (quoted total; F's simple-route count 45.3931; complex 3.247% vs the simple route); spot sum 1.01305 > 1; p_win 0.9000
- **paulmillr/noble-curves** complex-buy UP: split x = 56.2695 repo tokens [0.574178 sUSDS-eq], sell x DOWN for P = 11.5983 repo tokens, buy 15.0898 UP -> **71.3593 UP + 56.2695 child Invalid** (quoted total; F's simple-route count 70.0298; complex 1.898% vs the simple route); spot sum 1.01698 > 1; p_win 0.8500
- **flashbots/rbuilder** complex-buy UP: split x = 8.3158 repo tokens [0.084856 sUSDS-eq], sell x DOWN for P = 2.2331 repo tokens, buy 3.0245 UP -> **11.3403 UP + 8.3158 child Invalid** (quoted total; F's simple-route count 11.1888; complex 1.355% vs the simple route); spot sum 1.01129 > 1; p_win 0.7500
- **Consensys/gnark-crypto** complex-buy UP: split x = 23.2754 repo tokens [0.237504 sUSDS-eq], sell x DOWN for P = 3.7494 repo tokens, buy 4.3373 UP -> **27.6126 UP + 23.2754 child Invalid** (quoted total; F's simple-route count 26.4348; complex 4.456% vs the simple route); spot sum 1.03965 > 1; p_win 0.9000
- **taikoxyz/taiko-mono** complex-buy UP: split x = 10.9896 repo tokens [0.112139 sUSDS-eq], sell x DOWN for P = 2.9534 repo tokens, buy 4.0185 UP -> **15.0082 UP + 10.9896 child Invalid** (quoted total; F's simple-route count 14.8257; complex 1.231% vs the simple route); spot sum 1.01141 > 1; p_win 0.7500
- **ethereum/js-ethereum-cryptography** complex-buy DOWN: split x = 9.0334 repo tokens [0.092177 sUSDS-eq], sell x UP for P = 4.9327 repo tokens, buy 10.1774 DOWN -> **19.2107 DOWN + 9.0334 child Invalid** (quoted total; F's simple-route count 17.9282; complex 7.154% vs the simple route); spot sum 1.01100 > 1; p_win 0.5500
- **wighawag/hardhat-deploy** complex-buy UP: split x = 8.6143 repo tokens [0.087901 sUSDS-eq], sell x DOWN for P = 2.3484 repo tokens, buy 3.1849 UP -> **11.7993 UP + 8.6143 child Invalid** (quoted total; F's simple-route count 11.5996; complex 1.721% vs the simple route); spot sum 1.01295 > 1; p_win 0.7500
- **Plonky3/Plonky3** complex-buy UP: split x = 6.8006 repo tokens [0.069394 sUSDS-eq], sell x DOWN for P = 1.4885 repo tokens, buy 1.8837 UP -> **8.6843 UP + 6.8006 child Invalid** (quoted total; F's simple-route count 8.5600; complex 1.452% vs the simple route); spot sum 1.01274 > 1; p_win 0.8000
- **intellij-solidity/intellij-solidity** complex-buy UP: split x = 7.2701 repo tokens [0.074185 sUSDS-eq], sell x DOWN for P = 1.6378 repo tokens, buy 2.0747 UP -> **9.3448 UP + 7.2701 child Invalid** (quoted total; F's simple-route count 9.1561; complex 2.061% vs the simple route); spot sum 1.01833 > 1; p_win 0.8000
- **dappnode/DAppNode** complex-buy UP: split x = 28.3831 repo tokens [0.289624 sUSDS-eq], sell x DOWN for P = 8.9855 repo tokens, buy 13.5567 UP -> **41.9398 UP + 28.3831 child Invalid** (quoted total; F's simple-route count 41.8866, on the post-set-sell book; complex 0.127% vs the simple route); spot sum 1.05741 > 1; p_win 0.7000
- **wealdtech/ethdo** complex-buy UP: split x = 7.0874 repo tokens [0.072320 sUSDS-eq], sell x DOWN for P = 1.8941 repo tokens, buy 2.5589 UP -> **9.6462 UP + 7.0874 child Invalid** (quoted total; F's simple-route count 9.5219; complex 1.306% vs the simple route); spot sum 1.01194 > 1; p_win 0.7500
- **lambdaclass/lambdaworks** complex-buy UP: split x = 15.7226 repo tokens [0.160435 sUSDS-eq], sell x DOWN for P = 2.7949 repo tokens, buy 3.3808 UP -> **19.1034 UP + 15.7226 child Invalid** (quoted total; F's simple-route count 18.7816; complex 1.713% vs the simple route); spot sum 1.01444 > 1; p_win 0.8500
- **smartcontracts/simple-optimism-node** complex-buy UP: split x = 16.3933 repo tokens [0.167278 sUSDS-eq], sell x DOWN for P = 7.6422 repo tokens, buy 14.4396 UP -> **30.8328 UP + 16.3933 child Invalid** (quoted total; F's simple-route count 30.5641; complex 0.879% vs the simple route); spot sum 1.00295 > 1; p_win 0.5500
- **skalenetwork/libBLS** complex-buy UP: split x = 8.0048 repo tokens [0.081682 sUSDS-eq], sell x DOWN for P = 2.1580 repo tokens, buy 2.9203 UP -> **10.9251 UP + 8.0048 child Invalid** (quoted total; F's simple-route count 10.7650; complex 1.488% vs the simple route); spot sum 1.01384 > 1; p_win 0.7500
- **shazow/whatsabi** complex-buy UP: split x = 59.5316 repo tokens [0.607465 sUSDS-eq], sell x DOWN for P = 11.2372 repo tokens, buy 14.7083 UP -> **74.2399 UP + 59.5316 child Invalid** (quoted total; F's simple-route count 74.2964, on the post-set-sell book; complex -0.076% vs the simple route); spot sum 1.08352 > 1; p_win 0.8500
- **succinctlabs/sp1** complex-buy UP: split x = 11.2198 repo tokens [0.114488 sUSDS-eq], sell x DOWN for P = 3.0430 repo tokens, buy 4.1482 UP -> **15.3680 UP + 11.2198 child Invalid** (quoted total; F's simple-route count 15.1527; complex 1.421% vs the simple route); spot sum 1.00873 > 1; p_win 0.7500
- **otterscan/otterscan** complex-buy DOWN: split x = 3.2536 repo tokens [0.033200 sUSDS-eq], sell x UP for P = 2.3754 repo tokens, buy 8.2650 DOWN -> **11.5185 DOWN + 3.2536 child Invalid** (quoted total; F's simple-route count 11.2187; complex 2.672% vs the simple route); spot sum 1.01240 > 1; p_win 0.3000
- **lambdaclass/ethrex** complex-buy UP: split x = 15.1103 repo tokens [0.154187 sUSDS-eq], sell x DOWN for P = 3.2759 repo tokens, buy 4.2083 UP -> **19.3186 UP + 15.1103 child Invalid** (quoted total; F's simple-route count 19.1799; complex 0.724% vs the simple route); spot sum 1.00530 > 1; p_win 0.8000
- **Commit-Boost/commit-boost-client** complex-buy UP: split x = 35.7215 repo tokens [0.364505 sUSDS-eq], sell x DOWN for P = 7.7308 repo tokens, buy 10.3050 UP -> **46.0265 UP + 35.7215 child Invalid** (quoted total; F's simple-route count 46.2932, on the post-set-sell book; complex -0.576% vs the simple route); spot sum 1.06440 > 1; p_win 0.8000
- **Cyfrin/aderyn** complex-buy UP: split x = 10.6952 repo tokens [0.109135 sUSDS-eq], sell x DOWN for P = 3.2370 repo tokens, buy 4.7166 UP -> **15.4118 UP + 10.6952 child Invalid** (quoted total; F's simple-route count 15.4581; complex -0.299% vs the simple route); spot sum 1.00003 > 1; p_win 0.7000
- **0xMiden/miden-vm** complex-buy UP: split x = 29.4643 repo tokens [0.300657 sUSDS-eq], sell x DOWN for P = 5.7372 repo tokens, buy 7.1099 UP -> **36.5743 UP + 29.4643 child Invalid** (quoted total; F's simple-route count 35.6784; complex 2.511% vs the simple route); spot sum 1.02324 > 1; p_win 0.8500
- **holiman/goevmlab** complex-buy UP: split x = 47.6189 repo tokens [0.485907 sUSDS-eq], sell x DOWN for P = 10.4566 repo tokens, buy 14.2457 UP -> **61.8646 UP + 47.6189 child Invalid** (quoted total; F's simple-route count 62.4792, on the post-set-sell book; complex -0.984% vs the simple route); spot sum 1.07618 > 1; p_win 0.8000
- **edb-rs/edb** complex-buy UP: split x = 36.8961 repo tokens [0.376491 sUSDS-eq], sell x DOWN for P = 9.3008 repo tokens, buy 12.4559 UP -> **49.3520 UP + 36.8961 child Invalid** (quoted total; F's simple-route count 47.9797; complex 2.860% vs the simple route); spot sum 1.01762 > 1; p_win 0.8000
- **succinctlabs/rsp** complex-buy DOWN: split x = 2.7435 repo tokens [0.027995 sUSDS-eq], sell x UP for P = 1.8124 repo tokens, buy 4.7214 DOWN -> **7.4649 DOWN + 2.7435 child Invalid** (quoted total; F's simple-route count 7.0735; complex 5.534% vs the simple route); spot sum 1.03806 > 1; p_win 0.4000
- **OffchainLabs/stylus-sdk-rs** complex-buy UP: split x = 15.3934 repo tokens [0.157075 sUSDS-eq], sell x DOWN for P = 3.3050 repo tokens, buy 4.2500 UP -> **19.6434 UP + 15.3934 child Invalid** (quoted total; F's simple-route count 19.5499, on the post-set-sell book; complex 0.478% vs the simple route); spot sum 1.06177 > 1; p_win 0.8000
- **ethstaker/ethstaker-deposit-cli** complex-buy DOWN: split x = 6.5158 repo tokens [0.066488 sUSDS-eq], sell x UP for P = 3.8692 repo tokens, buy 9.1274 DOWN -> **15.6432 DOWN + 6.5158 child Invalid** (quoted total; F's simple-route count 15.1102; complex 3.528% vs the simple route); spot sum 1.00998 > 1; p_win 0.4500
- **dl-solarity/solidity-lib** complex-buy UP: split x = 17.3975 repo tokens [0.177526 sUSDS-eq], sell x DOWN for P = 5.1546 repo tokens, buy 7.0960 UP -> **24.4935 UP + 17.3975 child Invalid** (quoted total; F's simple-route count 23.6365; complex 3.626% vs the simple route); spot sum 1.03611 > 1; p_win 0.7500
- **powdr-labs/powdr** complex-buy UP: split x = 33.7005 repo tokens [0.343882 sUSDS-eq], sell x DOWN for P = 7.0425 repo tokens, buy 8.8093 UP -> **42.5097 UP + 33.7005 child Invalid** (quoted total; F's simple-route count 41.0308; complex 3.604% vs the simple route); spot sum 1.02373 > 1; p_win 0.8500
- **axiom-crypto/snark-verifier** complex-buy DOWN: split x = 2.4320 repo tokens [0.024816 sUSDS-eq], sell x UP for P = 1.6429 repo tokens, buy 4.8300 DOWN -> **7.2620 DOWN + 2.4320 child Invalid** (quoted total; F's simple-route count 7.1002; complex 2.278% vs the simple route); spot sum 1.01205 > 1; p_win 0.3500
- **swiss-knife-xyz/swiss-knife** complex-buy DOWN: split x = 4.1093 repo tokens [0.041932 sUSDS-eq], sell x UP for P = 3.1002 repo tokens, buy 11.1810 DOWN -> **15.2903 DOWN + 4.1093 child Invalid** (quoted total; F's simple-route count 14.5963; complex 4.755% vs the simple route); spot sum 1.02111 > 1; p_win 0.3000
- **a16z/helios** complex-buy UP: split x = 11.1497 repo tokens [0.113772 sUSDS-eq], sell x DOWN for P = 2.3780 repo tokens, buy 3.0357 UP -> **14.1854 UP + 11.1497 child Invalid** (quoted total; F's simple-route count 14.1025; complex 0.588% vs the simple route); spot sum 1.00050 > 1; p_win 0.8000
- **alloy-rs/alloy** complex-buy UP: split x = 47.2142 repo tokens [0.481777 sUSDS-eq], sell x DOWN for P = 8.6932 repo tokens, buy 11.1272 UP -> **58.3414 UP + 47.2142 child Invalid** (quoted total; F's simple-route count 58.1920, on the post-set-sell book; complex 0.257% vs the simple route); spot sum 1.07410 > 1; p_win 0.8500
- **apeworx/ape** complex-buy UP: split x = 12.1983 repo tokens [0.124472 sUSDS-eq], sell x DOWN for P = 3.3086 repo tokens, buy 4.5125 UP -> **16.7107 UP + 12.1983 child Invalid** (quoted total; F's simple-route count 16.4789; complex 1.407% vs the simple route); spot sum 1.01256 > 1; p_win 0.7500
- **consensys/teku** complex-buy UP: split x = 11.8101 repo tokens [0.120511 sUSDS-eq], sell x DOWN for P = 2.6234 repo tokens, buy 3.3487 UP -> **15.1588 UP + 11.8101 child Invalid** (quoted total; F's simple-route count 14.9378; complex 1.480% vs the simple route); spot sum 1.01625 > 1; p_win 0.8000
- **erigontech/erigon** complex-buy UP: split x = 11.7506 repo tokens [0.119904 sUSDS-eq], sell x DOWN for P = 3.1889 repo tokens, buy 4.3454 UP -> **16.0959 UP + 11.7506 child Invalid** (quoted total; F's simple-route count 15.8661; complex 1.449% vs the simple route); spot sum 1.01323 > 1; p_win 0.7500
- **ethereum-lists/chains** complex-buy UP: split x = 15.4152 repo tokens [0.157298 sUSDS-eq], sell x DOWN for P = 4.1999 repo tokens, buy 5.7714 UP -> **21.1866 UP + 15.4152 child Invalid** (quoted total; F's simple-route count 20.9161; complex 1.293% vs the simple route); spot sum 1.00617 > 1; p_win 0.7500
- **argotorg/fe** complex-buy UP: split x = 47.4247 repo tokens [0.483926 sUSDS-eq], sell x DOWN for P = 8.7990 repo tokens, buy 11.2685 UP -> **58.6932 UP + 47.4247 child Invalid** (quoted total; F's simple-route count 58.4705, on the post-set-sell book; complex 0.381% vs the simple route); spot sum 1.05474 > 1; p_win 0.8500
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

### 5d. Simple-buy (10 groups: one approve and one `exactInputSingle`, min 99.5% of the quote)

- **DefiLlama/chainlist** simple-buy DOWN: stake 8.7314 repo tokens [0.089096 sUSDS-eq], quoted out 31.4420 DOWN (F count 31.4420), floor 31.2848; spot sum 0.97928 < 1; p_win 0.3000
- **ChainSafe/bls** simple-buy DOWN: stake 16.8990 repo tokens [0.172438 sUSDS-eq], quoted out 36.3319 DOWN (F count 36.3319), floor 36.1502; spot sum 0.99992 < 1; p_win 0.5000
- **eth-infinitism/account-abstraction** simple-buy UP: stake 29.2519 repo tokens [0.298489 sUSDS-eq], quoted out 43.2859 UP (F count 43.2859), floor 43.0694; spot sum 0.99756 < 1; p_win 0.7000
- **ethereum/consensus-specs** simple-buy UP: stake 11.8368 repo tokens [0.120784 sUSDS-eq], quoted out 13.2939 UP (F count 13.2939), floor 13.2275; spot sum 0.97797 < 1; p_win 0.9000
- **ipsilon/evmone** simple-buy UP: stake 34.4617 repo tokens [0.351650 sUSDS-eq], quoted out 42.0009 UP (F count 42.0009), floor 41.7909; spot sum 0.98734 < 1; p_win 0.8500
- **foundry-rs/foundry** simple-buy UP: stake 8.6802 repo tokens [0.088574 sUSDS-eq], quoted out 10.2990 UP (F count 10.2990), floor 10.2475; spot sum 0.98186 < 1; p_win 0.8500
- **nomicfoundation/hardhat** simple-buy UP: stake 15.4789 repo tokens [0.157948 sUSDS-eq], quoted out 19.6506 UP (F count 19.6506), floor 19.5523; spot sum 0.99139 < 1; p_win 0.8000
- **OffchainLabs/prysm** simple-buy UP: stake 15.8377 repo tokens [0.161609 sUSDS-eq], quoted out 20.1141 UP (F count 20.1141), floor 20.0135; spot sum 0.97605 < 1; p_win 0.8000
- **argotorg/hevm** simple-buy UP: stake 19.4902 repo tokens [0.198880 sUSDS-eq], quoted out 24.8565 UP (F count 24.8565), floor 24.7322; spot sum 0.99997 < 1; p_win 0.8000
- **erigontech/silkworm** simple-buy UP: stake 51.7935 repo tokens [0.528505 sUSDS-eq], quoted out 68.3081 UP (F count 68.3081), floor 67.9666; spot sum 0.99999 < 1; p_win 0.8000

### 5e. Skipped rows (0: never sent; the executor writes each `status: "skipped"` with its reason)

- none

## 6. Group order and gas (send order)

| # | group | tx | gas used |
|---|---|---|---|
| 0 | `complex-buy:ethereum/py_ecc:UP` | 0-5 | 969,341 |
| 1 | `complex-buy:blockscout/blockscout:UP` | 6-11 | 874,417 |
| 2 | `complex-buy:herumi/mcl:UP` | 12-17 | 912,392 |
| 3 | `complex-buy:paulmillr/noble-curves:UP` | 18-23 | 1,060,338 |
| 4 | `complex-buy:flashbots/rbuilder:UP` | 24-29 | 921,019 |
| 5 | `complex-buy:Consensys/gnark-crypto:UP` | 30-35 | 918,877 |
| 6 | `complex-buy:taikoxyz/taiko-mono:UP` | 36-41 | 877,532 |
| 7 | `complex-buy:ethereum/js-ethereum-cryptography:DOWN` | 42-47 | 910,705 |
| 8 | `complex-buy:wighawag/hardhat-deploy:UP` | 48-53 | 897,348 |
| 9 | `simple-buy:DefiLlama/chainlist:DOWN` | 54-55 | 209,690 |
| 10 | `complex-buy:Plonky3/Plonky3:UP` | 56-61 | 857,126 |
| 11 | `simple-buy:ChainSafe/bls:DOWN` | 62-63 | 184,603 |
| 12 | `complex-buy:intellij-solidity/intellij-solidity:UP` | 64-69 | 886,204 |
| 13 | `set-sell:dappnode/DAppNode` | 70-75 | 895,654 |
| 14 | `complex-buy:dappnode/DAppNode:UP` | 76-81 | 919,397 |
| 15 | `complex-buy:wealdtech/ethdo:UP` | 82-87 | 874,332 |
| 16 | `complex-buy:lambdaclass/lambdaworks:UP` | 88-93 | 939,919 |
| 17 | `complex-buy:smartcontracts/simple-optimism-node:UP` | 94-99 | 889,030 |
| 18 | `complex-buy:skalenetwork/libBLS:UP` | 100-105 | 884,768 |
| 19 | `set-sell:shazow/whatsabi` | 106-111 | 926,603 |
| 20 | `complex-buy:shazow/whatsabi:UP` | 112-117 | 998,129 |
| 21 | `complex-buy:succinctlabs/sp1:UP` | 118-123 | 921,963 |
| 22 | `complex-buy:otterscan/otterscan:DOWN` | 124-129 | 887,031 |
| 23 | `complex-buy:lambdaclass/ethrex:UP` | 130-135 | 900,585 |
| 24 | `set-sell:Commit-Boost/commit-boost-client` | 136-141 | 917,982 |
| 25 | `complex-buy:Commit-Boost/commit-boost-client:UP` | 142-147 | 964,060 |
| 26 | `complex-buy:Cyfrin/aderyn:UP` | 148-153 | 908,009 |
| 27 | `complex-buy:0xMiden/miden-vm:UP` | 154-159 | 969,587 |
| 28 | `set-sell:holiman/goevmlab` | 160-165 | 906,198 |
| 29 | `complex-buy:holiman/goevmlab:UP` | 166-171 | 964,798 |
| 30 | `complex-buy:edb-rs/edb:UP` | 172-177 | 919,555 |
| 31 | `complex-buy:succinctlabs/rsp:DOWN` | 178-183 | 921,833 |
| 32 | `set-sell:OffchainLabs/stylus-sdk-rs` | 184-189 | 923,955 |
| 33 | `complex-buy:OffchainLabs/stylus-sdk-rs:UP` | 190-195 | 893,857 |
| 34 | `complex-buy:ethstaker/ethstaker-deposit-cli:DOWN` | 196-201 | 874,678 |
| 35 | `complex-buy:dl-solarity/solidity-lib:UP` | 202-207 | 877,968 |
| 36 | `complex-buy:powdr-labs/powdr:UP` | 208-213 | 942,966 |
| 37 | `complex-buy:axiom-crypto/snark-verifier:DOWN` | 214-219 | 901,754 |
| 38 | `complex-buy:swiss-knife-xyz/swiss-knife:DOWN` | 220-225 | 955,190 |
| 39 | `complex-buy:a16z/helios:UP` | 226-231 | 906,762 |
| 40 | `set-sell:alloy-rs/alloy` | 232-237 | 938,623 |
| 41 | `complex-buy:alloy-rs/alloy:UP` | 238-243 | 972,778 |
| 42 | `complex-buy:apeworx/ape:UP` | 244-249 | 913,254 |
| 43 | `complex-buy:consensys/teku:UP` | 250-255 | 911,732 |
| 44 | `complex-buy:erigontech/erigon:UP` | 256-261 | 924,681 |
| 45 | `simple-buy:eth-infinitism/account-abstraction:UP` | 262-263 | 169,946 |
| 46 | `complex-buy:ethereum-lists/chains:UP` | 264-269 | 905,990 |
| 47 | `simple-buy:ethereum/consensus-specs:UP` | 270-271 | 165,587 |
| 48 | `simple-buy:ipsilon/evmone:UP` | 272-273 | 186,976 |
| 49 | `set-sell:argotorg/fe` | 274-279 | 910,600 |
| 50 | `complex-buy:argotorg/fe:UP` | 280-285 | 978,696 |
| 51 | `complex-buy:ethers-io/ethers.js:DOWN` | 286-291 | 895,998 |
| 52 | `simple-buy:foundry-rs/foundry:UP` | 292-293 | 155,227 |
| 53 | `complex-buy:grandinetech/grandine:UP` | 294-299 | 851,995 |
| 54 | `complex-buy:hyperledger-web3j/web3j:UP` | 300-305 | 863,665 |
| 55 | `complex-buy:nethereum/nethereum:UP` | 306-311 | 889,834 |
| 56 | `simple-buy:nomicfoundation/hardhat:UP` | 312-313 | 172,940 |
| 57 | `complex-buy:openzeppelin/openzeppelin-contracts:UP` | 314-319 | 884,645 |
| 58 | `simple-buy:OffchainLabs/prysm:UP` | 320-321 | 172,295 |
| 59 | `complex-buy:safe-global/safe-smart-account:UP` | 322-327 | 965,896 |
| 60 | `complex-buy:sigp/lighthouse:UP` | 328-333 | 904,327 |
| 61 | `complex-buy:status-im/nimbus-eth2:UP` | 334-339 | 922,076 |
| 62 | `complex-buy:vyperlang/titanoboa:UP` | 340-345 | 912,532 |
| 63 | `simple-buy:argotorg/hevm:UP` | 346-347 | 162,508 |
| 64 | `complex-buy:ethdebug/format:UP` | 348-353 | 935,530 |
| 65 | `complex-buy:ethpandaops/ethereum-helm-charts:UP` | 354-359 | 906,206 |
| 66 | `complex-buy:ethpandaops/checkpointz:UP` | 360-365 | 934,556 |
| 67 | `complex-buy:lambdaclass/lambda_ethereum_consensus:UP` | 366-371 | 899,537 |
| 68 | `simple-buy:erigontech/silkworm:UP` | 372-373 | 177,173 |

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

- calldata audit: 69 groups, 374 transactions decoded and re-derived from allocation.json (69 rows: 69 in groups, 0 skipped), kinds {"complex-buy":52,"simple-buy":10,"set-sell":7}, every approval exact (none near 2^256), every swap recipient the holder, every tier the candidates.json tier, dual-buy inMax = min(stake x 1.005, remaining); failures 0
- fresh re-simulation of run/2026-10-31T2058Z/g-sim-main.json (sha256 fab030c3d150b886895145262a364133ad39746d032f3cffb159704781a48d5e): {"entries":69,"count":374,"all_success":true,"failed_count":0,"over_cap_count":0,"clamped_count":0,"pending_nonce":4359,"overrides_active":"absent","no_max_used_gas_count":0}
- holder nonce latest/pending before 4359/4359, after 4359/4359 (the plan's 4359); per-call rows of the fresh simulation: 374 checked, every status 0x1 and every fresh peak within the plan's gas_limit; gasUsed equal to the build's on all
- AUDIT PASSED: every acceptance check holds
