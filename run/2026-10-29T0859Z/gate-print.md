# G gate print - run 2026-10-29T0859Z

**Optimism mainnet, holder 0x2AD670e5953a85C998cDf1C2f6D74386aB735d4a. Built, simulated and verified: nothing has been signed or sent.** Pending nonce 3480; head at G's read 158832895 (blocks are reported, never compared between reads). Every group below is an ordered sequence of single transactions, one signer call each.

## 1. The numbers

| | |
|---|---|
| **Allocation input** | `run/2026-10-29T0859Z/allocation.json` (sha256 `43723fd26479da8f45ecb0a54ddb6b62797a38d9e629e88cc949918c368f53c4`), generated 2026-10-29T09:02:40Z, 78 rows; 69 markets traded, 0 rows skipped (section 5e) |
| **Counts per route** | pair (`dual-buy`) **1** markets (2 rows); `simple-buy` **23**; `complex-buy` **41** (34 single-side markets with spot sum > 1, plus 7 on a market whose `set-sell` runs first); `set-sell` **11**; `merge-arb` (`buy-and-merge`) **1**; mint groups **4** (mint-parent, mint-middle-A, mint-middle-B, mint-middle-C); PSM3 ramp: none |
| **Total sUSDS staked** | **140.324473992044 sUSDS** = `totals.staked` = the new mint `M` (the holder holds 577.136995285407498579). Middles split: A by m_X = 200.504467222994414475, B by m_X = 258.389203294166323006, C by m_X = 140.324473992044. Each traded market's budget is its held repo tokens plus m_X; the rows' stakes sum to 1999.8280 repo tokens of 69 different tokens (20.4064 sUSDS-equivalent at the labelled 1/98) |
| **Expected value** | **0.932686 sUSDS** at the labelled 1/N = 1/98 (F's `totals.expected_value`; 91.4032 repo tokens summed over heterogeneous markets, / 98; 0 for any repo that is not evaluated) |
| **Worst case** | `correlated_worst_case` **-140.324474 sUSDS** (F's definition); a `set-sell` row's gain is locked only if its whole group lands |
| **Number of transactions** | **377** in **81** keep-whole groups (mint 8, complex-buy 246, simple-buy 46, set-sell 66, merge-arb 7, dual-buy 4), nonces 3480 to 3856 |
| **Estimated gas** | **66,900,060 gas used** (mints 13,071,820; complex-buy 38,112,790; simple-buy 3,999,708; set-sell 10,361,055; merge-arb 991,268; dual-buy 363,419); sum of the gas limits 92,847,810, largest limit 6,247,748 (2^24 = 16,777,216). In ETH: **0.000067259912215367 ETH** at `eth_gasPrice` 1000299 wei (execution 0.00006692006311794 + L1 data fee 0.000000339849097427 from `GasPriceOracle.getL1Fee`), at most 0.000134179975333307 ETH at the signer's ceiling (2 x gas price); about **0.1390 sUSDS** (2303.39 USD/ETH from QuoterV2 WETH/USDC fee 500, / 1.114472 USD per sUSDS from PSM3) |
| **Simulation** | 1 `eth_simulateV1` request(s) (helper `simulate`, one `blockStateCalls` entry per keep-whole group), no state overrides: `all_success` **true**, `failed_count` 0, `clamped_count` 0, `over_cap_count` 0, pending nonce 3480 |

## 2. ETH for gas

The holder holds **0.005369217552469683 ETH**; `eth_gasPrice` 1000299 wei (base fee 299 wei). The simulation runs with `validation: false` and does not see ETH, so it is walked here: the signer refuses a transaction unless the balance covers `gasLimit x maxFeePerGas` (execution only), and before each group G section 8 asks for ETH >= 0.002 ETH + the group's `gas_limit x 2 x eth_gasPrice`. The executor makes that check fresh before each group; this is a projection.

| price assumption | effective price | cost of all 377 transactions (execution + L1 data fee) | starting balance the walk needs | first transaction the signer would refuse | first group failing the affordability gate | lowest balance at a group start |
|---|---|---|---|---|---|---|
| effective price = eth_gasPrice (what the node suggests) | 1000299 wei | 0.000067259912215367 ETH | 0.000067702142666918 ETH | none | none | 0.005302136795780153 ETH (group 80) |
| effective price = the signer's ceiling maxFeePerGas = 2 x eth_gasPrice | 2000598 wei | 0.000134179975333307 ETH | 0.000134248434422062 ETH | none | none | 0.00523539395863694 ETH (group 80) |

Result: **no ETH shortfall** under either assumption.

## 3. Drift, the simulation, and what was checked

- **Pool drift since F sized the plan** (`run/2026-10-29T0859Z/planner/g-drift.json`): 0 of 138 pools moved, on 0 market(s). A moved pool is reported, never stale by itself; each call carries its own floor and the pre-send re-check decides. Fresh quotes vs F's `quoted_fill`: largest relative gap 7.05e-15 (drift, not a check).
- **Simulation**: one request: the whole ordered sequence. 81 entries and 377 calls in all, from the holder, in send order.
- **Gas limits** are the helper's `gas_limit` per call, copied, never computed by hand: `ceil(maxUsedGas x 1.2)` on every call; the largest is 6,247,748.
- **Calldata**: all 377 calldatas re-encoded by the helper's `encode` equal the ethers encoding (bytes and keccak256); the signer's policy-only `check` **allowed all 377** signer-input files (`run/2026-10-29T0859Z/g-tx/tx-NNN.json`, each `{"calls":[one call],"gasLimit":"<helper gas_limit>"}`).
- **End state**: the simulated end state equals the prediction on **239 of 239** probed balances.
- **Independent read**: not run (`--indep` not given; it is supervised-only, because the helper pins one RPC).
- **Trading boundary at build**: 69 of 69 children clear at block 158832899 (timestamp 1793264575); parent and 3 middles payoutDenominator 0/0/0/0. Re-read immediately before every group at send time.
- **Route of a market with a `set` row** (Commit-Boost/commit-boost-client): fresh spot sum 1.075628 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.
- **Route of a market with a `set` row** (succinctlabs/rsp): fresh spot sum 1.121059 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.
- **Route of a market with a `set` row** (OffchainLabs/stylus-sdk-rs): fresh spot sum 0.939884 -> simple-buy; sum after its own set-sell 0.999900 -> simple-buy: they agree.
- **Route of a market with a `set` row** (ethstaker/ethstaker-deposit-cli): fresh spot sum 1.083905 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.
- **Route of a market with a `set` row** (risc0/risc0-ethereum): fresh spot sum 1.070276 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.
- **Route of a market with a `set` row** (alloy-rs/alloy): fresh spot sum 1.080066 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.
- **Route of a market with a `set` row** (safe-global/safe-smart-account): fresh spot sum 1.138364 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.
- **Route of a market with a `set` row** (ethpandaops/ethereum-package): fresh spot sum 1.106312 -> complex-buy; sum after its own set-sell 1.000100 -> complex-buy: they agree.

## 4. Mints (4 groups at the head of the sequence, each `[approve, split]`)

- `mint-parent`: approve sUSDS -> Router (M) ; Router.splitPosition(sUSDS, parent, M) (gas used 51,089 + 568,698)
- `mint-middle-A`: approve bundle A -> Router (m_X) ; Router.splitPosition(sUSDS, middle A, m_X) (gas used 49,001 + 4,058,317)
- `mint-middle-B`: approve bundle B -> Router (m_X) ; Router.splitPosition(sUSDS, middle B, m_X) (gas used 49,001 + 4,165,165)
- `mint-middle-C`: approve bundle C -> Router (m_X) ; Router.splitPosition(sUSDS, middle C, m_X) (gas used 48,989 + 4,081,560)

## 5. Per-market print (units: the row's own repo token; sUSDS equivalent at the labelled 1/98 in brackets)

### 5a. Pairs: `dual-buy`, "pair (sum < 1 - f)", f = 0.0001 (1 markets)

- **grandinetech/grandine** pair (sum < 1 - f): q = 8.0299 repo tokens; spot sum 0.97585; locked-in sum = cost/q = 7.9323/8.0299 = 0.98785; cost 7.9323 [0.080942 sUSDS]
  - outcome: +(1 - sum)*q = 0.0976 repo tokens if the repo is evaluated and its child resolves to a score | nothing of value lost if the repo is not evaluated
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, loss sum*q = 7.9323 repo tokens | risk (b): n_X and k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +44.5088 tokens for 34.3666 repo tokens (UP leg total 52.5387 tokens at stake 40.3133)
  - legs: UP count 52.5387 (stake 40.3133, inMax 40.5149), DOWN count 8.0299 (stake 1.9856, inMax 1.9955); group `[approve, buy UP, approve, buy DOWN]`, 4 transactions

Pairs in total: cost 7.9323 repo tokens, locked gain 0.0976 repo tokens if every repo is evaluated and every child resolves to a score (heterogeneous tokens, informational).

### 5b. Set rows: set-sell and merge-arb (12 markets)

- **OffchainLabs/stylus-sdk-rs** merge-arb: 20.2944 pairs, cost ~ 19.6699, gain ~ 0.6245 repo tokens now, consumes 20.2944 child Invalid held from earlier runs (I_j 67.7678; recorded in their fills.json after it lands, oldest first). Leg bounds: UP amountInMaximum 14.235677792665354118, DOWN 5.532605803670623117 (quoted_in x min(q / cost, 1.005)); group [approve, buy q UP, buy q DOWN, approve UP, approve DOWN, approve child Invalid, merge q], 7 transactions.
- **Certora/CertoraProver** set-sell: 19.6242 sets, proceeds ~ 20.1780, gain ~ 0.5537 repo tokens, keeps 19.6242 child Invalid [0.205898 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 15.841688830222084307, DOWN leg >= 4.235392723331701274. Fresh spot sum 1.057922.
- **Commit-Boost/commit-boost-client** set-sell: 16.6756 sets, proceeds ~ 17.2822, gain ~ 0.6066 repo tokens, keeps 16.6756 child Invalid [0.176349 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 12.117137038475883094, DOWN leg >= 5.078637579536578886. Fresh spot sum 1.075628.
- **succinctlabs/rsp** set-sell: 30.9587 sets, proceeds ~ 32.7397, gain ~ 1.7810 repo tokens, keeps 30.9587 child Invalid [0.334079 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 22.047039044540699718, DOWN leg >= 10.529001192997008543. Fresh spot sum 1.121059.
- **ethstaker/ethstaker-deposit-cli** set-sell: 26.0734 sets, proceeds ~ 27.1354, gain ~ 1.0620 repo tokens, keeps 26.0734 child Invalid [0.276892 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 16.457896542369066824, DOWN leg >= 10.541826505527858662. Fresh spot sum 1.083905.
- **risc0/risc0-ethereum** set-sell: 28.0525 sets, proceeds ~ 29.0160, gain ~ 0.9635 repo tokens, keeps 28.0525 child Invalid [0.296082 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 21.236523964661562325, DOWN leg >= 7.634388271761121412. Fresh spot sum 1.070276.
- **alloy-rs/alloy** set-sell: 22.8256 sets, proceeds ~ 23.7035, gain ~ 0.8779 repo tokens, keeps 22.8256 child Invalid [0.241872 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 18.383593599937233953, DOWN leg >= 5.201346029188839584. Fresh spot sum 1.080066.
- **argotorg/sourcify** set-sell: 18.0865 sets, proceeds ~ 18.5291, gain ~ 0.4426 repo tokens, keeps 18.0865 child Invalid [0.189072 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 13.615831305028180122, DOWN leg >= 4.820583099884994775. Fresh spot sum 1.049918.
- **safe-global/safe-smart-account** set-sell: 57.2414 sets, proceeds ~ 61.0623, gain ~ 3.8208 repo tokens, keeps 57.2414 child Invalid [0.623084 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 41.444660235466127379, DOWN leg >= 19.312281526826879668. Fresh spot sum 1.138364.
- **sigp/lighthouse** set-sell: 18.7627 sets, proceeds ~ 19.3164, gain ~ 0.5537 repo tokens, keeps 18.7627 child Invalid [0.197106 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 16.08898030886696424, DOWN leg >= 3.13080173303792882. Fresh spot sum 1.061119.
- **status-im/nimbus-eth2** set-sell: 14.5308 sets, proceeds ~ 14.8888, gain ~ 0.3579 repo tokens, keeps 14.5308 child Invalid [0.151926 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 13.025879015094237833, DOWN leg >= 1.788456367082266106. Fresh spot sum 1.051281.
- **ethpandaops/ethereum-package** set-sell: 33.1640 sets, proceeds ~ 34.8593, gain ~ 1.6954 repo tokens, keeps 33.1640 child Invalid [0.355708 sUSDS-equivalent proceeds]. No-loss floors (sum >= q): UP leg >= 23.595389853951923827, DOWN leg >= 11.089652212032396197. Fresh spot sum 1.106312.

### 5c. Complex-buy (41 groups: split `x = stake`, sell the other leg, buy the own leg with the proceeds; keeps `x` child Invalid; the last two transactions are rebuilt at send time with the realised proceeds)

- **ethereum/py_ecc** complex-buy UP: split x = 21.0922 repo tokens [0.215226 sUSDS-eq], sell x DOWN for P = 3.4811 repo tokens, buy 4.2506 UP -> **25.3428 UP + 21.0922 child Invalid** (quoted total; F's simple-route count 25.3231; complex 0.078% vs the simple route); spot sum 1.00010 > 1; p_win 0.8500
- **Consensys/gnark-crypto** complex-buy UP: split x = 20.4454 repo tokens [0.208626 sUSDS-eq], sell x DOWN for P = 2.6598 repo tokens, buy 3.0635 UP -> **23.5089 UP + 20.4454 child Invalid** (quoted total; F's simple-route count 23.1582; complex 1.514% vs the simple route); spot sum 1.00693 > 1; p_win 0.9000
- **taikoxyz/taiko-mono** complex-buy UP: split x = 11.8927 repo tokens [0.121354 sUSDS-eq], sell x DOWN for P = 3.0757 repo tokens, buy 4.1926 UP -> **16.0853 UP + 11.8927 child Invalid** (quoted total; F's simple-route count 16.0595; complex 0.160% vs the simple route); spot sum 1.00010 > 1; p_win 0.7500
- **ethereum/js-ethereum-cryptography** complex-buy DOWN: split x = 11.8447 repo tokens [0.120865 sUSDS-eq], sell x UP for P = 6.6316 repo tokens, buy 14.2367 DOWN -> **26.0815 DOWN + 11.8447 child Invalid** (quoted total; F's simple-route count 24.1975; complex 7.786% vs the simple route); spot sum 1.00010 > 1; p_win 0.5500
- **ChainSafe/bls** complex-buy DOWN: split x = 19.7055 repo tokens [0.201076 sUSDS-eq], sell x UP for P = 11.4363 repo tokens, buy 25.7771 DOWN -> **45.4826 DOWN + 19.7055 child Invalid** (quoted total; F's simple-route count 42.8999; complex 6.020% vs the simple route); spot sum 1.01175 > 1; p_win 0.5000
- **wealdtech/ethdo** complex-buy UP: split x = 9.8172 repo tokens [0.100175 sUSDS-eq], sell x DOWN for P = 2.7667 repo tokens, buy 3.7563 UP -> **13.5735 UP + 9.8172 child Invalid** (quoted total; F's simple-route count 13.2282; complex 2.610% vs the simple route); spot sum 1.02526 > 1; p_win 0.7500
- **lambdaclass/lambdaworks** complex-buy UP: split x = 19.0890 repo tokens [0.194785 sUSDS-eq], sell x DOWN for P = 3.3663 repo tokens, buy 4.0966 UP -> **23.1856 UP + 19.0890 child Invalid** (quoted total; F's simple-route count 22.8781; complex 1.344% vs the simple route); spot sum 1.01017 > 1; p_win 0.8500
- **shazow/whatsabi** complex-buy UP: split x = 51.3597 repo tokens [0.524079 sUSDS-eq], sell x DOWN for P = 11.1102 repo tokens, buy 14.3054 UP -> **65.6651 UP + 51.3597 child Invalid** (quoted total; F's simple-route count 63.5671; complex 3.300% vs the simple route); spot sum 1.04302 > 1; p_win 0.8500
- **succinctlabs/op-succinct** complex-buy UP: split x = 21.3738 repo tokens [0.218100 sUSDS-eq], sell x DOWN for P = 8.4205 repo tokens, buy 14.6207 UP -> **35.9945 UP + 21.3738 child Invalid** (quoted total; F's simple-route count 36.5446; complex -1.505% vs the simple route); spot sum 1.00202 > 1; p_win 0.6000
- **lambdaclass/ethrex** complex-buy UP: split x = 20.0550 repo tokens [0.204643 sUSDS-eq], sell x DOWN for P = 4.9835 repo tokens, buy 6.4558 UP -> **26.5109 UP + 20.0550 child Invalid** (quoted total; F's simple-route count 25.5857; complex 3.616% vs the simple route); spot sum 1.03742 > 1; p_win 0.8000
- **Commit-Boost/commit-boost-client** complex-buy UP: split x = 50.8700 repo tokens [0.519082 sUSDS-eq], sell x DOWN for P = 11.1618 repo tokens, buy 15.2971 UP -> **66.1672 UP + 50.8700 child Invalid** (quoted total; F's simple-route count 66.9689, on the post-set-sell book; complex -1.197% vs the simple route); spot sum 1.07563 > 1; p_win 0.8000
- **Cyfrin/aderyn** complex-buy UP: split x = 30.5838 repo tokens [0.312080 sUSDS-eq], sell x DOWN for P = 9.7140 repo tokens, buy 14.6853 UP -> **45.2691 UP + 30.5838 child Invalid** (quoted total; F's simple-route count 45.1895; complex 0.176% vs the simple route); spot sum 1.01539 > 1; p_win 0.7000
- **holiman/goevmlab** complex-buy UP: split x = 46.6969 repo tokens [0.476499 sUSDS-eq], sell x DOWN for P = 11.1560 repo tokens, buy 15.1585 UP -> **61.8555 UP + 46.6969 child Invalid** (quoted total; F's simple-route count 61.2106; complex 1.053% vs the simple route); spot sum 1.02711 > 1; p_win 0.8000
- **edb-rs/edb** complex-buy UP: split x = 44.1618 repo tokens [0.450631 sUSDS-eq], sell x DOWN for P = 11.6321 repo tokens, buy 15.7868 UP -> **59.9486 UP + 44.1618 child Invalid** (quoted total; F's simple-route count 57.8876; complex 3.560% vs the simple route); spot sum 1.02497 > 1; p_win 0.8000
- **succinctlabs/rsp** complex-buy DOWN: split x = 11.9491 repo tokens [0.121930 sUSDS-eq], sell x UP for P = 8.2750 repo tokens, buy 24.8489 DOWN -> **36.7981 DOWN + 11.9491 child Invalid** (quoted total; F's simple-route count 34.4235, on the post-set-sell book; complex 6.898% vs the simple route); spot sum 1.12106 > 1; p_win 0.4000
- **ethstaker/ethstaker-deposit-cli** complex-buy DOWN: split x = 12.9560 repo tokens [0.132204 sUSDS-eq], sell x UP for P = 7.9746 repo tokens, buy 19.9614 DOWN -> **32.9174 DOWN + 12.9560 child Invalid** (quoted total; F's simple-route count 31.3961, on the post-set-sell book; complex 4.846% vs the simple route); spot sum 1.08391 > 1; p_win 0.4500
- **dl-solarity/solidity-lib** complex-buy UP: split x = 14.1338 repo tokens [0.144223 sUSDS-eq], sell x DOWN for P = 3.7872 repo tokens, buy 5.1845 UP -> **19.3183 UP + 14.1338 child Invalid** (quoted total; F's simple-route count 19.1343; complex 0.962% vs the simple route); spot sum 1.00757 > 1; p_win 0.7500
- **risc0/risc0-ethereum** complex-buy DOWN: split x = 9.6394 repo tokens [0.098361 sUSDS-eq], sell x UP for P = 7.1032 repo tokens, buy 26.0811 DOWN -> **35.7204 DOWN + 9.6394 child Invalid** (quoted total; F's simple-route count 34.7032, on the post-set-sell book; complex 2.931% vs the simple route); spot sum 1.07028 > 1; p_win 0.3000
- **powdr-labs/powdr** complex-buy UP: split x = 54.3616 repo tokens [0.554711 sUSDS-eq], sell x DOWN for P = 11.2880 repo tokens, buy 14.6760 UP -> **69.0376 UP + 54.3616 child Invalid** (quoted total; F's simple-route count 67.6326; complex 2.077% vs the simple route); spot sum 1.00247 > 1; p_win 0.8500
- **axiom-crypto/snark-verifier** complex-buy DOWN: split x = 3.2770 repo tokens [0.033439 sUSDS-eq], sell x UP for P = 2.2379 repo tokens, buy 6.6440 DOWN -> **9.9211 DOWN + 3.2770 child Invalid** (quoted total; F's simple-route count 9.6405; complex 2.911% vs the simple route); spot sum 1.01482 > 1; p_win 0.3500
- **swiss-knife-xyz/swiss-knife** complex-buy DOWN: split x = 4.8888 repo tokens [0.049886 sUSDS-eq], sell x UP for P = 3.7783 repo tokens, buy 13.8195 DOWN -> **18.7083 DOWN + 4.8888 child Invalid** (quoted total; F's simple-route count 17.5837; complex 6.395% vs the simple route); spot sum 1.03356 > 1; p_win 0.3000
- **a16z/helios** complex-buy UP: split x = 14.3750 repo tokens [0.146684 sUSDS-eq], sell x DOWN for P = 3.2644 repo tokens, buy 4.1921 UP -> **18.5671 UP + 14.3750 child Invalid** (quoted total; F's simple-route count 18.2445; complex 1.768% vs the simple route); spot sum 1.01146 > 1; p_win 0.8000
- **alloy-rs/alloy** complex-buy UP: split x = 34.1724 repo tokens [0.348698 sUSDS-eq], sell x DOWN for P = 6.0664 repo tokens, buy 7.5851 UP -> **41.7575 UP + 34.1724 child Invalid** (quoted total; F's simple-route count 41.5709, on the post-set-sell book; complex 0.449% vs the simple route); spot sum 1.08007 > 1; p_win 0.8500
- **apeworx/ape** complex-buy UP: split x = 16.8390 repo tokens [0.171826 sUSDS-eq], sell x DOWN for P = 4.6407 repo tokens, buy 6.3839 UP -> **23.2229 UP + 16.8390 child Invalid** (quoted total; F's simple-route count 22.8628; complex 1.575% vs the simple route); spot sum 1.01418 > 1; p_win 0.7500
- **consensys/teku** complex-buy UP: split x = 15.2277 repo tokens [0.155384 sUSDS-eq], sell x DOWN for P = 3.3575 repo tokens, buy 4.3121 UP -> **19.5398 UP + 15.2277 child Invalid** (quoted total; F's simple-route count 19.3267; complex 1.103% vs the simple route); spot sum 1.01292 > 1; p_win 0.8000
- **erigontech/erigon** complex-buy UP: split x = 16.2055 repo tokens [0.165363 sUSDS-eq], sell x DOWN for P = 4.3950 repo tokens, buy 6.0390 UP -> **22.2445 UP + 16.2055 child Invalid** (quoted total; F's simple-route count 21.9871; complex 1.171% vs the simple route); spot sum 1.01014 > 1; p_win 0.7500
- **eth-infinitism/account-abstraction** complex-buy UP: split x = 12.7800 repo tokens [0.130408 sUSDS-eq], sell x DOWN for P = 4.2208 repo tokens, buy 6.1849 UP -> **18.9649 UP + 12.7800 child Invalid** (quoted total; F's simple-route count 18.5373; complex 2.307% vs the simple route); spot sum 1.01887 > 1; p_win 0.7000
- **ethereum-lists/chains** complex-buy UP: split x = 21.3300 repo tokens [0.217653 sUSDS-eq], sell x DOWN for P = 5.9147 repo tokens, buy 8.2226 UP -> **29.5525 UP + 21.3300 child Invalid** (quoted total; F's simple-route count 29.1387; complex 1.420% vs the simple route); spot sum 1.00536 > 1; p_win 0.7500
- **ethereum/consensus-specs** complex-buy UP: split x = 13.4148 repo tokens [0.136885 sUSDS-eq], sell x DOWN for P = 1.5529 repo tokens, buy 1.7655 UP -> **15.1803 UP + 13.4148 child Invalid** (quoted total; F's simple-route count 15.0878; complex 0.613% vs the simple route); spot sum 1.01711 > 1; p_win 0.9000
- **ipsilon/evmone** complex-buy UP: split x = 44.2054 repo tokens [0.451075 sUSDS-eq], sell x DOWN for P = 9.7436 repo tokens, buy 12.4286 UP -> **56.6340 UP + 44.2054 child Invalid** (quoted total; F's simple-route count 54.4295; complex 4.050% vs the simple route); spot sum 1.02501 > 1; p_win 0.8500
- **ethereum/execution-apis** complex-buy UP: split x = 24.4619 repo tokens [0.249611 sUSDS-eq], sell x DOWN for P = 4.6094 repo tokens, buy 6.0161 UP -> **30.4780 UP + 24.4619 child Invalid** (quoted total; F's simple-route count 31.3160; complex -2.676% vs the simple route); spot sum 1.00511 > 1; p_win 0.8000
- **foundry-rs/foundry** complex-buy UP: split x = 12.9999 repo tokens [0.132652 sUSDS-eq], sell x DOWN for P = 2.1309 repo tokens, buy 2.5661 UP -> **15.5661 UP + 12.9999 child Invalid** (quoted total; F's simple-route count 15.4899; complex 0.491% vs the simple route); spot sum 1.00005 > 1; p_win 0.8500
- **nethereum/nethereum** complex-buy UP: split x = 11.6171 repo tokens [0.118542 sUSDS-eq], sell x DOWN for P = 2.1133 repo tokens, buy 2.5373 UP -> **14.1544 UP + 11.6171 child Invalid** (quoted total; F's simple-route count 13.8211; complex 2.411% vs the simple route); spot sum 1.02306 > 1; p_win 0.8500
- **nomicfoundation/hardhat** complex-buy UP: split x = 20.3552 repo tokens [0.207706 sUSDS-eq], sell x DOWN for P = 4.8513 repo tokens, buy 6.2859 UP -> **26.6411 UP + 20.3552 child Invalid** (quoted total; F's simple-route count 25.9687; complex 2.589% vs the simple route); spot sum 1.03140 > 1; p_win 0.8000
- **openzeppelin/openzeppelin-contracts** complex-buy UP: split x = 17.0570 repo tokens [0.174051 sUSDS-eq], sell x DOWN for P = 3.0546 repo tokens, buy 3.7039 UP -> **20.7609 UP + 17.0570 child Invalid** (quoted total; F's simple-route count 20.4031; complex 1.754% vs the simple route); spot sum 1.01413 > 1; p_win 0.8500
- **OffchainLabs/prysm** complex-buy UP: split x = 20.3021 repo tokens [0.207164 sUSDS-eq], sell x DOWN for P = 4.4644 repo tokens, buy 5.7868 UP -> **26.0889 UP + 20.3021 child Invalid** (quoted total; F's simple-route count 25.9009; complex 0.726% vs the simple route); spot sum 1.00899 > 1; p_win 0.8000
- **safe-global/safe-smart-account** complex-buy UP: split x = 83.0831 repo tokens [0.847786 sUSDS-eq], sell x DOWN for P = 22.9696 repo tokens, buy 32.3182 UP -> **115.4012 UP + 83.0831 child Invalid** (quoted total; F's simple-route count 108.5080, on the post-set-sell book; complex 6.353% vs the simple route); spot sum 1.13836 > 1; p_win 0.8500
- **argotorg/hevm** complex-buy UP: split x = 45.0584 repo tokens [0.459780 sUSDS-eq], sell x DOWN for P = 10.6769 repo tokens, buy 14.4963 UP -> **59.5548 UP + 45.0584 child Invalid** (quoted total; F's simple-route count 59.0336; complex 0.883% vs the simple route); spot sum 1.00470 > 1; p_win 0.8000
- **ethpandaops/ethereum-package** complex-buy DOWN: split x = 7.6756 repo tokens [0.078322 sUSDS-eq], sell x UP for P = 5.3126 repo tokens, buy 16.6447 DOWN -> **24.3203 DOWN + 7.6756 child Invalid** (quoted total; F's simple-route count 23.5415, on the post-set-sell book; complex 3.308% vs the simple route); spot sum 1.10631 > 1; p_win 0.3500
- **ethpandaops/checkpointz** complex-buy UP: split x = 49.1715 repo tokens [0.501750 sUSDS-eq], sell x DOWN for P = 20.7338 repo tokens, buy 35.9553 UP -> **85.1268 UP + 49.1715 child Invalid** (quoted total; F's simple-route count 81.6469; complex 4.262% vs the simple route); spot sum 1.00978 > 1; p_win 0.6500
- **lambdaclass/lambda_ethereum_consensus** complex-buy UP: split x = 16.2730 repo tokens [0.166051 sUSDS-eq], sell x DOWN for P = 3.5761 repo tokens, buy 4.6045 UP -> **20.8775 UP + 16.2730 child Invalid** (quoted total; F's simple-route count 20.6829; complex 0.941% vs the simple route); spot sum 1.00619 > 1; p_win 0.8000

### 5d. Simple-buy (23 groups: one approve and one `exactInputSingle`, min 99.5% of the quote)

- **herumi/mcl** simple-buy UP: stake 51.2637 repo tokens [0.523099 sUSDS-eq], quoted out 59.9144 UP (F count 59.9144), floor 59.6148; spot sum 0.99990 < 1; p_win 0.9000
- **DefiLlama/chainlist** simple-buy DOWN: stake 2.8128 repo tokens [0.028702 sUSDS-eq], quoted out 9.6059 DOWN (F count 9.6059), floor 9.5579; spot sum 0.99385 < 1; p_win 0.3000
- **skalenetwork/libBLS** simple-buy UP: stake 18.1362 repo tokens [0.185063 sUSDS-eq], quoted out 24.6585 UP (F count 24.6585), floor 24.5352; spot sum 0.99990 < 1; p_win 0.7500
- **TrueBlocks/trueblocks-core** simple-buy UP: stake 26.3885 repo tokens [0.269270 sUSDS-eq], quoted out 31.8419 UP (F count 31.8419), floor 31.6827; spot sum 0.99990 < 1; p_win 0.8500
- **EspressoSystems/jellyfish** simple-buy UP: stake 52.5984 repo tokens [0.536719 sUSDS-eq], quoted out 85.8958 UP (F count 85.8958), floor 85.4663; spot sum 0.97191 < 1; p_win 0.6500
- **a16z/halmos** simple-buy UP: stake 25.0817 repo tokens [0.255936 sUSDS-eq], quoted out 34.3284 UP (F count 34.3284), floor 34.1567; spot sum 0.99323 < 1; p_win 0.7500
- **succinctlabs/sp1** simple-buy UP: stake 22.2800 repo tokens [0.227347 sUSDS-eq], quoted out 30.4772 UP (F count 30.4772), floor 30.3248; spot sum 0.99060 < 1; p_win 0.7500
- **otterscan/otterscan** simple-buy DOWN: stake 7.7255 repo tokens [0.078832 sUSDS-eq], quoted out 27.9622 DOWN (F count 27.9622), floor 27.8224; spot sum 0.99990 < 1; p_win 0.3000
- **NethermindEth/juno** simple-buy UP: stake 25.4350 repo tokens [0.259541 sUSDS-eq], quoted out 34.8213 UP (F count 34.8213), floor 34.6472; spot sum 0.99930 < 1; p_win 0.7500
- **0xMiden/miden-vm** simple-buy UP: stake 51.2195 repo tokens [0.522648 sUSDS-eq], quoted out 63.3915 UP (F count 63.3915), floor 63.0745; spot sum 0.99990 < 1; p_win 0.8500
- **evmts/tevm-monorepo** simple-buy DOWN: stake 3.8757 repo tokens [0.039548 sUSDS-eq], quoted out 11.6576 DOWN (F count 11.6576), floor 11.5993; spot sum 0.99990 < 1; p_win 0.3500
- **OffchainLabs/stylus-sdk-rs** simple-buy UP: stake 57.2759 repo tokens [0.584448 sUSDS-eq], quoted out 76.0566 UP (F count 76.0566), floor 75.6763; spot sum 0.93988 (quoted on the post-set-sell state); p_win 0.8000
- **argotorg/fe** simple-buy UP: stake 44.9510 repo tokens [0.458683 sUSDS-eq], quoted out 55.2822 UP (F count 55.2822), floor 55.0058; spot sum 0.99990 < 1; p_win 0.8500
- **argotorg/solidity** simple-buy UP: stake 20.8130 repo tokens [0.212377 sUSDS-eq], quoted out 24.9884 UP (F count 24.9884), floor 24.8634; spot sum 0.99590 < 1; p_win 0.8500
- **hyperledger-web3j/web3j** simple-buy UP: stake 19.5606 repo tokens [0.199598 sUSDS-eq], quoted out 26.6377 UP (F count 26.6377), floor 26.5045; spot sum 0.99028 < 1; p_win 0.7500
- **hyperledger/besu** simple-buy UP: stake 25.9890 repo tokens [0.265194 sUSDS-eq], quoted out 33.3632 UP (F count 33.3632), floor 33.1964; spot sum 0.99701 < 1; p_win 0.8000
- **nethermindeth/nethermind** simple-buy UP: stake 13.6811 repo tokens [0.139603 sUSDS-eq], quoted out 18.5157 UP (F count 18.5157), floor 18.4231; spot sum 0.99990 < 1; p_win 0.7500
- **scaffold-eth/scaffold-eth-2** simple-buy DOWN: stake 7.2431 repo tokens [0.073909 sUSDS-eq], quoted out 21.5546 DOWN (F count 21.5546), floor 21.4468; spot sum 0.99990 < 1; p_win 0.3500
- **vyperlang/titanoboa** simple-buy UP: stake 27.1800 repo tokens [0.277347 sUSDS-eq], quoted out 37.3142 UP (F count 37.3142), floor 37.1277; spot sum 0.99990 < 1; p_win 0.7500
- **vyperlang/vyper** simple-buy UP: stake 14.0061 repo tokens [0.142919 sUSDS-eq], quoted out 17.7523 UP (F count 17.7523), floor 17.6635; spot sum 0.98037 < 1; p_win 0.8000
- **wevm/viem** simple-buy UP: stake 30.0039 repo tokens [0.306162 sUSDS-eq], quoted out 38.6540 UP (F count 38.6540), floor 38.4607; spot sum 0.99990 < 1; p_win 0.8000
- **ethdebug/format** simple-buy UP: stake 65.6917 repo tokens [0.670323 sUSDS-eq], quoted out 82.6470 UP (F count 82.6470), floor 82.2338; spot sum 0.99219 < 1; p_win 0.8500
- **erigontech/silkworm** simple-buy UP: stake 51.8535 repo tokens [0.529118 sUSDS-eq], quoted out 68.3916 UP (F count 68.3916), floor 68.0497; spot sum 0.99990 < 1; p_win 0.8000

### 5e. Skipped rows (0: never sent; the executor writes each `status: "skipped"` with its reason)

- none

## 6. Group order and gas (send order)

| # | group | tx | gas used |
|---|---|---|---|
| 0 | `mint-parent` | 0-1 | 619,787 |
| 1 | `mint-middle-A` | 2-3 | 4,107,318 |
| 2 | `mint-middle-B` | 4-5 | 4,214,166 |
| 3 | `mint-middle-C` | 6-7 | 4,130,549 |
| 4 | `complex-buy:ethereum/py_ecc:UP` | 8-13 | 1,001,210 |
| 5 | `simple-buy:herumi/mcl:UP` | 14-15 | 177,159 |
| 6 | `complex-buy:Consensys/gnark-crypto:UP` | 16-21 | 887,048 |
| 7 | `complex-buy:taikoxyz/taiko-mono:UP` | 22-27 | 877,684 |
| 8 | `complex-buy:ethereum/js-ethereum-cryptography:DOWN` | 28-33 | 917,122 |
| 9 | `simple-buy:DefiLlama/chainlist:DOWN` | 34-35 | 172,988 |
| 10 | `set-sell:Certora/CertoraProver` | 36-41 | 958,445 |
| 11 | `complex-buy:ChainSafe/bls:DOWN` | 42-47 | 955,107 |
| 12 | `complex-buy:wealdtech/ethdo:UP` | 48-53 | 864,566 |
| 13 | `complex-buy:lambdaclass/lambdaworks:UP` | 54-59 | 939,972 |
| 14 | `simple-buy:skalenetwork/libBLS:UP` | 60-61 | 155,902 |
| 15 | `complex-buy:shazow/whatsabi:UP` | 62-67 | 1,006,973 |
| 16 | `simple-buy:TrueBlocks/trueblocks-core:UP` | 68-69 | 162,586 |
| 17 | `simple-buy:EspressoSystems/jellyfish:UP` | 70-71 | 219,960 |
| 18 | `simple-buy:a16z/halmos:UP` | 72-73 | 180,382 |
| 19 | `complex-buy:succinctlabs/op-succinct:UP` | 74-79 | 894,900 |
| 20 | `simple-buy:succinctlabs/sp1:UP` | 80-81 | 163,258 |
| 21 | `simple-buy:otterscan/otterscan:DOWN` | 82-83 | 192,566 |
| 22 | `complex-buy:lambdaclass/ethrex:UP` | 84-89 | 906,722 |
| 23 | `simple-buy:NethermindEth/juno:UP` | 90-91 | 180,382 |
| 24 | `set-sell:Commit-Boost/commit-boost-client` | 92-97 | 918,987 |
| 25 | `complex-buy:Commit-Boost/commit-boost-client:UP` | 98-103 | 990,449 |
| 26 | `complex-buy:Cyfrin/aderyn:UP` | 104-109 | 976,009 |
| 27 | `simple-buy:0xMiden/miden-vm:UP` | 110-111 | 177,853 |
| 28 | `complex-buy:holiman/goevmlab:UP` | 112-117 | 981,840 |
| 29 | `complex-buy:edb-rs/edb:UP` | 118-123 | 917,177 |
| 30 | `simple-buy:evmts/tevm-monorepo:DOWN` | 124-125 | 177,897 |
| 31 | `set-sell:succinctlabs/rsp` | 126-131 | 988,378 |
| 32 | `complex-buy:succinctlabs/rsp:DOWN` | 132-137 | 947,986 |
| 33 | `merge-arb:OffchainLabs/stylus-sdk-rs` | 138-144 | 991,268 |
| 34 | `simple-buy:OffchainLabs/stylus-sdk-rs:UP` | 145-146 | 184,501 |
| 35 | `set-sell:ethstaker/ethstaker-deposit-cli` | 147-152 | 911,409 |
| 36 | `complex-buy:ethstaker/ethstaker-deposit-cli:DOWN` | 153-158 | 879,735 |
| 37 | `complex-buy:dl-solarity/solidity-lib:UP` | 159-164 | 877,980 |
| 38 | `set-sell:risc0/risc0-ethereum` | 165-170 | 898,819 |
| 39 | `complex-buy:risc0/risc0-ethereum:DOWN` | 171-176 | 875,324 |
| 40 | `complex-buy:powdr-labs/powdr:UP` | 177-182 | 962,901 |
| 41 | `complex-buy:axiom-crypto/snark-verifier:DOWN` | 183-188 | 910,107 |
| 42 | `complex-buy:swiss-knife-xyz/swiss-knife:DOWN` | 189-194 | 955,150 |
| 43 | `complex-buy:a16z/helios:UP` | 195-200 | 914,171 |
| 44 | `set-sell:alloy-rs/alloy` | 201-206 | 938,737 |
| 45 | `complex-buy:alloy-rs/alloy:UP` | 207-212 | 960,169 |
| 46 | `complex-buy:apeworx/ape:UP` | 213-218 | 913,256 |
| 47 | `complex-buy:consensys/teku:UP` | 219-224 | 915,816 |
| 48 | `complex-buy:erigontech/erigon:UP` | 225-230 | 932,006 |
| 49 | `complex-buy:eth-infinitism/account-abstraction:UP` | 231-236 | 864,908 |
| 50 | `complex-buy:ethereum-lists/chains:UP` | 237-242 | 908,935 |
| 51 | `complex-buy:ethereum/consensus-specs:UP` | 243-248 | 971,234 |
| 52 | `complex-buy:ipsilon/evmone:UP` | 249-254 | 937,318 |
| 53 | `complex-buy:ethereum/execution-apis:UP` | 255-260 | 1,002,408 |
| 54 | `simple-buy:argotorg/fe:UP` | 261-262 | 170,511 |
| 55 | `simple-buy:argotorg/solidity:UP` | 263-264 | 155,275 |
| 56 | `set-sell:argotorg/sourcify` | 265-270 | 895,559 |
| 57 | `complex-buy:foundry-rs/foundry:UP` | 271-276 | 912,608 |
| 58 | `dual-buy:grandinetech/grandine` | 277-280 | 363,419 |
| 59 | `simple-buy:hyperledger-web3j/web3j:UP` | 281-282 | 173,050 |
| 60 | `simple-buy:hyperledger/besu:UP` | 283-284 | 162,508 |
| 61 | `complex-buy:nethereum/nethereum:UP` | 285-290 | 887,848 |
| 62 | `simple-buy:nethermindeth/nethermind:UP` | 291-292 | 155,269 |
| 63 | `complex-buy:nomicfoundation/hardhat:UP` | 293-298 | 966,712 |
| 64 | `complex-buy:openzeppelin/openzeppelin-contracts:UP` | 299-304 | 880,283 |
| 65 | `complex-buy:OffchainLabs/prysm:UP` | 305-310 | 962,584 |
| 66 | `set-sell:safe-global/safe-smart-account` | 311-316 | 988,642 |
| 67 | `complex-buy:safe-global/safe-smart-account:UP` | 317-322 | 970,990 |
| 68 | `simple-buy:scaffold-eth/scaffold-eth-2:DOWN` | 323-324 | 169,908 |
| 69 | `set-sell:sigp/lighthouse` | 325-330 | 963,033 |
| 70 | `set-sell:status-im/nimbus-eth2` | 331-336 | 953,050 |
| 71 | `simple-buy:vyperlang/titanoboa:UP` | 337-338 | 162,632 |
| 72 | `simple-buy:vyperlang/vyper:UP` | 339-340 | 155,147 |
| 73 | `simple-buy:wevm/viem:UP` | 341-342 | 170,515 |
| 74 | `complex-buy:argotorg/hevm:UP` | 343-348 | 967,516 |
| 75 | `simple-buy:ethdebug/format:UP` | 349-350 | 202,286 |
| 76 | `set-sell:ethpandaops/ethereum-package` | 351-356 | 945,996 |
| 77 | `complex-buy:ethpandaops/ethereum-package:DOWN` | 357-362 | 883,996 |
| 78 | `complex-buy:ethpandaops/checkpointz:UP` | 363-368 | 934,521 |
| 79 | `complex-buy:lambdaclass/lambda_ethereum_consensus:UP` | 369-374 | 899,549 |
| 80 | `simple-buy:erigontech/silkworm:UP` | 375-376 | 177,173 |

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

- calldata audit: 81 groups, 377 transactions decoded and re-derived from allocation.json (78 rows: 78 in groups, 0 skipped), kinds {"mint":4,"complex-buy":41,"simple-buy":23,"set-sell":11,"merge-arb":1,"dual-buy":1}, every approval exact (none near 2^256), every swap recipient the holder, every tier the candidates.json tier, dual-buy inMax = min(stake x 1.005, remaining); failures 0
- fresh re-simulation of run/2026-10-29T0859Z/g-sim-main.json (sha256 c749b52ec5d0455a79542f16deef74c21394c180201ba162143330bbbd5eb470): {"entries":81,"count":377,"all_success":true,"failed_count":0,"over_cap_count":0,"clamped_count":0,"pending_nonce":3480,"overrides_active":"absent","no_max_used_gas_count":0}
- holder nonce latest/pending before 3480/3480, after 3480/3480 (the plan's 3480); per-call rows of the fresh simulation: 377 checked, every status 0x1 and every fresh peak within the plan's gas_limit; gasUsed equal to the build's on all
- AUDIT PASSED: every acceptance check holds
