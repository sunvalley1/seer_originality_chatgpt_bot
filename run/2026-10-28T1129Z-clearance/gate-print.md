# G gate print - run 2026-10-28T1129Z-clearance

**Optimism mainnet, holder 0x2AD670e5953a85C998cDf1C2f6D74386aB735d4a. Built, simulated and verified: nothing has been signed or sent.** Pending nonce 2693; head at G's read 158794243 (blocks are reported, never compared between reads). Every group below is an ordered sequence of single transactions, one signer call each.

## 1. The numbers

| | |
|---|---|
| **Allocation input** | `run/2026-10-28T1129Z-clearance/allocation.json` (sha256 `bc25db0c93f468f2b6b9b272503da7ef9292f06026d3d4434c73726485828261`), generated 2026-10-28T11:33:51Z, 155 rows; 92 markets traded, 0 rows skipped (section 5e) |
| **Counts per route** | pair (`dual-buy`) **31** markets (62 rows); `simple-buy` **42**; `complex-buy` **15** (15 single-side markets with spot sum > 1); `set-sell` **0**; `merge-arb` (`buy-and-merge`) **36**; mint groups **4** (mint-parent, mint-middle-A, mint-middle-B, mint-middle-C); PSM3 ramp: none |
| **Total sUSDS staked** | **143.444913115499 sUSDS** = `totals.staked` = the new mint `M` (the holder holds 666.632973623565635236). Middles split: A by m_X = 143.444913115499, B by m_X = 143.444913115499, C by m_X = 143.444913115499. Each traded market's budget is its held repo tokens plus m_X; the rows' stakes sum to 3877.5159 repo tokens of 92 different tokens (39.5665 sUSDS-equivalent at the labelled 1/98) |
| **Expected value** | **2.212101 sUSDS** at the labelled 1/N = 1/98 (F's `totals.expected_value`; 216.7859 repo tokens summed over heterogeneous markets, / 98; 0 for any repo that is not evaluated) |
| **Worst case** | `correlated_worst_case` **-143.444913 sUSDS** (F's definition); a `set-sell` row's gain is locked only if its whole group lands |
| **Number of transactions** | **558** in **128** keep-whole groups (mint 8, merge-arb 252, simple-buy 84, complex-buy 90, dual-buy 124), nonces 2693 to 3250 |
| **Estimated gas** | **83,604,090 gas used** (mints 13,071,863; merge-arb 36,448,011; simple-buy 7,729,423; complex-buy 14,317,583; dual-buy 12,037,210); sum of the gas limits 112,887,227, largest limit 6,227,228 (2^24 = 16,777,216). In ETH: **0.000084473886570624 ETH** at `eth_gasPrice` 1000288 wei (execution 0.00008362816797792 + L1 data fee 0.000000845718592704 from `GasPriceOracle.getL1Fee`), at most 0.000168102054548544 ETH at the signer's ceiling (2 x gas price); about **0.1782 sUSDS** (2350.48 USD/ETH from QuoterV2 WETH/USDC fee 500, / 1.114370 USD per sUSDS from PSM3) |
| **Simulation** | 2 `eth_simulateV1` request(s) (helper `simulate`, one `blockStateCalls` entry per keep-whole group), **windowed: not one request**, no state overrides: `all_success` **true**, `failed_count` 0, `clamped_count` 0, `over_cap_count` 0, pending nonce 2693 |

## 2. ETH for gas

The holder holds **0.00548971301409488 ETH**; `eth_gasPrice` 1000288 wei (base fee 288 wei). The simulation runs with `validation: false` and does not see ETH, so it is walked here: the signer refuses a transaction unless the balance covers `gasLimit x maxFeePerGas` (execution only), and before each group G section 8 asks for ETH >= 0.002 ETH + the group's `gas_limit x 2 x eth_gasPrice`. The executor makes that check fresh before each group; this is a projection.

| price assumption | effective price | cost of all 558 transactions (execution + L1 data fee) | starting balance the walk needs | first transaction the signer would refuse | first group failing the affordability gate | lowest balance at a group start |
|---|---|---|---|---|---|---|
| effective price = eth_gasPrice (what the node suggests) | 1000288 wei | 0.000084473886570624 ETH | 0.000084700755281116 ETH | none | none | 0.005405644351973661 ETH (group 127) |
| effective price = the signer's ceiling maxFeePerGas = 2 x eth_gasPrice | 2000576 wei | 0.000168102054548544 ETH | 0.000168170277582236 ETH | none | none | 0.005322415011825085 ETH (group 127) |

Result: **no ETH shortfall** under either assumption.

## 3. Drift, the simulation, and what was checked

- **Pool drift since F sized the plan** (`run/2026-10-28T1129Z-clearance/planner/g-drift.json`): 0 of 184 pools moved, on 0 market(s). A moved pool is reported, never stale by itself; each call carries its own floor and the pre-send re-check decides. Fresh quotes vs F's `quoted_fill`: largest relative gap 6.57e-15 (drift, not a check).
- **Simulation**: NOT one request: the plan was cut into windows between markets, each beginning with the mint prefix and simulated from chain state without the earlier windows' effects (G section 8, Money rules). 132 entries and 566 calls in all, from the holder, in send order.
- **Gas limits** are the helper's `gas_limit` per call, copied, never computed by hand: `ceil(maxUsedGas x 1.2)` on every call; the largest is 6,227,228.
- **Calldata**: all 558 calldatas re-encoded by the helper's `encode` equal the ethers encoding (bytes and keccak256); the signer's policy-only `check` **allowed all 558** signer-input files (`run/2026-10-28T1129Z-clearance/g-tx/tx-NNN.json`, each `{"calls":[one call],"gasLimit":"<helper gas_limit>"}`).
- **End state**: the simulated end state equals the prediction on **318 of 318** probed balances.
- **Independent read**: requested (`run/2026-10-28T1129Z-clearance/g-indep-request.json`, 903 reads): run each with a second tool against a second RPC at its block and compare; the helper pins one RPC, so the planner does not make this read itself.
- **Trading boundary at build**: 92 of 92 children clear at block 158794251 (timestamp 1793187279); parent and 3 middles payoutDenominator 0/0/0/0. Re-read immediately before every group at send time.
- **Route of a market with a `set` row** (ethereum/py_ecc): fresh spot sum 0.903507 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (protofire/solhint): fresh spot sum 0.916192 -> simple-buy; sum after its own set-sell 0.993285 -> simple-buy: they agree.
- **Route of a market with a `set` row** (l2beat/l2beat): fresh spot sum 0.942334 -> simple-buy; sum after its own set-sell 0.981557 -> simple-buy: they agree.
- **Route of a market with a `set` row** (taikoxyz/taiko-mono): fresh spot sum 0.917466 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (flashbots/mev-boost): fresh spot sum 0.919977 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (ChainSafe/bls): fresh spot sum 0.892957 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (dappnode/DAppNode): fresh spot sum 0.902338 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (lambdaclass/lambdaworks): fresh spot sum 0.951860 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (shazow/whatsabi): fresh spot sum 0.931608 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (TrueBlocks/trueblocks-core): fresh spot sum 0.887206 -> dual-buy; sum after its own set-sell 0.926654 -> dual-buy: they agree.
- **Route of a market with a `set` row** (succinctlabs/sp1): fresh spot sum 0.940095 -> simple-buy; sum after its own set-sell 0.990600 -> simple-buy: they agree.
- **Route of a market with a `set` row** (otterscan/otterscan): fresh spot sum 0.952925 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (NethermindEth/juno): fresh spot sum 0.911139 -> simple-buy; sum after its own set-sell 0.980729 -> simple-buy: they agree.
- **Route of a market with a `set` row** (0xMiden/miden-vm): fresh spot sum 0.927680 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (holiman/goevmlab): fresh spot sum 0.916025 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (evmts/tevm-monorepo): fresh spot sum 0.905138 -> dual-buy; sum after its own set-sell 0.931438 -> dual-buy: they agree.
- **Route of a market with a `set` row** (succinctlabs/rsp): fresh spot sum 0.846920 -> dual-buy; sum after its own set-sell 0.911746 -> dual-buy: they agree.
- **Route of a market with a `set` row** (risc0/risc0-ethereum): fresh spot sum 0.952055 -> simple-buy; sum after its own set-sell 0.997071 -> simple-buy: they agree.
- **Route of a market with a `set` row** (swiss-knife-xyz/swiss-knife): fresh spot sum 0.921150 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (alloy-rs/alloy): fresh spot sum 0.945040 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (ipsilon/evmone): fresh spot sum 0.957645 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (ethereum/execution-apis): fresh spot sum 0.840654 -> dual-buy; sum after its own set-sell 0.898377 -> dual-buy: they agree.
- **Route of a market with a `set` row** (argotorg/fe): fresh spot sum 0.913370 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (remix-project-org/remix-project): fresh spot sum 0.955548 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (argotorg/solidity): fresh spot sum 0.955300 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (foundry-rs/foundry): fresh spot sum 0.888728 -> dual-buy; sum after its own set-sell 0.947231 -> dual-buy: they agree.
- **Route of a market with a `set` row** (hyperledger/besu): fresh spot sum 0.913204 -> simple-buy; sum after its own set-sell 0.997011 -> simple-buy: they agree.
- **Route of a market with a `set` row** (nomicfoundation/hardhat): fresh spot sum 0.936196 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (openzeppelin/openzeppelin-contracts): fresh spot sum 0.953594 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (status-im/nimbus-eth2): fresh spot sum 0.958034 -> simple-buy; sum after its own set-sell 0.991369 -> simple-buy: they agree.
- **Route of a market with a `set` row** (wevm/viem): fresh spot sum 0.898985 -> dual-buy; sum after its own set-sell 0.938106 -> dual-buy: they agree.
- **Route of a market with a `set` row** (ethpandaops/ethereum-helm-charts): fresh spot sum 0.854027 -> dual-buy; sum after its own set-sell 0.921440 -> dual-buy: they agree.

## 4. Mints (4 groups at the head of the sequence, each `[approve, split]`)

- `mint-parent`: approve sUSDS -> Router (M) ; Router.splitPosition(sUSDS, parent, M) (gas used 51,101 + 596,068)
- `mint-middle-A`: approve bundle A -> Router (m_X) ; Router.splitPosition(sUSDS, middle A, m_X) (gas used 49,001 + 4,044,637)
- `mint-middle-B`: approve bundle B -> Router (m_X) ; Router.splitPosition(sUSDS, middle B, m_X) (gas used 49,001 + 4,151,485)
- `mint-middle-C`: approve bundle C -> Router (m_X) ; Router.splitPosition(sUSDS, middle C, m_X) (gas used 49,001 + 4,081,569)

## 5. Per-market print (units: the row's own repo token; sUSDS equivalent at the labelled 1/98 in brackets)

### 5a. Pairs: `dual-buy`, "pair (sum < 1 - f)", f = 0.0001 (31 markets)

- **arkworks-rs/algebra** pair (sum < 1 - f): q = 12.3953 repo tokens; spot sum 0.96626; locked-in sum = cost/q = 12.1835/12.3953 = 0.98291; cost 12.1835 [0.124321 sUSDS]
  - outcome: +(1 - sum)*q = 0.2118 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 12.1835 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +20.6610 tokens for 17.2699 repo tokens (UP leg total 33.0563 tokens at stake 27.3579)
  - legs: UP count 33.0563 (stake 27.3579, inMax 27.4947), DOWN count 12.3953 (stake 2.0955, inMax 2.1060); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **flashbots/mev-boost-relay** pair (sum < 1 - f): q = 23.7649 repo tokens; spot sum 0.93264; locked-in sum = cost/q = 22.9398/23.7649 = 0.96528; cost 22.9398 [0.234080 sUSDS]
  - outcome: +(1 - sum)*q = 0.8250 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 22.9398 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +13.5009 tokens for 10.6856 repo tokens (UP leg total 37.2658 tokens at stake 28.9518)
  - legs: UP count 37.2658 (stake 28.9518, inMax 29.0966), DOWN count 23.7649 (stake 4.6736, inMax 4.6970); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **wighawag/hardhat-deploy** pair (sum < 1 - f): q = 15.2455 repo tokens; spot sum 0.96490; locked-in sum = cost/q = 14.9758/15.2455 = 0.98231; cost 14.9758 [0.152814 sUSDS]
  - outcome: +(1 - sum)*q = 0.2697 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 14.9758 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +16.0137 tokens for 11.8482 repo tokens (UP leg total 31.2593 tokens at stake 22.8345)
  - legs: UP count 31.2593 (stake 22.8345, inMax 22.9486), DOWN count 15.2455 (stake 3.9895, inMax 4.0094); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **ethstaker/eth-docker** pair (sum < 1 - f): q = 16.2633 repo tokens; spot sum 0.96572; locked-in sum = cost/q = 15.9828/16.2633 = 0.98276; cost 15.9828 [0.163090 sUSDS]
  - outcome: +(1 - sum)*q = 0.2804 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 15.9828 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +50.3946 tokens for 18.8898 repo tokens (DOWN leg total 66.6578 tokens at stake 24.4887)
  - legs: UP count 16.2633 (stake 10.3839, inMax 10.4358), DOWN count 66.6578 (stake 24.4887, inMax 24.6111); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **DefiLlama/DefiLlama-Adapters** pair (sum < 1 - f): q = 13.7117 repo tokens; spot sum 0.95407; locked-in sum = cost/q = 13.3905/13.7117 = 0.97658; cost 13.3905 [0.136637 sUSDS]
  - outcome: +(1 - sum)*q = 0.3212 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 13.3905 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +12.9426 tokens for 3.6509 repo tokens (DOWN leg total 26.6542 tokens at stake 7.0715)
  - legs: UP count 13.7117 (stake 9.9699, inMax 10.0197), DOWN count 26.6542 (stake 7.0715, inMax 7.1069); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **Plonky3/Plonky3** pair (sum < 1 - f): q = 14.2270 repo tokens; spot sum 0.96131; locked-in sum = cost/q = 13.9482/14.2270 = 0.98040; cost 13.9482 [0.142328 sUSDS]
  - outcome: +(1 - sum)*q = 0.2789 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 13.9482 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +29.5519 tokens for 23.0854 repo tokens (UP leg total 43.7789 tokens at stake 33.8165)
  - legs: UP count 43.7789 (stake 33.8165, inMax 33.9855), DOWN count 14.2270 (stake 3.2171, inMax 3.2332); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **smartcontracts/simple-optimism-node** pair (sum < 1 - f): q = 16.6589 repo tokens; spot sum 0.96186; locked-in sum = cost/q = 16.3386/16.6589 = 0.98078; cost 16.3386 [0.166721 sUSDS]
  - outcome: +(1 - sum)*q = 0.3202 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 16.3386 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +33.8588 tokens for 14.3893 repo tokens (DOWN leg total 50.5177 tokens at stake 20.8972)
  - legs: UP count 16.6589 (stake 9.8307, inMax 9.8798), DOWN count 50.5177 (stake 20.8972, inMax 21.0017); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **TrueBlocks/trueblocks-core** pair (sum < 1 - f): q = 23.0870; the pair-cost quote at q failed (print only)
- **succinctlabs/op-succinct** pair (sum < 1 - f): q = 12.9639 repo tokens; spot sum 0.93921; locked-in sum = cost/q = 12.5604/12.9639 = 0.96887; cost 12.5604 [0.128168 sUSDS]
  - outcome: +(1 - sum)*q = 0.4035 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 12.5604 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +82.4358 tokens for 46.7344 repo tokens (UP leg total 95.3997 tokens at stake 53.6190)
  - legs: UP count 95.3997 (stake 53.6190, inMax 53.8871), DOWN count 12.9639 (stake 5.6758, inMax 5.7042); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **lambdaclass/ethrex** pair (sum < 1 - f): q = 12.5933 repo tokens; spot sum 0.95948; locked-in sum = cost/q = 12.3340/12.5933 = 0.97941; cost 12.3340 [0.125858 sUSDS]
  - outcome: +(1 - sum)*q = 0.2593 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 12.3340 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +57.7038 tokens for 44.1116 repo tokens (UP leg total 70.2971 tokens at stake 53.2224)
  - legs: UP count 70.2971 (stake 53.2224, inMax 53.4885), DOWN count 12.5933 (stake 3.2233, inMax 3.2394); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **Commit-Boost/commit-boost-client** pair (sum < 1 - f): q = 9.9640 repo tokens; spot sum 0.96400; locked-in sum = cost/q = 9.7819/9.9640 = 0.98172; cost 9.7819 [0.099815 sUSDS]
  - outcome: +(1 - sum)*q = 0.1822 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 9.7819 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +50.2949 tokens for 38.6908 repo tokens (UP leg total 60.2590 tokens at stake 46.0059)
  - legs: UP count 60.2590 (stake 46.0059, inMax 46.2359), DOWN count 9.9640 (stake 2.4668, inMax 2.4791); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **edb-rs/edb** pair (sum < 1 - f): q = 12.6418 repo tokens; spot sum 0.96523; locked-in sum = cost/q = 12.4198/12.6418 = 0.98244; cost 12.4198 [0.126732 sUSDS]
  - outcome: +(1 - sum)*q = 0.2220 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 12.4198 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +79.9627 tokens for 59.9423 repo tokens (UP leg total 92.6045 tokens at stake 68.7347)
  - legs: UP count 92.6045 (stake 68.7347, inMax 69.0784), DOWN count 12.6418 (stake 3.6273, inMax 3.6455); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **evmts/tevm-monorepo** pair (sum < 1 - f): q = 20.1304; the pair-cost quote at q failed (print only)
- **succinctlabs/rsp** pair (sum < 1 - f): q = 32.1594; the pair-cost quote at q failed (print only)
- **ethstaker/ethstaker-deposit-cli** pair (sum < 1 - f): q = 12.1883 repo tokens; spot sum 0.96674; locked-in sum = cost/q = 11.9839/12.1883 = 0.98323; cost 11.9839 [0.122285 sUSDS]
  - outcome: +(1 - sum)*q = 0.2044 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 11.9839 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +45.0724 tokens for 17.9510 repo tokens (DOWN leg total 57.2607 tokens at stake 22.1177)
  - legs: UP count 12.1883 (stake 7.8172, inMax 7.8563), DOWN count 57.2607 (stake 22.1177, inMax 22.2282); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **powdr-labs/powdr** pair (sum < 1 - f): q = 10.8379 repo tokens; spot sum 0.97164; locked-in sum = cost/q = 10.6831/10.8379 = 0.98571; cost 10.6831 [0.109011 sUSDS]
  - outcome: +(1 - sum)*q = 0.1548 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 10.6831 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +67.6326 tokens for 54.3616 repo tokens (UP leg total 78.4705 tokens at stake 62.5280)
  - legs: UP count 78.4705 (stake 62.5280, inMax 62.8407), DOWN count 10.8379 (stake 2.5167, inMax 2.5292); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **consensys/teku** pair (sum < 1 - f): q = 11.2649 repo tokens; spot sum 0.96256; locked-in sum = cost/q = 11.0506/11.2649 = 0.98097; cost 11.0506 [0.112761 sUSDS]
  - outcome: +(1 - sum)*q = 0.2143 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 11.0506 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +30.1885 tokens for 23.5855 repo tokens (UP leg total 41.4535 tokens at stake 32.1060)
  - legs: UP count 41.4535 (stake 32.1060, inMax 32.2665), DOWN count 11.2649 (stake 2.5301, inMax 2.5427); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **ethereum-lists/chains** pair (sum < 1 - f): q = 12.5683 repo tokens; spot sum 0.96963; locked-in sum = cost/q = 12.3761/12.5683 = 0.98471; cost 12.3761 [0.126287 sUSDS]
  - outcome: +(1 - sum)*q = 0.1921 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 12.3761 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +29.1387 tokens for 21.3300 repo tokens (UP leg total 41.7070 tokens at stake 30.2176)
  - legs: UP count 41.7070 (stake 30.2176, inMax 30.3686), DOWN count 12.5683 (stake 3.4885, inMax 3.5060); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **ethereum/execution-apis** pair (sum < 1 - f): q = 19.5431; the pair-cost quote at q failed (print only)
- **ethers-io/ethers.js** pair (sum < 1 - f): q = 12.7543 repo tokens; spot sum 0.96833; locked-in sum = cost/q = 12.5496/12.7543 = 0.98395; cost 12.5496 [0.128057 sUSDS]
  - outcome: +(1 - sum)*q = 0.2047 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 12.5496 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +28.9459 tokens for 3.6780 repo tokens (DOWN leg total 41.7002 tokens at stake 4.9642)
  - legs: UP count 12.7543 (stake 11.2634, inMax 11.3197), DOWN count 41.7002 (stake 4.9642, inMax 4.9891); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **foundry-rs/foundry** pair (sum < 1 - f): q = 23.3386; the pair-cost quote at q failed (print only)
- **nethermindeth/nethermind** pair (sum < 1 - f): q = 13.9297 repo tokens; spot sum 0.96363; locked-in sum = cost/q = 13.6738/13.9297 = 0.98162; cost 13.6738 [0.139528 sUSDS]
  - outcome: +(1 - sum)*q = 0.2560 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 13.6738 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +18.5157 tokens for 13.6811 repo tokens (UP leg total 32.4454 tokens at stake 23.7095)
  - legs: UP count 32.4454 (stake 23.7095, inMax 23.8280), DOWN count 13.9297 (stake 3.6453, inMax 3.6636); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **OffchainLabs/prysm** pair (sum < 1 - f): q = 9.8956 repo tokens; spot sum 0.96728; locked-in sum = cost/q = 9.7316/9.8956 = 0.98343; cost 9.7316 [0.099302 sUSDS]
  - outcome: +(1 - sum)*q = 0.1640 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 9.7316 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +33.5598 tokens for 26.1491 repo tokens (UP leg total 43.4553 tokens at stake 33.6018)
  - legs: UP count 43.4553 (stake 33.6018, inMax 33.7698), DOWN count 9.8956 (stake 2.2789, inMax 2.2903); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **scaffold-eth/scaffold-eth-2** pair (sum < 1 - f): q = 10.1430 repo tokens; spot sum 0.97655; locked-in sum = cost/q = 10.0238/10.1430 = 0.98825; cost 10.0238 [0.102284 sUSDS]
  - outcome: +(1 - sum)*q = 0.1192 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 10.0238 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +21.5546 tokens for 7.2431 repo tokens (DOWN leg total 31.6976 tokens at stake 10.4552)
  - legs: UP count 10.1430 (stake 6.8117, inMax 6.8458), DOWN count 31.6976 (stake 10.4552, inMax 10.5074); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **sigp/lighthouse** pair (sum < 1 - f): q = 18.5564 repo tokens; spot sum 0.95449; locked-in sum = cost/q = 18.1256/18.5564 = 0.97678; cost 18.1256 [0.184955 sUSDS]
  - outcome: +(1 - sum)*q = 0.4308 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 18.1256 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +18.5010 tokens for 2.5311 repo tokens (DOWN leg total 37.0574 tokens at stake 4.6588)
  - legs: UP count 18.5564 (stake 15.9979, inMax 16.0779), DOWN count 37.0574 (stake 4.6588, inMax 4.6820); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **vyperlang/titanoboa** pair (sum < 1 - f): q = 8.1194 repo tokens; spot sum 0.97487; locked-in sum = cost/q = 8.0167/8.1194 = 0.98735; cost 8.0167 [0.081803 sUSDS]
  - outcome: +(1 - sum)*q = 0.1027 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 8.0167 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +37.3142 tokens for 27.1800 repo tokens (UP leg total 45.4336 tokens at stake 32.8882)
  - legs: UP count 45.4336 (stake 32.8882, inMax 33.0526), DOWN count 8.1194 (stake 2.3085, inMax 2.3201); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **wevm/viem** pair (sum < 1 - f): q = 18.3419; the pair-cost quote at q failed (print only)
- **ethpandaops/ethereum-helm-charts** pair (sum < 1 - f): q = 35.2486; the pair-cost quote at q failed (print only)
- **ethpandaops/checkpointz** pair (sum < 1 - f): q = 11.9541 repo tokens; spot sum 0.97337; locked-in sum = cost/q = 11.7943/11.9541 = 0.98664; cost 11.7943 [0.120350 sUSDS]
  - outcome: +(1 - sum)*q = 0.1597 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 11.7943 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +77.0573 tokens for 46.5999 repo tokens (UP leg total 89.0114 tokens at stake 53.2538)
  - legs: UP count 89.0114 (stake 53.2538, inMax 53.5201), DOWN count 11.9541 (stake 5.1404, inMax 5.1661); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **lambdaclass/lambda_ethereum_consensus** pair (sum < 1 - f): q = 14.0151 repo tokens; spot sum 0.96219; locked-in sum = cost/q = 13.7467/14.0151 = 0.98085; cost 13.7467 [0.140273 sUSDS]
  - outcome: +(1 - sum)*q = 0.2684 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 13.7467 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +20.6829 tokens for 16.2730 repo tokens (UP leg total 34.6980 tokens at stake 26.9977)
  - legs: UP count 34.6980 (stake 26.9977, inMax 27.1327), DOWN count 14.0151 (stake 3.0220, inMax 3.0371); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **erigontech/silkworm** pair (sum < 1 - f): q = 15.2164 repo tokens; spot sum 0.95031; locked-in sum = cost/q = 14.8305/15.2164 = 0.97464; cost 14.8305 [0.151331 sUSDS]
  - outcome: +(1 - sum)*q = 0.3859 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 14.8305 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +68.3916 tokens for 51.8535 repo tokens (UP leg total 83.6081 tokens at stake 62.6617)
  - legs: UP count 83.6081 (stake 62.6617, inMax 62.9750), DOWN count 15.2164 (stake 4.0223, inMax 4.0424); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions

Pairs in total: cost 315.4416 repo tokens, locked gain 6.4315 repo tokens if every repo is evaluated and every child resolves to a score (heterogeneous tokens, informational).

### 5b. Set rows: set-sell and merge-arb (36 markets)

- **ethereum/py_ecc** merge-arb: 26.8586 pairs, cost ~ 25.4901, gain ~ 1.3685 repo tokens now, consumes 26.8586 child Invalid held from earlier runs (I_j 47.4470; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 19.904750774742751921, DOWN 5.712822966422564401 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **protofire/solhint** merge-arb: 24.9900 pairs, cost ~ 23.8282, gain ~ 1.1618 repo tokens now, consumes 24.9900 child Invalid held from earlier runs (I_j 24.9900; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 16.999747241045133348, DOWN 6.947588088439839461 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **l2beat/l2beat** merge-arb: 14.0202 pairs, cost ~ 13.4831, gain ~ 0.5371 repo tokens now, consumes 14.0202 child Invalid held from earlier runs (I_j 14.0202; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 10.57042517164219378, DOWN 2.980042046966857079 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **taikoxyz/taiko-mono** merge-arb: 27.6202 pairs, cost ~ 26.4418, gain ~ 1.1784 repo tokens now, consumes 27.6202 child Invalid held from earlier runs (I_j 46.4711; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 18.669472974462489056, DOWN 7.904545576166300576 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **flashbots/mev-boost** merge-arb: 40.9259 pairs, cost ~ 39.2434, gain ~ 1.6825 repo tokens now, consumes 40.9259 child Invalid held from earlier runs (I_j 54.6886; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 36.127472924009907842, DOWN 3.312122087492088596 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **libp2p/libp2p** merge-arb: 25.9441 pairs, cost ~ 25.2285, gain ~ 0.7156 repo tokens now, consumes 25.9441 child Invalid held from earlier runs (I_j 35.3021; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 21.489191253892974769, DOWN 3.865473357990368818 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **supranational/blst** merge-arb: 34.3231 pairs, cost ~ 33.1630, gain ~ 1.1602 repo tokens now, consumes 34.3231 child Invalid held from earlier runs (I_j 35.8295; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 30.397235590737363309, DOWN 2.931538794753819285 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **ChainSafe/bls** merge-arb: 51.0705 pairs, cost ~ 48.2538, gain ~ 2.8167 repo tokens now, consumes 51.0705 child Invalid held from earlier runs (I_j 225.5682; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 32.508021753968867343, DOWN 15.987017329465011229 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **dappnode/DAppNode** merge-arb: 36.4125 pairs, cost ~ 34.5692, gain ~ 1.8433 repo tokens now, consumes 36.4125 child Invalid held from earlier runs (I_j 38.1537; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 23.936183229438503475, DOWN 10.805833883827382831 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **lambdaclass/lambdaworks** merge-arb: 15.8558 pairs, cost ~ 15.4658, gain ~ 0.3900 repo tokens now, consumes 15.8558 child Invalid held from earlier runs (I_j 40.0700; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 12.338096732720796163, DOWN 3.204992271903902531 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **shazow/whatsabi** merge-arb: 18.9916 pairs, cost ~ 18.3200, gain ~ 0.6717 repo tokens now, consumes 18.9916 child Invalid held from earlier runs (I_j 30.3781; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 13.639491062464560035, DOWN 4.772060968334644998 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **TrueBlocks/trueblocks-core** merge-arb: 15.2270 pairs, cost ~ 13.8040, gain ~ 1.4230 repo tokens now, consumes 15.2270 child Invalid held from earlier runs (I_j 15.2270; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 11.789991582396447357, DOWN 2.082999396392581462 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **succinctlabs/sp1** merge-arb: 22.3113 pairs, cost ~ 21.5312, gain ~ 0.7801 repo tokens now, consumes 22.3113 child Invalid held from earlier runs (I_j 22.3113; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 15.687089527210965294, DOWN 5.951789265326485652 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **otterscan/otterscan** merge-arb: 18.6935 pairs, cost ~ 18.2469, gain ~ 0.4466 repo tokens now, consumes 18.6935 child Invalid held from earlier runs (I_j 52.8634; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 13.797808982060524854, DOWN 4.540310844537277323 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **NethermindEth/juno** merge-arb: 20.0320 pairs, cost ~ 18.9250, gain ~ 1.1070 repo tokens now, consumes 20.0320 child Invalid held from earlier runs (I_j 20.0320; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 14.110346630912403644, DOWN 4.909253741808546393 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **0xMiden/miden-vm** merge-arb: 23.9073 pairs, cost ~ 23.0127, gain ~ 0.8946 repo tokens now, consumes 23.9073 child Invalid held from earlier runs (I_j 30.4867; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 18.116135102152452944, DOWN 5.01163998741667238 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **holiman/goevmlab** merge-arb: 22.2481 pairs, cost ~ 21.2739, gain ~ 0.9741 repo tokens now, consumes 22.2481 child Invalid held from earlier runs (I_j 25.4865; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 15.403189485349376767, DOWN 5.977116593600929262 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **evmts/tevm-monorepo** merge-arb: 8.8238 pairs, cost ~ 8.1021, gain ~ 0.7217 repo tokens now, consumes 8.8238 child Invalid held from earlier runs (I_j 8.8238; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 5.850467756456404191, DOWN 2.29218341212653977 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **succinctlabs/rsp** merge-arb: 28.9067 pairs, cost ~ 25.3938, gain ~ 3.5129 repo tokens now, consumes 28.9067 child Invalid held from earlier runs (I_j 28.9067; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 19.831840680779693916, DOWN 5.688900607865504889 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **risc0/risc0-ethereum** merge-arb: 19.6288 pairs, cost ~ 19.1250, gain ~ 0.5037 repo tokens now, consumes 19.6288 child Invalid held from earlier runs (I_j 19.6288; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 14.102729862632648639, DOWN 5.117920159591986658 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **swiss-knife-xyz/swiss-knife** merge-arb: 26.6841 pairs, cost ~ 25.5949, gain ~ 1.0893 repo tokens now, consumes 26.6841 child Invalid held from earlier runs (I_j 38.7897; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 19.503986240588063806, DOWN 6.218867139126593923 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **alloy-rs/alloy** merge-arb: 15.9666 pairs, cost ~ 15.5161, gain ~ 0.4504 repo tokens now, consumes 15.9666 child Invalid held from earlier runs (I_j 36.1832; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 11.79943688410523419, DOWN 3.794293070655505871 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **ethereum/eips** merge-arb: 20.4565 pairs, cost ~ 19.9593, gain ~ 0.4972 repo tokens now, consumes 20.4565 child Invalid held from earlier runs (I_j 28.8602; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 18.365747762170808271, DOWN 1.693313676226120165 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **ipsilon/evmone** merge-arb: 16.5805 pairs, cost ~ 16.2246, gain ~ 0.3559 repo tokens now, consumes 16.5805 child Invalid held from earlier runs (I_j 27.9608; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 12.347633849418905919, DOWN 3.958076370360129163 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **ethereum/execution-apis** merge-arb: 16.5757 pairs, cost ~ 14.3894, gain ~ 2.1863 repo tokens now, consumes 16.5757 child Invalid held from earlier runs (I_j 16.5757; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 12.189823076298209052, DOWN 2.271526325195013811 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **argotorg/fe** merge-arb: 30.2904 pairs, cost ~ 28.9235, gain ~ 1.3669 repo tokens now, consumes 30.2904 child Invalid held from earlier runs (I_j 32.0793; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 23.128922287733423527, DOWN 5.939188048552132191 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **remix-project-org/remix-project** merge-arb: 16.2250 pairs, cost ~ 15.8582, gain ~ 0.3669 repo tokens now, consumes 16.2250 child Invalid held from earlier runs (I_j 23.9560; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 12.665809735838123502, DOWN 3.271653682937500504 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **argotorg/solidity** merge-arb: 17.7136 pairs, cost ~ 17.3108, gain ~ 0.4028 repo tokens now, consumes 17.7136 child Invalid held from earlier runs (I_j 25.6873; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 14.587651168854556517, DOWN 2.809671209028714301 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **foundry-rs/foundry** merge-arb: 29.5445 pairs, cost ~ 27.1040, gain ~ 2.4404 repo tokens now, consumes 29.5445 child Invalid held from earlier runs (I_j 29.5445; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 23.72545837820187808, DOWN 3.514072402344462732 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **hyperledger/besu** merge-arb: 31.3847 pairs, cost ~ 29.9303, gain ~ 1.4545 repo tokens now, consumes 31.3847 child Invalid held from earlier runs (I_j 31.3847; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 23.346943913548841593, DOWN 6.732967113489915461 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **nomicfoundation/hardhat** merge-arb: 18.2851 pairs, cost ~ 17.6834, gain ~ 0.6018 repo tokens now, consumes 18.2851 child Invalid held from earlier runs (I_j 30.3516; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 13.348337707185553289, DOWN 4.423450729363815246 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **openzeppelin/openzeppelin-contracts** merge-arb: 17.7713 pairs, cost ~ 17.3512, gain ~ 0.4202 repo tokens now, consumes 17.7713 child Invalid held from earlier runs (I_j 41.3285; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 14.464564964191378218, DOWN 2.97337412399508716 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **status-im/nimbus-eth2** merge-arb: 15.0667 pairs, cost ~ 14.6824, gain ~ 0.3843 repo tokens now, consumes 15.0667 child Invalid held from earlier runs (I_j 15.0667; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 13.832763441635110344, DOWN 0.923076019767152966 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **wevm/viem** merge-arb: 13.6393 pairs, cost ~ 12.5239, gain ~ 1.1154 repo tokens now, consumes 13.6393 child Invalid held from earlier runs (I_j 13.6393; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 9.935655605464679302, DOWN 2.650844869502405561 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **argotorg/act** merge-arb: 25.2138 pairs, cost ~ 24.3483, gain ~ 0.8654 repo tokens now, consumes 25.2138 child Invalid held from earlier runs (I_j 29.4622; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 19.760029017651659099, DOWN 4.710062489670568269 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **ethpandaops/ethereum-helm-charts** merge-arb: 34.5772 pairs, cost ~ 30.6737, gain ~ 3.9035 repo tokens now, consumes 34.5772 child Invalid held from earlier runs (I_j 34.5772; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 19.316207519898645266, DOWN 11.510884216311246161 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.

### 5c. Complex-buy (15 groups: split `x = stake`, sell the other leg, buy the own leg with the proceeds; keeps `x` child Invalid; the last two transactions are rebuilt at send time with the realised proceeds)

- **herumi/mcl** complex-buy UP: split x = 101.5777 repo tokens [1.036508 sUSDS-eq], sell x DOWN for P = 21.1639 repo tokens, buy 28.2474 UP -> **129.8251 UP + 101.5777 child Invalid** (quoted total; F's simple-route count 125.0874; complex 3.788% vs the simple route); spot sum 1.01980 > 1; p_win 0.9000
- **paulmillr/noble-curves** complex-buy UP: split x = 9.5379 repo tokens [0.097325 sUSDS-eq], sell x DOWN for P = 1.8899 repo tokens, buy 2.2611 UP -> **11.7990 UP + 9.5379 child Invalid** (quoted total; F's simple-route count 11.3261; complex 4.175% vs the simple route); spot sum 1.03988 > 1; p_win 0.8500
- **Consensys/gnark-crypto** complex-buy UP: split x = 38.1415 repo tokens [0.389199 sUSDS-eq], sell x DOWN for P = 5.3344 repo tokens, buy 6.3393 UP -> **44.4808 UP + 38.1415 child Invalid** (quoted total; F's simple-route count 43.9412; complex 1.228% vs the simple route); spot sum 1.00044 > 1; p_win 0.9000
- **ethereum/js-ethereum-cryptography** complex-buy DOWN: split x = 12.7754 repo tokens [0.130362 sUSDS-eq], sell x UP for P = 7.4165 repo tokens, buy 16.1008 DOWN -> **28.8763 DOWN + 12.7754 child Invalid** (quoted total; F's simple-route count 26.3547; complex 9.568% vs the simple route); spot sum 1.01297 > 1; p_win 0.5500
- **Certora/CertoraProver** complex-buy UP: split x = 48.9295 repo tokens [0.499281 sUSDS-eq], sell x DOWN for P = 12.0364 repo tokens, buy 16.4367 UP -> **65.3662 UP + 48.9295 child Invalid** (quoted total; F's simple-route count 64.3335; complex 1.605% vs the simple route); spot sum 1.02205 > 1; p_win 0.8000
- **wealdtech/ethdo** complex-buy UP: split x = 22.5142 repo tokens [0.229737 sUSDS-eq], sell x DOWN for P = 6.0696 repo tokens, buy 8.4404 UP -> **30.9546 UP + 22.5142 child Invalid** (quoted total; F's simple-route count 30.7583; complex 0.638% vs the simple route); spot sum 1.00388 > 1; p_win 0.7500
- **skalenetwork/libBLS** complex-buy UP: split x = 40.6059 repo tokens [0.414346 sUSDS-eq], sell x DOWN for P = 12.0560 repo tokens, buy 17.3300 UP -> **57.9359 UP + 40.6059 child Invalid** (quoted total; F's simple-route count 56.5919; complex 2.375% vs the simple route); spot sum 1.02701 > 1; p_win 0.7500
- **Cyfrin/aderyn** complex-buy UP: split x = 28.5067 repo tokens [0.290885 sUSDS-eq], sell x DOWN for P = 9.3779 repo tokens, buy 14.1169 UP -> **42.6236 UP + 28.5067 child Invalid** (quoted total; F's simple-route count 42.0225; complex 1.430% vs the simple route); spot sum 1.02889 > 1; p_win 0.7000
- **OffchainLabs/stylus-sdk-rs** complex-buy UP: split x = 36.5295 repo tokens [0.372751 sUSDS-eq], sell x DOWN for P = 8.5427 repo tokens, buy 11.4208 UP -> **47.9504 UP + 36.5295 child Invalid** (quoted total; F's simple-route count 47.4367; complex 1.083% vs the simple route); spot sum 1.00435 > 1; p_win 0.8000
- **dl-solarity/solidity-lib** complex-buy UP: split x = 23.0085 repo tokens [0.234781 sUSDS-eq], sell x DOWN for P = 6.7441 repo tokens, buy 9.3822 UP -> **32.3907 UP + 23.0085 child Invalid** (quoted total; F's simple-route count 31.4519; complex 2.985% vs the simple route); spot sum 1.02962 > 1; p_win 0.7500
- **axiom-crypto/snark-verifier** complex-buy DOWN: split x = 6.6981 repo tokens [0.068348 sUSDS-eq], sell x UP for P = 4.5975 repo tokens, buy 14.2193 DOWN -> **20.9174 DOWN + 6.6981 child Invalid** (quoted total; F's simple-route count 20.3338; complex 2.870% vs the simple route); spot sum 1.00006 > 1; p_win 0.3500
- **erigontech/erigon** complex-buy UP: split x = 14.2001 repo tokens [0.144898 sUSDS-eq], sell x DOWN for P = 3.7004 repo tokens, buy 5.0663 UP -> **19.2664 UP + 14.2001 child Invalid** (quoted total; F's simple-route count 19.2243; complex 0.219% vs the simple route); spot sum 1.00007 > 1; p_win 0.7500
- **ethereum/consensus-specs** complex-buy UP: split x = 13.4148 repo tokens [0.136885 sUSDS-eq], sell x DOWN for P = 1.5529 repo tokens, buy 1.7655 UP -> **15.1803 UP + 13.4148 child Invalid** (quoted total; F's simple-route count 15.0878; complex 0.613% vs the simple route); spot sum 1.01711 > 1; p_win 0.9000
- **argotorg/hevm** complex-buy UP: split x = 44.3079 repo tokens [0.452121 sUSDS-eq], sell x DOWN for P = 11.3461 repo tokens, buy 15.3695 UP -> **59.6774 UP + 44.3079 child Invalid** (quoted total; F's simple-route count 58.0038; complex 2.885% vs the simple route); spot sum 1.02920 > 1; p_win 0.8000
- **ethpandaops/ethereum-package** complex-buy DOWN: split x = 9.0791 repo tokens [0.092644 sUSDS-eq], sell x UP for P = 6.3493 repo tokens, buy 20.2312 DOWN -> **29.3103 DOWN + 9.0791 child Invalid** (quoted total; F's simple-route count 28.2254; complex 3.844% vs the simple route); spot sum 1.00003 > 1; p_win 0.3500

### 5d. Simple-buy (42 groups: one approve and one `exactInputSingle`, min 99.5% of the quote)

- **ethereum/py_ecc** simple-buy UP: stake 62.0470 repo tokens [0.633132 sUSDS-eq], quoted out 77.5817 UP (F count 77.5817), floor 77.1938; spot sum 0.90351 (quoted on the post-set-sell state); p_win 0.8500
- **blockscout/blockscout** simple-buy UP: stake 39.0585 repo tokens [0.398556 sUSDS-eq], quoted out 58.3497 UP (F count 58.3497), floor 58.0580; spot sum 0.99391 < 1; p_win 0.7000
- **LFDT-web3j/web3j** simple-buy UP: stake 32.9636 repo tokens [0.336363 sUSDS-eq], quoted out 42.6062 UP (F count 42.6062), floor 42.3932; spot sum 0.96623 < 1; p_win 0.8000
- **flashbots/rbuilder** simple-buy UP: stake 39.0512 repo tokens [0.398482 sUSDS-eq], quoted out 54.3725 UP (F count 54.3725), floor 54.1007; spot sum 0.98064 < 1; p_win 0.7500
- **protofire/solhint** simple-buy UP: stake 39.0472 repo tokens [0.398441 sUSDS-eq], quoted out 54.2923 UP (F count 54.2923), floor 54.0209; spot sum 0.91619 (quoted on the post-set-sell state); p_win 0.7500
- **l2beat/l2beat** simple-buy UP: stake 26.1938 repo tokens [0.267284 sUSDS-eq], quoted out 33.6276 UP (F count 33.6276), floor 33.4595; spot sum 0.94233 (quoted on the post-set-sell state); p_win 0.8000
- **taikoxyz/taiko-mono** simple-buy UP: stake 40.6342 repo tokens [0.414635 sUSDS-eq], quoted out 56.6203 UP (F count 56.6203), floor 56.3372; spot sum 0.91747 (quoted on the post-set-sell state); p_win 0.7500
- **flashbots/mev-boost** simple-buy DOWN: stake 1.2901 repo tokens [0.013164 sUSDS-eq], quoted out 13.4984 DOWN (F count 13.4984), floor 13.4309; spot sum 0.91998 (quoted on the post-set-sell state); p_win 0.1000
- **DefiLlama/chainlist** simple-buy UP: stake 10.1196 repo tokens [0.103261 sUSDS-eq], quoted out 14.6262 UP (F count 14.6262), floor 14.5530; spot sum 0.99538 < 1; p_win 0.7000
- **ChainSafe/bls** simple-buy DOWN: stake 42.9380 repo tokens [0.438143 sUSDS-eq], quoted out 104.3720 DOWN (F count 104.3720), floor 103.8502; spot sum 0.89296 (quoted on the post-set-sell state); p_win 0.5000
- **intellij-solidity/intellij-solidity** simple-buy UP: stake 17.8012 repo tokens [0.181645 sUSDS-eq], quoted out 22.6666 UP (F count 22.6666), floor 22.5533; spot sum 0.98889 < 1; p_win 0.8000
- **dappnode/DAppNode** simple-buy UP: stake 17.6120 repo tokens [0.179715 sUSDS-eq], quoted out 25.6693 UP (F count 25.6693), floor 25.5410; spot sum 0.90234 (quoted on the post-set-sell state); p_win 0.7000
- **lambdaclass/lambdaworks** simple-buy UP: stake 41.1808 repo tokens [0.420212 sUSDS-eq], quoted out 50.4486 UP (F count 50.4486), floor 50.1963; spot sum 0.95186 (quoted on the post-set-sell state); p_win 0.8500
- **shazow/whatsabi** simple-buy UP: stake 79.4774 repo tokens [0.810994 sUSDS-eq], quoted out 101.2522 UP (F count 101.2522), floor 100.7460; spot sum 0.93161 (quoted on the post-set-sell state); p_win 0.8500
- **EspressoSystems/jellyfish** simple-buy UP: stake 52.5984 repo tokens [0.536719 sUSDS-eq], quoted out 85.8958 UP (F count 85.8958), floor 85.4663; spot sum 0.97191 < 1; p_win 0.6500
- **a16z/halmos** simple-buy UP: stake 25.0817 repo tokens [0.255936 sUSDS-eq], quoted out 34.3284 UP (F count 34.3284), floor 34.1567; spot sum 0.99323 < 1; p_win 0.7500
- **succinctlabs/sp1** simple-buy UP: stake 22.2800 repo tokens [0.227347 sUSDS-eq], quoted out 30.4772 UP (F count 30.4772), floor 30.3248; spot sum 0.94010 (quoted on the post-set-sell state); p_win 0.7500
- **otterscan/otterscan** simple-buy DOWN: stake 7.7255 repo tokens [0.078832 sUSDS-eq], quoted out 27.9622 DOWN (F count 27.9622), floor 27.8224; spot sum 0.95293 (quoted on the post-set-sell state); p_win 0.3000
- **NethermindEth/juno** simple-buy UP: stake 25.4350 repo tokens [0.259541 sUSDS-eq], quoted out 34.8213 UP (F count 34.8213), floor 34.6472; spot sum 0.91114 (quoted on the post-set-sell state); p_win 0.7500
- **0xMiden/miden-vm** simple-buy UP: stake 51.2195 repo tokens [0.522648 sUSDS-eq], quoted out 63.3915 UP (F count 63.3915), floor 63.0745; spot sum 0.92768 (quoted on the post-set-sell state); p_win 0.8500
- **holiman/goevmlab** simple-buy UP: stake 64.8199 repo tokens [0.661428 sUSDS-eq], quoted out 86.6013 UP (F count 86.6013), floor 86.1683; spot sum 0.91603 (quoted on the post-set-sell state); p_win 0.8000
- **risc0/risc0-ethereum** simple-buy DOWN: stake 6.5390 repo tokens [0.066725 sUSDS-eq], quoted out 22.9507 DOWN (F count 22.9507), floor 22.8359; spot sum 0.95205 (quoted on the post-set-sell state); p_win 0.3000
- **swiss-knife-xyz/swiss-knife** simple-buy DOWN: stake 4.8888 repo tokens [0.049886 sUSDS-eq], quoted out 17.5837 DOWN (F count 17.5837), floor 17.4958; spot sum 0.92115 (quoted on the post-set-sell state); p_win 0.3000
- **a16z/helios** simple-buy UP: stake 28.1846 repo tokens [0.287598 sUSDS-eq], quoted out 36.3067 UP (F count 36.3067), floor 36.1252; spot sum 0.98875 < 1; p_win 0.8000
- **alloy-rs/alloy** simple-buy UP: stake 66.6894 repo tokens [0.680505 sUSDS-eq], quoted out 83.8428 UP (F count 83.8428), floor 83.4236; spot sum 0.94504 (quoted on the post-set-sell state); p_win 0.8500
- **apeworx/ape** simple-buy UP: stake 16.8390 repo tokens [0.171826 sUSDS-eq], quoted out 22.8628 UP (F count 22.8628), floor 22.7485; spot sum 0.99993 < 1; p_win 0.7500
- **eth-infinitism/account-abstraction** simple-buy UP: stake 44.6001 repo tokens [0.455103 sUSDS-eq], quoted out 67.2623 UP (F count 67.2623), floor 66.9260; spot sum 0.99272 < 1; p_win 0.7000
- **ipsilon/evmone** simple-buy UP: stake 59.6810 repo tokens [0.608990 sUSDS-eq], quoted out 74.7031 UP (F count 74.7031), floor 74.3296; spot sum 0.95764 (quoted on the post-set-sell state); p_win 0.8500
- **argotorg/fe** simple-buy UP: stake 44.9510 repo tokens [0.458683 sUSDS-eq], quoted out 55.2822 UP (F count 55.2822), floor 55.0058; spot sum 0.91337 (quoted on the post-set-sell state); p_win 0.8500
- **remix-project-org/remix-project** simple-buy UP: stake 8.2008 repo tokens [0.083682 sUSDS-eq], quoted out 10.3365 UP (F count 10.3365), floor 10.2848; spot sum 0.95555 (quoted on the post-set-sell state); p_win 0.8000
- **argotorg/solidity** simple-buy UP: stake 11.4974 repo tokens [0.117320 sUSDS-eq], quoted out 13.6783 UP (F count 13.6783), floor 13.6099; spot sum 0.95530 (quoted on the post-set-sell state); p_win 0.8500
- **argotorg/sourcify** simple-buy UP: stake 29.2914 repo tokens [0.298892 sUSDS-eq], quoted out 40.3344 UP (F count 40.3344), floor 40.1327; spot sum 0.98511 < 1; p_win 0.7500
- **grandinetech/grandine** simple-buy UP: stake 40.3133 repo tokens [0.411360 sUSDS-eq], quoted out 52.5387 UP (F count 52.5387), floor 52.2760; spot sum 0.95340 < 1; p_win 0.8000
- **hyperledger-web3j/web3j** simple-buy UP: stake 19.5606 repo tokens [0.199598 sUSDS-eq], quoted out 26.6377 UP (F count 26.6377), floor 26.5045; spot sum 0.99028 < 1; p_win 0.7500
- **hyperledger/besu** simple-buy UP: stake 25.9890 repo tokens [0.265194 sUSDS-eq], quoted out 33.3632 UP (F count 33.3632), floor 33.1964; spot sum 0.91320 (quoted on the post-set-sell state); p_win 0.8000
- **nethereum/nethereum** simple-buy UP: stake 11.6171 repo tokens [0.118542 sUSDS-eq], quoted out 13.8211 UP (F count 13.8211), floor 13.7520; spot sum 0.98287 < 1; p_win 0.8500
- **nomicfoundation/hardhat** simple-buy UP: stake 40.8125 repo tokens [0.416454 sUSDS-eq], quoted out 53.1694 UP (F count 53.1694), floor 52.9036; spot sum 0.93620 (quoted on the post-set-sell state); p_win 0.8000
- **openzeppelin/openzeppelin-contracts** simple-buy UP: stake 17.5169 repo tokens [0.178744 sUSDS-eq], quoted out 20.9627 UP (F count 20.9627), floor 20.8579; spot sum 0.95359 (quoted on the post-set-sell state); p_win 0.8500
- **safe-global/safe-smart-account** simple-buy UP: stake 143.4449 repo tokens [1.463724 sUSDS-eq], quoted out 203.6325 UP (F count 203.6325), floor 202.6144; spot sum 0.99570 < 1; p_win 0.8500
- **status-im/nimbus-eth2** simple-buy DOWN: stake 2.4809 repo tokens [0.025316 sUSDS-eq], quoted out 30.4169 DOWN (F count 30.4169), floor 30.2649; spot sum 0.95803 (quoted on the post-set-sell state); p_win 0.1000
- **vyperlang/vyper** simple-buy UP: stake 14.0061 repo tokens [0.142919 sUSDS-eq], quoted out 17.7523 UP (F count 17.7523), floor 17.6635; spot sum 0.98037 < 1; p_win 0.8000
- **ethdebug/format** simple-buy UP: stake 65.6917 repo tokens [0.670323 sUSDS-eq], quoted out 82.6470 UP (F count 82.6470), floor 82.2338; spot sum 0.99219 < 1; p_win 0.8500

### 5e. Skipped rows (0: never sent; the executor writes each `status: "skipped"` with its reason)

- none

## 6. Group order and gas (send order)

| # | group | tx | gas used |
|---|---|---|---|
| 0 | `mint-parent` | 0-1 | 647,169 |
| 1 | `mint-middle-A` | 2-3 | 4,093,638 |
| 2 | `mint-middle-B` | 4-5 | 4,200,486 |
| 3 | `mint-middle-C` | 6-7 | 4,130,570 |
| 4 | `merge-arb:ethereum/py_ecc` | 8-14 | 1,110,932 |
| 5 | `simple-buy:ethereum/py_ecc:UP` | 15-16 | 184,517 |
| 6 | `simple-buy:blockscout/blockscout:UP` | 17-18 | 194,359 |
| 7 | `simple-buy:LFDT-web3j/web3j:UP` | 19-20 | 186,960 |
| 8 | `complex-buy:herumi/mcl:UP` | 21-26 | 1,047,767 |
| 9 | `complex-buy:paulmillr/noble-curves:UP` | 27-32 | 984,005 |
| 10 | `dual-buy:arkworks-rs/algebra` | 33-36 | 353,339 |
| 11 | `simple-buy:flashbots/rbuilder:UP` | 37-38 | 187,715 |
| 12 | `merge-arb:protofire/solhint` | 39-45 | 988,462 |
| 13 | `simple-buy:protofire/solhint:UP` | 46-47 | 169,936 |
| 14 | `merge-arb:l2beat/l2beat` | 48-54 | 1,030,361 |
| 15 | `simple-buy:l2beat/l2beat:UP` | 55-56 | 162,520 |
| 16 | `complex-buy:Consensys/gnark-crypto:UP` | 57-62 | 931,207 |
| 17 | `merge-arb:taikoxyz/taiko-mono` | 63-69 | 989,066 |
| 18 | `simple-buy:taikoxyz/taiko-mono:UP` | 70-71 | 169,960 |
| 19 | `merge-arb:flashbots/mev-boost` | 72-78 | 1,051,289 |
| 20 | `simple-buy:flashbots/mev-boost:DOWN` | 79-80 | 178,027 |
| 21 | `dual-buy:flashbots/mev-boost-relay` | 81-84 | 388,813 |
| 22 | `complex-buy:ethereum/js-ethereum-cryptography:DOWN` | 85-90 | 932,687 |
| 23 | `merge-arb:libp2p/libp2p` | 91-97 | 1,005,887 |
| 24 | `merge-arb:supranational/blst` | 98-104 | 1,060,238 |
| 25 | `dual-buy:wighawag/hardhat-deploy` | 105-108 | 357,120 |
| 26 | `dual-buy:ethstaker/eth-docker` | 109-112 | 391,410 |
| 27 | `dual-buy:DefiLlama/DefiLlama-Adapters` | 113-116 | 391,644 |
| 28 | `simple-buy:DefiLlama/chainlist:UP` | 117-118 | 173,014 |
| 29 | `complex-buy:Certora/CertoraProver:UP` | 119-124 | 1,025,034 |
| 30 | `dual-buy:Plonky3/Plonky3` | 125-128 | 370,471 |
| 31 | `merge-arb:ChainSafe/bls` | 129-135 | 1,058,821 |
| 32 | `simple-buy:ChainSafe/bls:DOWN` | 136-137 | 257,871 |
| 33 | `simple-buy:intellij-solidity/intellij-solidity:UP` | 138-139 | 180,258 |
| 34 | `merge-arb:dappnode/DAppNode` | 140-146 | 1,006,385 |
| 35 | `simple-buy:dappnode/DAppNode:UP` | 147-148 | 163,272 |
| 36 | `complex-buy:wealdtech/ethdo:UP` | 149-154 | 903,966 |
| 37 | `merge-arb:lambdaclass/lambdaworks` | 155-161 | 1,021,120 |
| 38 | `simple-buy:lambdaclass/lambdaworks:UP` | 162-163 | 170,535 |
| 39 | `dual-buy:smartcontracts/simple-optimism-node` | 164-167 | 377,484 |
| 40 | `complex-buy:skalenetwork/libBLS:UP` | 168-173 | 967,171 |
| 41 | `merge-arb:shazow/whatsabi` | 174-180 | 975,954 |
| 42 | `simple-buy:shazow/whatsabi:UP` | 181-182 | 192,504 |
| 43 | `merge-arb:TrueBlocks/trueblocks-core` | 183-189 | 969,396 |
| 44 | `dual-buy:TrueBlocks/trueblocks-core` | 190-193 | 403,520 |
| 45 | `simple-buy:EspressoSystems/jellyfish:UP` | 194-195 | 219,960 |
| 46 | `simple-buy:a16z/halmos:UP` | 196-197 | 180,382 |
| 47 | `dual-buy:succinctlabs/op-succinct` | 198-201 | 406,092 |
| 48 | `merge-arb:succinctlabs/sp1` | 202-208 | 1,018,099 |
| 49 | `simple-buy:succinctlabs/sp1:UP` | 209-210 | 163,258 |
| 50 | `merge-arb:otterscan/otterscan` | 211-217 | 982,536 |
| 51 | `simple-buy:otterscan/otterscan:DOWN` | 218-219 | 192,566 |
| 52 | `dual-buy:lambdaclass/ethrex` | 220-223 | 390,951 |
| 53 | `merge-arb:NethermindEth/juno` | 224-230 | 1,058,215 |
| 54 | `simple-buy:NethermindEth/juno:UP` | 231-232 | 163,282 |
| 55 | `dual-buy:Commit-Boost/commit-boost-client` | 233-236 | 383,868 |
| 56 | `complex-buy:Cyfrin/aderyn:UP` | 237-242 | 976,961 |
| 57 | `merge-arb:0xMiden/miden-vm` | 243-249 | 1,016,628 |
| 58 | `simple-buy:0xMiden/miden-vm:UP` | 250-251 | 177,853 |
| 59 | `merge-arb:holiman/goevmlab` | 252-258 | 984,739 |
| 60 | `simple-buy:holiman/goevmlab:UP` | 259-260 | 185,166 |
| 61 | `dual-buy:edb-rs/edb` | 261-264 | 374,548 |
| 62 | `merge-arb:evmts/tevm-monorepo` | 265-271 | 963,759 |
| 63 | `dual-buy:evmts/tevm-monorepo` | 272-275 | 388,084 |
| 64 | `merge-arb:succinctlabs/rsp` | 276-282 | 1,038,391 |
| 65 | `dual-buy:succinctlabs/rsp` | 283-286 | 500,406 |
| 66 | `complex-buy:OffchainLabs/stylus-sdk-rs:UP` | 287-292 | 927,420 |
| 67 | `dual-buy:ethstaker/ethstaker-deposit-cli` | 293-296 | 419,205 |
| 68 | `complex-buy:dl-solarity/solidity-lib:UP` | 297-302 | 912,922 |
| 69 | `merge-arb:risc0/risc0-ethereum` | 303-309 | 951,186 |
| 70 | `simple-buy:risc0/risc0-ethereum:DOWN` | 310-311 | 177,911 |
| 71 | `dual-buy:powdr-labs/powdr` | 312-315 | 383,913 |
| 72 | `complex-buy:axiom-crypto/snark-verifier:DOWN` | 316-321 | 917,423 |
| 73 | `merge-arb:swiss-knife-xyz/swiss-knife` | 322-328 | 1,073,189 |
| 74 | `simple-buy:swiss-knife-xyz/swiss-knife:DOWN` | 329-330 | 185,232 |
| 75 | `simple-buy:a16z/helios:UP` | 331-332 | 186,936 |
| 76 | `merge-arb:alloy-rs/alloy` | 333-339 | 996,744 |
| 77 | `simple-buy:alloy-rs/alloy:UP` | 340-341 | 184,529 |
| 78 | `simple-buy:apeworx/ape:UP` | 342-343 | 173,026 |
| 79 | `dual-buy:consensys/teku` | 344-347 | 394,683 |
| 80 | `complex-buy:erigontech/erigon:UP` | 348-353 | 937,481 |
| 81 | `simple-buy:eth-infinitism/account-abstraction:UP` | 354-355 | 201,673 |
| 82 | `dual-buy:ethereum-lists/chains` | 356-359 | 345,613 |
| 83 | `complex-buy:ethereum/consensus-specs:UP` | 360-365 | 971,234 |
| 84 | `merge-arb:ethereum/eips` | 366-372 | 1,025,174 |
| 85 | `merge-arb:ipsilon/evmone` | 373-379 | 983,372 |
| 86 | `simple-buy:ipsilon/evmone:UP` | 380-381 | 184,541 |
| 87 | `merge-arb:ethereum/execution-apis` | 382-388 | 1,014,896 |
| 88 | `dual-buy:ethereum/execution-apis` | 389-392 | 445,393 |
| 89 | `merge-arb:argotorg/fe` | 393-399 | 1,002,558 |
| 90 | `simple-buy:argotorg/fe:UP` | 400-401 | 170,511 |
| 91 | `merge-arb:remix-project-org/remix-project` | 402-408 | 977,761 |
| 92 | `simple-buy:remix-project-org/remix-project:UP` | 409-410 | 155,828 |
| 93 | `merge-arb:argotorg/solidity` | 411-417 | 1,032,087 |
| 94 | `simple-buy:argotorg/solidity:UP` | 418-419 | 155,239 |
| 95 | `simple-buy:argotorg/sourcify:UP` | 420-421 | 180,382 |
| 96 | `dual-buy:ethers-io/ethers.js` | 422-425 | 461,825 |
| 97 | `merge-arb:foundry-rs/foundry` | 426-432 | 1,022,701 |
| 98 | `dual-buy:foundry-rs/foundry` | 433-436 | 353,405 |
| 99 | `simple-buy:grandinetech/grandine:UP` | 437-438 | 187,615 |
| 100 | `simple-buy:hyperledger-web3j/web3j:UP` | 439-440 | 173,050 |
| 101 | `merge-arb:hyperledger/besu` | 441-447 | 1,002,698 |
| 102 | `simple-buy:hyperledger/besu:UP` | 448-449 | 162,508 |
| 103 | `simple-buy:nethereum/nethereum:UP` | 450-451 | 172,976 |
| 104 | `dual-buy:nethermindeth/nethermind` | 452-455 | 347,122 |
| 105 | `merge-arb:nomicfoundation/hardhat` | 456-462 | 1,047,034 |
| 106 | `simple-buy:nomicfoundation/hardhat:UP` | 463-464 | 170,515 |
| 107 | `merge-arb:openzeppelin/openzeppelin-contracts` | 465-471 | 966,843 |
| 108 | `simple-buy:openzeppelin/openzeppelin-contracts:UP` | 472-473 | 155,263 |
| 109 | `dual-buy:OffchainLabs/prysm` | 474-477 | 360,471 |
| 110 | `simple-buy:safe-global/safe-smart-account:UP` | 478-479 | 274,857 |
| 111 | `dual-buy:scaffold-eth/scaffold-eth-2` | 480-483 | 356,338 |
| 112 | `dual-buy:sigp/lighthouse` | 484-487 | 410,070 |
| 113 | `merge-arb:status-im/nimbus-eth2` | 488-494 | 1,004,376 |
| 114 | `simple-buy:status-im/nimbus-eth2:DOWN` | 495-496 | 265,483 |
| 115 | `dual-buy:vyperlang/titanoboa` | 497-500 | 380,464 |
| 116 | `simple-buy:vyperlang/vyper:UP` | 501-502 | 155,147 |
| 117 | `merge-arb:wevm/viem` | 503-509 | 995,150 |
| 118 | `dual-buy:wevm/viem` | 510-513 | 388,787 |
| 119 | `complex-buy:argotorg/hevm:UP` | 514-519 | 966,492 |
| 120 | `simple-buy:ethdebug/format:UP` | 520-521 | 202,286 |
| 121 | `merge-arb:argotorg/act` | 522-528 | 1,012,412 |
| 122 | `complex-buy:ethpandaops/ethereum-package:DOWN` | 529-534 | 915,813 |
| 123 | `merge-arb:ethpandaops/ethereum-helm-charts` | 535-541 | 1,009,552 |
| 124 | `dual-buy:ethpandaops/ethereum-helm-charts` | 542-545 | 365,576 |
| 125 | `dual-buy:ethpandaops/checkpointz` | 546-549 | 384,466 |
| 126 | `dual-buy:lambdaclass/lambda_ethereum_consensus` | 550-553 | 363,416 |
| 127 | `dual-buy:erigontech/silkworm` | 554-557 | 398,713 |

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

Files: `g-plan.json` (groups, every call with calldata, keccak256, gas limit, floors and expected effects), `g-tx/tx-NNN.json` (one signer-input file per transaction), `g-sim-w1-of-2.json`, `g-sim-w2-of-2.json` (the helper simulate inputs), `planner/g-drift.json` (the drift report).

## 9. Audit of the written plan (run after `g-plan.json` was written)

- calldata audit: 128 groups, 558 transactions decoded and re-derived from allocation.json (155 rows: 155 in groups, 0 skipped), kinds {"mint":4,"merge-arb":36,"simple-buy":42,"complex-buy":15,"dual-buy":31}, every approval exact (none near 2^256), every swap recipient the holder, every tier the candidates.json tier, dual-buy inMax = min(stake x 1.005, remaining); failures 0
- fresh re-simulation of run/2026-10-28T1129Z-clearance/g-sim-w1-of-2.json (sha256 0e029193e93aaf353fbb03f74bdffcbe60e1f94b0d12e4cd73f85644e21493f0): {"entries":64,"count":276,"all_success":true,"failed_count":0,"over_cap_count":0,"clamped_count":0,"pending_nonce":2693,"overrides_active":"absent","no_max_used_gas_count":0}
- fresh re-simulation of run/2026-10-28T1129Z-clearance/g-sim-w2-of-2.json (sha256 efd67e584321691e97505612928b1a30d7ff00bd81746b4a2f277a753b927ff9): {"entries":68,"count":290,"all_success":true,"failed_count":0,"over_cap_count":0,"clamped_count":0,"pending_nonce":2693,"overrides_active":"absent","no_max_used_gas_count":0}
- holder nonce latest/pending before 2693/2693, after 2693/2693 (the plan's 2693); per-call rows of the fresh simulation: 566 checked, every status 0x1 and every fresh peak within the plan's gas_limit; gasUsed equal to the build's on all
- AUDIT PASSED: every acceptance check holds
