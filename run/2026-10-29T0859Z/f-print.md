# F plan: allocation.json of run 2026-10-29T0859Z

Holder `0x2AD670e5953a85C998cDf1C2f6D74386aB735d4a`. Pool state read at blocks 158832820..158832822 (both pools of a market in one multicall file, so each market has one pinned block; the head moves, so no two reads are compared by block). Nothing is sent by F.

objective max-ev; 98 independent per-market budgets, each `held_j + M` (held_j = the repo token held plus its bundle's unsplit tokens, which G middle-splits first; 97 market(s) hold some), so each market may spend up to held_j + M = held_j + 140.324473992044 of its own repo token.
Bankroll = the holder's whole sUSDS balance 577.136995285407. USDC and USDS are 0: no PSM3 ramp, so the bankroll is not provisional. M = min(bankroll, max_j (cap_j - held_j)+) = 140.324473992044 sUSDS: the books bind (largest unconstrained cap above held_j 140.3245 repo tokens at safe-global/safe-smart-account).

A `set` row's worst_case 0 holds only if its whole keep-whole group lands: the planner sends every group as an ordered sequence of single transactions, on any signer, so a group can be left half-done between transactions, and a half-done group carries the stray leg's risk until its recovery batch lands (G section 8 step 5).

totals.staked = M = 140.324474 sUSDS (G splits the parent by M and then each middle whose bundle holds a position by M); totals.expected_value = 0.932686 sUSDS at the labelled 1/N = 1/98 scenario (a repo token is worth 0 if its repo is not evaluated); correlated_worst_case = -140.324474 sUSDS (the whole outlay can go to zero together; no correlation control).

Gas floors use F step 7's 2.4e-7 ETH per swap leg = 0.04863 repo tokens (set group 7 legs 0.3404, pair 2 legs 0.0973), converted at 2067.56 sUSDS per ETH (QuoterV2 WETH/USDC and PSM3 usdPerSusds 1.114471304608511) and x98; F simulates nothing. For the record: eth_gasPrice 1000291 wei, l1BaseFee 51555763 wei, signer ETH 0.005369217552469683 (F does not gate on it; G's affordability check does).

Negative-ev rows: 1 of 78 rows have ev < 0 (sum -0.3796 repo tokens); all are legs of a step-3b pair on a CSV market, which keeps its p-based fields although the pair is bought whatever the CSV says (F step 3b and the schema conventions); 0 market(s) have a negative total ev. The step-3b pair is a CSV-independent arbitrage, so it can sit above the CSV's own value of one leg.

Budget headroom: 1 market(s) spend their whole budget held_j + M; on a dual-buy pair that binds the budget, G clamps the second leg's amountInMaximum to what the first leg leaves (G section 3), so F reserves no headroom.

Rows sized on a state a step-3a set-sell or merge-arb left (marked "post-set-sell" below; after a merge-arb, a pair leg or folded extra is quoted on the live pool at q + count less the quote at q, an exact-output swap's cost being path-additive) are computed from the 3a quote's sqrtPriceX96After and the pool's liquidity with the exact integer Uniswap v3 single-range model, because the chain helper's call and multicall carry no state override (F step 8); the same model reproduced every QuoterV2 answer of this plan to within 2.5e-10 relative. Each such row was then probed on simulated state with the helper's simulate "return" probe (the mint prefix it needs, the set group, then QuoterV2 flagged return): Commit-Boost/commit-boost-client UP: fill gap 1.9e-15, confirmed; succinctlabs/rsp DOWN: fill gap 2.4e-15, confirmed; ethstaker/ethstaker-deposit-cli DOWN: fill gap 5.0e-15, confirmed; risc0/risc0-ethereum DOWN: fill gap 1.0e-15, confirmed; alloy-rs/alloy UP: fill gap 4.1e-16, confirmed; safe-global/safe-smart-account UP: fill gap 5.8e-16, confirmed; ethpandaops/ethereum-package DOWN: fill gap 5.1e-16, confirmed; OffchainLabs/stylus-sdk-rs UP: fill gap 4.4e-16, confirmed.

Held child Invalid on a sub-1 market is step 3a's merge-arb (F step 3a): on OffchainLabs/stylus-sdk-rs (I_j 67.767781294662949398, merge-arb q 20.2944) the pairs are bought and merged with the held child Invalid at once, returning q repo tokens now; that child Invalid was retained by earlier runs, and G records its consumption in their fills.json, oldest first.

Verification of the plan before it was written: 25 of 25 checks passed (planner/f-verify.json). No planned market's pools moved between F's read and its re-quote.

## Pairs: 1 markets, "pair (sum < 1 - f)", f = 0.0001

- **grandinetech/grandine** pair (sum < 1 - f): q = 8.0299 RT:grandinetech/grandine; spot sum 0.97585; locked-in sum = cost/q = 7.9323/8.0299 = 0.98785 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.0976 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 7.9323 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +44.5088 tokens for 34.3666 repo tokens (p = 0.8, stop at P = p(1-f) = 0.799920), ev 1.2405; UP leg total 52.5387 tokens at stake 40.3133 [limited_by marginal-ev-zero]

## Set rows: 12

- **Certora/CertoraProver** set-sell: 19.6242 sets, proceeds ≈ 20.1780, gain ≈ 0.5537 repo tokens, keeps 19.6242 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **Commit-Boost/commit-boost-client** set-sell: 16.6756 sets, proceeds ≈ 17.2822, gain ≈ 0.6066 repo tokens, keeps 16.6756 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **succinctlabs/rsp** set-sell: 30.9587 sets, proceeds ≈ 32.7397, gain ≈ 1.7810 repo tokens, keeps 30.9587 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **OffchainLabs/stylus-sdk-rs** merge-arb: 20.2944 pairs, cost ≈ 19.6699, gain ≈ 0.6245 repo tokens now, consumes 20.2944 child Invalid held from earlier runs (I_j 67.7678; G records it in the source runs' fills.json, oldest first) [limited_by marginal-ev-zero; group = approve, buy q UP, buy q DOWN, approve UP, DOWN and child Invalid, merge: 7 legs]
- **ethstaker/ethstaker-deposit-cli** set-sell: 26.0734 sets, proceeds ≈ 27.1354, gain ≈ 1.0620 repo tokens, keeps 26.0734 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **risc0/risc0-ethereum** set-sell: 28.0525 sets, proceeds ≈ 29.0160, gain ≈ 0.9635 repo tokens, keeps 28.0525 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **alloy-rs/alloy** set-sell: 22.8256 sets, proceeds ≈ 23.7035, gain ≈ 0.8779 repo tokens, keeps 22.8256 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **argotorg/sourcify** set-sell: 18.0865 sets, proceeds ≈ 18.5291, gain ≈ 0.4426 repo tokens, keeps 18.0865 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **safe-global/safe-smart-account** set-sell: 57.2414 sets, proceeds ≈ 61.0623, gain ≈ 3.8208 repo tokens, keeps 57.2414 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **sigp/lighthouse** set-sell: 18.7627 sets, proceeds ≈ 19.3164, gain ≈ 0.5537 repo tokens, keeps 18.7627 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **status-im/nimbus-eth2** set-sell: 14.5308 sets, proceeds ≈ 14.8888, gain ≈ 0.3579 repo tokens, keeps 14.5308 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **ethpandaops/ethereum-package** set-sell: 33.1640 sets, proceeds ≈ 34.8593, gain ≈ 1.6954 repo tokens, keeps 33.1640 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]

## Directional (stand-alone, one side) rows: 64

The count is stake / quoted_fill, the simple route's; on a one-side market with sum > 1 G routes the row complex-buy, whose delivered count is its own (G section 3).

- **ethereum/py_ecc** UP: stake 21.0922 repo tokens -> 25.3231 tokens, quoted_fill 0.83292, p 0.85, ev 0.4325, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **herumi/mcl** UP: stake 51.2637 repo tokens -> 59.9144 tokens, quoted_fill 0.85562, p 0.9, ev 2.6592, limited_by marginal-ev-zero
- **Consensys/gnark-crypto** UP: stake 20.4454 repo tokens -> 23.1582 tokens, quoted_fill 0.88285, p 0.9, ev 0.3971, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **taikoxyz/taiko-mono** UP: stake 11.8927 repo tokens -> 16.0595 tokens, quoted_fill 0.74054, p 0.75, ev 0.1520, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ethereum/js-ethereum-cryptography** DOWN: stake 11.8447 repo tokens -> 24.1975 tokens, quoted_fill 0.48950, p 0.55, ev 1.4639, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **DefiLlama/chainlist** DOWN: stake 2.8128 repo tokens -> 9.6059 tokens, quoted_fill 0.29282, p 0.30000000000000004, ev 0.0690, limited_by marginal-ev-zero
- **ChainSafe/bls** DOWN: stake 19.7055 repo tokens -> 42.8999 tokens, quoted_fill 0.45934, p 0.5, ev 1.7445, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **wealdtech/ethdo** UP: stake 9.8172 repo tokens -> 13.2282 tokens, quoted_fill 0.74214, p 0.75, ev 0.1040, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **lambdaclass/lambdaworks** UP: stake 19.0890 repo tokens -> 22.8781 tokens, quoted_fill 0.83438, p 0.85, ev 0.3575, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **skalenetwork/libBLS** UP: stake 18.1362 repo tokens -> 24.6585 tokens, quoted_fill 0.73549, p 0.75, ev 0.3577, limited_by marginal-ev-zero
- **shazow/whatsabi** UP: stake 51.3597 repo tokens -> 63.5671 tokens, quoted_fill 0.80796, p 0.85, ev 2.6723, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **TrueBlocks/trueblocks-core** UP: stake 26.3885 repo tokens -> 31.8419 tokens, quoted_fill 0.82873, p 0.85, ev 0.6771, limited_by marginal-ev-zero
- **EspressoSystems/jellyfish** UP: stake 52.5984 repo tokens -> 85.8958 tokens, quoted_fill 0.61235, p 0.65, ev 3.2338, limited_by marginal-ev-zero
- **a16z/halmos** UP: stake 25.0817 repo tokens -> 34.3284 tokens, quoted_fill 0.73064, p 0.75, ev 0.6645, limited_by marginal-ev-zero
- **succinctlabs/op-succinct** UP: stake 21.3738 repo tokens -> 36.5446 tokens, quoted_fill 0.58487, p 0.6, ev 0.5529, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **succinctlabs/sp1** UP: stake 22.2800 repo tokens -> 30.4772 tokens, quoted_fill 0.73104, p 0.75, ev 0.5780, limited_by marginal-ev-zero
- **otterscan/otterscan** DOWN: stake 7.7255 repo tokens -> 27.9622 tokens, quoted_fill 0.27629, p 0.30000000000000004, ev 0.6631, limited_by marginal-ev-zero
- **lambdaclass/ethrex** UP: stake 20.0550 repo tokens -> 25.5857 tokens, quoted_fill 0.78384, p 0.8, ev 0.4135, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **NethermindEth/juno** UP: stake 25.4350 repo tokens -> 34.8213 tokens, quoted_fill 0.73044, p 0.75, ev 0.6810, limited_by marginal-ev-zero
- **Commit-Boost/commit-boost-client** UP: stake 50.8700 repo tokens -> 66.9689 tokens, quoted_fill 0.75961, p 0.8, ev 2.7051 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **Cyfrin/aderyn** UP: stake 30.5838 repo tokens -> 45.1895 tokens, quoted_fill 0.67679, p 0.7, ev 1.0488, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **0xMiden/miden-vm** UP: stake 51.2195 repo tokens -> 63.3915 tokens, quoted_fill 0.80799, p 0.85, ev 2.6632, limited_by marginal-ev-zero
- **holiman/goevmlab** UP: stake 46.6969 repo tokens -> 61.2106 tokens, quoted_fill 0.76289, p 0.8, ev 2.2716, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **edb-rs/edb** UP: stake 44.1618 repo tokens -> 57.8876 tokens, quoted_fill 0.76289, p 0.8, ev 2.1483, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **evmts/tevm-monorepo** DOWN: stake 3.8757 repo tokens -> 11.6576 tokens, quoted_fill 0.33246, p 0.35, ev 0.2045, limited_by marginal-ev-zero
- **succinctlabs/rsp** DOWN: stake 11.9491 repo tokens -> 34.4235 tokens, quoted_fill 0.34712, p 0.4, ev 1.8203 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **OffchainLabs/stylus-sdk-rs** UP: stake 57.2759 repo tokens -> 76.0566 tokens, quoted_fill 0.75307, p 0.8, ev 3.5693 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero
- **ethstaker/ethstaker-deposit-cli** DOWN: stake 12.9560 repo tokens -> 31.3961 tokens, quoted_fill 0.41266, p 0.44999999999999996, ev 1.1722 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **dl-solarity/solidity-lib** UP: stake 14.1338 repo tokens -> 19.1343 tokens, quoted_fill 0.73866, p 0.75, ev 0.2169, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **risc0/risc0-ethereum** DOWN: stake 9.6394 repo tokens -> 34.7032 tokens, quoted_fill 0.27777, p 0.30000000000000004, ev 0.7716 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **powdr-labs/powdr** UP: stake 54.3616 repo tokens -> 67.6326 tokens, quoted_fill 0.80378, p 0.85, ev 3.1261, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **axiom-crypto/snark-verifier** DOWN: stake 3.2770 repo tokens -> 9.6405 tokens, quoted_fill 0.33992, p 0.35, ev 0.0971, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **swiss-knife-xyz/swiss-knife** DOWN: stake 4.8888 repo tokens -> 17.5837 tokens, quoted_fill 0.27803, p 0.30000000000000004, ev 0.3863, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **a16z/helios** UP: stake 14.3750 repo tokens -> 18.2445 tokens, quoted_fill 0.78791, p 0.8, ev 0.2206, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **alloy-rs/alloy** UP: stake 34.1724 repo tokens -> 41.5709 tokens, quoted_fill 0.82203, p 0.85, ev 1.1628 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **apeworx/ape** UP: stake 16.8390 repo tokens -> 22.8628 tokens, quoted_fill 0.73652, p 0.75, ev 0.3082, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **consensys/teku** UP: stake 15.2277 repo tokens -> 19.3267 tokens, quoted_fill 0.78791, p 0.8, ev 0.2337, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **erigontech/erigon** UP: stake 16.2055 repo tokens -> 21.9871 tokens, quoted_fill 0.73705, p 0.75, ev 0.2848, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **eth-infinitism/account-abstraction** UP: stake 12.7800 repo tokens -> 18.5373 tokens, quoted_fill 0.68942, p 0.7, ev 0.1961, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ethereum-lists/chains** UP: stake 21.3300 repo tokens -> 29.1387 tokens, quoted_fill 0.73201, p 0.75, ev 0.5241, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ethereum/consensus-specs** UP: stake 13.4148 repo tokens -> 15.0878 tokens, quoted_fill 0.88911, p 0.9, ev 0.1643, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ipsilon/evmone** UP: stake 44.2054 repo tokens -> 54.4295 tokens, quoted_fill 0.81216, p 0.85, ev 2.0597, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ethereum/execution-apis** UP: stake 24.4619 repo tokens -> 31.3160 tokens, quoted_fill 0.78113, p 0.8, ev 0.5908, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **argotorg/fe** UP: stake 44.9510 repo tokens -> 55.2822 tokens, quoted_fill 0.81312, p 0.85, ev 2.0389, limited_by marginal-ev-zero
- **argotorg/solidity** UP: stake 20.8130 repo tokens -> 24.9884 tokens, quoted_fill 0.83291, p 0.85, ev 0.4271, limited_by marginal-ev-zero
- **foundry-rs/foundry** UP: stake 12.9999 repo tokens -> 15.4899 tokens, quoted_fill 0.83925, p 0.85, ev 0.1665, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **hyperledger-web3j/web3j** UP: stake 19.5606 repo tokens -> 26.6377 tokens, quoted_fill 0.73432, p 0.75, ev 0.4176, limited_by marginal-ev-zero
- **hyperledger/besu** UP: stake 25.9890 repo tokens -> 33.3632 tokens, quoted_fill 0.77897, p 0.8, ev 0.7016, limited_by marginal-ev-zero
- **nethereum/nethereum** UP: stake 11.6171 repo tokens -> 13.8211 tokens, quoted_fill 0.84053, p 0.85, ev 0.1309, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **nethermindeth/nethermind** UP: stake 13.6811 repo tokens -> 18.5157 tokens, quoted_fill 0.73889, p 0.75, ev 0.2057, limited_by marginal-ev-zero
- **nomicfoundation/hardhat** UP: stake 20.3552 repo tokens -> 25.9687 tokens, quoted_fill 0.78384, p 0.8, ev 0.4197, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **openzeppelin/openzeppelin-contracts** UP: stake 17.0570 repo tokens -> 20.4031 tokens, quoted_fill 0.83600, p 0.85, ev 0.2856, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **OffchainLabs/prysm** UP: stake 20.3021 repo tokens -> 25.9009 tokens, quoted_fill 0.78384, p 0.8, ev 0.4186, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **safe-global/safe-smart-account** UP: stake 83.0831 repo tokens -> 108.5080 tokens, quoted_fill 0.76569, p 0.85, ev 9.1487 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **scaffold-eth/scaffold-eth-2** DOWN: stake 7.2431 repo tokens -> 21.5546 tokens, quoted_fill 0.33603, p 0.35, ev 0.3010, limited_by marginal-ev-zero
- **vyperlang/titanoboa** UP: stake 27.1800 repo tokens -> 37.3142 tokens, quoted_fill 0.72841, p 0.75, ev 0.8057, limited_by marginal-ev-zero
- **vyperlang/vyper** UP: stake 14.0061 repo tokens -> 17.7523 tokens, quoted_fill 0.78897, p 0.8, ev 0.1958, limited_by marginal-ev-zero
- **wevm/viem** UP: stake 30.0039 repo tokens -> 38.6540 tokens, quoted_fill 0.77622, p 0.8, ev 0.9193, limited_by marginal-ev-zero
- **argotorg/hevm** UP: stake 45.0584 repo tokens -> 59.0336 tokens, quoted_fill 0.76327, p 0.8, ev 2.1684, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ethdebug/format** UP: stake 65.6917 repo tokens -> 82.6470 tokens, quoted_fill 0.79485, p 0.85, ev 4.5583, limited_by marginal-ev-zero
- **ethpandaops/ethereum-package** DOWN: stake 7.6756 repo tokens -> 23.5415 tokens, quoted_fill 0.32605, p 0.35, ev 0.5639 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ethpandaops/checkpointz** UP: stake 49.1715 repo tokens -> 81.6469 tokens, quoted_fill 0.60225, p 0.65, ev 3.8990, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **lambdaclass/lambda_ethereum_consensus** UP: stake 16.2730 repo tokens -> 20.6829 tokens, quoted_fill 0.78679, p 0.8, ev 0.2733, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **erigontech/silkworm** UP: stake 51.8535 repo tokens -> 68.3916 tokens, quoted_fill 0.75819, p 0.8, ev 2.8598, limited_by marginal-ev-zero

## Dropped by step 7 (130)

- ethereum/py_ecc: set-sell limited_by volume-min ev -0.0000 q 0.0000 (iteration 1)
- blockscout/blockscout: set-sell limited_by gas ev 0.3151 q 14.2416 (iteration 1)
- LFDT-web3j/web3j: set-sell limited_by gas ev 0.0516 q 5.8170 (iteration 1)
- herumi/mcl: merge-arb limited_by volume-min ev 0.0000 q 0.0000 (iteration 1)
- paulmillr/noble-curves: set-sell limited_by gas ev 0.0008 q 0.8106 (iteration 1)
- arkworks-rs/algebra: set-sell limited_by gas ev 0.0043 q 1.8369 (iteration 1)
- flashbots/rbuilder: set-sell limited_by gas ev 0.3223 q 15.3118 (iteration 1)
- protofire/solhint: set-sell limited_by gas ev 0.0506 q 5.7480 (iteration 1)
- l2beat/l2beat: set-sell limited_by gas ev 0.0886 q 7.7732 (iteration 1)
- Consensys/gnark-crypto: set-sell limited_by gas ev 0.0091 q 2.6755 (iteration 1)
- Vectorized/solady: set-sell limited_by gas ev 0.0414 q 4.3548 (iteration 1)
- taikoxyz/taiko-mono: set-sell limited_by volume-min ev -0.0000 q 0.0000 (iteration 1)
- flashbots/mev-boost: set-sell limited_by gas ev 0.0169 q 3.8654 (iteration 1)
- flashbots/mev-boost-relay: set-sell limited_by gas ev 0.0451 q 5.4274 (iteration 1)
- ethereum/js-ethereum-cryptography: set-sell limited_by volume-min ev 0.0000 q 0.0000 (iteration 1)
- libp2p/libp2p: set-sell limited_by gas ev 0.0880 q 8.8303 (iteration 1)
- supranational/blst: set-sell limited_by gas ev 0.0550 q 7.0863 (iteration 1)
- wighawag/hardhat-deploy: set-sell limited_by gas ev 0.1737 q 11.9853 (iteration 1)
- ethstaker/eth-docker: set-sell limited_by gas ev 0.0212 q 4.3602 (iteration 1)
- DefiLlama/DefiLlama-Adapters: set-sell limited_by gas ev 0.1515 q 8.9147 (iteration 1)
- DefiLlama/chainlist: merge-arb limited_by gas ev 0.0071 q 2.3405 (iteration 1)
- Certora/CertoraProver: directional UP limited_by gas ev 0.0007 stake 0.8399 (iteration 1)
- Plonky3/Plonky3: set-sell limited_by gas ev 0.2399 q 13.1647 (iteration 1)
- ChainSafe/bls: set-sell limited_by gas ev 0.0266 q 4.5818 (iteration 1)
- intellij-solidity/intellij-solidity: set-sell limited_by gas ev 0.1884 q 11.9180 (iteration 1)
- dappnode/DAppNode: set-sell limited_by gas ev 0.1239 q 9.1727 (iteration 1)
- wealdtech/ethdo: set-sell limited_by gas ev 0.1047 q 8.4054 (iteration 1)
- lambdaclass/lambdaworks: set-sell limited_by gas ev 0.0170 q 3.4022 (iteration 1)
- smartcontracts/simple-optimism-node: set-sell limited_by gas ev 0.2219 q 13.2268 (iteration 1)
- skalenetwork/libBLS: merge-arb limited_by volume-min ev -0.0000 q 0.0000 (iteration 1)
- shazow/whatsabi: set-sell limited_by gas ev 0.2341 q 11.1467 (iteration 1)
- TrueBlocks/trueblocks-core: merge-arb limited_by volume-min ev -0.0000 q 0.0000 (iteration 1)
- TrueBlocks/trueblocks-core: pair limited_by volume-min gain 0.0000 q 0.0000 (iteration 1)
- EspressoSystems/jellyfish: merge-arb limited_by gas ev 0.0659 q 4.6478 (iteration 1)
- a16z/halmos: merge-arb limited_by gas ev 0.0057 q 1.6917 (iteration 1)
- succinctlabs/op-succinct: set-sell limited_by gas ev 0.0004 q 0.4117 (iteration 1)
- succinctlabs/sp1: pair limited_by gas gain 0.0181 q 3.8796 (iteration 1)
- otterscan/otterscan: merge-arb limited_by volume-min ev -0.0000 q 0.0000 (iteration 1)
- lambdaclass/ethrex: set-sell limited_by gas ev 0.2067 q 11.2615 (iteration 1)
- NethermindEth/juno: pair limited_by gas gain 0.0000 q 0.1436 (iteration 1)
- Cyfrin/aderyn: set-sell limited_by gas ev 0.0283 q 3.7218 (iteration 1)
- 0xMiden/miden-vm: merge-arb limited_by volume-min ev -0.0000 q 0.0000 (iteration 1)
- holiman/goevmlab: set-sell limited_by gas ev 0.0858 q 6.4392 (iteration 1)
- edb-rs/edb: set-sell limited_by gas ev 0.1081 q 8.7761 (iteration 1)
- evmts/tevm-monorepo: pair limited_by volume-min gain -0.0000 q 0.0000 (iteration 1)
- aestus-relay/mev-boost-relay: set-sell limited_by gas ev 0.0150 q 2.1675 (iteration 1)
- dl-solarity/solidity-lib: set-sell limited_by gas ev 0.0095 q 2.5562 (iteration 1)
- powdr-labs/powdr: set-sell limited_by gas ev 0.0010 q 0.8748 (iteration 1)
- axiom-crypto/snark-verifier: set-sell limited_by gas ev 0.0360 q 4.9184 (iteration 1)
- swiss-knife-xyz/swiss-knife: set-sell limited_by gas ev 0.1708 q 10.3612 (iteration 1)
- a16z/helios: set-sell limited_by gas ev 0.0260 q 4.5943 (iteration 1)
- apeworx/ape: set-sell limited_by gas ev 0.0327 q 4.6755 (iteration 1)
- chainsafe/lodestar: directional UP limited_by gas ev 0.0380 stake 6.1619 (iteration 1)
- consensys/teku: set-sell limited_by gas ev 0.0235 q 3.6902 (iteration 1)
- erigontech/erigon: set-sell limited_by gas ev 0.0167 q 3.3368 (iteration 1)
- eth-infinitism/account-abstraction: set-sell limited_by gas ev 0.0670 q 7.1862 (iteration 1)
- ethereum-lists/chains: set-sell limited_by gas ev 0.0055 q 2.0994 (iteration 1)
- ethereum/consensus-specs: set-sell limited_by gas ev 0.0271 q 3.2415 (iteration 1)
- ethereum/eips: merge-arb limited_by volume-min ev -0.0000 q 0.0000 (iteration 1)
- ipsilon/evmone: set-sell limited_by gas ev 0.1155 q 9.3606 (iteration 1)
- ethereum/execution-apis: set-sell limited_by gas ev 0.0019 q 0.7414 (iteration 1)
- argotorg/fe: merge-arb limited_by volume-min ev -0.0000 q 0.0000 (iteration 1)
- ethereum/go-ethereum: pair limited_by gas gain 0.0006 q 0.5955 (iteration 1)
- remix-project-org/remix-project: set-sell limited_by gas ev 0.0150 q 3.3315 (iteration 1)
- argotorg/solidity: pair limited_by gas gain 0.0029 q 1.4380 (iteration 1)
- argotorg/sourcify: directional UP limited_by gas ev 0.0077 stake 2.6685 (iteration 1)
- ethereum/web3.py: directional DOWN limited_by gas ev 0.0423 stake 2.0449 (iteration 1)
- ethers-io/ethers.js: set-sell limited_by gas ev 0.2113 q 11.9373 (iteration 1)
- grandinetech/grandine: merge-arb limited_by gas ev 0.0976 q 8.0299 (iteration 1)
- hyperledger-web3j/web3j: merge-arb limited_by gas ev 0.0161 q 3.3454 (iteration 1)
- hyperledger/besu: pair limited_by gas gain 0.0014 q 0.9638 (iteration 1)
- nethereum/nethereum: set-sell limited_by gas ev 0.0852 q 7.5031 (iteration 1)
- nethermindeth/nethermind: pair limited_by volume-min gain -0.0000 q 0.0000 (iteration 1)
- nomicfoundation/hardhat: set-sell limited_by gas ev 0.1288 q 8.3596 (iteration 1)
- openzeppelin/openzeppelin-contracts: set-sell limited_by gas ev 0.0338 q 4.8548 (iteration 1)
- paradigmxyz/reth: merge-arb limited_by gas ev 0.0564 q 6.0528 (iteration 1)
- OffchainLabs/prysm: set-sell limited_by gas ev 0.0115 q 2.5879 (iteration 1)
- scaffold-eth/scaffold-eth-2: merge-arb limited_by volume-min ev -0.0000 q 0.0000 (iteration 1)
- sigp/lighthouse: directional UP limited_by gas ev 0.0004 stake 0.6594 (iteration 1)
- status-im/nimbus-eth2: directional UP limited_by gas ev 0.0312 stake 5.8454 (iteration 1)
- vyperlang/titanoboa: merge-arb limited_by volume-min ev -0.0000 q 0.0000 (iteration 1)
- vyperlang/vyper: merge-arb limited_by gas ev 0.0554 q 5.6121 (iteration 1)
- wevm/viem: merge-arb limited_by volume-min ev -0.0000 q 0.0000 (iteration 1)
- wevm/viem: pair limited_by volume-min gain 0.0000 q 0.0000 (iteration 1)
- argotorg/hevm: set-sell limited_by gas ev 0.0033 q 1.4529 (iteration 1)
- ethdebug/format: merge-arb limited_by gas ev 0.0101 q 2.6005 (iteration 1)
- argotorg/act: merge-arb limited_by volume-min ev 0.0000 q 0.0000 (iteration 1)
- ethpandaops/ethereum-helm-charts: set-sell limited_by gas ev 0.1216 q 9.9712 (iteration 1)
- ethpandaops/checkpointz: set-sell limited_by gas ev 0.0203 q 4.2108 (iteration 1)
- lambdaclass/lambda_ethereum_consensus: set-sell limited_by gas ev 0.0065 q 2.1253 (iteration 1)
- erigontech/silkworm: merge-arb limited_by volume-min ev -0.0000 q 0.0000 (iteration 1)
- LFDT-web3j/web3j: directional UP limited_by volume-min ev -0.0000 stake 0.0000 (iteration 2)
- herumi/mcl: pair limited_by volume-min gain 0.0000 q 0.0000 (iteration 2)
- paulmillr/noble-curves: directional UP limited_by volume-min ev -0.0000 stake 0.0000 (iteration 2)
- arkworks-rs/algebra: directional DOWN limited_by volume-min ev -0.0000 stake 0.0000 (iteration 2)
- l2beat/l2beat: directional UP limited_by volume-min ev -0.0000 stake 0.0000 (iteration 2)
- flashbots/mev-boost: directional UP limited_by volume-min ev -0.0000 stake 0.0000 (iteration 2)
- flashbots/mev-boost-relay: directional UP limited_by volume-min ev -0.0000 stake 0.0000 (iteration 2)
- libp2p/libp2p: directional UP limited_by volume-min ev -0.0000 stake 0.0000 (iteration 2)
- supranational/blst: directional UP limited_by volume-min ev -0.0000 stake 0.0000 (iteration 2)
- wighawag/hardhat-deploy: directional UP limited_by gas ev 0.0150 stake 3.6221 (iteration 2)
- ethstaker/eth-docker: directional UP limited_by gas ev 0.0046 stake 1.7082 (iteration 2)
- DefiLlama/DefiLlama-Adapters: directional DOWN limited_by volume-min ev -0.0000 stake 0.0000 (iteration 2)
- DefiLlama/chainlist: pair limited_by gas gain 0.0071 q 2.3405 (iteration 2)
- Plonky3/Plonky3: directional UP limited_by volume-min ev -0.0000 stake 0.0000 (iteration 2)
- intellij-solidity/intellij-solidity: directional UP limited_by gas ev 0.0105 stake 3.1833 (iteration 2)
- dappnode/DAppNode: directional UP limited_by volume-min ev -0.0000 stake 0.0000 (iteration 2)
- skalenetwork/libBLS: pair limited_by volume-min gain -0.0000 q 0.0000 (iteration 2)
- EspressoSystems/jellyfish: pair limited_by gas gain 0.0659 q 4.6478 (iteration 2)
- a16z/halmos: pair limited_by gas gain 0.0057 q 1.6917 (iteration 2)
- otterscan/otterscan: pair limited_by volume-min gain -0.0000 q 0.0000 (iteration 2)
- 0xMiden/miden-vm: pair limited_by volume-min gain -0.0000 q 0.0000 (iteration 2)
- aestus-relay/mev-boost-relay: directional DOWN limited_by gas ev 0.0157 stake 0.6840 (iteration 2)
- ethereum/eips: pair limited_by volume-min gain -0.0000 q 0.0000 (iteration 2)
- argotorg/fe: pair limited_by volume-min gain -0.0000 q 0.0000 (iteration 2)
- ethereum/go-ethereum: directional DOWN limited_by gas ev 0.0050 stake 0.4440 (iteration 2)
- remix-project-org/remix-project: directional DOWN limited_by gas ev 0.0124 stake 0.8106 (iteration 2)
- ethers-io/ethers.js: directional DOWN limited_by gas ev 0.0100 stake 0.4860 (iteration 2)
- hyperledger-web3j/web3j: pair limited_by gas gain 0.0161 q 3.3454 (iteration 2)
- paradigmxyz/reth: pair limited_by gas gain 0.0564 q 6.0528 (iteration 2)
- scaffold-eth/scaffold-eth-2: pair limited_by volume-min gain -0.0000 q 0.0000 (iteration 2)
- vyperlang/titanoboa: pair limited_by volume-min gain -0.0000 q 0.0000 (iteration 2)
- vyperlang/vyper: pair limited_by gas gain 0.0554 q 5.6121 (iteration 2)
- ethdebug/format: pair limited_by gas gain 0.0101 q 2.6005 (iteration 2)
- argotorg/act: pair limited_by volume-min gain 0.0000 q 0.0000 (iteration 2)
- erigontech/silkworm: pair limited_by volume-min gain -0.0000 q 0.0000 (iteration 2)
- ethereum/eips: directional DOWN limited_by gas ev 0.0341 stake 0.7563 (iteration 3)
- paradigmxyz/reth: directional UP limited_by gas ev 0.0372 stake 6.1077 (iteration 3)
- argotorg/act: directional UP limited_by gas ev 0.0079 stake 2.8100 (iteration 3)
- paradigmxyz/reth: directional DOWN limited_by gas ev 0.0220 stake 0.9665 (iteration 4)

## Class vs the candidates.json snapshot (pools[].price): 9 market(s) whose class differs

- ethereum/py_ecc: snapshot sum 1.000042 (band) -> live 1.000100 (set-sell)
- taikoxyz/taiko-mono: snapshot sum 1.000091 (band) -> live 1.000100 (set-sell)
- ethereum/js-ethereum-cryptography: snapshot sum 1.000100 (band) -> live 1.000100 (set-sell)
- skalenetwork/libBLS: snapshot sum 0.999963 (band) -> live 0.999900 (sub1)
- 0xMiden/miden-vm: snapshot sum 0.999912 (band) -> live 0.999900 (sub1)
- evmts/tevm-monorepo: snapshot sum 0.999918 (band) -> live 0.999900 (sub1)
- ethereum/eips: snapshot sum 0.999927 (band) -> live 0.999900 (sub1)
- argotorg/fe: snapshot sum 0.999944 (band) -> live 0.999900 (sub1)
- scaffold-eth/scaffold-eth-2: snapshot sum 0.999908 (band) -> live 0.999900 (sub1)
- live classes: {"set-sell":67,"sub1":28,"band":3}

## No row (skipped): 29 markets

- blockscout/blockscout: spot sum 1.045102; p = [0.30000000000000004, 0.7, 0]; neither side clears p(1-f) > price; set-sell dropped by step 7 (limited_by gas): ev 0.3151 repo tokens vs gas 0.3404
- LFDT-web3j/web3j: spot sum 1.017996; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0516 repo tokens vs gas 0.3404; directional UP dropped by step 7 (limited_by volume-min): ev 0.0000 repo tokens vs VOLUME_MIN 0.01
- paulmillr/noble-curves: spot sum 1.002073; p = [0.15000000000000002, 0.85, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0008 repo tokens vs gas 0.3404; directional UP dropped by step 7 (limited_by volume-min): ev 0.0000 repo tokens vs VOLUME_MIN 0.01
- arkworks-rs/algebra: spot sum 1.004813; p = [0.15000000000000002, 0.85, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0043 repo tokens vs gas 0.3404; directional DOWN dropped by step 7 (limited_by volume-min): ev 0.0000 repo tokens vs VOLUME_MIN 0.01
- flashbots/rbuilder: spot sum 1.042853; p = [0.25, 0.75, 0]; neither side clears p(1-f) > price; set-sell dropped by step 7 (limited_by gas): ev 0.3223 repo tokens vs gas 0.3404
- protofire/solhint: spot sum 1.017835; p = [0.25, 0.75, 0]; neither side clears p(1-f) > price; set-sell dropped by step 7 (limited_by gas): ev 0.0506 repo tokens vs gas 0.3404
- l2beat/l2beat: spot sum 1.023125; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0886 repo tokens vs gas 0.3404; directional UP dropped by step 7 (limited_by volume-min): ev 0.0000 repo tokens vs VOLUME_MIN 0.01
- Vectorized/solady: spot sum 1.019323; p = [0.25, 0.75, 0]; neither side clears p(1-f) > price; set-sell dropped by step 7 (limited_by gas): ev 0.0414 repo tokens vs gas 0.3404
- flashbots/mev-boost: spot sum 1.008863; p = [0.09999999999999998, 0.9, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0169 repo tokens vs gas 0.3404; directional UP dropped by step 7 (limited_by volume-min): ev 0.0000 repo tokens vs VOLUME_MIN 0.01
- flashbots/mev-boost-relay: spot sum 1.016858; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0451 repo tokens vs gas 0.3404; directional UP dropped by step 7 (limited_by volume-min): ev 0.0000 repo tokens vs VOLUME_MIN 0.01
- libp2p/libp2p: spot sum 1.020167; p = [0.15000000000000002, 0.85, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0880 repo tokens vs gas 0.3404; directional UP dropped by step 7 (limited_by volume-min): ev 0.0000 repo tokens vs VOLUME_MIN 0.01
- supranational/blst: spot sum 1.015713; p = [0.09999999999999998, 0.9, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0550 repo tokens vs gas 0.3404; directional UP dropped by step 7 (limited_by volume-min): ev 0.0000 repo tokens vs VOLUME_MIN 0.01
- wighawag/hardhat-deploy: spot sum 1.029356; p = [0.25, 0.75, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.1737 repo tokens vs gas 0.3404; directional UP dropped by step 7 (limited_by gas): ev 0.0150 repo tokens vs gas 0.0486
- ethstaker/eth-docker: spot sum 1.009831; p = [0.4, 0.6, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0212 repo tokens vs gas 0.3404; directional UP dropped by step 7 (limited_by gas): ev 0.0046 repo tokens vs gas 0.0486
- DefiLlama/DefiLlama-Adapters: spot sum 1.034652; p = [0.30000000000000004, 0.7, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.1515 repo tokens vs gas 0.3404; directional DOWN dropped by step 7 (limited_by volume-min): ev 0.0000 repo tokens vs VOLUME_MIN 0.01
- Plonky3/Plonky3: spot sum 1.037086; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.2399 repo tokens vs gas 0.3404; directional UP dropped by step 7 (limited_by volume-min): ev 0.0000 repo tokens vs VOLUME_MIN 0.01
- intellij-solidity/intellij-solidity: spot sum 1.032097; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.1884 repo tokens vs gas 0.3404; directional UP dropped by step 7 (limited_by gas): ev 0.0105 repo tokens vs gas 0.0486
- dappnode/DAppNode: spot sum 1.027397; p = [0.30000000000000004, 0.7, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.1239 repo tokens vs gas 0.3404; directional UP dropped by step 7 (limited_by volume-min): ev 0.0000 repo tokens vs VOLUME_MIN 0.01
- smartcontracts/simple-optimism-node: spot sum 1.033984; p = [0.44999999999999996, 0.55, 0]; neither side clears p(1-f) > price; set-sell dropped by step 7 (limited_by gas): ev 0.2219 repo tokens vs gas 0.3404
- aestus-relay/mev-boost-relay: spot sum 1.014048; p = [0.30000000000000004, 0.7, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0150 repo tokens vs gas 0.3404; directional DOWN dropped by step 7 (limited_by gas): ev 0.0157 repo tokens vs gas 0.0486
- chainsafe/lodestar: spot sum 0.999959; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; sum within [1-f, 1/(1-f)] so neither 3a nor 3b applies; directional UP dropped by step 7 (limited_by gas): ev 0.0380 repo tokens vs gas 0.0486
- ethereum/eips: spot sum 0.999900; p = [0.09999999999999998, 0.9, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; merge-arb dropped by step 7 (limited_by volume-min): ev -0.0000 repo tokens vs VOLUME_MIN 0.01; pair dropped by step 7 (limited_by volume-min): gain -0.0000 repo tokens vs VOLUME_MIN 0.01; directional DOWN dropped by step 7 (limited_by gas): ev 0.0341 repo tokens vs gas 0.0486
- ethereum/go-ethereum: spot sum 0.997994; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; pair dropped by step 7 (limited_by gas): gain 0.0006 repo tokens vs gas 0.0973; directional DOWN dropped by step 7 (limited_by gas): ev 0.0050 repo tokens vs gas 0.0486
- remix-project-org/remix-project: spot sum 1.009164; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0150 repo tokens vs gas 0.3404; directional DOWN dropped by step 7 (limited_by gas): ev 0.0124 repo tokens vs gas 0.0486
- ethereum/web3.py: spot sum 0.999993; p = [0.30000000000000004, 0.7, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; sum within [1-f, 1/(1-f)] so neither 3a nor 3b applies; directional DOWN dropped by step 7 (limited_by gas): ev 0.0423 repo tokens vs gas 0.0486
- ethers-io/ethers.js: spot sum 1.036258; p = [0.15000000000000002, 0.85, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.2113 repo tokens vs gas 0.3404; directional DOWN dropped by step 7 (limited_by gas): ev 0.0100 repo tokens vs gas 0.0486
- paradigmxyz/reth: spot sum 0.981438; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; merge-arb dropped by step 7 (limited_by gas): ev 0.0564 repo tokens vs gas 0.3404; pair dropped by step 7 (limited_by gas): gain 0.0564 repo tokens vs gas 0.0973; directional UP dropped by step 7 (limited_by gas): ev 0.0372 repo tokens vs gas 0.0486; directional DOWN dropped by step 7 (limited_by gas): ev 0.0220 repo tokens vs gas 0.0486
- argotorg/act: spot sum 0.999900; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; merge-arb dropped by step 7 (limited_by volume-min): ev 0.0000 repo tokens vs VOLUME_MIN 0.01; pair dropped by step 7 (limited_by volume-min): gain 0.0000 repo tokens vs VOLUME_MIN 0.01; directional UP dropped by step 7 (limited_by gas): ev 0.0079 repo tokens vs gas 0.0486
- ethpandaops/ethereum-helm-charts: spot sum 1.024660; p = [0.4, 0.6, 0]; neither side clears p(1-f) > price; set-sell dropped by step 7 (limited_by gas): ev 0.1216 repo tokens vs gas 0.3404

**Totals:** 78 rows over 69 markets; sum ev = 91.4032 repo tokens (different tokens per market) => expected_value 0.932686 sUSDS at 1/98.
