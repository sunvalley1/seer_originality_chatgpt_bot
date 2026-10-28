# F plan: allocation.json of run 2026-10-28T1129Z-clearance

Holder `0x2AD670e5953a85C998cDf1C2f6D74386aB735d4a`. Pool state read at blocks 158794093..158794098 (both pools of a market in one multicall file, so each market has one pinned block; the head moves, so no two reads are compared by block). Nothing is sent by F.

objective max-ev; 98 independent per-market budgets, each `held_j + M` (held_j = the repo token held plus its bundle's unsplit tokens, which G middle-splits first; 97 market(s) hold some), so each market may spend up to held_j + M = held_j + 143.444913115499 of its own repo token.
Bankroll = the holder's whole sUSDS balance 666.632973623565. USDC and USDS are 0: no PSM3 ramp, so the bankroll is not provisional. M = min(bankroll, max_j (cap_j - held_j)+) = 143.444913115499 sUSDS: the books bind (largest unconstrained cap above held_j 143.4449 repo tokens at safe-global/safe-smart-account).

A `set` row's worst_case 0 holds only if its whole keep-whole group lands: the planner sends every group as an ordered sequence of single transactions, on any signer, so a group can be left half-done between transactions, and a half-done group carries the stray leg's risk until its recovery batch lands (G section 8 step 5).

totals.staked = M = 143.444913 sUSDS (G splits the parent by M and then each middle whose bundle holds a position by M); totals.expected_value = 2.212101 sUSDS at the labelled 1/N = 1/98 scenario (a repo token is worth 0 if its repo is not evaluated); correlated_worst_case = -143.444913 sUSDS (the whole outlay can go to zero together; no correlation control).

Gas floors use F step 7's 2.4e-7 ETH per swap leg = 0.04958 repo tokens (set group 7 legs 0.3470, pair 2 legs 0.0992), converted at 2107.79 sUSDS per ETH (QuoterV2 WETH/USDC and PSM3 usdPerSusds 1.114369231262476) and x98; F simulates nothing. For the record: eth_gasPrice 1000292 wei, l1BaseFee 100477332 wei, signer ETH 0.00548971301409488 (F does not gate on it; G's affordability check does).

Negative-ev rows: 27 of 155 rows have ev < 0 (sum -16.6840 repo tokens); all are legs of a step-3b pair on a CSV market, which keeps its p-based fields although the pair is bought whatever the CSV says (F step 3b and the schema conventions); 0 market(s) have a negative total ev. The step-3b pair is a CSV-independent arbitrage, so it can sit above the CSV's own value of one leg.

Budget headroom: 1 market(s) spend their whole budget held_j + M; on a dual-buy pair that binds the budget, G clamps the second leg's amountInMaximum to what the first leg leaves (G section 3), so F reserves no headroom.

Rows sized on a state a step-3a set-sell or merge-arb left (marked "post-set-sell" below; after a merge-arb, a pair leg or folded extra is quoted on the live pool at q + count less the quote at q, an exact-output swap's cost being path-additive) are computed from the 3a quote's sqrtPriceX96After and the pool's liquidity with the exact integer Uniswap v3 single-range model, because the chain helper's call and multicall carry no state override (F step 8); the same model reproduced every QuoterV2 answer of this plan to within 8.4e-18 relative. Each such row was then probed on simulated state with the helper's simulate "return" probe (the mint prefix it needs, the set group, then QuoterV2 flagged return): ethereum/py_ecc UP: fill gap 4.2e-16, confirmed; protofire/solhint UP: fill gap 2.3e-15, confirmed; l2beat/l2beat UP: probe not run (simulate did not succeed cleanly (all_success false, failed 1, overrides false)): the model's numbers are used; taikoxyz/taiko-mono UP: fill gap 1.4e-15, confirmed; flashbots/mev-boost DOWN: fill gap 2.5e-15, confirmed; ChainSafe/bls DOWN: fill gap 1.3e-16, confirmed; dappnode/DAppNode UP: fill gap 5.5e-15, confirmed; lambdaclass/lambdaworks UP: fill gap 2.2e-15, confirmed; shazow/whatsabi UP: fill gap 5.7e-16, confirmed; TrueBlocks/trueblocks-core UP: fill gap 1.8e-15, confirmed; TrueBlocks/trueblocks-core DOWN: fill gap 2.0e-15, confirmed; succinctlabs/sp1 UP: probe not run (simulate did not succeed cleanly (all_success false, failed 1, overrides false)): the model's numbers are used; otterscan/otterscan DOWN: fill gap 4.0e-16, confirmed; NethermindEth/juno UP: probe not run (simulate did not succeed cleanly (all_success false, failed 1, overrides false)): the model's numbers are used; 0xMiden/miden-vm UP: fill gap 1.4e-16, confirmed; holiman/goevmlab UP: fill gap 3.0e-16, confirmed; evmts/tevm-monorepo UP: probe not run (simulate did not succeed cleanly (all_success false, failed 1, overrides false)): the model's numbers are used; evmts/tevm-monorepo DOWN: probe not run (simulate did not succeed cleanly (all_success false, failed 1, overrides false)): the model's numbers are used; succinctlabs/rsp UP: fill gap 2.2e-15, confirmed; succinctlabs/rsp DOWN: fill gap 1.7e-15, confirmed; risc0/risc0-ethereum DOWN: fill gap 9.7e-16, confirmed; swiss-knife-xyz/swiss-knife DOWN: fill gap 1.6e-15, confirmed; alloy-rs/alloy UP: fill gap 5.6e-16, confirmed; ipsilon/evmone UP: fill gap 1.4e-16, confirmed; ethereum/execution-apis UP: fill gap 4.3e-16, confirmed; ethereum/execution-apis DOWN: fill gap 2.2e-15, confirmed; argotorg/fe UP: fill gap 5.5e-16, confirmed; remix-project-org/remix-project UP: fill gap 0.0e+0, confirmed; argotorg/solidity UP: fill gap 1.1e-15, confirmed; foundry-rs/foundry UP: fill gap 5.3e-16, confirmed; foundry-rs/foundry DOWN: fill gap 1.2e-15, confirmed; hyperledger/besu UP: probe not run (simulate did not succeed cleanly (all_success false, failed 1, overrides false)): the model's numbers are used; nomicfoundation/hardhat UP: fill gap 4.3e-16, confirmed; openzeppelin/openzeppelin-contracts UP: fill gap 5.6e-15, confirmed; status-im/nimbus-eth2 DOWN: fill gap 6.8e-16, confirmed; wevm/viem UP: fill gap 7.3e-16, confirmed; wevm/viem DOWN: fill gap 9.8e-16, confirmed; ethpandaops/ethereum-helm-charts UP: fill gap 7.5e-16, confirmed; ethpandaops/ethereum-helm-charts DOWN: fill gap 5.2e-15, confirmed.

Held child Invalid on a sub-1 market is step 3a's merge-arb (F step 3a): on ethereum/py_ecc (I_j 47.446968858049890279, merge-arb q 26.8586), protofire/solhint (I_j 24.9900350297934, merge-arb q 24.9900), l2beat/l2beat (I_j 14.0201850408541, merge-arb q 14.0202), taikoxyz/taiko-mono (I_j 46.47108034100714722, merge-arb q 27.6202), flashbots/mev-boost (I_j 54.68858476756018, merge-arb q 40.9259), libp2p/libp2p (I_j 35.3020659693004, merge-arb q 25.9441), supranational/blst (I_j 35.829534698259473272, merge-arb q 34.3231), ChainSafe/bls (I_j 225.56824887644955, merge-arb q 51.0705), dappnode/DAppNode (I_j 38.153697188197062531, merge-arb q 36.4125), lambdaclass/lambdaworks (I_j 40.069996559553831737, merge-arb q 15.8558), shazow/whatsabi (I_j 30.378143932228428053, merge-arb q 18.9916), TrueBlocks/trueblocks-core (I_j 15.2269889269892, merge-arb q 15.2270, then a 3b pair of the remainder q 23.0870), succinctlabs/sp1 (I_j 22.3113136418181, merge-arb q 22.3113), otterscan/otterscan (I_j 52.86340683033877, merge-arb q 18.6935), NethermindEth/juno (I_j 20.03201590785368, merge-arb q 20.0320), 0xMiden/miden-vm (I_j 30.486664885554790663, merge-arb q 23.9073), holiman/goevmlab (I_j 25.4864726552162, merge-arb q 22.2481), evmts/tevm-monorepo (I_j 8.82381033712145, merge-arb q 8.8238, then a 3b pair of the remainder q 20.1304), succinctlabs/rsp (I_j 28.906670723516072897, merge-arb q 28.9067, then a 3b pair of the remainder q 32.1594), risc0/risc0-ethereum (I_j 19.62876728035435, merge-arb q 19.6288), swiss-knife-xyz/swiss-knife (I_j 38.78969106933213, merge-arb q 26.6841), alloy-rs/alloy (I_j 36.183198943842688268, merge-arb q 15.9666), ethereum/eips (I_j 28.8601855413876, merge-arb q 20.4565), ipsilon/evmone (I_j 27.9608041416791, merge-arb q 16.5805), ethereum/execution-apis (I_j 16.5757298084798, merge-arb q 16.5757, then a 3b pair of the remainder q 19.5431), argotorg/fe (I_j 32.079325692128420548, merge-arb q 30.2904), remix-project-org/remix-project (I_j 23.95598646713855, merge-arb q 16.2250), argotorg/solidity (I_j 25.6872768849111, merge-arb q 17.7136), foundry-rs/foundry (I_j 29.5444528012592, merge-arb q 29.5445, then a 3b pair of the remainder q 23.3386), hyperledger/besu (I_j 31.38473633773553, merge-arb q 31.3847), nomicfoundation/hardhat (I_j 30.351648244710828173, merge-arb q 18.2851), openzeppelin/openzeppelin-contracts (I_j 41.328501438853, merge-arb q 17.7713), status-im/nimbus-eth2 (I_j 15.0666948226677, merge-arb q 15.0667), wevm/viem (I_j 13.6392934330327, merge-arb q 13.6393, then a 3b pair of the remainder q 18.3419), argotorg/act (I_j 29.46218042521521, merge-arb q 25.2138), ethpandaops/ethereum-helm-charts (I_j 34.5772135331898, merge-arb q 34.5772, then a 3b pair of the remainder q 35.2486) the pairs are bought and merged with the held child Invalid at once, returning q repo tokens now; that child Invalid was retained by earlier runs, and G records its consumption in their fills.json, oldest first.

Verification of the plan before it was written: 25 of 25 checks passed (planner/f-verify.json). No planned market's pools moved between F's read and its re-quote.

## Pairs: 31 markets, "pair (sum < 1 - f)", f = 0.0001

- **arkworks-rs/algebra** pair (sum < 1 - f): q = 12.3953 RT:arkworks-rs/algebra; spot sum 0.96626; locked-in sum = cost/q = 12.1835/12.3953 = 0.98291 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.2118 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 12.1835 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +20.6610 tokens for 17.2699 repo tokens (p = 0.85, stop at P = p(1-f) = 0.849915), ev 0.2920; UP leg total 33.0563 tokens at stake 27.3579 [limited_by marginal-ev-zero]
- **flashbots/mev-boost-relay** pair (sum < 1 - f): q = 23.7649 RT:flashbots/mev-boost-relay; spot sum 0.93264; locked-in sum = cost/q = 22.9398/23.7649 = 0.96528 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.8250 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 22.9398 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +13.5009 tokens for 10.6856 repo tokens (p = 0.8, stop at P = p(1-f) = 0.799920), ev 0.1151; UP leg total 37.2658 tokens at stake 28.9518 [limited_by marginal-ev-zero]
- **wighawag/hardhat-deploy** pair (sum < 1 - f): q = 15.2455 RT:wighawag/hardhat-deploy; spot sum 0.96490; locked-in sum = cost/q = 14.9758/15.2455 = 0.98231 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.2697 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 14.9758 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +16.0137 tokens for 11.8482 repo tokens (p = 0.75, stop at P = p(1-f) = 0.749925), ev 0.1621; UP leg total 31.2593 tokens at stake 22.8345 [limited_by marginal-ev-zero]
- **ethstaker/eth-docker** pair (sum < 1 - f): q = 16.2633 RT:ethstaker/eth-docker; spot sum 0.96572; locked-in sum = cost/q = 15.9828/16.2633 = 0.98276 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.2804 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 15.9828 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +50.3946 tokens for 18.8898 repo tokens (p = 0.4, stop at P = p(1-f) = 0.399960), ev 1.2681; DOWN leg total 66.6578 tokens at stake 24.4887 [limited_by marginal-ev-zero]
- **DefiLlama/DefiLlama-Adapters** pair (sum < 1 - f): q = 13.7117 RT:DefiLlama/DefiLlama-Adapters; spot sum 0.95407; locked-in sum = cost/q = 13.3905/13.7117 = 0.97658 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.3212 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 13.3905 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +12.9426 tokens for 3.6509 repo tokens (p = 0.30000000000000004, stop at P = p(1-f) = 0.299970), ev 0.2318; DOWN leg total 26.6542 tokens at stake 7.0715 [limited_by marginal-ev-zero]
- **Plonky3/Plonky3** pair (sum < 1 - f): q = 14.2270 RT:Plonky3/Plonky3; spot sum 0.96131; locked-in sum = cost/q = 13.9482/14.2270 = 0.98040 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.2789 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 13.9482 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +29.5519 tokens for 23.0854 repo tokens (p = 0.8, stop at P = p(1-f) = 0.799920), ev 0.5561; UP leg total 43.7789 tokens at stake 33.8165 [limited_by marginal-ev-zero]
- **smartcontracts/simple-optimism-node** pair (sum < 1 - f): q = 16.6589 RT:smartcontracts/simple-optimism-node; spot sum 0.96186; locked-in sum = cost/q = 16.3386/16.6589 = 0.98078 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.3202 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 16.3386 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +33.8588 tokens for 14.3893 repo tokens (p = 0.44999999999999996, stop at P = p(1-f) = 0.449955), ev 0.8472; DOWN leg total 50.5177 tokens at stake 20.8972 [limited_by marginal-ev-zero]
- **TrueBlocks/trueblocks-core** pair (sum < 1 - f): q = 23.0870 RT:TrueBlocks/trueblocks-core; spot sum 0.88721; locked-in sum = cost/q = 22.2043/23.0870 = 0.96177 [limited_by marginal-ev-zero]
  - after this market's merge-arb of 15.2270 pairs: the remainder of the pair bound, priced on the post-merge-arb state
  - outcome: +(1 - sum)*q = 0.8827 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 22.2043 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +31.8274 tokens for 26.3768 repo tokens (p = 0.85, stop at P = p(1-f) = 0.849915), ev 0.6765; UP leg total 54.9144 tokens at stake 44.6991 [limited_by marginal-ev-zero]
- **succinctlabs/op-succinct** pair (sum < 1 - f): q = 12.9639 RT:succinctlabs/op-succinct; spot sum 0.93921; locked-in sum = cost/q = 12.5604/12.9639 = 0.96887 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.4035 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 12.5604 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +82.4358 tokens for 46.7344 repo tokens (p = 0.6, stop at P = p(1-f) = 0.599940), ev 2.7271; UP leg total 95.3997 tokens at stake 53.6190 [limited_by marginal-ev-zero]
- **lambdaclass/ethrex** pair (sum < 1 - f): q = 12.5933 RT:lambdaclass/ethrex; spot sum 0.95948; locked-in sum = cost/q = 12.3340/12.5933 = 0.97941 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.2593 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 12.3340 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +57.7038 tokens for 44.1116 repo tokens (p = 0.8, stop at P = p(1-f) = 0.799920), ev 2.0515; UP leg total 70.2971 tokens at stake 53.2224 [limited_by marginal-ev-zero]
- **Commit-Boost/commit-boost-client** pair (sum < 1 - f): q = 9.9640 RT:Commit-Boost/commit-boost-client; spot sum 0.96400; locked-in sum = cost/q = 9.7819/9.9640 = 0.98172 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.1822 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 9.7819 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +50.2949 tokens for 38.6908 repo tokens (p = 0.8, stop at P = p(1-f) = 0.799920), ev 1.5452; UP leg total 60.2590 tokens at stake 46.0059 [limited_by marginal-ev-zero]
- **edb-rs/edb** pair (sum < 1 - f): q = 12.6418 RT:edb-rs/edb; spot sum 0.96523; locked-in sum = cost/q = 12.4198/12.6418 = 0.98244 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.2220 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 12.4198 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +79.9627 tokens for 59.9423 repo tokens (p = 0.8, stop at P = p(1-f) = 0.799920), ev 4.0279; UP leg total 92.6045 tokens at stake 68.7347 [limited_by marginal-ev-zero]
- **evmts/tevm-monorepo** pair (sum < 1 - f): q = 20.1304 RT:evmts/tevm-monorepo; spot sum 0.90514; locked-in sum = cost/q = 19.4196/20.1304 = 0.96469 [limited_by marginal-ev-zero]
  - after this market's merge-arb of 8.8238 pairs: the remainder of the pair bound, priced on the post-merge-arb state
  - outcome: +(1 - sum)*q = 0.7108 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 19.4196 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +11.6526 tokens for 3.8741 repo tokens (p = 0.35, stop at P = p(1-f) = 0.349965), ev 0.2043; DOWN leg total 31.7831 tokens at stake 9.7251 [limited_by marginal-ev-zero]
- **succinctlabs/rsp** pair (sum < 1 - f): q = 32.1594 RT:succinctlabs/rsp; spot sum 0.84692; locked-in sum = cost/q = 30.6882/32.1594 = 0.95425 [limited_by marginal-ev-zero]
  - after this market's merge-arb of 28.9067 pairs: the remainder of the pair bound, priced on the post-merge-arb state
  - outcome: +(1 - sum)*q = 1.4712 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 30.6882 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +50.7024 tokens for 16.5644 repo tokens (p = 0.4, stop at P = p(1-f) = 0.399960), ev 3.7166; DOWN leg total 82.8618 tokens at stake 24.2519 [limited_by marginal-ev-zero]
- **ethstaker/ethstaker-deposit-cli** pair (sum < 1 - f): q = 12.1883 RT:ethstaker/ethstaker-deposit-cli; spot sum 0.96674; locked-in sum = cost/q = 11.9839/12.1883 = 0.98323 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.2044 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 11.9839 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +45.0724 tokens for 17.9510 repo tokens (p = 0.44999999999999996, stop at P = p(1-f) = 0.449955), ev 2.3316; DOWN leg total 57.2607 tokens at stake 22.1177 [limited_by marginal-ev-zero]
- **powdr-labs/powdr** pair (sum < 1 - f): q = 10.8379 RT:powdr-labs/powdr; spot sum 0.97164; locked-in sum = cost/q = 10.6831/10.8379 = 0.98571 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.1548 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 10.6831 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +67.6326 tokens for 54.3616 repo tokens (p = 0.85, stop at P = p(1-f) = 0.849915), ev 3.1261; UP leg total 78.4705 tokens at stake 62.5280 [limited_by marginal-ev-zero]
- **consensys/teku** pair (sum < 1 - f): q = 11.2649 RT:consensys/teku; spot sum 0.96256; locked-in sum = cost/q = 11.0506/11.2649 = 0.98097 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.2143 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 11.0506 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +30.1885 tokens for 23.5855 repo tokens (p = 0.8, stop at P = p(1-f) = 0.799920), ev 0.5654; UP leg total 41.4535 tokens at stake 32.1060 [limited_by marginal-ev-zero]
- **ethereum-lists/chains** pair (sum < 1 - f): q = 12.5683 RT:ethereum-lists/chains; spot sum 0.96963; locked-in sum = cost/q = 12.3761/12.5683 = 0.98471 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.1921 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 12.3761 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +29.1387 tokens for 21.3300 repo tokens (p = 0.75, stop at P = p(1-f) = 0.749925), ev 0.5241; UP leg total 41.7070 tokens at stake 30.2176 [limited_by marginal-ev-zero]
- **ethereum/execution-apis** pair (sum < 1 - f): q = 19.5431 RT:ethereum/execution-apis; spot sum 0.84065; locked-in sum = cost/q = 18.4703/19.5431 = 0.94510 [limited_by marginal-ev-zero]
  - after this market's merge-arb of 16.5757 pairs: the remainder of the pair bound, priced on the post-merge-arb state
  - outcome: +(1 - sum)*q = 1.0728 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 18.4703 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +31.3160 tokens for 24.4619 repo tokens (p = 0.8, stop at P = p(1-f) = 0.799920), ev 0.5908; UP leg total 50.8591 tokens at stake 39.1514 [limited_by marginal-ev-zero]
- **ethers-io/ethers.js** pair (sum < 1 - f): q = 12.7543 RT:ethers-io/ethers.js; spot sum 0.96833; locked-in sum = cost/q = 12.5496/12.7543 = 0.98395 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.2047 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 12.5496 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +28.9459 tokens for 3.6780 repo tokens (p = 0.15000000000000002, stop at P = p(1-f) = 0.149985), ev 0.6638; DOWN leg total 41.7002 tokens at stake 4.9642 [limited_by marginal-ev-zero]
- **foundry-rs/foundry** pair (sum < 1 - f): q = 23.3386 RT:foundry-rs/foundry; spot sum 0.88873; locked-in sum = cost/q = 22.7114/23.3386 = 0.97312 [limited_by marginal-ev-zero]
  - after this market's merge-arb of 29.5445 pairs: the remainder of the pair bound, priced on the post-merge-arb state
  - outcome: +(1 - sum)*q = 0.6273 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 22.7114 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +0.0961 tokens for 0.0144 repo tokens (p = 0.15000000000000002, stop at P = p(1-f) = 0.149985), ev 0.0000; DOWN leg total 23.4347 tokens at stake 3.2614 [limited_by marginal-ev-zero]
- **nethermindeth/nethermind** pair (sum < 1 - f): q = 13.9297 RT:nethermindeth/nethermind; spot sum 0.96363; locked-in sum = cost/q = 13.6738/13.9297 = 0.98162 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.2560 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 13.6738 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +18.5157 tokens for 13.6811 repo tokens (p = 0.75, stop at P = p(1-f) = 0.749925), ev 0.2057; UP leg total 32.4454 tokens at stake 23.7095 [limited_by marginal-ev-zero]
- **OffchainLabs/prysm** pair (sum < 1 - f): q = 9.8956 RT:OffchainLabs/prysm; spot sum 0.96728; locked-in sum = cost/q = 9.7316/9.8956 = 0.98343 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.1640 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 9.7316 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +33.5598 tokens for 26.1491 repo tokens (p = 0.8, stop at P = p(1-f) = 0.799920), ev 0.6987; UP leg total 43.4553 tokens at stake 33.6018 [limited_by marginal-ev-zero]
- **scaffold-eth/scaffold-eth-2** pair (sum < 1 - f): q = 10.1430 RT:scaffold-eth/scaffold-eth-2; spot sum 0.97655; locked-in sum = cost/q = 10.0238/10.1430 = 0.98825 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.1192 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 10.0238 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +21.5546 tokens for 7.2431 repo tokens (p = 0.35, stop at P = p(1-f) = 0.349965), ev 0.3010; DOWN leg total 31.6976 tokens at stake 10.4552 [limited_by marginal-ev-zero]
- **sigp/lighthouse** pair (sum < 1 - f): q = 18.5564 RT:sigp/lighthouse; spot sum 0.95449; locked-in sum = cost/q = 18.1256/18.5564 = 0.97678 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.4308 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 18.1256 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +18.5010 tokens for 2.5311 repo tokens (p = 0.15000000000000002, stop at P = p(1-f) = 0.149985), ev 0.2441; DOWN leg total 37.0574 tokens at stake 4.6588 [limited_by marginal-ev-zero]
- **vyperlang/titanoboa** pair (sum < 1 - f): q = 8.1194 RT:vyperlang/titanoboa; spot sum 0.97487; locked-in sum = cost/q = 8.0167/8.1194 = 0.98735 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.1027 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 8.0167 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +37.3142 tokens for 27.1800 repo tokens (p = 0.75, stop at P = p(1-f) = 0.749925), ev 0.8057; UP leg total 45.4336 tokens at stake 32.8882 [limited_by marginal-ev-zero]
- **wevm/viem** pair (sum < 1 - f): q = 18.3419 RT:wevm/viem; spot sum 0.89898; locked-in sum = cost/q = 17.7567/18.3419 = 0.96810 [limited_by marginal-ev-zero]
  - after this market's merge-arb of 13.6393 pairs: the remainder of the pair bound, priced on the post-merge-arb state
  - outcome: +(1 - sum)*q = 0.5852 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 17.7567 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +38.6540 tokens for 30.0039 repo tokens (p = 0.8, stop at P = p(1-f) = 0.799920), ev 0.9193; UP leg total 56.9959 tokens at stake 43.6257 [limited_by marginal-ev-zero]
- **ethpandaops/ethereum-helm-charts** pair (sum < 1 - f): q = 35.2486 RT:ethpandaops/ethereum-helm-charts; spot sum 0.85403; locked-in sum = cost/q = 33.8339/35.2486 = 0.95986 [limited_by marginal-ev-zero]
  - after this market's merge-arb of 34.5772 pairs: the remainder of the pair bound, priced on the post-merge-arb state
  - outcome: +(1 - sum)*q = 1.4147 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 33.8339 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on DOWN: +4.5539 tokens for 1.8073 repo tokens (p = 0.4, stop at P = p(1-f) = 0.399960), ev 0.0143; DOWN leg total 39.8025 tokens at stake 14.8902 [limited_by marginal-ev-zero]
- **ethpandaops/checkpointz** pair (sum < 1 - f): q = 11.9541 RT:ethpandaops/checkpointz; spot sum 0.97337; locked-in sum = cost/q = 11.7943/11.9541 = 0.98664 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.1597 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 11.7943 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +77.0573 tokens for 46.5999 repo tokens (p = 0.65, stop at P = p(1-f) = 0.649935), ev 3.4874; UP leg total 89.0114 tokens at stake 53.2538 [limited_by marginal-ev-zero]
- **lambdaclass/lambda_ethereum_consensus** pair (sum < 1 - f): q = 14.0151 RT:lambdaclass/lambda_ethereum_consensus; spot sum 0.96219; locked-in sum = cost/q = 13.7467/14.0151 = 0.98085 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.2684 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 13.7467 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +20.6829 tokens for 16.2730 repo tokens (p = 0.8, stop at P = p(1-f) = 0.799920), ev 0.2733; UP leg total 34.6980 tokens at stake 26.9977 [limited_by marginal-ev-zero]
- **erigontech/silkworm** pair (sum < 1 - f): q = 15.2164 RT:erigontech/silkworm; spot sum 0.95031; locked-in sum = cost/q = 14.8305/15.2164 = 0.97464 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.3859 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 14.8305 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +68.3916 tokens for 51.8535 repo tokens (p = 0.8, stop at P = p(1-f) = 0.799920), ev 2.8598; UP leg total 83.6081 tokens at stake 62.6617 [limited_by marginal-ev-zero]

## Set rows: 36

- **ethereum/py_ecc** merge-arb: 26.8586 pairs, cost ≈ 25.4901, gain ≈ 1.3685 repo tokens now, consumes 26.8586 child Invalid held from earlier runs (I_j 47.4470; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **protofire/solhint** merge-arb: 24.9900 pairs, cost ≈ 23.8282, gain ≈ 1.1618 repo tokens now, consumes 24.9900 child Invalid held from earlier runs (I_j 24.9900; G records it in the source runs' fills.json, oldest first) [limited_by invalid-held; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **l2beat/l2beat** merge-arb: 14.0202 pairs, cost ≈ 13.4831, gain ≈ 0.5371 repo tokens now, consumes 14.0202 child Invalid held from earlier runs (I_j 14.0202; G records it in the source runs' fills.json, oldest first) [limited_by invalid-held; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **taikoxyz/taiko-mono** merge-arb: 27.6202 pairs, cost ≈ 26.4418, gain ≈ 1.1784 repo tokens now, consumes 27.6202 child Invalid held from earlier runs (I_j 46.4711; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **flashbots/mev-boost** merge-arb: 40.9259 pairs, cost ≈ 39.2434, gain ≈ 1.6825 repo tokens now, consumes 40.9259 child Invalid held from earlier runs (I_j 54.6886; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **libp2p/libp2p** merge-arb: 25.9441 pairs, cost ≈ 25.2285, gain ≈ 0.7156 repo tokens now, consumes 25.9441 child Invalid held from earlier runs (I_j 35.3021; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **supranational/blst** merge-arb: 34.3231 pairs, cost ≈ 33.1630, gain ≈ 1.1602 repo tokens now, consumes 34.3231 child Invalid held from earlier runs (I_j 35.8295; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **ChainSafe/bls** merge-arb: 51.0705 pairs, cost ≈ 48.2538, gain ≈ 2.8167 repo tokens now, consumes 51.0705 child Invalid held from earlier runs (I_j 225.5682; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **dappnode/DAppNode** merge-arb: 36.4125 pairs, cost ≈ 34.5692, gain ≈ 1.8433 repo tokens now, consumes 36.4125 child Invalid held from earlier runs (I_j 38.1537; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **lambdaclass/lambdaworks** merge-arb: 15.8558 pairs, cost ≈ 15.4658, gain ≈ 0.3900 repo tokens now, consumes 15.8558 child Invalid held from earlier runs (I_j 40.0700; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **shazow/whatsabi** merge-arb: 18.9916 pairs, cost ≈ 18.3200, gain ≈ 0.6717 repo tokens now, consumes 18.9916 child Invalid held from earlier runs (I_j 30.3781; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **TrueBlocks/trueblocks-core** merge-arb: 15.2270 pairs, cost ≈ 13.8040, gain ≈ 1.4230 repo tokens now, consumes 15.2270 child Invalid held from earlier runs (I_j 15.2270; G records it in the source runs' fills.json, oldest first) [limited_by invalid-held; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **succinctlabs/sp1** merge-arb: 22.3113 pairs, cost ≈ 21.5312, gain ≈ 0.7801 repo tokens now, consumes 22.3113 child Invalid held from earlier runs (I_j 22.3113; G records it in the source runs' fills.json, oldest first) [limited_by invalid-held; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **otterscan/otterscan** merge-arb: 18.6935 pairs, cost ≈ 18.2469, gain ≈ 0.4466 repo tokens now, consumes 18.6935 child Invalid held from earlier runs (I_j 52.8634; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **NethermindEth/juno** merge-arb: 20.0320 pairs, cost ≈ 18.9250, gain ≈ 1.1070 repo tokens now, consumes 20.0320 child Invalid held from earlier runs (I_j 20.0320; G records it in the source runs' fills.json, oldest first) [limited_by invalid-held; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **0xMiden/miden-vm** merge-arb: 23.9073 pairs, cost ≈ 23.0127, gain ≈ 0.8946 repo tokens now, consumes 23.9073 child Invalid held from earlier runs (I_j 30.4867; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **holiman/goevmlab** merge-arb: 22.2481 pairs, cost ≈ 21.2739, gain ≈ 0.9741 repo tokens now, consumes 22.2481 child Invalid held from earlier runs (I_j 25.4865; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **evmts/tevm-monorepo** merge-arb: 8.8238 pairs, cost ≈ 8.1021, gain ≈ 0.7217 repo tokens now, consumes 8.8238 child Invalid held from earlier runs (I_j 8.8238; G records it in the source runs' fills.json, oldest first) [limited_by invalid-held; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **succinctlabs/rsp** merge-arb: 28.9067 pairs, cost ≈ 25.3938, gain ≈ 3.5129 repo tokens now, consumes 28.9067 child Invalid held from earlier runs (I_j 28.9067; G records it in the source runs' fills.json, oldest first) [limited_by invalid-held; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **risc0/risc0-ethereum** merge-arb: 19.6288 pairs, cost ≈ 19.1250, gain ≈ 0.5037 repo tokens now, consumes 19.6288 child Invalid held from earlier runs (I_j 19.6288; G records it in the source runs' fills.json, oldest first) [limited_by invalid-held; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **swiss-knife-xyz/swiss-knife** merge-arb: 26.6841 pairs, cost ≈ 25.5949, gain ≈ 1.0893 repo tokens now, consumes 26.6841 child Invalid held from earlier runs (I_j 38.7897; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **alloy-rs/alloy** merge-arb: 15.9666 pairs, cost ≈ 15.5161, gain ≈ 0.4504 repo tokens now, consumes 15.9666 child Invalid held from earlier runs (I_j 36.1832; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **ethereum/eips** merge-arb: 20.4565 pairs, cost ≈ 19.9593, gain ≈ 0.4972 repo tokens now, consumes 20.4565 child Invalid held from earlier runs (I_j 28.8602; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **ipsilon/evmone** merge-arb: 16.5805 pairs, cost ≈ 16.2246, gain ≈ 0.3559 repo tokens now, consumes 16.5805 child Invalid held from earlier runs (I_j 27.9608; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **ethereum/execution-apis** merge-arb: 16.5757 pairs, cost ≈ 14.3894, gain ≈ 2.1863 repo tokens now, consumes 16.5757 child Invalid held from earlier runs (I_j 16.5757; G records it in the source runs' fills.json, oldest first) [limited_by invalid-held; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **argotorg/fe** merge-arb: 30.2904 pairs, cost ≈ 28.9235, gain ≈ 1.3669 repo tokens now, consumes 30.2904 child Invalid held from earlier runs (I_j 32.0793; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **remix-project-org/remix-project** merge-arb: 16.2250 pairs, cost ≈ 15.8582, gain ≈ 0.3669 repo tokens now, consumes 16.2250 child Invalid held from earlier runs (I_j 23.9560; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **argotorg/solidity** merge-arb: 17.7136 pairs, cost ≈ 17.3108, gain ≈ 0.4028 repo tokens now, consumes 17.7136 child Invalid held from earlier runs (I_j 25.6873; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **foundry-rs/foundry** merge-arb: 29.5445 pairs, cost ≈ 27.1040, gain ≈ 2.4404 repo tokens now, consumes 29.5445 child Invalid held from earlier runs (I_j 29.5445; G records it in the source runs' fills.json, oldest first) [limited_by invalid-held; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **hyperledger/besu** merge-arb: 31.3847 pairs, cost ≈ 29.9303, gain ≈ 1.4545 repo tokens now, consumes 31.3847 child Invalid held from earlier runs (I_j 31.3847; G records it in the source runs' fills.json, oldest first) [limited_by invalid-held; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **nomicfoundation/hardhat** merge-arb: 18.2851 pairs, cost ≈ 17.6834, gain ≈ 0.6018 repo tokens now, consumes 18.2851 child Invalid held from earlier runs (I_j 30.3516; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **openzeppelin/openzeppelin-contracts** merge-arb: 17.7713 pairs, cost ≈ 17.3512, gain ≈ 0.4202 repo tokens now, consumes 17.7713 child Invalid held from earlier runs (I_j 41.3285; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **status-im/nimbus-eth2** merge-arb: 15.0667 pairs, cost ≈ 14.6824, gain ≈ 0.3843 repo tokens now, consumes 15.0667 child Invalid held from earlier runs (I_j 15.0667; G records it in the source runs' fills.json, oldest first) [limited_by invalid-held; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **wevm/viem** merge-arb: 13.6393 pairs, cost ≈ 12.5239, gain ≈ 1.1154 repo tokens now, consumes 13.6393 child Invalid held from earlier runs (I_j 13.6393; G records it in the source runs' fills.json, oldest first) [limited_by invalid-held; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **argotorg/act** merge-arb: 25.2138 pairs, cost ≈ 24.3483, gain ≈ 0.8654 repo tokens now, consumes 25.2138 child Invalid held from earlier runs (I_j 29.4622; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **ethpandaops/ethereum-helm-charts** merge-arb: 34.5772 pairs, cost ≈ 30.6737, gain ≈ 3.9035 repo tokens now, consumes 34.5772 child Invalid held from earlier runs (I_j 34.5772; G records it in the source runs' fills.json, oldest first) [limited_by invalid-held; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]

## Directional (stand-alone, one side) rows: 57

The count is stake / quoted_fill, the simple route's; on a one-side market with sum > 1 G routes the row complex-buy, whose delivered count is its own (G section 3).

- **ethereum/py_ecc** UP: stake 62.0470 repo tokens -> 77.5817 tokens, quoted_fill 0.79976, p 0.85, ev 3.8974 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **blockscout/blockscout** UP: stake 39.0585 repo tokens -> 58.3497 tokens, quoted_fill 0.66939, p 0.7, ev 1.7863, limited_by marginal-ev-zero
- **LFDT-web3j/web3j** UP: stake 32.9636 repo tokens -> 42.6062 tokens, quoted_fill 0.77368, p 0.8, ev 1.1214, limited_by marginal-ev-zero
- **herumi/mcl** UP: stake 101.5777 repo tokens -> 125.0874 tokens, quoted_fill 0.81205, p 0.9, ev 11.0009, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **paulmillr/noble-curves** UP: stake 9.5379 repo tokens -> 11.3261 tokens, quoted_fill 0.84212, p 0.85, ev 0.0893, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **flashbots/rbuilder** UP: stake 39.0512 repo tokens -> 54.3725 tokens, quoted_fill 0.71822, p 0.75, ev 1.7282, limited_by marginal-ev-zero
- **protofire/solhint** UP: stake 39.0472 repo tokens -> 54.2923 tokens, quoted_fill 0.71920, p 0.75, ev 1.6721 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **l2beat/l2beat** UP: stake 26.1938 repo tokens -> 33.6276 tokens, quoted_fill 0.77894, p 0.8, ev 0.7083 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **Consensys/gnark-crypto** UP: stake 38.1415 repo tokens -> 43.9412 tokens, quoted_fill 0.86801, p 0.9, ev 1.4055, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **taikoxyz/taiko-mono** UP: stake 40.6342 repo tokens -> 56.6203 tokens, quoted_fill 0.71766, p 0.75, ev 1.8310 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **flashbots/mev-boost** DOWN: stake 1.2901 repo tokens -> 13.4984 tokens, quoted_fill 0.09557, p 0.09999999999999998, ev 0.0598 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **ethereum/js-ethereum-cryptography** DOWN: stake 12.7754 repo tokens -> 26.3547 tokens, quoted_fill 0.48475, p 0.55, ev 1.7196, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **DefiLlama/chainlist** UP: stake 10.1196 repo tokens -> 14.6262 tokens, quoted_fill 0.69188, p 0.7, ev 0.1187, limited_by marginal-ev-zero
- **Certora/CertoraProver** UP: stake 48.9295 repo tokens -> 64.3335 tokens, quoted_fill 0.76056, p 0.8, ev 2.5373, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ChainSafe/bls** DOWN: stake 42.9380 repo tokens -> 104.3720 tokens, quoted_fill 0.41139, p 0.5, ev 9.2480 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **intellij-solidity/intellij-solidity** UP: stake 17.8012 repo tokens -> 22.6666 tokens, quoted_fill 0.78535, p 0.8, ev 0.3321, limited_by marginal-ev-zero
- **dappnode/DAppNode** UP: stake 17.6120 repo tokens -> 25.6693 tokens, quoted_fill 0.68611, p 0.7, ev 0.3565 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **wealdtech/ethdo** UP: stake 22.5142 repo tokens -> 30.7583 tokens, quoted_fill 0.73197, p 0.75, ev 0.5546, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **lambdaclass/lambdaworks** UP: stake 41.1808 repo tokens -> 50.4486 tokens, quoted_fill 0.81629, p 0.85, ev 1.7005 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **skalenetwork/libBLS** UP: stake 40.6059 repo tokens -> 56.5919 tokens, quoted_fill 0.71752, p 0.75, ev 1.8380, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **shazow/whatsabi** UP: stake 79.4774 repo tokens -> 101.2522 tokens, quoted_fill 0.78495, p 0.85, ev 6.5870 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **EspressoSystems/jellyfish** UP: stake 52.5984 repo tokens -> 85.8958 tokens, quoted_fill 0.61235, p 0.65, ev 3.2338, limited_by marginal-ev-zero
- **a16z/halmos** UP: stake 25.0817 repo tokens -> 34.3284 tokens, quoted_fill 0.73064, p 0.75, ev 0.6645, limited_by marginal-ev-zero
- **succinctlabs/sp1** UP: stake 22.2800 repo tokens -> 30.4772 tokens, quoted_fill 0.73104, p 0.75, ev 0.5780 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **otterscan/otterscan** DOWN: stake 7.7255 repo tokens -> 27.9622 tokens, quoted_fill 0.27629, p 0.30000000000000004, ev 0.6631 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **NethermindEth/juno** UP: stake 25.4350 repo tokens -> 34.8213 tokens, quoted_fill 0.73044, p 0.75, ev 0.6810 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **Cyfrin/aderyn** UP: stake 28.5067 repo tokens -> 42.0225 tokens, quoted_fill 0.67837, p 0.7, ev 0.9091, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **0xMiden/miden-vm** UP: stake 51.2195 repo tokens -> 63.3915 tokens, quoted_fill 0.80799, p 0.85, ev 2.6632 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **holiman/goevmlab** UP: stake 64.8199 repo tokens -> 86.6013 tokens, quoted_fill 0.74849, p 0.8, ev 4.4611 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **OffchainLabs/stylus-sdk-rs** UP: stake 36.5295 repo tokens -> 47.4367 tokens, quoted_fill 0.77007, p 0.8, ev 1.4198, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **dl-solarity/solidity-lib** UP: stake 23.0085 repo tokens -> 31.4519 tokens, quoted_fill 0.73155, p 0.75, ev 0.5804, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **risc0/risc0-ethereum** DOWN: stake 6.5390 repo tokens -> 22.9507 tokens, quoted_fill 0.28492, p 0.30000000000000004, ev 0.3461 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **axiom-crypto/snark-verifier** DOWN: stake 6.6981 repo tokens -> 20.3338 tokens, quoted_fill 0.32941, p 0.35, ev 0.4187, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **swiss-knife-xyz/swiss-knife** DOWN: stake 4.8888 repo tokens -> 17.5837 tokens, quoted_fill 0.27803, p 0.30000000000000004, ev 0.3863 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **a16z/helios** UP: stake 28.1846 repo tokens -> 36.3067 tokens, quoted_fill 0.77629, p 0.8, ev 0.8607, limited_by marginal-ev-zero
- **alloy-rs/alloy** UP: stake 66.6894 repo tokens -> 83.8428 tokens, quoted_fill 0.79541, p 0.85, ev 4.5770 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **apeworx/ape** UP: stake 16.8390 repo tokens -> 22.8628 tokens, quoted_fill 0.73652, p 0.75, ev 0.3082, limited_by marginal-ev-zero
- **erigontech/erigon** UP: stake 14.2001 repo tokens -> 19.2243 tokens, quoted_fill 0.73865, p 0.75, ev 0.2182, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **eth-infinitism/account-abstraction** UP: stake 44.6001 repo tokens -> 67.2623 tokens, quoted_fill 0.66308, p 0.7, ev 2.4835, limited_by marginal-ev-zero
- **ethereum/consensus-specs** UP: stake 13.4148 repo tokens -> 15.0878 tokens, quoted_fill 0.88911, p 0.9, ev 0.1643, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ipsilon/evmone** UP: stake 59.6810 repo tokens -> 74.7031 tokens, quoted_fill 0.79891, p 0.85, ev 3.8166 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **argotorg/fe** UP: stake 44.9510 repo tokens -> 55.2822 tokens, quoted_fill 0.81312, p 0.85, ev 2.0389 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **remix-project-org/remix-project** UP: stake 8.2008 repo tokens -> 10.3365 tokens, quoted_fill 0.79339, p 0.8, ev 0.0684 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **argotorg/solidity** UP: stake 11.4974 repo tokens -> 13.6783 tokens, quoted_fill 0.84056, p 0.85, ev 0.1292 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **argotorg/sourcify** UP: stake 29.2914 repo tokens -> 40.3344 tokens, quoted_fill 0.72621, p 0.75, ev 0.9594, limited_by marginal-ev-zero
- **grandinetech/grandine** UP: stake 40.3133 repo tokens -> 52.5387 tokens, quoted_fill 0.76731, p 0.8, ev 1.7176, limited_by marginal-ev-zero
- **hyperledger-web3j/web3j** UP: stake 19.5606 repo tokens -> 26.6377 tokens, quoted_fill 0.73432, p 0.75, ev 0.4176, limited_by marginal-ev-zero
- **hyperledger/besu** UP: stake 25.9890 repo tokens -> 33.3632 tokens, quoted_fill 0.77897, p 0.8, ev 0.7016 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **nethereum/nethereum** UP: stake 11.6171 repo tokens -> 13.8211 tokens, quoted_fill 0.84053, p 0.85, ev 0.1309, limited_by marginal-ev-zero
- **nomicfoundation/hardhat** UP: stake 40.8125 repo tokens -> 53.1694 tokens, quoted_fill 0.76759, p 0.8, ev 1.7231 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **openzeppelin/openzeppelin-contracts** UP: stake 17.5169 repo tokens -> 20.9627 tokens, quoted_fill 0.83562, p 0.85, ev 0.3014 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **safe-global/safe-smart-account** UP: stake 143.4449 repo tokens -> 203.6325 tokens, quoted_fill 0.70443, p 0.85, ev 29.6427, limited_by marginal-ev-zero
- **status-im/nimbus-eth2** DOWN: stake 2.4809 repo tokens -> 30.4169 tokens, quoted_fill 0.08156, p 0.09999999999999998, ev 0.5607 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **vyperlang/vyper** UP: stake 14.0061 repo tokens -> 17.7523 tokens, quoted_fill 0.78897, p 0.8, ev 0.1958, limited_by marginal-ev-zero
- **argotorg/hevm** UP: stake 44.3079 repo tokens -> 58.0038 tokens, quoted_fill 0.76388, p 0.8, ev 2.0951, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ethdebug/format** UP: stake 65.6917 repo tokens -> 82.6470 tokens, quoted_fill 0.79485, p 0.85, ev 4.5583, limited_by marginal-ev-zero
- **ethpandaops/ethereum-package** DOWN: stake 9.0791 repo tokens -> 28.2254 tokens, quoted_fill 0.32166, p 0.35, ev 0.7998, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)

## Dropped by step 7 (85)

- blockscout/blockscout: pair limited_by gas gain 0.0055 q 1.8188 (iteration 1)
- LFDT-web3j/web3j: merge-arb limited_by gas ev 0.1295 q 4.9763 (iteration 1)
- LFDT-web3j/web3j: pair limited_by gas gain 0.0516 q 5.6041 (iteration 1)
- herumi/mcl: set-sell limited_by gas ev 0.0601 q 6.1512 (iteration 1)
- paulmillr/noble-curves: set-sell limited_by gas ev 0.2734 q 13.9850 (iteration 1)
- arkworks-rs/algebra: merge-arb limited_by gas ev 0.2118 q 12.3953 (iteration 1)
- flashbots/rbuilder: pair limited_by gas gain 0.0660 q 6.7981 (iteration 1)
- protofire/solhint: pair limited_by gas gain 0.0064 q 1.9164 (iteration 1)
- l2beat/l2beat: pair limited_by gas gain 0.0560 q 6.0583 (iteration 1)
- Consensys/gnark-crypto: set-sell limited_by gas ev 0.0000 q 0.1213 (iteration 1)
- Vectorized/solady: set-sell limited_by gas ev 0.0414 q 4.3548 (iteration 1)
- flashbots/mev-boost-relay: merge-arb limited_by volume-min ev 0.0000 q 0.0000 (iteration 1)
- ethereum/js-ethereum-cryptography: set-sell limited_by gas ev 0.0179 q 2.8030 (iteration 1)
- libp2p/libp2p: directional UP limited_by gas ev 0.0208 stake 4.5425 (iteration 1)
- supranational/blst: directional DOWN limited_by gas ev 0.0454 stake 1.2360 (iteration 1)
- wighawag/hardhat-deploy: merge-arb limited_by gas ev 0.2697 q 15.2455 (iteration 1)
- ethstaker/eth-docker: merge-arb limited_by gas ev 0.2804 q 16.2633 (iteration 1)
- DefiLlama/DefiLlama-Adapters: merge-arb limited_by gas ev 0.3212 q 13.7117 (iteration 1)
- DefiLlama/chainlist: merge-arb limited_by gas ev 0.0038 q 1.6619 (iteration 1)
- Certora/CertoraProver: set-sell limited_by gas ev 0.0656 q 6.0400 (iteration 1)
- Plonky3/Plonky3: merge-arb limited_by gas ev 0.2789 q 14.2270 (iteration 1)
- intellij-solidity/intellij-solidity: merge-arb limited_by gas ev 0.0236 q 4.2701 (iteration 1)
- wealdtech/ethdo: set-sell limited_by gas ev 0.0024 q 1.2560 (iteration 1)
- smartcontracts/simple-optimism-node: merge-arb limited_by gas ev 0.3202 q 16.6589 (iteration 1)
- skalenetwork/libBLS: set-sell limited_by gas ev 0.1051 q 7.8968 (iteration 1)
- EspressoSystems/jellyfish: merge-arb limited_by gas ev 0.0659 q 4.6478 (iteration 1)
- a16z/halmos: merge-arb limited_by gas ev 0.0057 q 1.6917 (iteration 1)
- succinctlabs/op-succinct: merge-arb limited_by gas ev 0.1924 q 3.6529 (iteration 1)
- succinctlabs/sp1: pair limited_by gas gain 0.0181 q 3.8796 (iteration 1)
- lambdaclass/ethrex: merge-arb limited_by gas ev 0.2593 q 12.5933 (iteration 1)
- NethermindEth/juno: pair limited_by gas gain 0.0464 q 4.7905 (iteration 1)
- Commit-Boost/commit-boost-client: merge-arb limited_by gas ev 0.1822 q 9.9640 (iteration 1)
- Cyfrin/aderyn: set-sell limited_by gas ev 0.0979 q 6.8891 (iteration 1)
- edb-rs/edb: merge-arb limited_by gas ev 0.2220 q 12.6418 (iteration 1)
- aestus-relay/mev-boost-relay: merge-arb limited_by gas ev 0.0260 q 2.7542 (iteration 1)
- OffchainLabs/stylus-sdk-rs: set-sell limited_by gas ev 0.0030 q 1.4364 (iteration 1)
- ethstaker/ethstaker-deposit-cli: merge-arb limited_by gas ev 0.2044 q 12.1883 (iteration 1)
- dl-solarity/solidity-lib: set-sell limited_by gas ev 0.1363 q 9.3380 (iteration 1)
- risc0/risc0-ethereum: pair limited_by gas gain 0.0017 q 1.1782 (iteration 1)
- powdr-labs/powdr: merge-arb limited_by gas ev 0.1548 q 10.8379 (iteration 1)
- a16z/helios: merge-arb limited_by gas ev 0.0252 q 4.5039 (iteration 1)
- chainsafe/lodestar: directional UP limited_by gas ev 0.0380 stake 6.1619 (iteration 1)
- eth-infinitism/account-abstraction: merge-arb limited_by gas ev 0.0095 q 2.6329 (iteration 1)
- ethereum/consensus-specs: set-sell limited_by gas ev 0.0271 q 3.2415 (iteration 1)
- ethereum/eips: directional DOWN limited_by gas ev 0.0341 stake 0.7563 (iteration 1)
- ethereum/go-ethereum: pair limited_by gas gain 0.0006 q 0.5955 (iteration 1)
- argotorg/sourcify: merge-arb limited_by gas ev 0.0394 q 5.2974 (iteration 1)
- ethereum/web3.py: directional DOWN limited_by gas ev 0.0423 stake 2.0449 (iteration 1)
- ethers-io/ethers.js: merge-arb limited_by gas ev 0.0378 q 1.2561 (iteration 1)
- grandinetech/grandine: merge-arb limited_by gas ev 0.3163 q 9.3714 (iteration 1)
- grandinetech/grandine: pair limited_by gas gain 0.0740 q 7.0843 (iteration 1)
- hyperledger-web3j/web3j: merge-arb limited_by gas ev 0.0161 q 3.3454 (iteration 1)
- hyperledger/besu: pair limited_by gas gain 0.0014 q 0.9638 (iteration 1)
- nethereum/nethereum: merge-arb limited_by gas ev 0.0544 q 6.3382 (iteration 1)
- paradigmxyz/reth: merge-arb limited_by gas ev 0.0564 q 6.0528 (iteration 1)
- safe-global/safe-smart-account: merge-arb limited_by gas ev 0.0037 q 1.7533 (iteration 1)
- scaffold-eth/scaffold-eth-2: merge-arb limited_by gas ev 0.1192 q 10.1430 (iteration 1)
- status-im/nimbus-eth2: pair limited_by gas gain 0.0154 q 3.5950 (iteration 1)
- vyperlang/titanoboa: merge-arb limited_by gas ev 0.1027 q 8.1194 (iteration 1)
- vyperlang/vyper: merge-arb limited_by gas ev 0.0554 q 5.6121 (iteration 1)
- argotorg/hevm: set-sell limited_by gas ev 0.1258 q 8.7500 (iteration 1)
- ethdebug/format: merge-arb limited_by gas ev 0.0101 q 2.6005 (iteration 1)
- argotorg/act: directional UP limited_by gas ev 0.0079 stake 2.8100 (iteration 1)
- ethpandaops/checkpointz: merge-arb limited_by gas ev 0.1597 q 11.9541 (iteration 1)
- lambdaclass/lambda_ethereum_consensus: merge-arb limited_by gas ev 0.2684 q 14.0151 (iteration 1)
- erigontech/silkworm: merge-arb limited_by gas ev 0.2226 q 5.3953 (iteration 1)
- DefiLlama/chainlist: pair limited_by gas gain 0.0038 q 1.6619 (iteration 2)
- intellij-solidity/intellij-solidity: pair limited_by gas gain 0.0236 q 4.2701 (iteration 2)
- EspressoSystems/jellyfish: pair limited_by gas gain 0.0659 q 4.6478 (iteration 2)
- a16z/halmos: pair limited_by gas gain 0.0057 q 1.6917 (iteration 2)
- aestus-relay/mev-boost-relay: pair limited_by gas gain 0.0260 q 2.7542 (iteration 2)
- a16z/helios: pair limited_by gas gain 0.0252 q 4.5039 (iteration 2)
- eth-infinitism/account-abstraction: pair limited_by gas gain 0.0095 q 2.6329 (iteration 2)
- ethereum/go-ethereum: directional DOWN limited_by gas ev 0.0050 stake 0.4440 (iteration 2)
- argotorg/sourcify: pair limited_by gas gain 0.0394 q 5.2974 (iteration 2)
- hyperledger-web3j/web3j: pair limited_by gas gain 0.0161 q 3.3454 (iteration 2)
- nethereum/nethereum: pair limited_by gas gain 0.0544 q 6.3382 (iteration 2)
- paradigmxyz/reth: pair limited_by gas gain 0.0564 q 6.0528 (iteration 2)
- safe-global/safe-smart-account: pair limited_by gas gain 0.0037 q 1.7533 (iteration 2)
- vyperlang/vyper: pair limited_by gas gain 0.0554 q 5.6121 (iteration 2)
- ethdebug/format: pair limited_by gas gain 0.0101 q 2.6005 (iteration 2)
- aestus-relay/mev-boost-relay: directional DOWN limited_by gas ev 0.0157 stake 0.6840 (iteration 3)
- paradigmxyz/reth: directional UP limited_by gas ev 0.0372 stake 6.1077 (iteration 3)
- aestus-relay/mev-boost-relay: directional UP limited_by gas ev 0.0139 stake 3.6513 (iteration 4)
- paradigmxyz/reth: directional DOWN limited_by gas ev 0.0220 stake 0.9665 (iteration 4)

## Class vs the candidates.json snapshot (pools[].price): 0 market(s) whose class differs

- live classes: {"sub1":79,"set-sell":13,"band":6}

## No row (skipped): 6 markets

- Vectorized/solady: spot sum 1.019323; p = [0.25, 0.75, 0]; neither side clears p(1-f) > price; set-sell dropped by step 7 (limited_by gas): ev 0.0414 repo tokens vs gas 0.3470
- aestus-relay/mev-boost-relay: spot sum 0.981264; p = [0.30000000000000004, 0.7, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; merge-arb dropped by step 7 (limited_by gas): ev 0.0260 repo tokens vs gas 0.3470; pair dropped by step 7 (limited_by gas): gain 0.0260 repo tokens vs gas 0.0992; directional DOWN dropped by step 7 (limited_by gas): ev 0.0157 repo tokens vs gas 0.0496; directional UP dropped by step 7 (limited_by gas): ev 0.0139 repo tokens vs gas 0.0496
- chainsafe/lodestar: spot sum 0.999959; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; sum within [1-f, 1/(1-f)] so neither 3a nor 3b applies; directional UP dropped by step 7 (limited_by gas): ev 0.0380 repo tokens vs gas 0.0496
- ethereum/go-ethereum: spot sum 0.997994; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; pair dropped by step 7 (limited_by gas): gain 0.0006 repo tokens vs gas 0.0992; directional DOWN dropped by step 7 (limited_by gas): ev 0.0050 repo tokens vs gas 0.0496
- ethereum/web3.py: spot sum 0.999993; p = [0.30000000000000004, 0.7, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; sum within [1-f, 1/(1-f)] so neither 3a nor 3b applies; directional DOWN dropped by step 7 (limited_by gas): ev 0.0423 repo tokens vs gas 0.0496
- paradigmxyz/reth: spot sum 0.981438; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; merge-arb dropped by step 7 (limited_by gas): ev 0.0564 repo tokens vs gas 0.3470; pair dropped by step 7 (limited_by gas): gain 0.0564 repo tokens vs gas 0.0992; directional UP dropped by step 7 (limited_by gas): ev 0.0372 repo tokens vs gas 0.0496; directional DOWN dropped by step 7 (limited_by gas): ev 0.0220 repo tokens vs gas 0.0496

**Totals:** 155 rows over 92 markets; sum ev = 216.7859 repo tokens (different tokens per market) => expected_value 2.212101 sUSDS at 1/98.
