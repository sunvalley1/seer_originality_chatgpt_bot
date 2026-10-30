# F plan: allocation.json of run 2026-10-30T2103Z

Holder `0x2AD670e5953a85C998cDf1C2f6D74386aB735d4a`. Pool state read at blocks 158897741..158897744 (both pools of a market in one multicall file, so each market has one pinned block; the head moves, so no two reads are compared by block). Nothing is sent by F.

objective max-ev; 98 independent per-market budgets, each `held_j + M` (held_j = the repo token held plus its bundle's unsplit tokens, which G middle-splits first; 98 market(s) hold some), so each market may spend up to held_j + M = held_j + 14.8564242378734 of its own repo token.
Bankroll = the holder's whole sUSDS balance 433.705911148178. USDC and USDS are 0: no PSM3 ramp, so the bankroll is not provisional. M = min(bankroll, max_j (cap_j - held_j)+) = 14.8564242378734 sUSDS: the books bind (largest unconstrained cap above held_j 14.8564 repo tokens at safe-global/safe-smart-account).

A `set` row's worst_case 0 holds only if its whole keep-whole group lands: the planner sends every group as an ordered sequence of single transactions, on any signer, so a group can be left half-done between transactions, and a half-done group carries the stray leg's risk until its recovery batch lands (G section 8 step 5).

totals.staked = M = 14.856424 sUSDS (G splits the parent by M and then each middle whose bundle holds a position by M); totals.expected_value = 0.505792 sUSDS at the labelled 1/N = 1/98 scenario (a repo token is worth 0 if its repo is not evaluated); correlated_worst_case = -14.856424 sUSDS (the whole outlay can go to zero together; no correlation control).

Gas floors use F step 7's 2.4e-7 ETH per swap leg = 0.04697 repo tokens (set group 7 legs 0.3288, pair 2 legs 0.0939), converted at 1997.14 sUSDS per ETH (QuoterV2 WETH/USDC and PSM3 usdPerSusds 1.114642452114434) and x98; F simulates nothing. For the record: eth_gasPrice 1000315 wei, l1BaseFee 127948130 wei, signer ETH 0.005212144311310398 (F does not gate on it; G's affordability check does).

Negative-ev rows: 1 of 72 rows have ev < 0 (sum -0.0636 repo tokens); all are legs of a step-3b pair on a CSV market, which keeps its p-based fields although the pair is bought whatever the CSV says (F step 3b and the schema conventions); 0 market(s) have a negative total ev. The step-3b pair is a CSV-independent arbitrage, so it can sit above the CSV's own value of one leg.

Budget headroom: 1 market(s) spend their whole budget held_j + M; on a dual-buy pair that binds the budget, G clamps the second leg's amountInMaximum to what the first leg leaves (G section 3), so F reserves no headroom.

Rows sized on a state a step-3a set-sell or merge-arb left (marked "post-set-sell" below; after a merge-arb, a pair leg or folded extra is quoted on the live pool at q + count less the quote at q, an exact-output swap's cost being path-additive) are computed from the 3a quote's sqrtPriceX96After and the pool's liquidity with the exact integer Uniswap v3 single-range model, because the chain helper's call and multicall carry no state override (F step 8); the same model reproduced every QuoterV2 answer of this plan to within 2.3e-17 relative. Each such row was then probed on simulated state with the helper's simulate "return" probe (the mint prefix it needs, the set group, then QuoterV2 flagged return): dappnode/DAppNode UP: fill gap 1.6e-15, confirmed; shazow/whatsabi UP: fill gap 1.4e-15, confirmed; Commit-Boost/commit-boost-client UP: fill gap 2.7e-15, confirmed; holiman/goevmlab UP: fill gap 1.5e-15, confirmed; OffchainLabs/stylus-sdk-rs UP: fill gap 3.7e-15, confirmed; alloy-rs/alloy UP: fill gap 5.5e-16, confirmed; argotorg/fe UP: fill gap 1.2e-15, confirmed.

Verification of the plan before it was written: 25 of 25 checks passed (planner/f-verify.json). No planned market's pools moved between F's read and its re-quote.

## Pairs: 1 markets, "pair (sum < 1 - f)", f = 0.0001

- **OffchainLabs/prysm** pair (sum < 1 - f): q = 7.8274 RT:OffchainLabs/prysm; spot sum 0.97596; locked-in sum = cost/q = 7.7326/7.8274 = 0.98789 [limited_by marginal-ev-zero]
  - outcome: +(1 - sum)*q = 0.0948 repo tokens if the repo is evaluated and its child resolves to a score; nothing of value lost if the repo is not evaluated (the repo tokens spent were worth 0 then)
  - risk (a): evaluated but the child resolves INVALID anyway: UP + DOWN pay 0, a loss of sum*q = 7.7326 repo tokens
  - risk (b): the parent's n_X and the middle's k_X disagree: a repo token pays (n_X/N)/k_X
  - folded directional extra on UP: +12.2867 tokens for 9.7341 repo tokens (p = 0.8, stop at P = p(1-f) = 0.799920), ev 0.0952; UP leg total 20.1141 tokens at stake 15.8377 [limited_by marginal-ev-zero]

## Set rows: 7

- **dappnode/DAppNode** set-sell: 17.2804 sets, proceeds ≈ 17.7652, gain ≈ 0.4848 repo tokens, keeps 17.2804 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **shazow/whatsabi** set-sell: 20.7975 sets, proceeds ≈ 21.6437, gain ≈ 0.8462 repo tokens, keeps 20.7975 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **Commit-Boost/commit-boost-client** set-sell: 15.7931 sets, proceeds ≈ 16.2914, gain ≈ 0.4983 repo tokens, keeps 15.7931 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **holiman/goevmlab** set-sell: 17.5316 sets, proceeds ≈ 18.1860, gain ≈ 0.6544 repo tokens, keeps 17.5316 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **OffchainLabs/stylus-sdk-rs** set-sell: 21.4833 sets, proceeds ≈ 22.1304, gain ≈ 0.6470 repo tokens, keeps 21.4833 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **alloy-rs/alloy** set-sell: 20.0571 sets, proceeds ≈ 20.7853, gain ≈ 0.7282 repo tokens, keeps 20.0571 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **argotorg/fe** set-sell: 15.3170 sets, proceeds ≈ 15.7248, gain ≈ 0.4078 repo tokens, keeps 15.3170 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- merge-arb: none (88 market(s) hold child Invalid, none of them a sub-1 market whose merge-arb survived step 7)

## Directional (stand-alone, one side) rows: 63

The count is stake / quoted_fill, the simple route's; on a one-side market with sum > 1 G routes the row complex-buy, whose delivered count is its own (G section 3).

- **ethereum/py_ecc** UP: stake 13.9107 repo tokens -> 16.5852 tokens, quoted_fill 0.83874, p 0.85, ev 0.1868, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **blockscout/blockscout** UP: stake 7.3040 repo tokens -> 10.5203 tokens, quoted_fill 0.69428, p 0.7, ev 0.0602, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **herumi/mcl** UP: stake 39.3089 repo tokens -> 45.3931 tokens, quoted_fill 0.86597, p 0.9, ev 1.5449, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **paulmillr/noble-curves** UP: stake 56.2795 repo tokens -> 70.0430 tokens, quoted_fill 0.80350, p 0.85, ev 3.2571, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **flashbots/rbuilder** UP: stake 8.3158 repo tokens -> 11.1888 tokens, quoted_fill 0.74323, p 0.75, ev 0.0757, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **l2beat/l2beat** UP: stake 6.8180 repo tokens -> 8.5813 tokens, quoted_fill 0.79452, p 0.8, ev 0.0470, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **Consensys/gnark-crypto** UP: stake 23.2027 repo tokens -> 26.3505 tokens, quoted_fill 0.88054, p 0.9, ev 0.5127, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **taikoxyz/taiko-mono** UP: stake 11.0002 repo tokens -> 14.8402 tokens, quoted_fill 0.74125, p 0.75, ev 0.1299, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ethereum/js-ethereum-cryptography** DOWN: stake 9.0334 repo tokens -> 17.9282 tokens, quoted_fill 0.50386, p 0.55, ev 0.8272, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **wighawag/hardhat-deploy** UP: stake 8.6143 repo tokens -> 11.5996 tokens, quoted_fill 0.74264, p 0.75, ev 0.0854, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **DefiLlama/chainlist** DOWN: stake 8.7414 repo tokens -> 31.4809 tokens, quoted_fill 0.27767, p 0.30000000000000004, ev 0.7029, limited_by marginal-ev-zero
- **Plonky3/Plonky3** UP: stake 6.8006 repo tokens -> 8.5600 tokens, quoted_fill 0.79446, p 0.8, ev 0.0474, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ChainSafe/bls** DOWN: stake 16.8990 repo tokens -> 36.3319 tokens, quoted_fill 0.46513, p 0.5, ev 1.2670, limited_by marginal-ev-zero
- **intellij-solidity/intellij-solidity** UP: stake 7.2701 repo tokens -> 9.1561 tokens, quoted_fill 0.79402, p 0.8, ev 0.0548, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **dappnode/DAppNode** UP: stake 28.3787 repo tokens -> 41.8798 tokens, quoted_fill 0.67762, p 0.7, ev 0.9372 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **wealdtech/ethdo** UP: stake 7.0874 repo tokens -> 9.5219 tokens, quoted_fill 0.74432, p 0.75, ev 0.0540, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **lambdaclass/lambdaworks** UP: stake 15.7226 repo tokens -> 18.7816 tokens, quoted_fill 0.83713, p 0.85, ev 0.2417, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **smartcontracts/simple-optimism-node** UP: stake 16.4033 repo tokens -> 30.5832 tokens, quoted_fill 0.53635, p 0.55, ev 0.4175, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **skalenetwork/libBLS** UP: stake 8.0048 repo tokens -> 10.7650 tokens, quoted_fill 0.74360, p 0.75, ev 0.0689, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **shazow/whatsabi** UP: stake 59.6817 repo tokens -> 74.4952 tokens, quoted_fill 0.80115, p 0.85, ev 3.6392 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **succinctlabs/sp1** UP: stake 11.2298 repo tokens -> 15.1664 tokens, quoted_fill 0.74044, p 0.75, ev 0.1450, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **otterscan/otterscan** DOWN: stake 3.2636 repo tokens -> 11.2544 tokens, quoted_fill 0.28998, p 0.30000000000000004, ev 0.1127, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **lambdaclass/ethrex** UP: stake 15.1103 repo tokens -> 19.1799 tokens, quoted_fill 0.78782, p 0.8, ev 0.2336, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **Commit-Boost/commit-boost-client** UP: stake 35.7789 repo tokens -> 46.3704 tokens, quoted_fill 0.77159, p 0.8, ev 1.3174 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **Cyfrin/aderyn** UP: stake 10.6453 repo tokens -> 15.3852 tokens, quoted_fill 0.69192, p 0.7, ev 0.1243, limited_by marginal-ev-zero
- **0xMiden/miden-vm** UP: stake 29.4563 repo tokens -> 35.6684 tokens, quoted_fill 0.82584, p 0.85, ev 0.8618, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **holiman/goevmlab** UP: stake 47.7564 repo tokens -> 62.6685 tokens, quoted_fill 0.76205, p 0.8, ev 2.3784 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **edb-rs/edb** UP: stake 36.8961 repo tokens -> 47.9797 tokens, quoted_fill 0.76899, p 0.8, ev 1.4876, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **succinctlabs/rsp** DOWN: stake 2.7397 repo tokens -> 7.0635 tokens, quoted_fill 0.38788, p 0.4, ev 0.0856, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **OffchainLabs/stylus-sdk-rs** UP: stake 15.3892 repo tokens -> 19.5446 tokens, quoted_fill 0.78739, p 0.8, ev 0.2464 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ethstaker/ethstaker-deposit-cli** DOWN: stake 6.5258 repo tokens -> 15.1344 tokens, quoted_fill 0.43119, p 0.44999999999999996, ev 0.2846, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **dl-solarity/solidity-lib** UP: stake 17.3975 repo tokens -> 23.6365 tokens, quoted_fill 0.73605, p 0.75, ev 0.3298, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **powdr-labs/powdr** UP: stake 33.6925 repo tokens -> 41.0208 tokens, quoted_fill 0.82135, p 0.85, ev 1.1751, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **axiom-crypto/snark-verifier** DOWN: stake 2.4286 repo tokens -> 7.0902 tokens, quoted_fill 0.34253, p 0.35, ev 0.0529, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **swiss-knife-xyz/swiss-knife** DOWN: stake 4.1067 repo tokens -> 14.5863 tokens, quoted_fill 0.28154, p 0.30000000000000004, ev 0.2692, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **a16z/helios** UP: stake 11.1497 repo tokens -> 14.1025 tokens, quoted_fill 0.79062, p 0.8, ev 0.1323, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **alloy-rs/alloy** UP: stake 47.3755 repo tokens -> 58.4004 tokens, quoted_fill 0.81122, p 0.85, ev 2.2648 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **apeworx/ape** UP: stake 12.1983 repo tokens -> 16.4789 tokens, quoted_fill 0.74024, p 0.75, ev 0.1609, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **consensys/teku** UP: stake 11.8201 repo tokens -> 14.9506 tokens, quoted_fill 0.79061, p 0.8, ev 0.1403, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **erigontech/erigon** UP: stake 11.7606 repo tokens -> 15.8797 tokens, quoted_fill 0.74060, p 0.75, ev 0.1493, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **eth-infinitism/account-abstraction** UP: stake 29.2619 repo tokens -> 43.3012 tokens, quoted_fill 0.67578, p 0.7, ev 1.0490, limited_by marginal-ev-zero
- **ethereum-lists/chains** UP: stake 15.4152 repo tokens -> 20.9161 tokens, quoted_fill 0.73700, p 0.75, ev 0.2719, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ethereum/consensus-specs** UP: stake 11.8368 repo tokens -> 13.2939 tokens, quoted_fill 0.89039, p 0.9, ev 0.1277, limited_by marginal-ev-zero
- **ipsilon/evmone** UP: stake 34.4617 repo tokens -> 42.0009 tokens, quoted_fill 0.82050, p 0.85, ev 1.2391, limited_by marginal-ev-zero
- **ethereum/execution-apis** UP: stake 6.9737 repo tokens -> 8.7761 tokens, quoted_fill 0.79462, p 0.8, ev 0.0472, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **argotorg/fe** UP: stake 47.4247 repo tokens -> 58.4705 tokens, quoted_fill 0.81109, p 0.85, ev 2.2752 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ethers-io/ethers.js** DOWN: stake 1.2136 repo tokens -> 8.5202 tokens, quoted_fill 0.14243, p 0.15000000000000002, ev 0.0645, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **foundry-rs/foundry** UP: stake 8.6802 repo tokens -> 10.2990 tokens, quoted_fill 0.84282, p 0.85, ev 0.0739, limited_by marginal-ev-zero
- **grandinetech/grandine** UP: stake 9.1484 repo tokens -> 11.5426 tokens, quoted_fill 0.79258, p 0.8, ev 0.0856, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **hyperledger-web3j/web3j** UP: stake 7.3422 repo tokens -> 9.8670 tokens, quoted_fill 0.74412, p 0.75, ev 0.0581, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **nethereum/nethereum** UP: stake 9.5455 repo tokens -> 11.3338 tokens, quoted_fill 0.84222, p 0.85, ev 0.0882, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **nomicfoundation/hardhat** UP: stake 15.4789 repo tokens -> 19.6506 tokens, quoted_fill 0.78771, p 0.8, ev 0.2415, limited_by marginal-ev-zero
- **openzeppelin/openzeppelin-contracts** UP: stake 14.0024 repo tokens -> 16.6992 tokens, quoted_fill 0.83851, p 0.85, ev 0.1919, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **safe-global/safe-smart-account** UP: stake 58.4780 repo tokens -> 73.9614 tokens, quoted_fill 0.79066, p 0.85, ev 4.3892, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **sigp/lighthouse** UP: stake 7.1690 repo tokens -> 8.4920 tokens, quoted_fill 0.84421, p 0.85, ev 0.0491, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **status-im/nimbus-eth2** UP: stake 9.7612 repo tokens -> 10.9428 tokens, quoted_fill 0.89202, p 0.9, ev 0.0873, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **vyperlang/titanoboa** UP: stake 9.9360 repo tokens -> 13.3890 tokens, quoted_fill 0.74211, p 0.75, ev 0.1057, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **argotorg/hevm** UP: stake 19.4902 repo tokens -> 24.8565 tokens, quoted_fill 0.78411, p 0.8, ev 0.3949, limited_by marginal-ev-zero
- **ethdebug/format** UP: stake 28.5774 repo tokens -> 34.5971 tokens, quoted_fill 0.82601, p 0.85, ev 0.8301, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ethpandaops/ethereum-helm-charts** UP: stake 14.6438 repo tokens -> 24.9184 tokens, quoted_fill 0.58767, p 0.6, ev 0.3072, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ethpandaops/checkpointz** UP: stake 49.1489 repo tokens -> 81.6064 tokens, quoted_fill 0.60227, p 0.65, ev 3.8953, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **lambdaclass/lambda_ethereum_consensus** UP: stake 16.3117 repo tokens -> 20.7329 tokens, quoted_fill 0.78675, p 0.8, ev 0.2746, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **erigontech/silkworm** UP: stake 51.8035 repo tokens -> 68.3220 tokens, quoted_fill 0.75823, p 0.8, ev 2.8541, limited_by marginal-ev-zero

## Dropped by step 7 (128)

- ethereum/py_ecc: set-sell limited_by gas ev 0.3172 q 13.3479 (iteration 1)
- blockscout/blockscout: set-sell limited_by gas ev 0.0210 q 3.7203 (iteration 1)
- LFDT-web3j/web3j: set-sell limited_by gas ev 0.0507 q 5.7670 (iteration 1)
- herumi/mcl: set-sell limited_by gas ev 0.0343 q 5.3397 (iteration 1)
- paulmillr/noble-curves: set-sell limited_by gas ev 0.0417 q 4.9806 (iteration 1)
- arkworks-rs/algebra: set-sell limited_by gas ev 0.0784 q 7.4977 (iteration 1)
- flashbots/rbuilder: set-sell limited_by gas ev 0.0229 q 4.1219 (iteration 1)
- protofire/solhint: set-sell limited_by gas ev 0.0402 q 5.0819 (iteration 1)
- l2beat/l2beat: set-sell limited_by gas ev 0.0442 q 5.4359 (iteration 1)
- Consensys/gnark-crypto: set-sell limited_by gas ev 0.2779 q 13.9906 (iteration 1)
- Vectorized/solady: set-sell limited_by gas ev 0.0706 q 5.5868 (iteration 1)
- taikoxyz/taiko-mono: set-sell limited_by gas ev 0.0220 q 3.8254 (iteration 1)
- flashbots/mev-boost: set-sell limited_by gas ev 0.0178 q 3.9699 (iteration 1)
- flashbots/mev-boost-relay: set-sell limited_by gas ev 0.0466 q 5.5138 (iteration 1)
- ethereum/js-ethereum-cryptography: set-sell limited_by gas ev 0.0118 q 2.1792 (iteration 1)
- libp2p/libp2p: set-sell limited_by gas ev 0.0276 q 4.9601 (iteration 1)
- supranational/blst: set-sell limited_by gas ev 0.0564 q 7.1717 (iteration 1)
- wighawag/hardhat-deploy: set-sell limited_by gas ev 0.0339 q 5.3227 (iteration 1)
- ethstaker/eth-docker: set-sell limited_by gas ev 0.0213 q 4.3708 (iteration 1)
- DefiLlama/DefiLlama-Adapters: set-sell limited_by gas ev 0.0197 q 3.2445 (iteration 1)
- DefiLlama/chainlist: merge-arb limited_by gas ev 0.0881 q 8.4639 (iteration 1)
- Certora/CertoraProver: set-sell limited_by gas ev 0.0000 q 0.0818 (iteration 1)
- Plonky3/Plonky3: set-sell limited_by gas ev 0.0288 q 4.6038 (iteration 1)
- ChainSafe/bls: merge-arb limited_by volume-min ev 0.0000 q 0.0000 (iteration 1)
- intellij-solidity/intellij-solidity: set-sell limited_by gas ev 0.0619 q 6.8666 (iteration 1)
- wealdtech/ethdo: set-sell limited_by gas ev 0.0240 q 4.0885 (iteration 1)
- lambdaclass/lambdaworks: set-sell limited_by gas ev 0.0343 q 4.8500 (iteration 1)
- smartcontracts/simple-optimism-node: set-sell limited_by gas ev 0.0016 q 1.1054 (iteration 1)
- skalenetwork/libBLS: set-sell limited_by gas ev 0.0317 q 4.6688 (iteration 1)
- TrueBlocks/trueblocks-core: set-sell limited_by gas ev 0.0637 q 6.2031 (iteration 1)
- EspressoSystems/jellyfish: set-sell limited_by gas ev 0.0170 q 2.5316 (iteration 1)
- a16z/halmos: set-sell limited_by gas ev 0.0480 q 5.0858 (iteration 1)
- succinctlabs/op-succinct: set-sell limited_by gas ev 0.0168 q 2.7401 (iteration 1)
- succinctlabs/sp1: set-sell limited_by gas ev 0.0154 q 3.5857 (iteration 1)
- otterscan/otterscan: set-sell limited_by gas ev 0.0266 q 4.3716 (iteration 1)
- lambdaclass/ethrex: set-sell limited_by gas ev 0.0044 q 1.7107 (iteration 1)
- NethermindEth/juno: set-sell limited_by gas ev 0.0260 q 3.6679 (iteration 1)
- Cyfrin/aderyn: merge-arb limited_by volume-min ev -0.0000 q 0.0000 (iteration 1)
- 0xMiden/miden-vm: set-sell limited_by gas ev 0.0832 q 7.2596 (iteration 1)
- edb-rs/edb: set-sell limited_by gas ev 0.0556 q 6.4134 (iteration 1)
- evmts/tevm-monorepo: set-sell limited_by gas ev 0.0450 q 4.8027 (iteration 1)
- succinctlabs/rsp: set-sell limited_by gas ev 0.1771 q 9.4698 (iteration 1)
- aestus-relay/mev-boost-relay: set-sell limited_by gas ev 0.0649 q 4.3999 (iteration 1)
- ethstaker/ethstaker-deposit-cli: set-sell limited_by gas ev 0.0153 q 3.1207 (iteration 1)
- dl-solarity/solidity-lib: set-sell limited_by gas ev 0.2071 q 11.5714 (iteration 1)
- risc0/risc0-ethereum: set-sell limited_by gas ev 0.0651 q 7.1371 (iteration 1)
- powdr-labs/powdr: set-sell limited_by gas ev 0.1058 q 9.0314 (iteration 1)
- axiom-crypto/snark-verifier: set-sell limited_by gas ev 0.0236 q 3.9585 (iteration 1)
- swiss-knife-xyz/swiss-knife: set-sell limited_by gas ev 0.0661 q 6.3421 (iteration 1)
- a16z/helios: set-sell limited_by gas ev 0.0000 q 0.1464 (iteration 1)
- apeworx/ape: set-sell limited_by gas ev 0.0259 q 4.2054 (iteration 1)
- chainsafe/lodestar: directional UP limited_by gas ev 0.0380 stake 6.1619 (iteration 1)
- consensys/teku: set-sell limited_by gas ev 0.0376 q 4.6918 (iteration 1)
- erigontech/erigon: set-sell limited_by gas ev 0.0288 q 4.4076 (iteration 1)
- eth-infinitism/account-abstraction: merge-arb limited_by volume-min ev -0.0000 q 0.0000 (iteration 1)
- eth-infinitism/account-abstraction: pair limited_by gas gain 0.0010 q 0.8916 (iteration 1)
- ethereum-lists/chains: set-sell limited_by gas ev 0.0074 q 2.4442 (iteration 1)
- ethereum/consensus-specs: merge-arb limited_by gas ev 0.0600 q 5.3476 (iteration 1)
- ethereum/eips: set-sell limited_by gas ev 0.0000 q 0.0882 (iteration 1)
- ipsilon/evmone: merge-arb limited_by gas ev 0.0339 q 5.3509 (iteration 1)
- ethereum/execution-apis: set-sell limited_by gas ev 0.0266 q 2.9539 (iteration 1)
- ethereum/go-ethereum: pair limited_by gas gain 0.0005 q 0.5708 (iteration 1)
- remix-project-org/remix-project: set-sell limited_by gas ev 0.0158 q 3.4142 (iteration 1)
- argotorg/solidity: set-sell limited_by gas ev 0.0707 q 7.2573 (iteration 1)
- argotorg/sourcify: set-sell limited_by gas ev 0.0000 q 0.0557 (iteration 1)
- ethereum/web3.py: directional DOWN limited_by gas ev 0.0429 stake 2.0593 (iteration 1)
- ethers-io/ethers.js: set-sell limited_by gas ev 0.0658 q 6.7236 (iteration 1)
- foundry-rs/foundry: merge-arb limited_by volume-min ev 0.0000 q 0.0000 (iteration 1)
- foundry-rs/foundry: pair limited_by gas gain 0.0694 q 7.6120 (iteration 1)
- grandinetech/grandine: set-sell limited_by gas ev 0.0619 q 6.5744 (iteration 1)
- hyperledger-web3j/web3j: set-sell limited_by gas ev 0.0250 q 4.1860 (iteration 1)
- hyperledger/besu: set-sell limited_by gas ev 0.0331 q 4.8317 (iteration 1)
- nethereum/nethereum: set-sell limited_by gas ev 0.0087 q 2.4695 (iteration 1)
- nethermindeth/nethermind: set-sell limited_by gas ev 0.0247 q 4.3089 (iteration 1)
- nomicfoundation/hardhat: merge-arb limited_by gas ev 0.0111 q 2.5954 (iteration 1)
- openzeppelin/openzeppelin-contracts: set-sell limited_by gas ev 0.0498 q 5.9211 (iteration 1)
- paradigmxyz/reth: merge-arb limited_by gas ev 0.0536 q 5.8969 (iteration 1)
- OffchainLabs/prysm: merge-arb limited_by gas ev 0.0948 q 7.8274 (iteration 1)
- safe-global/safe-smart-account: set-sell limited_by gas ev 0.0309 q 5.3824 (iteration 1)
- scaffold-eth/scaffold-eth-2: set-sell limited_by gas ev 0.0198 q 4.0610 (iteration 1)
- sigp/lighthouse: set-sell limited_by gas ev 0.0645 q 6.2666 (iteration 1)
- status-im/nimbus-eth2: set-sell limited_by gas ev 0.0606 q 5.8150 (iteration 1)
- vyperlang/titanoboa: set-sell limited_by gas ev 0.1846 q 10.8284 (iteration 1)
- vyperlang/vyper: set-sell limited_by gas ev 0.0006 q 0.6080 (iteration 1)
- wevm/viem: set-sell limited_by gas ev 0.1263 q 8.5811 (iteration 1)
- argotorg/hevm: merge-arb limited_by volume-min ev -0.0000 q 0.0000 (iteration 1)
- ethdebug/format: set-sell limited_by volume-min ev 0.0000 q 0.0000 (iteration 1)
- argotorg/act: set-sell limited_by gas ev 0.0589 q 6.1926 (iteration 1)
- ethpandaops/ethereum-package: set-sell limited_by gas ev 0.1255 q 8.8715 (iteration 1)
- ethpandaops/ethereum-helm-charts: set-sell limited_by gas ev 0.0132 q 3.2550 (iteration 1)
- ethpandaops/checkpointz: set-sell limited_by gas ev 0.0202 q 4.2002 (iteration 1)
- lambdaclass/lambda_ethereum_consensus: set-sell limited_by gas ev 0.0069 q 2.1981 (iteration 1)
- LFDT-web3j/web3j: directional UP limited_by gas ev 0.0000 stake 0.0400 (iteration 2)
- arkworks-rs/algebra: directional UP limited_by gas ev 0.0168 stake 4.1673 (iteration 2)
- protofire/solhint: directional UP limited_by gas ev 0.0209 stake 4.4526 (iteration 2)
- flashbots/mev-boost: directional UP limited_by gas ev 0.0000 stake 0.0450 (iteration 2)
- flashbots/mev-boost-relay: directional UP limited_by gas ev 0.0000 stake 0.0400 (iteration 2)
- libp2p/libp2p: directional UP limited_by gas ev 0.0114 stake 3.3720 (iteration 2)
- supranational/blst: directional UP limited_by gas ev 0.0000 stake 0.0450 (iteration 2)
- ethstaker/eth-docker: directional UP limited_by gas ev 0.0048 stake 1.7380 (iteration 2)
- DefiLlama/DefiLlama-Adapters: directional DOWN limited_by gas ev 0.0460 stake 1.6549 (iteration 2)
- DefiLlama/chainlist: pair limited_by gas gain 0.0881 q 8.4639 (iteration 2)
- Certora/CertoraProver: directional UP limited_by gas ev 0.0008 stake 0.8799 (iteration 2)
- ChainSafe/bls: pair limited_by volume-min gain 0.0000 q 0.0000 (iteration 2)
- TrueBlocks/trueblocks-core: directional UP limited_by gas ev 0.0233 stake 4.9421 (iteration 2)
- EspressoSystems/jellyfish: directional UP limited_by gas ev 0.0142 stake 3.5797 (iteration 2)
- a16z/halmos: directional UP limited_by gas ev 0.0055 stake 2.3129 (iteration 2)
- succinctlabs/op-succinct: directional UP limited_by gas ev 0.0442 stake 6.0957 (iteration 2)
- NethermindEth/juno: directional UP limited_by gas ev 0.0186 stake 4.2532 (iteration 2)
- Cyfrin/aderyn: pair limited_by volume-min gain -0.0000 q 0.0000 (iteration 2)
- evmts/tevm-monorepo: directional DOWN limited_by gas ev 0.0206 stake 1.2531 (iteration 2)
- ethereum/consensus-specs: pair limited_by gas gain 0.0600 q 5.3476 (iteration 2)
- ethereum/eips: directional DOWN limited_by gas ev 0.0300 stake 0.7109 (iteration 2)
- ipsilon/evmone: pair limited_by gas gain 0.0339 q 5.3509 (iteration 2)
- ethereum/go-ethereum: directional DOWN limited_by gas ev 0.0050 stake 0.4440 (iteration 2)
- remix-project-org/remix-project: directional DOWN limited_by gas ev 0.0112 stake 0.7699 (iteration 2)
- argotorg/solidity: directional UP limited_by gas ev 0.0095 stake 3.1301 (iteration 2)
- argotorg/sourcify: directional UP limited_by gas ev 0.0080 stake 2.7058 (iteration 2)
- hyperledger/besu: directional UP limited_by gas ev 0.0435 stake 6.5359 (iteration 2)
- nethermindeth/nethermind: directional UP limited_by gas ev 0.0092 stake 2.9073 (iteration 2)
- nomicfoundation/hardhat: pair limited_by gas gain 0.0111 q 2.5954 (iteration 2)
- paradigmxyz/reth: pair limited_by gas gain 0.0536 q 5.8969 (iteration 2)
- scaffold-eth/scaffold-eth-2: directional DOWN limited_by gas ev 0.0331 stake 2.4333 (iteration 2)
- wevm/viem: directional UP limited_by gas ev 0.0128 stake 3.5825 (iteration 2)
- argotorg/hevm: pair limited_by volume-min gain -0.0000 q 0.0000 (iteration 2)
- argotorg/act: directional UP limited_by gas ev 0.0334 stake 5.7570 (iteration 2)
- paradigmxyz/reth: directional UP limited_by gas ev 0.0372 stake 6.1077 (iteration 3)
- paradigmxyz/reth: directional DOWN limited_by gas ev 0.0198 stake 0.9165 (iteration 4)

## Class vs the candidates.json snapshot (pools[].price): 2 market(s) whose class differs

- ChainSafe/bls: snapshot sum 0.999934 (band) -> live 0.999900 (sub1)
- Cyfrin/aderyn: snapshot sum 0.999928 (band) -> live 0.999900 (sub1)
- live classes: {"set-sell":83,"sub1":12,"band":3}

## No row (skipped): 34 markets

- LFDT-web3j/web3j: spot sum 1.017839; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0507 repo tokens vs gas 0.3288; directional UP dropped by step 7 (limited_by gas): ev 0.0000 repo tokens vs gas 0.0470
- arkworks-rs/algebra: spot sum 1.021214; p = [0.15000000000000002, 0.85, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0784 repo tokens vs gas 0.3288; directional UP dropped by step 7 (limited_by gas): ev 0.0168 repo tokens vs gas 0.0470
- protofire/solhint: spot sum 1.016018; p = [0.25, 0.75, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0402 repo tokens vs gas 0.3288; directional UP dropped by step 7 (limited_by gas): ev 0.0209 repo tokens vs gas 0.0470
- Vectorized/solady: spot sum 1.025751; p = [0.25, 0.75, 0]; neither side clears p(1-f) > price; set-sell dropped by step 7 (limited_by gas): ev 0.0706 repo tokens vs gas 0.3288
- flashbots/mev-boost: spot sum 1.009110; p = [0.09999999999999998, 0.9, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0178 repo tokens vs gas 0.3288; directional UP dropped by step 7 (limited_by gas): ev 0.0000 repo tokens vs gas 0.0470
- flashbots/mev-boost-relay: spot sum 1.017142; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0466 repo tokens vs gas 0.3288; directional UP dropped by step 7 (limited_by gas): ev 0.0000 repo tokens vs gas 0.0470
- libp2p/libp2p: spot sum 1.011280; p = [0.15000000000000002, 0.85, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0276 repo tokens vs gas 0.3288; directional UP dropped by step 7 (limited_by gas): ev 0.0114 repo tokens vs gas 0.0470
- supranational/blst: spot sum 1.015914; p = [0.09999999999999998, 0.9, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0564 repo tokens vs gas 0.3288; directional UP dropped by step 7 (limited_by gas): ev 0.0000 repo tokens vs gas 0.0470
- ethstaker/eth-docker: spot sum 1.009855; p = [0.4, 0.6, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0213 repo tokens vs gas 0.3288; directional UP dropped by step 7 (limited_by gas): ev 0.0048 repo tokens vs gas 0.0470
- DefiLlama/DefiLlama-Adapters: spot sum 1.012289; p = [0.30000000000000004, 0.7, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0197 repo tokens vs gas 0.3288; directional DOWN dropped by step 7 (limited_by gas): ev 0.0460 repo tokens vs gas 0.0470
- Certora/CertoraProver: spot sum 1.000325; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0000 repo tokens vs gas 0.3288; directional UP dropped by step 7 (limited_by gas): ev 0.0008 repo tokens vs gas 0.0470
- TrueBlocks/trueblocks-core: spot sum 1.020882; p = [0.15000000000000002, 0.85, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0637 repo tokens vs gas 0.3288; directional UP dropped by step 7 (limited_by gas): ev 0.0233 repo tokens vs gas 0.0470
- EspressoSystems/jellyfish: spot sum 1.013597; p = [0.35, 0.65, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0170 repo tokens vs gas 0.3288; directional UP dropped by step 7 (limited_by gas): ev 0.0142 repo tokens vs gas 0.0470
- a16z/halmos: spot sum 1.019144; p = [0.25, 0.75, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0480 repo tokens vs gas 0.3288; directional UP dropped by step 7 (limited_by gas): ev 0.0055 repo tokens vs gas 0.0470
- succinctlabs/op-succinct: spot sum 1.012455; p = [0.4, 0.6, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0168 repo tokens vs gas 0.3288; directional UP dropped by step 7 (limited_by gas): ev 0.0442 repo tokens vs gas 0.0470
- NethermindEth/juno: spot sum 1.014402; p = [0.25, 0.75, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0260 repo tokens vs gas 0.3288; directional UP dropped by step 7 (limited_by gas): ev 0.0186 repo tokens vs gas 0.0470
- evmts/tevm-monorepo: spot sum 1.018984; p = [0.35, 0.65, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0450 repo tokens vs gas 0.3288; directional DOWN dropped by step 7 (limited_by gas): ev 0.0206 repo tokens vs gas 0.0470
- aestus-relay/mev-boost-relay: spot sum 1.030153; p = [0.30000000000000004, 0.7, 0]; neither side clears p(1-f) > price; set-sell dropped by step 7 (limited_by gas): ev 0.0649 repo tokens vs gas 0.3288
- risc0/risc0-ethereum: spot sum 1.018448; p = [0.30000000000000004, 0.7, 0]; neither side clears p(1-f) > price; set-sell dropped by step 7 (limited_by gas): ev 0.0651 repo tokens vs gas 0.3288
- chainsafe/lodestar: spot sum 0.999959; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; sum within [1-f, 1/(1-f)] so neither 3a nor 3b applies; directional UP dropped by step 7 (limited_by gas): ev 0.0380 repo tokens vs gas 0.0470
- ethereum/eips: spot sum 1.000321; p = [0.09999999999999998, 0.9, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0000 repo tokens vs gas 0.3288; directional DOWN dropped by step 7 (limited_by gas): ev 0.0300 repo tokens vs gas 0.0470
- ethereum/go-ethereum: spot sum 0.998073; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; pair dropped by step 7 (limited_by gas): gain 0.0005 repo tokens vs gas 0.0939; directional DOWN dropped by step 7 (limited_by gas): ev 0.0050 repo tokens vs gas 0.0470
- remix-project-org/remix-project: spot sum 1.009397; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0158 repo tokens vs gas 0.3288; directional DOWN dropped by step 7 (limited_by gas): ev 0.0112 repo tokens vs gas 0.0470
- argotorg/solidity: spot sum 1.019757; p = [0.15000000000000002, 0.85, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0707 repo tokens vs gas 0.3288; directional UP dropped by step 7 (limited_by gas): ev 0.0095 repo tokens vs gas 0.0470
- argotorg/sourcify: spot sum 1.000246; p = [0.25, 0.75, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0000 repo tokens vs gas 0.3288; directional UP dropped by step 7 (limited_by gas): ev 0.0080 repo tokens vs gas 0.0470
- ethereum/web3.py: spot sum 0.999932; p = [0.30000000000000004, 0.7, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; sum within [1-f, 1/(1-f)] so neither 3a nor 3b applies; directional DOWN dropped by step 7 (limited_by gas): ev 0.0429 repo tokens vs gas 0.0470
- hyperledger/besu: spot sum 1.013892; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0331 repo tokens vs gas 0.3288; directional UP dropped by step 7 (limited_by gas): ev 0.0435 repo tokens vs gas 0.0470
- nethermindeth/nethermind: spot sum 1.011608; p = [0.25, 0.75, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0247 repo tokens vs gas 0.3288; directional UP dropped by step 7 (limited_by gas): ev 0.0092 repo tokens vs gas 0.0470
- paradigmxyz/reth: spot sum 0.981888; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; merge-arb dropped by step 7 (limited_by gas): ev 0.0536 repo tokens vs gas 0.3288; pair dropped by step 7 (limited_by gas): gain 0.0536 repo tokens vs gas 0.0939; directional UP dropped by step 7 (limited_by gas): ev 0.0372 repo tokens vs gas 0.0470; directional DOWN dropped by step 7 (limited_by gas): ev 0.0198 repo tokens vs gas 0.0470
- scaffold-eth/scaffold-eth-2: spot sum 1.009885; p = [0.35, 0.65, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0198 repo tokens vs gas 0.3288; directional DOWN dropped by step 7 (limited_by gas): ev 0.0331 repo tokens vs gas 0.0470
- vyperlang/vyper: spot sum 1.002173; p = [0.19999999999999996, 0.8, 0]; neither side clears p(1-f) > price; set-sell dropped by step 7 (limited_by gas): ev 0.0006 repo tokens vs gas 0.3288
- wevm/viem: spot sum 1.029980; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.1263 repo tokens vs gas 0.3288; directional UP dropped by step 7 (limited_by gas): ev 0.0128 repo tokens vs gas 0.0470
- argotorg/act: spot sum 1.019282; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0589 repo tokens vs gas 0.3288; directional UP dropped by step 7 (limited_by gas): ev 0.0334 repo tokens vs gas 0.0470
- ethpandaops/ethereum-package: spot sum 1.028692; p = [0.35, 0.65, 0]; neither side clears p(1-f) > price; set-sell dropped by step 7 (limited_by gas): ev 0.1255 repo tokens vs gas 0.3288

**Totals:** 72 rows over 64 markets; sum ev = 49.5676 repo tokens (different tokens per market) => expected_value 0.505792 sUSDS at 1/98.
