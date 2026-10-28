# G gate print - run 2026-10-28T1629Z

**Optimism mainnet, holder 0x2AD670e5953a85C998cDf1C2f6D74386aB735d4a. Built, simulated and verified: nothing has been signed or sent.** Pending nonce 2693; head at G's read 158803197 (blocks are reported, never compared between reads). Every group below is an ordered sequence of single transactions, one signer call each.

## 1. The numbers

| | |
|---|---|
| **Allocation input** | `run/2026-10-28T1629Z/allocation.json` (sha256 `8574bd928a5cfe95d1dcc6ac4b763ff9472f8e2d0bf1c5579436e3381a6f3169`), generated 2026-10-28T16:32:30Z, 171 rows; 92 markets traded, 0 rows skipped (section 5e) |
| **Counts per route** | pair (`dual-buy`) **42** markets (84 rows); `simple-buy` **35**; `complex-buy` **13** (13 single-side markets with spot sum > 1); `set-sell` **0**; `merge-arb` (`buy-and-merge`) **39**; mint groups **4** (mint-parent, mint-middle-A, mint-middle-B, mint-middle-C); PSM3 ramp: none |
| **Total sUSDS staked** | **130.921944906964 sUSDS** = `totals.staked` = the new mint `M` (the holder holds 666.632973623565635236). Middles split: A by m_X = 130.921944906964, B by m_X = 130.921944906964, C by m_X = 130.921944906964. Each traded market's budget is its held repo tokens plus m_X; the rows' stakes sum to 4337.5797 repo tokens of 92 different tokens (44.2610 sUSDS-equivalent at the labelled 1/98) |
| **Expected value** | **2.648872 sUSDS** at the labelled 1/N = 1/98 (F's `totals.expected_value`; 259.5894 repo tokens summed over heterogeneous markets, / 98; 0 for any repo that is not evaluated) |
| **Worst case** | `correlated_worst_case` **-130.921945 sUSDS** (F's definition); a `set-sell` row's gain is locked only if its whole group lands |
| **Number of transactions** | **597** in **133** keep-whole groups (mint 8, merge-arb 273, simple-buy 70, dual-buy 168, complex-buy 78), nonces 2693 to 3289 |
| **Estimated gas** | **88,087,654 gas used** (mints 13,071,778; merge-arb 39,398,751; simple-buy 6,301,466; dual-buy 16,787,700; complex-buy 12,527,959); sum of the gas limits 118,425,039, largest limit 6,227,213 (2^24 = 16,777,216). In ETH: **0.000090211330924506 ETH** at `eth_gasPrice` 1000311 wei (execution 0.000088115049260394 + L1 data fee 0.000002096281664112 from `GasPriceOracle.getL1Fee`), at most 0.0001783263801849 ETH at the signer's ceiling (2 x gas price); about **0.1878 sUSDS** (2319.37 USD/ETH from QuoterV2 WETH/USDC fee 500, / 1.114394 USD per sUSDS from PSM3) |
| **Simulation** | 2 `eth_simulateV1` request(s) (helper `simulate`, one `blockStateCalls` entry per keep-whole group), **windowed: not one request**, no state overrides: `all_success` **true**, `failed_count` 0, `clamped_count` 0, `over_cap_count` 0, pending nonce 2693 |

## 2. ETH for gas

The holder holds **0.00548971301409488 ETH**; `eth_gasPrice` 1000311 wei (base fee 311 wei). The simulation runs with `validation: false` and does not see ETH, so it is walked here: the signer refuses a transaction unless the balance covers `gasLimit x maxFeePerGas` (execution only), and before each group G section 8 asks for ETH >= 0.002 ETH + the group's `gas_limit x 2 x eth_gasPrice`. The executor makes that check fresh before each group; this is a projection.

| price assumption | effective price | cost of all 597 transactions (execution + L1 data fee) | starting balance the walk needs | first transaction the signer would refuse | first group failing the affordability gate | lowest balance at a group start |
|---|---|---|---|---|---|---|
| effective price = eth_gasPrice (what the node suggests) | 1000311 wei | 0.000090211330924506 ETH | 0.000090435656254096 ETH | none | none | 0.005399915246509669 ETH (group 132) |
| effective price = the signer's ceiling maxFeePerGas = 2 x eth_gasPrice | 2000622 wei | 0.0001783263801849 ETH | 0.00017839205618989 ETH | none | none | 0.005312199034249018 ETH (group 132) |

Result: **no ETH shortfall** under either assumption.

## 3. Drift, the simulation, and what was checked

- **Pool drift since F sized the plan** (`run/2026-10-28T1629Z/planner/g-drift.json`): 0 of 184 pools moved, on 0 market(s). A moved pool is reported, never stale by itself; each call carries its own floor and the pre-send re-check decides. Fresh quotes vs F's `quoted_fill`: largest relative gap 8.99e-15 (drift, not a check).
- **Simulation**: NOT one request: the plan was cut into windows between markets, each beginning with the mint prefix and simulated from chain state without the earlier windows' effects (G section 8, Money rules). 137 entries and 605 calls in all, from the holder, in send order.
- **Gas limits** are the helper's `gas_limit` per call, copied, never computed by hand: `ceil(maxUsedGas x 1.2)` on every call; the largest is 6,227,213.
- **Calldata**: all 597 calldatas re-encoded by the helper's `encode` equal the ethers encoding (bytes and keccak256); the signer's policy-only `check` **allowed all 597** signer-input files (`run/2026-10-28T1629Z/g-tx/tx-NNN.json`, each `{"calls":[one call],"gasLimit":"<helper gas_limit>"}`).
- **End state**: the simulated end state equals the prediction on **321 of 321** probed balances.
- **Independent read**: not run (`--indep` not given; it is supervised-only, because the helper pins one RPC).
- **Trading boundary at build**: 92 of 92 children clear at block 158803208 (timestamp 1793205193); parent and 3 middles payoutDenominator 0/0/0/0. Re-read immediately before every group at send time.
- **Route of a market with a `set` row** (ethereum/py_ecc): fresh spot sum 0.903507 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (arkworks-rs/algebra): fresh spot sum 0.917109 -> dual-buy; sum after its own set-sell 0.966644 -> dual-buy: they agree.
- **Route of a market with a `set` row** (protofire/solhint): fresh spot sum 0.839929 -> dual-buy; sum after its own set-sell 0.894680 -> dual-buy: they agree.
- **Route of a market with a `set` row** (l2beat/l2beat): fresh spot sum 0.942334 -> simple-buy; sum after its own set-sell 0.981557 -> simple-buy: they agree.
- **Route of a market with a `set` row** (taikoxyz/taiko-mono): fresh spot sum 0.889639 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (flashbots/mev-boost): fresh spot sum 0.855074 -> dual-buy; sum after its own set-sell 0.954044 -> dual-buy: they agree.
- **Route of a market with a `set` row** (libp2p/libp2p): fresh spot sum 0.845029 -> dual-buy; sum after its own set-sell 0.906994 -> dual-buy: they agree.
- **Route of a market with a `set` row** (supranational/blst): fresh spot sum 0.857711 -> dual-buy; sum after its own set-sell 0.919631 -> dual-buy: they agree.
- **Route of a market with a `set` row** (dappnode/DAppNode): fresh spot sum 0.902338 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (lambdaclass/lambdaworks): fresh spot sum 0.951860 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (smartcontracts/simple-optimism-node): fresh spot sum 0.948716 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (shazow/whatsabi): fresh spot sum 0.931581 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (TrueBlocks/trueblocks-core): fresh spot sum 0.887180 -> dual-buy; sum after its own set-sell 0.926628 -> dual-buy: they agree.
- **Route of a market with a `set` row** (succinctlabs/op-succinct): fresh spot sum 0.795209 -> dual-buy; sum after its own set-sell 0.804888 -> dual-buy: they agree.
- **Route of a market with a `set` row** (succinctlabs/sp1): fresh spot sum 0.940095 -> simple-buy; sum after its own set-sell 0.990600 -> simple-buy: they agree.
- **Route of a market with a `set` row** (otterscan/otterscan): fresh spot sum 0.952925 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (NethermindEth/juno): fresh spot sum 0.911139 -> simple-buy; sum after its own set-sell 0.980729 -> simple-buy: they agree.
- **Route of a market with a `set` row** (0xMiden/miden-vm): fresh spot sum 0.927680 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (holiman/goevmlab): fresh spot sum 0.916025 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (evmts/tevm-monorepo): fresh spot sum 0.905103 -> dual-buy; sum after its own set-sell 0.931400 -> dual-buy: they agree.
- **Route of a market with a `set` row** (succinctlabs/rsp): fresh spot sum 0.846920 -> dual-buy; sum after its own set-sell 0.911746 -> dual-buy: they agree.
- **Route of a market with a `set` row** (risc0/risc0-ethereum): fresh spot sum 0.878959 -> dual-buy; sum after its own set-sell 0.914957 -> dual-buy: they agree.
- **Route of a market with a `set` row** (swiss-knife-xyz/swiss-knife): fresh spot sum 0.921150 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (alloy-rs/alloy): fresh spot sum 0.945040 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (ipsilon/evmone): fresh spot sum 0.957645 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (ethereum/execution-apis): fresh spot sum 0.840654 -> dual-buy; sum after its own set-sell 0.898377 -> dual-buy: they agree.
- **Route of a market with a `set` row** (argotorg/fe): fresh spot sum 0.913370 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (remix-project-org/remix-project): fresh spot sum 0.846053 -> dual-buy; sum after its own set-sell 0.891575 -> dual-buy: they agree.
- **Route of a market with a `set` row** (argotorg/solidity): fresh spot sum 0.930925 -> simple-buy; sum after its own set-sell 0.995898 -> simple-buy: they agree.
- **Route of a market with a `set` row** (hyperledger/besu): fresh spot sum 0.913204 -> simple-buy; sum after its own set-sell 0.997011 -> simple-buy: they agree.
- **Route of a market with a `set` row** (nomicfoundation/hardhat): fresh spot sum 0.936196 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (openzeppelin/openzeppelin-contracts): fresh spot sum 0.876284 -> dual-buy; sum after its own set-sell 0.968673 -> dual-buy: they agree.
- **Route of a market with a `set` row** (status-im/nimbus-eth2): fresh spot sum 0.908489 -> dual-buy; sum after its own set-sell 0.939454 -> dual-buy: they agree.
- **Route of a market with a `set` row** (wevm/viem): fresh spot sum 0.898985 -> dual-buy; sum after its own set-sell 0.938106 -> dual-buy: they agree.
- **Route of a market with a `set` row** (ethpandaops/ethereum-package): fresh spot sum 0.838638 -> dual-buy; sum after its own set-sell 0.859436 -> dual-buy: they agree.
- **Route of a market with a `set` row** (ethpandaops/ethereum-helm-charts): fresh spot sum 0.854027 -> dual-buy; sum after its own set-sell 0.921440 -> dual-buy: they agree.
- **Route of a market with a `set` row** (ethpandaops/checkpointz): fresh spot sum 0.906043 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.

## 4. Mints (4 groups at the head of the sequence, each `[approve, split]`)

- `mint-parent`: approve sUSDS -> Router (M) ; Router.splitPosition(sUSDS, parent, M) (gas used 51,089 + 596,058)
- `mint-middle-A`: approve bundle A -> Router (m_X) ; Router.splitPosition(sUSDS, middle A, m_X) (gas used 48,989 + 4,044,628)
- `mint-middle-B`: approve bundle B -> Router (m_X) ; Router.splitPosition(sUSDS, middle B, m_X) (gas used 48,989 + 4,151,476)
- `mint-middle-C`: approve bundle C -> Router (m_X) ; Router.splitPosition(sUSDS, middle C, m_X) (gas used 48,989 + 4,081,560)

## 5. Per-market print (units: the row's own repo token; sUSDS equivalent at the labelled 1/98 in brackets)

### 5a. Pairs: `dual-buy`, "pair (sum < 1 - f)", f = 0.0001 (42 markets)

- **blockscout/blockscout** pair (sum < 1 - f): q = 15.0425 repo tokens; spot sum 0.95403; locked-in sum = cost/q = 14.6913/15.0425 = 0.97665; cost 14.6913 [0.149911 sUSDS]
  - outcome: +(1 - sum)*q = 0.3512 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 14.6913 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +43.3072 tokens for 29.3198 repo tokens (UP leg total 58.3497 tokens at stake 39.0585)
  - legs: UP count 58.3497 (stake 39.0585, inMax 39.2538), DOWN count 15.0425 (stake 4.9526, inMax 4.9774); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **paulmillr/noble-curves** pair (sum < 1 - f): q = 14.7698 repo tokens; spot sum 0.96539; locked-in sum = cost/q = 14.5115/14.7698 = 0.98251; cost 14.5115 [0.148076 sUSDS]
  - outcome: +(1 - sum)*q = 0.2584 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 14.5115 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +1.5504 tokens for 1.3161 repo tokens (UP leg total 16.3202 tokens at stake 13.6876)
  - legs: UP count 16.3202 (stake 13.6876, inMax 13.7560), DOWN count 14.7698 (stake 2.1400, inMax 2.1507); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **arkworks-rs/algebra** pair (sum < 1 - f): q = 13.7582; the pair-cost quote at q failed (print only)
- **protofire/solhint** pair (sum < 1 - f): q = 38.8535; the pair-cost quote at q failed (print only)
- **flashbots/mev-boost** pair (sum < 1 - f): q = 21.3487; the pair-cost quote at q failed (print only)
- **flashbots/mev-boost-relay** pair (sum < 1 - f): q = 23.7649 repo tokens; spot sum 0.93264; locked-in sum = cost/q = 22.9398/23.7649 = 0.96528; cost 22.9398 [0.234080 sUSDS]
  - outcome: +(1 - sum)*q = 0.8250 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 22.9398 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +13.5009 tokens for 10.6856 repo tokens (UP leg total 37.2658 tokens at stake 28.9518)
  - legs: UP count 37.2658 (stake 28.9518, inMax 29.0966), DOWN count 23.7649 (stake 4.6736, inMax 4.6970); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **libp2p/libp2p** pair (sum < 1 - f): q = 45.0957; the pair-cost quote at q failed (print only)
- **supranational/blst** pair (sum < 1 - f): q = 39.8241; the pair-cost quote at q failed (print only)
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
- **ChainSafe/bls** pair (sum < 1 - f): q = 11.9728 repo tokens; spot sum 0.97291; locked-in sum = cost/q = 11.8100/11.9728 = 0.98640; cost 11.8100 [0.120510 sUSDS]
  - outcome: +(1 - sum)*q = 0.1628 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 11.8100 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +102.3749 tokens for 42.2597 repo tokens (DOWN leg total 114.3477 tokens at stake 46.2584)
  - legs: UP count 11.9728 (stake 7.8113, inMax 7.8503), DOWN count 114.3477 (stake 46.2584, inMax 46.4897); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **TrueBlocks/trueblocks-core** pair (sum < 1 - f): q = 23.0948; the pair-cost quote at q failed (print only)
- **succinctlabs/op-succinct** pair (sum < 1 - f): q = 55.2022; the pair-cost quote at q failed (print only)
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
- **evmts/tevm-monorepo** pair (sum < 1 - f): q = 20.1435; the pair-cost quote at q failed (print only)
- **succinctlabs/rsp** pair (sum < 1 - f): q = 32.1594; the pair-cost quote at q failed (print only)
- **ethstaker/ethstaker-deposit-cli** pair (sum < 1 - f): q = 12.1883 repo tokens; spot sum 0.96674; locked-in sum = cost/q = 11.9839/12.1883 = 0.98323; cost 11.9839 [0.122285 sUSDS]
  - outcome: +(1 - sum)*q = 0.2044 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 11.9839 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +45.0724 tokens for 17.9510 repo tokens (DOWN leg total 57.2607 tokens at stake 22.1177)
  - legs: UP count 12.1883 (stake 7.8172, inMax 7.8563), DOWN count 57.2607 (stake 22.1177, inMax 22.2282); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **risc0/risc0-ethereum** pair (sum < 1 - f): q = 41.4179; the pair-cost quote at q failed (print only)
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
- **eth-infinitism/account-abstraction** pair (sum < 1 - f): q = 15.0707 repo tokens; spot sum 0.96196; locked-in sum = cost/q = 14.7812/15.0707 = 0.98079; cost 14.7812 [0.150829 sUSDS]
  - outcome: +(1 - sum)*q = 0.2895 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 14.7812 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +36.0398 tokens for 24.4970 repo tokens (UP leg total 51.1105 tokens at stake 34.3250)
  - legs: UP count 51.1105 (stake 34.3250, inMax 34.4966), DOWN count 15.0707 (stake 4.9532, inMax 4.9780); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **ethereum-lists/chains** pair (sum < 1 - f): q = 12.5683 repo tokens; spot sum 0.96963; locked-in sum = cost/q = 12.3761/12.5683 = 0.98471; cost 12.3761 [0.126287 sUSDS]
  - outcome: +(1 - sum)*q = 0.1921 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 12.3761 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +29.1387 tokens for 21.3300 repo tokens (UP leg total 41.7070 tokens at stake 30.2176)
  - legs: UP count 41.7070 (stake 30.2176, inMax 30.3686), DOWN count 12.5683 (stake 3.4885, inMax 3.5060); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **ethereum/execution-apis** pair (sum < 1 - f): q = 19.5431; the pair-cost quote at q failed (print only)
- **remix-project-org/remix-project** pair (sum < 1 - f): q = 46.9672; the pair-cost quote at q failed (print only)
- **ethers-io/ethers.js** pair (sum < 1 - f): q = 12.7543 repo tokens; spot sum 0.96833; locked-in sum = cost/q = 12.5496/12.7543 = 0.98395; cost 12.5496 [0.128057 sUSDS]
  - outcome: +(1 - sum)*q = 0.2047 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 12.5496 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +28.9459 tokens for 3.6780 repo tokens (DOWN leg total 41.7002 tokens at stake 4.9642)
  - legs: UP count 12.7543 (stake 11.2634, inMax 11.3197), DOWN count 41.7002 (stake 4.9642, inMax 4.9891); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **nethermindeth/nethermind** pair (sum < 1 - f): q = 13.9297 repo tokens; spot sum 0.96363; locked-in sum = cost/q = 13.6738/13.9297 = 0.98162; cost 13.6738 [0.139528 sUSDS]
  - outcome: +(1 - sum)*q = 0.2560 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 13.6738 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +18.5157 tokens for 13.6811 repo tokens (UP leg total 32.4454 tokens at stake 23.7095)
  - legs: UP count 32.4454 (stake 23.7095, inMax 23.8280), DOWN count 13.9297 (stake 3.6453, inMax 3.6636); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **openzeppelin/openzeppelin-contracts** pair (sum < 1 - f): q = 11.7657; the pair-cost quote at q failed (print only)
- **OffchainLabs/prysm** pair (sum < 1 - f): q = 9.8956 repo tokens; spot sum 0.96728; locked-in sum = cost/q = 9.7316/9.8956 = 0.98343; cost 9.7316 [0.099302 sUSDS]
  - outcome: +(1 - sum)*q = 0.1640 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 9.7316 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +33.5598 tokens for 26.1491 repo tokens (UP leg total 43.4553 tokens at stake 33.6018)
  - legs: UP count 43.4553 (stake 33.6018, inMax 33.7698), DOWN count 9.8956 (stake 2.2789, inMax 2.2903); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **safe-global/safe-smart-account** pair (sum < 1 - f): q = 14.3860 repo tokens; spot sum 0.96775; locked-in sum = cost/q = 14.1526/14.3860 = 0.98378; cost 14.1526 [0.144415 sUSDS]
  - outcome: +(1 - sum)*q = 0.2333 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 14.1526 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +159.6297 tokens for 116.7693 repo tokens (UP leg total 174.0157 tokens at stake 125.7132)
  - legs: UP count 174.0157 (stake 125.7132, inMax 126.3418), DOWN count 14.3860 (stake 5.2087, inMax 5.2087); the 0.5% band of DOWN is cut to what the market has left (G section 3); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
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
- **status-im/nimbus-eth2** pair (sum < 1 - f): q = 24.9266; the pair-cost quote at q failed (print only)
- **vyperlang/titanoboa** pair (sum < 1 - f): q = 8.1194 repo tokens; spot sum 0.97487; locked-in sum = cost/q = 8.0167/8.1194 = 0.98735; cost 8.0167 [0.081803 sUSDS]
  - outcome: +(1 - sum)*q = 0.1027 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 8.0167 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +37.3142 tokens for 27.1800 repo tokens (UP leg total 45.4336 tokens at stake 32.8882)
  - legs: UP count 45.4336 (stake 32.8882, inMax 33.0526), DOWN count 8.1194 (stake 2.3085, inMax 2.3201); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions
- **wevm/viem** pair (sum < 1 - f): q = 18.3419; the pair-cost quote at q failed (print only)
- **ethpandaops/ethereum-package** pair (sum < 1 - f): q = 62.3997; the pair-cost quote at q failed (print only)
- **ethpandaops/ethereum-helm-charts** pair (sum < 1 - f): q = 35.2486; the pair-cost quote at q failed (print only)
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

Pairs in total: cost 332.5114 repo tokens, locked gain 6.6314 repo tokens if every repo is evaluated and every child resolves to a score (heterogeneous tokens, informational).

### 5b. Set rows: set-sell and merge-arb (39 markets)

- **ethereum/py_ecc** merge-arb: 26.8586 pairs, cost ~ 25.4901, gain ~ 1.3685 repo tokens now, consumes 26.8586 child Invalid held from earlier runs (I_j 47.4470; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 19.904750774742751921, DOWN 5.712822966422564401 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **arkworks-rs/algebra** merge-arb: 22.8149 pairs, cost ~ 21.4789, gain ~ 1.3360 repo tokens now, consumes 22.8149 child Invalid held from earlier runs (I_j 22.8149; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 18.8187011646730879, DOWN 2.767640399406889392 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **protofire/solhint** merge-arb: 24.9900 pairs, cost ~ 21.6590, gain ~ 3.3311 repo tokens now, consumes 24.9900 child Invalid held from earlier runs (I_j 24.9900; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 16.99974724104513273, DOWN 4.767512264008538848 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **l2beat/l2beat** merge-arb: 14.0202 pairs, cost ~ 13.4831, gain ~ 0.5371 repo tokens now, consumes 14.0202 child Invalid held from earlier runs (I_j 14.0202; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 10.57042517164219378, DOWN 2.980042046966857079 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **taikoxyz/taiko-mono** merge-arb: 39.6063 pairs, cost ~ 37.3200, gain ~ 2.2863 repo tokens now, consumes 39.6063 child Invalid held from earlier runs (I_j 46.4711; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 27.017919965455993188, DOWN 10.488675286244619618 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **flashbots/mev-boost** merge-arb: 54.6886 pairs, cost ~ 49.3697, gain ~ 5.3189 repo tokens now, consumes 54.6886 child Invalid held from earlier runs (I_j 54.6886; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 45.244453226421889277, DOWN 4.372073239866290268 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **libp2p/libp2p** merge-arb: 35.3021 pairs, cost ~ 30.9041, gain ~ 4.3980 repo tokens now, consumes 35.3021 child Invalid held from earlier runs (I_j 35.3021; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 26.565758726648039973, DOWN 4.492822741539872623 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **supranational/blst** merge-arb: 35.8295 pairs, cost ~ 31.8188, gain ~ 4.0108 repo tokens now, consumes 35.8295 child Invalid held from earlier runs (I_j 35.8295; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 28.965903386819659713, DOWN 3.011956268673914033 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **dappnode/DAppNode** merge-arb: 36.4125 pairs, cost ~ 34.5692, gain ~ 1.8433 repo tokens now, consumes 36.4125 child Invalid held from earlier runs (I_j 38.1537; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 23.936183229438503475, DOWN 10.805833883827382831 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **lambdaclass/lambdaworks** merge-arb: 15.8558 pairs, cost ~ 15.4658, gain ~ 0.3900 repo tokens now, consumes 15.8558 child Invalid held from earlier runs (I_j 40.0700; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 12.338096732720796163, DOWN 3.204992271903902531 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **smartcontracts/simple-optimism-node** merge-arb: 23.1816 pairs, cost ~ 22.5798, gain ~ 0.6018 repo tokens now, consumes 23.1816 child Invalid held from earlier runs (I_j 159.6933; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 14.212179271774269731, DOWN 8.480517306229676305 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **shazow/whatsabi** merge-arb: 19.0004 pairs, cost ~ 18.3281, gain ~ 0.6723 repo tokens now, consumes 19.0004 child Invalid held from earlier runs (I_j 30.3781; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 13.645833133574463735, DOWN 4.773890754226522118 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **TrueBlocks/trueblocks-core** merge-arb: 15.2270 pairs, cost ~ 13.8036, gain ~ 1.4234 repo tokens now, consumes 15.2270 child Invalid held from earlier runs (I_j 15.2270; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 11.789588302631622786, DOWN 2.082999396392581553 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **succinctlabs/op-succinct** merge-arb: 3.6529 pairs, cost ~ 2.9227, gain ~ 0.7302 repo tokens now, consumes 3.6529 child Invalid held from earlier runs (I_j 3.6529; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 1.937542508817074435, DOWN 0.999786072931302253 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **succinctlabs/sp1** merge-arb: 22.3113 pairs, cost ~ 21.5312, gain ~ 0.7801 repo tokens now, consumes 22.3113 child Invalid held from earlier runs (I_j 22.3113; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 15.687089527210965294, DOWN 5.951789265326485652 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **otterscan/otterscan** merge-arb: 18.6935 pairs, cost ~ 18.2469, gain ~ 0.4466 repo tokens now, consumes 18.6935 child Invalid held from earlier runs (I_j 52.8634; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 13.797808982060524854, DOWN 4.540310844537277323 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **NethermindEth/juno** merge-arb: 20.0320 pairs, cost ~ 18.9250, gain ~ 1.1070 repo tokens now, consumes 20.0320 child Invalid held from earlier runs (I_j 20.0320; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 14.110346630912403644, DOWN 4.909253741808546393 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **0xMiden/miden-vm** merge-arb: 23.9073 pairs, cost ~ 23.0127, gain ~ 0.8946 repo tokens now, consumes 23.9073 child Invalid held from earlier runs (I_j 30.4867; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 18.116135102152452944, DOWN 5.01163998741667238 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **holiman/goevmlab** merge-arb: 22.2481 pairs, cost ~ 21.2739, gain ~ 0.9741 repo tokens now, consumes 22.2481 child Invalid held from earlier runs (I_j 25.4865; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 15.403189485349376767, DOWN 5.977116593600929262 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **evmts/tevm-monorepo** merge-arb: 8.8238 pairs, cost ~ 8.1018, gain ~ 0.7220 repo tokens now, consumes 8.8238 child Invalid held from earlier runs (I_j 8.8238; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 5.850467756456404191, DOWN 2.291862568487984267 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **succinctlabs/rsp** merge-arb: 28.9067 pairs, cost ~ 25.3938, gain ~ 3.5129 repo tokens now, consumes 28.9067 child Invalid held from earlier runs (I_j 28.9067; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 19.831840680779693916, DOWN 5.688900607865504889 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **risc0/risc0-ethereum** merge-arb: 19.6288 pairs, cost ~ 17.6039, gain ~ 2.0249 repo tokens now, consumes 19.6288 child Invalid held from earlier runs (I_j 19.6288; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 14.102729862632650192, DOWN 3.589173801715114777 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **swiss-knife-xyz/swiss-knife** merge-arb: 26.6841 pairs, cost ~ 25.5949, gain ~ 1.0893 repo tokens now, consumes 26.6841 child Invalid held from earlier runs (I_j 38.7897; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 19.503986240588063806, DOWN 6.218867139126593923 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **alloy-rs/alloy** merge-arb: 15.9666 pairs, cost ~ 15.5161, gain ~ 0.4504 repo tokens now, consumes 15.9666 child Invalid held from earlier runs (I_j 36.1832; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 11.79943688410523419, DOWN 3.794293070655505871 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **ethereum/eips** merge-arb: 20.4565 pairs, cost ~ 19.9593, gain ~ 0.4972 repo tokens now, consumes 20.4565 child Invalid held from earlier runs (I_j 28.8602; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 18.365747762170808271, DOWN 1.693313676226120165 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **ipsilon/evmone** merge-arb: 16.5805 pairs, cost ~ 16.2246, gain ~ 0.3559 repo tokens now, consumes 16.5805 child Invalid held from earlier runs (I_j 27.9608; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 12.347633849418905919, DOWN 3.958076370360129163 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **ethereum/execution-apis** merge-arb: 16.5757 pairs, cost ~ 14.3894, gain ~ 2.1863 repo tokens now, consumes 16.5757 child Invalid held from earlier runs (I_j 16.5757; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 12.189823076298209052, DOWN 2.271526325195013811 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **argotorg/fe** merge-arb: 30.2904 pairs, cost ~ 28.9235, gain ~ 1.3669 repo tokens now, consumes 30.2904 child Invalid held from earlier runs (I_j 32.0793; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 23.128922287733423527, DOWN 5.939188048552132191 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **remix-project-org/remix-project** merge-arb: 23.9560 pairs, cost ~ 20.8047, gain ~ 3.1513 repo tokens now, consumes 23.9560 child Invalid held from earlier runs (I_j 23.9560; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 17.873378079025137416, DOWN 3.035352459965672159 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **argotorg/solidity** merge-arb: 25.6873 pairs, cost ~ 24.7251, gain ~ 0.9621 repo tokens now, consumes 25.6873 child Invalid held from earlier runs (I_j 25.6873; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 20.642949981889873245, DOWN 4.205812600117142443 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **hyperledger/besu** merge-arb: 31.3847 pairs, cost ~ 29.9303, gain ~ 1.4545 repo tokens now, consumes 31.3847 child Invalid held from earlier runs (I_j 31.3847; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 23.346943913548841593, DOWN 6.732967113489915461 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **nomicfoundation/hardhat** merge-arb: 18.2851 pairs, cost ~ 17.6834, gain ~ 0.6018 repo tokens now, consumes 18.2851 child Invalid held from earlier runs (I_j 30.3516; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 13.348337707185553289, DOWN 4.423450729363815246 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **openzeppelin/openzeppelin-contracts** merge-arb: 41.3285 pairs, cost ~ 38.0477, gain ~ 3.2808 repo tokens now, consumes 41.3285 child Invalid held from earlier runs (I_j 41.3285; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 32.439886680481082189, DOWN 5.798058235043924491 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **status-im/nimbus-eth2** merge-arb: 15.0667 pairs, cost ~ 13.9184, gain ~ 1.1483 repo tokens now, consumes 15.0667 child Invalid held from earlier runs (I_j 15.0667; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 13.099283173761807983, DOWN 0.888690368280954743 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **wevm/viem** merge-arb: 13.6393 pairs, cost ~ 12.5239, gain ~ 1.1154 repo tokens now, consumes 13.6393 child Invalid held from earlier runs (I_j 13.6393; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 9.935655605464679302, DOWN 2.650844869502405561 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **argotorg/act** merge-arb: 25.2138 pairs, cost ~ 24.3483, gain ~ 0.8654 repo tokens now, consumes 25.2138 child Invalid held from earlier runs (I_j 29.4622; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 19.760029017651659099, DOWN 4.710062489670568269 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **ethpandaops/ethereum-package** merge-arb: 11.0472 pairs, cost ~ 9.3795, gain ~ 1.6677 repo tokens now, consumes 11.0472 child Invalid held from earlier runs (I_j 11.0472; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 7.325061829035873659, DOWN 2.101334852536923331 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **ethpandaops/ethereum-helm-charts** merge-arb: 34.5772 pairs, cost ~ 30.6737, gain ~ 3.9035 repo tokens now, consumes 34.5772 child Invalid held from earlier runs (I_j 34.5772; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 19.316207519898645266, DOWN 11.510884216311246161 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **ethpandaops/checkpointz** merge-arb: 44.2902 pairs, cost ~ 42.1574, gain ~ 2.1328 repo tokens now, consumes 44.2902 child Invalid held from earlier runs (I_j 63.5122; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 23.470458761347737769, DOWN 18.897680856272138907 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.

### 5c. Complex-buy (13 groups: split `x = stake`, sell the other leg, buy the own leg with the proceeds; keeps `x` child Invalid; the last two transactions are rebuilt at send time with the realised proceeds)

- **herumi/mcl** complex-buy UP: split x = 101.5777 repo tokens [1.036508 sUSDS-eq], sell x DOWN for P = 21.1639 repo tokens, buy 28.2474 UP -> **129.8251 UP + 101.5777 child Invalid** (quoted total; F's simple-route count 125.0874; complex 3.788% vs the simple route); spot sum 1.01980 > 1; p_win 0.9000
- **Consensys/gnark-crypto** complex-buy UP: split x = 38.1415 repo tokens [0.389199 sUSDS-eq], sell x DOWN for P = 5.3344 repo tokens, buy 6.3393 UP -> **44.4808 UP + 38.1415 child Invalid** (quoted total; F's simple-route count 43.9412; complex 1.228% vs the simple route); spot sum 1.00044 > 1; p_win 0.9000
- **ethereum/js-ethereum-cryptography** complex-buy DOWN: split x = 12.7754 repo tokens [0.130362 sUSDS-eq], sell x UP for P = 7.4165 repo tokens, buy 16.1008 DOWN -> **28.8763 DOWN + 12.7754 child Invalid** (quoted total; F's simple-route count 26.3547; complex 9.568% vs the simple route); spot sum 1.01297 > 1; p_win 0.5500
- **Certora/CertoraProver** complex-buy UP: split x = 50.7233 repo tokens [0.517585 sUSDS-eq], sell x DOWN for P = 12.1540 repo tokens, buy 16.6581 UP -> **67.3813 UP + 50.7233 child Invalid** (quoted total; F's simple-route count 66.8190; complex 0.842% vs the simple route); spot sum 1.01286 > 1; p_win 0.8000
- **wealdtech/ethdo** complex-buy UP: split x = 22.5142 repo tokens [0.229737 sUSDS-eq], sell x DOWN for P = 6.0696 repo tokens, buy 8.4404 UP -> **30.9546 UP + 22.5142 child Invalid** (quoted total; F's simple-route count 30.7583; complex 0.638% vs the simple route); spot sum 1.00388 > 1; p_win 0.7500
- **skalenetwork/libBLS** complex-buy UP: split x = 43.1426 repo tokens [0.440231 sUSDS-eq], sell x DOWN for P = 12.3950 repo tokens, buy 17.9110 UP -> **61.0536 UP + 43.1426 child Invalid** (quoted total; F's simple-route count 60.2978; complex 1.254% vs the simple route); spot sum 1.01416 > 1; p_win 0.7500
- **Cyfrin/aderyn** complex-buy UP: split x = 30.5838 repo tokens [0.312080 sUSDS-eq], sell x DOWN for P = 9.7140 repo tokens, buy 14.6853 UP -> **45.2691 UP + 30.5838 child Invalid** (quoted total; F's simple-route count 45.1895; complex 0.176% vs the simple route); spot sum 1.01539 > 1; p_win 0.7000
- **OffchainLabs/stylus-sdk-rs** complex-buy UP: split x = 82.0331 repo tokens [0.837073 sUSDS-eq], sell x DOWN for P = 20.5270 repo tokens, buy 29.8956 UP -> **111.9287 UP + 82.0331 child Invalid** (quoted total; F's simple-route count 111.9471; complex -0.016% vs the simple route); spot sum 1.00007 > 1; p_win 0.8000
- **axiom-crypto/snark-verifier** complex-buy DOWN: split x = 6.6981 repo tokens [0.068348 sUSDS-eq], sell x UP for P = 4.5975 repo tokens, buy 14.2193 DOWN -> **20.9174 DOWN + 6.6981 child Invalid** (quoted total; F's simple-route count 20.3338; complex 2.870% vs the simple route); spot sum 1.00006 > 1; p_win 0.3500
- **erigontech/erigon** complex-buy UP: split x = 14.2001 repo tokens [0.144898 sUSDS-eq], sell x DOWN for P = 3.7004 repo tokens, buy 5.0663 UP -> **19.2664 UP + 14.2001 child Invalid** (quoted total; F's simple-route count 19.2243; complex 0.219% vs the simple route); spot sum 1.00007 > 1; p_win 0.7500
- **ethereum/consensus-specs** complex-buy UP: split x = 13.4148 repo tokens [0.136885 sUSDS-eq], sell x DOWN for P = 1.5529 repo tokens, buy 1.7655 UP -> **15.1803 UP + 13.4148 child Invalid** (quoted total; F's simple-route count 15.0878; complex 0.613% vs the simple route); spot sum 1.01711 > 1; p_win 0.9000
- **foundry-rs/foundry** complex-buy UP: split x = 12.9999 repo tokens [0.132652 sUSDS-eq], sell x DOWN for P = 2.1309 repo tokens, buy 2.5661 UP -> **15.5661 UP + 12.9999 child Invalid** (quoted total; F's simple-route count 15.4899; complex 0.491% vs the simple route); spot sum 1.00005 > 1; p_win 0.8500
- **argotorg/hevm** complex-buy UP: split x = 47.0350 repo tokens [0.479949 sUSDS-eq], sell x DOWN for P = 11.6245 repo tokens, buy 15.8335 UP -> **62.8685 UP + 47.0350 child Invalid** (quoted total; F's simple-route count 61.7536; complex 1.805% vs the simple route); spot sum 1.01647 > 1; p_win 0.8000

### 5d. Simple-buy (35 groups: one approve and one `exactInputSingle`, min 99.5% of the quote)

- **ethereum/py_ecc** simple-buy UP: stake 62.0470 repo tokens [0.633132 sUSDS-eq], quoted out 77.5817 UP (F count 77.5817), floor 77.1938; spot sum 0.90351 (quoted on the post-set-sell state); p_win 0.8500
- **LFDT-web3j/web3j** simple-buy UP: stake 32.9636 repo tokens [0.336363 sUSDS-eq], quoted out 42.6062 UP (F count 42.6062), floor 42.3932; spot sum 0.96623 < 1; p_win 0.8000
- **flashbots/rbuilder** simple-buy UP: stake 39.0512 repo tokens [0.398482 sUSDS-eq], quoted out 54.3725 UP (F count 54.3725), floor 54.1007; spot sum 0.98064 < 1; p_win 0.7500
- **l2beat/l2beat** simple-buy UP: stake 26.1938 repo tokens [0.267284 sUSDS-eq], quoted out 33.6276 UP (F count 33.6276), floor 33.4595; spot sum 0.94233 (quoted on the post-set-sell state); p_win 0.8000
- **taikoxyz/taiko-mono** simple-buy UP: stake 32.3273 repo tokens [0.329871 sUSDS-eq], quoted out 44.6342 UP (F count 44.6342), floor 44.4110; spot sum 0.88964 (quoted on the post-set-sell state); p_win 0.7500
- **DefiLlama/chainlist** simple-buy UP: stake 10.1196 repo tokens [0.103261 sUSDS-eq], quoted out 14.6262 UP (F count 14.6262), floor 14.5530; spot sum 0.99538 < 1; p_win 0.7000
- **intellij-solidity/intellij-solidity** simple-buy UP: stake 17.8012 repo tokens [0.181645 sUSDS-eq], quoted out 22.6666 UP (F count 22.6666), floor 22.5533; spot sum 0.98889 < 1; p_win 0.8000
- **dappnode/DAppNode** simple-buy UP: stake 17.6120 repo tokens [0.179715 sUSDS-eq], quoted out 25.6693 UP (F count 25.6693), floor 25.5410; spot sum 0.90234 (quoted on the post-set-sell state); p_win 0.7000
- **lambdaclass/lambdaworks** simple-buy UP: stake 41.1808 repo tokens [0.420212 sUSDS-eq], quoted out 50.4486 UP (F count 50.4486), floor 50.1963; spot sum 0.95186 (quoted on the post-set-sell state); p_win 0.8500
- **smartcontracts/simple-optimism-node** simple-buy DOWN: stake 21.7771 repo tokens [0.222215 sUSDS-eq], quoted out 52.8402 DOWN (F count 52.8402), floor 52.5760; spot sum 0.94872 (quoted on the post-set-sell state); p_win 0.4500
- **shazow/whatsabi** simple-buy UP: stake 79.4711 repo tokens [0.810930 sUSDS-eq], quoted out 101.2435 UP (F count 101.2435), floor 100.7373; spot sum 0.93158 (quoted on the post-set-sell state); p_win 0.8500
- **EspressoSystems/jellyfish** simple-buy UP: stake 52.5984 repo tokens [0.536719 sUSDS-eq], quoted out 85.8958 UP (F count 85.8958), floor 85.4663; spot sum 0.97191 < 1; p_win 0.6500
- **a16z/halmos** simple-buy UP: stake 25.0817 repo tokens [0.255936 sUSDS-eq], quoted out 34.3284 UP (F count 34.3284), floor 34.1567; spot sum 0.99323 < 1; p_win 0.7500
- **succinctlabs/sp1** simple-buy UP: stake 22.2800 repo tokens [0.227347 sUSDS-eq], quoted out 30.4772 UP (F count 30.4772), floor 30.3248; spot sum 0.94010 (quoted on the post-set-sell state); p_win 0.7500
- **otterscan/otterscan** simple-buy DOWN: stake 7.7255 repo tokens [0.078832 sUSDS-eq], quoted out 27.9622 DOWN (F count 27.9622), floor 27.8224; spot sum 0.95293 (quoted on the post-set-sell state); p_win 0.3000
- **NethermindEth/juno** simple-buy UP: stake 25.4350 repo tokens [0.259541 sUSDS-eq], quoted out 34.8213 UP (F count 34.8213), floor 34.6472; spot sum 0.91114 (quoted on the post-set-sell state); p_win 0.7500
- **0xMiden/miden-vm** simple-buy UP: stake 51.2195 repo tokens [0.522648 sUSDS-eq], quoted out 63.3915 UP (F count 63.3915), floor 63.0745; spot sum 0.92768 (quoted on the post-set-sell state); p_win 0.8500
- **holiman/goevmlab** simple-buy UP: stake 64.8199 repo tokens [0.661428 sUSDS-eq], quoted out 86.6013 UP (F count 86.6013), floor 86.1683; spot sum 0.91603 (quoted on the post-set-sell state); p_win 0.8000
- **dl-solarity/solidity-lib** simple-buy UP: stake 48.9774 repo tokens [0.499770 sUSDS-eq], quoted out 68.9125 UP (F count 68.9125), floor 68.5680; spot sum 0.95357 < 1; p_win 0.7500
- **swiss-knife-xyz/swiss-knife** simple-buy DOWN: stake 4.8888 repo tokens [0.049886 sUSDS-eq], quoted out 17.5837 DOWN (F count 17.5837), floor 17.4958; spot sum 0.92115 (quoted on the post-set-sell state); p_win 0.3000
- **a16z/helios** simple-buy UP: stake 28.1846 repo tokens [0.287598 sUSDS-eq], quoted out 36.3067 UP (F count 36.3067), floor 36.1252; spot sum 0.98875 < 1; p_win 0.8000
- **alloy-rs/alloy** simple-buy UP: stake 66.6894 repo tokens [0.680505 sUSDS-eq], quoted out 83.8428 UP (F count 83.8428), floor 83.4236; spot sum 0.94504 (quoted on the post-set-sell state); p_win 0.8500
- **apeworx/ape** simple-buy UP: stake 16.8390 repo tokens [0.171826 sUSDS-eq], quoted out 22.8628 UP (F count 22.8628), floor 22.7485; spot sum 0.99993 < 1; p_win 0.7500
- **ipsilon/evmone** simple-buy UP: stake 59.6810 repo tokens [0.608990 sUSDS-eq], quoted out 74.7031 UP (F count 74.7031), floor 74.3296; spot sum 0.95764 (quoted on the post-set-sell state); p_win 0.8500
- **argotorg/fe** simple-buy UP: stake 44.9510 repo tokens [0.458683 sUSDS-eq], quoted out 55.2822 UP (F count 55.2822), floor 55.0058; spot sum 0.91337 (quoted on the post-set-sell state); p_win 0.8500
- **argotorg/solidity** simple-buy UP: stake 20.8130 repo tokens [0.212377 sUSDS-eq], quoted out 24.9884 UP (F count 24.9884), floor 24.8634; spot sum 0.93092 (quoted on the post-set-sell state); p_win 0.8500
- **argotorg/sourcify** simple-buy UP: stake 29.2914 repo tokens [0.298892 sUSDS-eq], quoted out 40.3344 UP (F count 40.3344), floor 40.1327; spot sum 0.98511 < 1; p_win 0.7500
- **grandinetech/grandine** simple-buy UP: stake 40.3133 repo tokens [0.411360 sUSDS-eq], quoted out 52.5387 UP (F count 52.5387), floor 52.2760; spot sum 0.95340 < 1; p_win 0.8000
- **hyperledger-web3j/web3j** simple-buy UP: stake 19.5606 repo tokens [0.199598 sUSDS-eq], quoted out 26.6377 UP (F count 26.6377), floor 26.5045; spot sum 0.99028 < 1; p_win 0.7500
- **hyperledger/besu** simple-buy UP: stake 25.9890 repo tokens [0.265194 sUSDS-eq], quoted out 33.3632 UP (F count 33.3632), floor 33.1964; spot sum 0.91320 (quoted on the post-set-sell state); p_win 0.8000
- **nethereum/nethereum** simple-buy UP: stake 11.6171 repo tokens [0.118542 sUSDS-eq], quoted out 13.8211 UP (F count 13.8211), floor 13.7520; spot sum 0.98287 < 1; p_win 0.8500
- **nomicfoundation/hardhat** simple-buy UP: stake 40.8125 repo tokens [0.416454 sUSDS-eq], quoted out 53.1694 UP (F count 53.1694), floor 52.9036; spot sum 0.93620 (quoted on the post-set-sell state); p_win 0.8000
- **vyperlang/vyper** simple-buy UP: stake 14.0061 repo tokens [0.142919 sUSDS-eq], quoted out 17.7523 UP (F count 17.7523), floor 17.6635; spot sum 0.98037 < 1; p_win 0.8000
- **ethdebug/format** simple-buy UP: stake 65.6917 repo tokens [0.670323 sUSDS-eq], quoted out 82.6470 UP (F count 82.6470), floor 82.2338; spot sum 0.99219 < 1; p_win 0.8500
- **ethpandaops/checkpointz** simple-buy UP: stake 54.6883 repo tokens [0.558044 sUSDS-eq], quoted out 91.6224 UP (F count 91.6224), floor 91.1643; spot sum 0.90604 (quoted on the post-set-sell state); p_win 0.6500

### 5e. Skipped rows (0: never sent; the executor writes each `status: "skipped"` with its reason)

- none

## 6. Group order and gas (send order)

| # | group | tx | gas used |
|---|---|---|---|
| 0 | `mint-parent` | 0-1 | 647,147 |
| 1 | `mint-middle-A` | 2-3 | 4,093,617 |
| 2 | `mint-middle-B` | 4-5 | 4,200,465 |
| 3 | `mint-middle-C` | 6-7 | 4,130,549 |
| 4 | `merge-arb:ethereum/py_ecc` | 8-14 | 1,110,932 |
| 5 | `simple-buy:ethereum/py_ecc:UP` | 15-16 | 184,517 |
| 6 | `dual-buy:blockscout/blockscout` | 17-20 | 384,668 |
| 7 | `simple-buy:LFDT-web3j/web3j:UP` | 21-22 | 186,960 |
| 8 | `complex-buy:herumi/mcl:UP` | 23-28 | 1,047,767 |
| 9 | `dual-buy:paulmillr/noble-curves` | 29-32 | 363,379 |
| 10 | `merge-arb:arkworks-rs/algebra` | 33-39 | 979,611 |
| 11 | `dual-buy:arkworks-rs/algebra` | 40-43 | 353,349 |
| 12 | `simple-buy:flashbots/rbuilder:UP` | 44-45 | 187,715 |
| 13 | `merge-arb:protofire/solhint` | 46-52 | 981,392 |
| 14 | `dual-buy:protofire/solhint` | 53-56 | 403,846 |
| 15 | `merge-arb:l2beat/l2beat` | 57-63 | 1,030,361 |
| 16 | `simple-buy:l2beat/l2beat:UP` | 64-65 | 162,520 |
| 17 | `complex-buy:Consensys/gnark-crypto:UP` | 66-71 | 931,207 |
| 18 | `merge-arb:taikoxyz/taiko-mono` | 72-78 | 1,024,532 |
| 19 | `simple-buy:taikoxyz/taiko-mono:UP` | 79-80 | 162,632 |
| 20 | `merge-arb:flashbots/mev-boost` | 81-87 | 1,079,554 |
| 21 | `dual-buy:flashbots/mev-boost` | 88-91 | 359,774 |
| 22 | `dual-buy:flashbots/mev-boost-relay` | 92-95 | 388,813 |
| 23 | `complex-buy:ethereum/js-ethereum-cryptography:DOWN` | 96-101 | 932,687 |
| 24 | `merge-arb:libp2p/libp2p` | 102-108 | 1,020,136 |
| 25 | `dual-buy:libp2p/libp2p` | 109-112 | 412,168 |
| 26 | `merge-arb:supranational/blst` | 113-119 | 1,053,220 |
| 27 | `dual-buy:supranational/blst` | 120-123 | 413,733 |
| 28 | `dual-buy:wighawag/hardhat-deploy` | 124-127 | 357,120 |
| 29 | `dual-buy:ethstaker/eth-docker` | 128-131 | 391,410 |
| 30 | `dual-buy:DefiLlama/DefiLlama-Adapters` | 132-135 | 391,644 |
| 31 | `simple-buy:DefiLlama/chainlist:UP` | 136-137 | 173,014 |
| 32 | `complex-buy:Certora/CertoraProver:UP` | 138-143 | 1,024,078 |
| 33 | `dual-buy:Plonky3/Plonky3` | 144-147 | 370,471 |
| 34 | `dual-buy:ChainSafe/bls` | 148-151 | 448,163 |
| 35 | `simple-buy:intellij-solidity/intellij-solidity:UP` | 152-153 | 180,258 |
| 36 | `merge-arb:dappnode/DAppNode` | 154-160 | 1,006,385 |
| 37 | `simple-buy:dappnode/DAppNode:UP` | 161-162 | 163,272 |
| 38 | `complex-buy:wealdtech/ethdo:UP` | 163-168 | 903,966 |
| 39 | `merge-arb:lambdaclass/lambdaworks` | 169-175 | 1,021,120 |
| 40 | `simple-buy:lambdaclass/lambdaworks:UP` | 176-177 | 170,535 |
| 41 | `merge-arb:smartcontracts/simple-optimism-node` | 178-184 | 988,018 |
| 42 | `simple-buy:smartcontracts/simple-optimism-node:DOWN` | 185-186 | 199,226 |
| 43 | `complex-buy:skalenetwork/libBLS:UP` | 187-192 | 974,619 |
| 44 | `merge-arb:shazow/whatsabi` | 193-199 | 975,964 |
| 45 | `simple-buy:shazow/whatsabi:UP` | 200-201 | 192,480 |
| 46 | `merge-arb:TrueBlocks/trueblocks-core` | 202-208 | 969,396 |
| 47 | `dual-buy:TrueBlocks/trueblocks-core` | 209-212 | 403,516 |
| 48 | `simple-buy:EspressoSystems/jellyfish:UP` | 213-214 | 219,960 |
| 49 | `simple-buy:a16z/halmos:UP` | 215-216 | 180,382 |
| 50 | `merge-arb:succinctlabs/op-succinct` | 217-223 | 949,644 |
| 51 | `dual-buy:succinctlabs/op-succinct` | 224-227 | 473,613 |
| 52 | `merge-arb:succinctlabs/sp1` | 228-234 | 1,018,099 |
| 53 | `simple-buy:succinctlabs/sp1:UP` | 235-236 | 163,258 |
| 54 | `merge-arb:otterscan/otterscan` | 237-243 | 982,536 |
| 55 | `simple-buy:otterscan/otterscan:DOWN` | 244-245 | 192,566 |
| 56 | `dual-buy:lambdaclass/ethrex` | 246-249 | 390,951 |
| 57 | `merge-arb:NethermindEth/juno` | 250-256 | 1,058,215 |
| 58 | `simple-buy:NethermindEth/juno:UP` | 257-258 | 163,282 |
| 59 | `dual-buy:Commit-Boost/commit-boost-client` | 259-262 | 383,868 |
| 60 | `complex-buy:Cyfrin/aderyn:UP` | 263-268 | 976,009 |
| 61 | `merge-arb:0xMiden/miden-vm` | 269-275 | 1,016,628 |
| 62 | `simple-buy:0xMiden/miden-vm:UP` | 276-277 | 177,853 |
| 63 | `merge-arb:holiman/goevmlab` | 278-284 | 984,739 |
| 64 | `simple-buy:holiman/goevmlab:UP` | 285-286 | 185,166 |
| 65 | `dual-buy:edb-rs/edb` | 287-290 | 374,548 |
| 66 | `merge-arb:evmts/tevm-monorepo` | 291-297 | 963,785 |
| 67 | `dual-buy:evmts/tevm-monorepo` | 298-301 | 388,084 |
| 68 | `merge-arb:succinctlabs/rsp` | 302-308 | 1,038,391 |
| 69 | `dual-buy:succinctlabs/rsp` | 309-312 | 500,406 |
| 70 | `complex-buy:OffchainLabs/stylus-sdk-rs:UP` | 313-318 | 1,024,022 |
| 71 | `dual-buy:ethstaker/ethstaker-deposit-cli` | 319-322 | 419,205 |
| 72 | `simple-buy:dl-solarity/solidity-lib:UP` | 323-324 | 212,161 |
| 73 | `merge-arb:risc0/risc0-ethereum` | 325-331 | 944,055 |
| 74 | `dual-buy:risc0/risc0-ethereum` | 332-335 | 458,962 |
| 75 | `dual-buy:powdr-labs/powdr` | 336-339 | 383,913 |
| 76 | `complex-buy:axiom-crypto/snark-verifier:DOWN` | 340-345 | 917,423 |
| 77 | `merge-arb:swiss-knife-xyz/swiss-knife` | 346-352 | 1,073,189 |
| 78 | `simple-buy:swiss-knife-xyz/swiss-knife:DOWN` | 353-354 | 185,232 |
| 79 | `simple-buy:a16z/helios:UP` | 355-356 | 186,936 |
| 80 | `merge-arb:alloy-rs/alloy` | 357-363 | 996,744 |
| 81 | `simple-buy:alloy-rs/alloy:UP` | 364-365 | 184,529 |
| 82 | `simple-buy:apeworx/ape:UP` | 366-367 | 173,026 |
| 83 | `dual-buy:consensys/teku` | 368-371 | 394,683 |
| 84 | `complex-buy:erigontech/erigon:UP` | 372-377 | 937,481 |
| 85 | `dual-buy:eth-infinitism/account-abstraction` | 378-381 | 371,217 |
| 86 | `dual-buy:ethereum-lists/chains` | 382-385 | 345,613 |
| 87 | `complex-buy:ethereum/consensus-specs:UP` | 386-391 | 971,234 |
| 88 | `merge-arb:ethereum/eips` | 392-398 | 1,025,174 |
| 89 | `merge-arb:ipsilon/evmone` | 399-405 | 983,372 |
| 90 | `simple-buy:ipsilon/evmone:UP` | 406-407 | 184,541 |
| 91 | `merge-arb:ethereum/execution-apis` | 408-414 | 1,014,896 |
| 92 | `dual-buy:ethereum/execution-apis` | 415-418 | 445,393 |
| 93 | `merge-arb:argotorg/fe` | 419-425 | 1,002,558 |
| 94 | `simple-buy:argotorg/fe:UP` | 426-427 | 170,511 |
| 95 | `merge-arb:remix-project-org/remix-project` | 428-434 | 985,853 |
| 96 | `dual-buy:remix-project-org/remix-project` | 435-438 | 445,368 |
| 97 | `merge-arb:argotorg/solidity` | 439-445 | 1,053,359 |
| 98 | `simple-buy:argotorg/solidity:UP` | 446-447 | 155,275 |
| 99 | `simple-buy:argotorg/sourcify:UP` | 448-449 | 180,382 |
| 100 | `dual-buy:ethers-io/ethers.js` | 450-453 | 461,825 |
| 101 | `complex-buy:foundry-rs/foundry:UP` | 454-459 | 912,608 |
| 102 | `simple-buy:grandinetech/grandine:UP` | 460-461 | 187,615 |
| 103 | `simple-buy:hyperledger-web3j/web3j:UP` | 462-463 | 173,050 |
| 104 | `merge-arb:hyperledger/besu` | 464-470 | 1,002,698 |
| 105 | `simple-buy:hyperledger/besu:UP` | 471-472 | 162,508 |
| 106 | `simple-buy:nethereum/nethereum:UP` | 473-474 | 172,976 |
| 107 | `dual-buy:nethermindeth/nethermind` | 475-478 | 347,122 |
| 108 | `merge-arb:nomicfoundation/hardhat` | 479-485 | 1,047,034 |
| 109 | `simple-buy:nomicfoundation/hardhat:UP` | 486-487 | 170,515 |
| 110 | `merge-arb:openzeppelin/openzeppelin-contracts` | 488-494 | 1,015,513 |
| 111 | `dual-buy:openzeppelin/openzeppelin-contracts` | 495-498 | 353,381 |
| 112 | `dual-buy:OffchainLabs/prysm` | 499-502 | 360,471 |
| 113 | `dual-buy:safe-global/safe-smart-account` | 503-506 | 434,758 |
| 114 | `dual-buy:scaffold-eth/scaffold-eth-2` | 507-510 | 356,338 |
| 115 | `dual-buy:sigp/lighthouse` | 511-514 | 410,070 |
| 116 | `merge-arb:status-im/nimbus-eth2` | 515-521 | 1,005,324 |
| 117 | `dual-buy:status-im/nimbus-eth2` | 522-525 | 453,111 |
| 118 | `dual-buy:vyperlang/titanoboa` | 526-529 | 380,464 |
| 119 | `simple-buy:vyperlang/vyper:UP` | 530-531 | 155,147 |
| 120 | `merge-arb:wevm/viem` | 532-538 | 995,150 |
| 121 | `dual-buy:wevm/viem` | 539-542 | 388,787 |
| 122 | `complex-buy:argotorg/hevm:UP` | 543-548 | 974,858 |
| 123 | `simple-buy:ethdebug/format:UP` | 549-550 | 202,286 |
| 124 | `merge-arb:argotorg/act` | 551-557 | 1,012,412 |
| 125 | `merge-arb:ethpandaops/ethereum-package` | 558-564 | 969,911 |
| 126 | `dual-buy:ethpandaops/ethereum-package` | 565-568 | 495,790 |
| 127 | `merge-arb:ethpandaops/ethereum-helm-charts` | 569-575 | 1,009,552 |
| 128 | `dual-buy:ethpandaops/ethereum-helm-charts` | 576-579 | 365,576 |
| 129 | `merge-arb:ethpandaops/checkpointz` | 580-586 | 1,009,299 |
| 130 | `simple-buy:ethpandaops/checkpointz:UP` | 587-588 | 199,180 |
| 131 | `dual-buy:lambdaclass/lambda_ethereum_consensus` | 589-592 | 363,416 |
| 132 | `dual-buy:erigontech/silkworm` | 593-596 | 398,713 |

## 7. Risks the human is told before any "yes" (supervised mode)

- **One transaction per signer call.** Every group above is an ordered sequence of single transactions and **can be left half-done between transactions** (one pair leg bought, a split without its sales, a `set-sell` whose gain is locked only if its whole group lands). A stopped group goes to the recovery rule (G section 8 step 4). EIP-7702 removes this risk and is recommended.
- **Residual risks (a) and (b)** of every pair and of the folded directional rows (section 5a): (a) the repo is evaluated but its child question resolves INVALID, UP + DOWN pay 0; (b) the parent's `n_X` and the middle's `k_X` disagree, a repo token pays `(n_X/N)/k_X`.
- **1 pair binds the market's repo-token budget** (safe-global/safe-smart-account): the second leg's `inMax` is cut to what the market has left (G section 3), so a drift at send larger than that headroom reverts it and leaves the pair half-done; that goes to the recovery rule, never to a resize.
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

- calldata audit: 133 groups, 597 transactions decoded and re-derived from allocation.json (171 rows: 171 in groups, 0 skipped), kinds {"mint":4,"merge-arb":39,"simple-buy":35,"dual-buy":42,"complex-buy":13}, every approval exact (none near 2^256), every swap recipient the holder, every tier the candidates.json tier, dual-buy inMax = min(stake x 1.005, remaining); failures 0
- fresh re-simulation of run/2026-10-28T1629Z/g-sim-w1-of-2.json (sha256 b2c486ef1720c95e0ecf24245209cec937d7442729ca75b7d78b355891724963): {"entries":68,"count":302,"all_success":true,"failed_count":0,"over_cap_count":0,"clamped_count":0,"pending_nonce":2693,"overrides_active":"absent","no_max_used_gas_count":0}
- fresh re-simulation of run/2026-10-28T1629Z/g-sim-w2-of-2.json (sha256 d644b6d3536aac1a3eecfd2b172f1a3d31440d6e2620f9d16ac9ec607d274141): {"entries":69,"count":303,"all_success":true,"failed_count":0,"over_cap_count":0,"clamped_count":0,"pending_nonce":2693,"overrides_active":"absent","no_max_used_gas_count":0}
- holder nonce latest/pending before 2693/2693, after 2693/2693 (the plan's 2693); per-call rows of the fresh simulation: 605 checked, every status 0x1 and every fresh peak within the plan's gas_limit; gasUsed equal to the build's on all
- AUDIT PASSED: every acceptance check holds
