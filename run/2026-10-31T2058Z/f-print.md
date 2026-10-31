# F plan: allocation.json of run 2026-10-31T2058Z

Holder `0x2AD670e5953a85C998cDf1C2f6D74386aB735d4a`. Pool state read at blocks 158940791..158940793 (both pools of a market in one multicall file, so each market has one pinned block; the head moves, so no two reads are compared by block). Nothing is sent by F.

objective max-ev; 98 independent per-market budgets, each `held_j + M` (held_j = the repo token held plus its bundle's unsplit tokens, which G middle-splits first; 98 market(s) hold some), so each market may spend up to held_j + M = held_j + 0 of its own repo token.
Bankroll = the holder's whole sUSDS balance 418.849486910304. USDC and USDS are 0: no PSM3 ramp, so the bankroll is not provisional. M = min(bankroll, max_j (cap_j - held_j)+) = 0 sUSDS: the books bind (largest unconstrained cap above held_j 0.0000 repo tokens at ethereum/py_ecc).

A `set` row's worst_case 0 holds only if its whole keep-whole group lands: the planner sends every group as an ordered sequence of single transactions, on any signer, so a group can be left half-done between transactions, and a half-done group carries the stray leg's risk until its recovery batch lands (G section 8 step 5).

totals.staked = M = 0.000000 sUSDS (G splits the parent by M and then each middle whose bundle holds a position by M); totals.expected_value = 0.504032 sUSDS at the labelled 1/N = 1/98 scenario (a repo token is worth 0 if its repo is not evaluated); correlated_worst_case = 0.000000 sUSDS (the whole outlay can go to zero together; no correlation control).

Gas floors use F step 7's 2.4e-7 ETH per swap leg = 0.04723 repo tokens (set group 7 legs 0.3306, pair 2 legs 0.0945), converted at 2008.17 sUSDS per ETH (QuoterV2 WETH/USDC and PSM3 usdPerSusds 1.1147559568509675) and x98; F simulates nothing. For the record: eth_gasPrice 1000275 wei, l1BaseFee 43927370 wei, signer ETH 0.00519431856602798 (F does not gate on it; G's affordability check does).

Negative-ev rows: 0 of 69 rows have ev < 0 (sum 0.0000 repo tokens); 0 market(s) have a negative total ev. The step-3b pair is a CSV-independent arbitrage, so it can sit above the CSV's own value of one leg.

Budget headroom: 1 market(s) spend their whole budget held_j + M; on a dual-buy pair that binds the budget, G clamps the second leg's amountInMaximum to what the first leg leaves (G section 3), so F reserves no headroom.

Rows sized on a state a step-3a set-sell or merge-arb left (marked "post-set-sell" below; after a merge-arb, a pair leg or folded extra is quoted on the live pool at q + count less the quote at q, an exact-output swap's cost being path-additive) are computed from the 3a quote's sqrtPriceX96After and the pool's liquidity with the exact integer Uniswap v3 single-range model, because the chain helper's call and multicall carry no state override (F step 8); the same model reproduced every QuoterV2 answer of this plan to within 2.3e-17 relative. Each such row was then probed on simulated state with the helper's simulate "return" probe (the mint prefix it needs, the set group, then QuoterV2 flagged return): dappnode/DAppNode UP: fill gap 2.0e-15, confirmed; shazow/whatsabi UP: fill gap 1.7e-15, confirmed; Commit-Boost/commit-boost-client UP: fill gap 1.4e-15, confirmed; holiman/goevmlab UP: fill gap 1.7e-15, confirmed; OffchainLabs/stylus-sdk-rs UP: fill gap 3.2e-15, confirmed; alloy-rs/alloy UP: fill gap 4.1e-16, confirmed; argotorg/fe UP: fill gap 2.2e-15, confirmed.

Verification of the plan before it was written: 25 of 25 checks passed (planner/f-verify.json). No planned market's pools moved between F's read and its re-quote.

## Pairs: 0 markets, "pair (sum < 1 - f)", f = 0.0001


## Set rows: 7

- **dappnode/DAppNode** set-sell: 17.2772 sets, proceeds ≈ 17.7618, gain ≈ 0.4846 repo tokens, keeps 17.2772 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **shazow/whatsabi** set-sell: 20.4993 sets, proceeds ≈ 21.3197, gain ≈ 0.8204 repo tokens, keeps 20.4993 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **Commit-Boost/commit-boost-client** set-sell: 15.6025 sets, proceeds ≈ 16.0883, gain ≈ 0.4858 repo tokens, keeps 15.6025 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **holiman/goevmlab** set-sell: 17.2454 sets, proceeds ≈ 17.8773, gain ≈ 0.6319 repo tokens, keeps 17.2454 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **OffchainLabs/stylus-sdk-rs** set-sell: 21.4787 sets, proceeds ≈ 22.1254, gain ≈ 0.6468 repo tokens, keeps 21.4787 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **alloy-rs/alloy** set-sell: 19.7490 sets, proceeds ≈ 20.4535, gain ≈ 0.7045 repo tokens, keeps 19.7490 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- **argotorg/fe** set-sell: 15.3070 sets, proceeds ≈ 15.7142, gain ≈ 0.4072 repo tokens, keeps 15.3070 child Invalid [limited_by marginal-ev-zero; group = approve, split, approve, sell UP, approve, sell DOWN: 7 legs]
- merge-arb: none (88 market(s) hold child Invalid, none of them a sub-1 market whose merge-arb survived step 7)

## Directional (stand-alone, one side) rows: 62

The count is stake / quoted_fill, the simple route's; on a one-side market with sum > 1 G routes the row complex-buy, whose delivered count is its own (G section 3).

- **ethereum/py_ecc** UP: stake 13.9189 repo tokens -> 16.5952 tokens, quoted_fill 0.83873, p 0.85, ev 0.1870, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **blockscout/blockscout** UP: stake 7.2940 repo tokens -> 10.5058 tokens, quoted_fill 0.69428, p 0.7, ev 0.0601, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **herumi/mcl** UP: stake 39.3089 repo tokens -> 45.3931 tokens, quoted_fill 0.86597, p 0.9, ev 1.5449, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **paulmillr/noble-curves** UP: stake 56.2695 repo tokens -> 70.0298 tokens, quoted_fill 0.80351, p 0.85, ev 3.2559, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **flashbots/rbuilder** UP: stake 8.3158 repo tokens -> 11.1888 tokens, quoted_fill 0.74323, p 0.75, ev 0.0757, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **Consensys/gnark-crypto** UP: stake 23.2754 repo tokens -> 26.4348 tokens, quoted_fill 0.88048, p 0.9, ev 0.5160, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **taikoxyz/taiko-mono** UP: stake 10.9896 repo tokens -> 14.8257 tokens, quoted_fill 0.74125, p 0.75, ev 0.1297, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ethereum/js-ethereum-cryptography** DOWN: stake 9.0334 repo tokens -> 17.9282 tokens, quoted_fill 0.50386, p 0.55, ev 0.8272, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **wighawag/hardhat-deploy** UP: stake 8.6143 repo tokens -> 11.5996 tokens, quoted_fill 0.74264, p 0.75, ev 0.0854, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **DefiLlama/chainlist** DOWN: stake 8.7314 repo tokens -> 31.4420 tokens, quoted_fill 0.27770, p 0.30000000000000004, ev 0.7012, limited_by marginal-ev-zero
- **Plonky3/Plonky3** UP: stake 6.8006 repo tokens -> 8.5600 tokens, quoted_fill 0.79446, p 0.8, ev 0.0474, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ChainSafe/bls** DOWN: stake 16.8990 repo tokens -> 36.3319 tokens, quoted_fill 0.46513, p 0.5, ev 1.2670, limited_by marginal-ev-zero
- **intellij-solidity/intellij-solidity** UP: stake 7.2701 repo tokens -> 9.1561 tokens, quoted_fill 0.79402, p 0.8, ev 0.0548, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **dappnode/DAppNode** UP: stake 28.3831 repo tokens -> 41.8866 tokens, quoted_fill 0.67762, p 0.7, ev 0.9375 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **wealdtech/ethdo** UP: stake 7.0874 repo tokens -> 9.5219 tokens, quoted_fill 0.74432, p 0.75, ev 0.0540, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **lambdaclass/lambdaworks** UP: stake 15.7226 repo tokens -> 18.7816 tokens, quoted_fill 0.83713, p 0.85, ev 0.2417, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **smartcontracts/simple-optimism-node** UP: stake 16.3933 repo tokens -> 30.5641 tokens, quoted_fill 0.53636, p 0.55, ev 0.4170, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **skalenetwork/libBLS** UP: stake 8.0048 repo tokens -> 10.7650 tokens, quoted_fill 0.74360, p 0.75, ev 0.0689, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **shazow/whatsabi** UP: stake 59.5316 repo tokens -> 74.2964 tokens, quoted_fill 0.80127, p 0.85, ev 3.6204 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **succinctlabs/sp1** UP: stake 11.2198 repo tokens -> 15.1527 tokens, quoted_fill 0.74045, p 0.75, ev 0.1447, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **otterscan/otterscan** DOWN: stake 3.2536 repo tokens -> 11.2187 tokens, quoted_fill 0.29001, p 0.30000000000000004, ev 0.1120, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **lambdaclass/ethrex** UP: stake 15.1103 repo tokens -> 19.1799 tokens, quoted_fill 0.78782, p 0.8, ev 0.2336, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **Commit-Boost/commit-boost-client** UP: stake 35.7215 repo tokens -> 46.2932 tokens, quoted_fill 0.77164, p 0.8, ev 1.3131 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **Cyfrin/aderyn** UP: stake 10.6952 repo tokens -> 15.4581 tokens, quoted_fill 0.69188, p 0.7, ev 0.1255, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **0xMiden/miden-vm** UP: stake 29.4643 repo tokens -> 35.6784 tokens, quoted_fill 0.82583, p 0.85, ev 0.8623, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **holiman/goevmlab** UP: stake 47.6189 repo tokens -> 62.4792 tokens, quoted_fill 0.76216, p 0.8, ev 2.3644 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **edb-rs/edb** UP: stake 36.8961 repo tokens -> 47.9797 tokens, quoted_fill 0.76899, p 0.8, ev 1.4876, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **succinctlabs/rsp** DOWN: stake 2.7435 repo tokens -> 7.0735 tokens, quoted_fill 0.38786, p 0.4, ev 0.0859, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **OffchainLabs/stylus-sdk-rs** UP: stake 15.3934 repo tokens -> 19.5499 tokens, quoted_fill 0.78739, p 0.8, ev 0.2466 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ethstaker/ethstaker-deposit-cli** DOWN: stake 6.5158 repo tokens -> 15.1102 tokens, quoted_fill 0.43122, p 0.44999999999999996, ev 0.2837, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **dl-solarity/solidity-lib** UP: stake 17.3975 repo tokens -> 23.6365 tokens, quoted_fill 0.73605, p 0.75, ev 0.3298, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **powdr-labs/powdr** UP: stake 33.7005 repo tokens -> 41.0308 tokens, quoted_fill 0.82135, p 0.85, ev 1.1757, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **axiom-crypto/snark-verifier** DOWN: stake 2.4320 repo tokens -> 7.1002 tokens, quoted_fill 0.34252, p 0.35, ev 0.0531, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **swiss-knife-xyz/swiss-knife** DOWN: stake 4.1093 repo tokens -> 14.5963 tokens, quoted_fill 0.28153, p 0.30000000000000004, ev 0.2696, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **a16z/helios** UP: stake 11.1497 repo tokens -> 14.1025 tokens, quoted_fill 0.79062, p 0.8, ev 0.1323, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **alloy-rs/alloy** UP: stake 47.2142 repo tokens -> 58.1920 tokens, quoted_fill 0.81135, p 0.85, ev 2.2490 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **apeworx/ape** UP: stake 12.1983 repo tokens -> 16.4789 tokens, quoted_fill 0.74024, p 0.75, ev 0.1609, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **consensys/teku** UP: stake 11.8101 repo tokens -> 14.9378 tokens, quoted_fill 0.79062, p 0.8, ev 0.1401, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **erigontech/erigon** UP: stake 11.7506 repo tokens -> 15.8661 tokens, quoted_fill 0.74061, p 0.75, ev 0.1490, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **eth-infinitism/account-abstraction** UP: stake 29.2519 repo tokens -> 43.2859 tokens, quoted_fill 0.67578, p 0.7, ev 1.0482, limited_by marginal-ev-zero
- **ethereum-lists/chains** UP: stake 15.4152 repo tokens -> 20.9161 tokens, quoted_fill 0.73700, p 0.75, ev 0.2719, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ethereum/consensus-specs** UP: stake 11.8368 repo tokens -> 13.2939 tokens, quoted_fill 0.89039, p 0.9, ev 0.1277, limited_by marginal-ev-zero
- **ipsilon/evmone** UP: stake 34.4617 repo tokens -> 42.0009 tokens, quoted_fill 0.82050, p 0.85, ev 1.2391, limited_by marginal-ev-zero
- **argotorg/fe** UP: stake 47.4247 repo tokens -> 58.4705 tokens, quoted_fill 0.81109, p 0.85, ev 2.2752 (post-set-sell, exact model, not the quoter), limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ethers-io/ethers.js** DOWN: stake 1.2036 repo tokens -> 8.4463 tokens, quoted_fill 0.14250, p 0.15000000000000002, ev 0.0634, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **foundry-rs/foundry** UP: stake 8.6802 repo tokens -> 10.2990 tokens, quoted_fill 0.84282, p 0.85, ev 0.0739, limited_by marginal-ev-zero
- **grandinetech/grandine** UP: stake 9.1484 repo tokens -> 11.5426 tokens, quoted_fill 0.79258, p 0.8, ev 0.0856, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **hyperledger-web3j/web3j** UP: stake 7.3422 repo tokens -> 9.8670 tokens, quoted_fill 0.74412, p 0.75, ev 0.0581, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **nethereum/nethereum** UP: stake 9.5455 repo tokens -> 11.3338 tokens, quoted_fill 0.84222, p 0.85, ev 0.0882, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **nomicfoundation/hardhat** UP: stake 15.4789 repo tokens -> 19.6506 tokens, quoted_fill 0.78771, p 0.8, ev 0.2415, limited_by marginal-ev-zero
- **openzeppelin/openzeppelin-contracts** UP: stake 14.0024 repo tokens -> 16.6992 tokens, quoted_fill 0.83851, p 0.85, ev 0.1919, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **OffchainLabs/prysm** UP: stake 15.8377 repo tokens -> 20.1141 tokens, quoted_fill 0.78739, p 0.8, ev 0.2536, limited_by marginal-ev-zero
- **safe-global/safe-smart-account** UP: stake 58.4780 repo tokens -> 73.9614 tokens, quoted_fill 0.79066, p 0.85, ev 4.3892, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **sigp/lighthouse** UP: stake 7.1774 repo tokens -> 8.5020 tokens, quoted_fill 0.84421, p 0.85, ev 0.0493, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **status-im/nimbus-eth2** UP: stake 9.7700 repo tokens -> 10.9528 tokens, quoted_fill 0.89201, p 0.9, ev 0.0875, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **vyperlang/titanoboa** UP: stake 9.9434 repo tokens -> 13.3990 tokens, quoted_fill 0.74210, p 0.75, ev 0.1058, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **argotorg/hevm** UP: stake 19.4902 repo tokens -> 24.8565 tokens, quoted_fill 0.78411, p 0.8, ev 0.3949, limited_by marginal-ev-zero
- **ethdebug/format** UP: stake 28.5774 repo tokens -> 34.5971 tokens, quoted_fill 0.82601, p 0.85, ev 0.8301, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ethpandaops/ethereum-helm-charts** UP: stake 14.6438 repo tokens -> 24.9184 tokens, quoted_fill 0.58767, p 0.6, ev 0.3072, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **ethpandaops/checkpointz** UP: stake 49.1389 repo tokens -> 81.5885 tokens, quoted_fill 0.60228, p 0.65, ev 3.8936, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **lambdaclass/lambda_ethereum_consensus** UP: stake 16.3117 repo tokens -> 20.7329 tokens, quoted_fill 0.78675, p 0.8, ev 0.2746, limited_by marginal-ev-zero; spot sum > 1 so G routes complex-buy: this count is a LOWER BOUND (more tokens plus child Invalid delivered)
- **erigontech/silkworm** UP: stake 51.7935 repo tokens -> 68.3081 tokens, quoted_fill 0.75823, p 0.8, ev 2.8530, limited_by marginal-ev-zero

## Dropped by step 7 (125)

- ethereum/py_ecc: set-sell limited_by gas ev 0.3062 q 13.1287 (iteration 1)
- blockscout/blockscout: set-sell limited_by gas ev 0.0210 q 3.7254 (iteration 1)
- LFDT-web3j/web3j: set-sell limited_by gas ev 0.0506 q 5.7570 (iteration 1)
- herumi/mcl: set-sell limited_by gas ev 0.0346 q 5.3634 (iteration 1)
- paulmillr/noble-curves: set-sell limited_by gas ev 0.0417 q 4.9853 (iteration 1)
- arkworks-rs/algebra: set-sell limited_by gas ev 0.0746 q 7.3182 (iteration 1)
- flashbots/rbuilder: set-sell limited_by gas ev 0.0231 q 4.1423 (iteration 1)
- protofire/solhint: set-sell limited_by gas ev 0.0405 q 5.1048 (iteration 1)
- l2beat/l2beat: set-sell limited_by gas ev 0.0446 q 5.4613 (iteration 1)
- Consensys/gnark-crypto: set-sell limited_by gas ev 0.2659 q 13.6983 (iteration 1)
- Vectorized/solady: set-sell limited_by gas ev 0.0699 q 5.5594 (iteration 1)
- taikoxyz/taiko-mono: set-sell limited_by gas ev 0.0211 q 3.7455 (iteration 1)
- flashbots/mev-boost: set-sell limited_by gas ev 0.0181 q 4.0006 (iteration 1)
- flashbots/mev-boost-relay: set-sell limited_by gas ev 0.0471 q 5.5406 (iteration 1)
- ethereum/js-ethereum-cryptography: set-sell limited_by gas ev 0.0118 q 2.1820 (iteration 1)
- libp2p/libp2p: set-sell limited_by gas ev 0.0279 q 4.9820 (iteration 1)
- supranational/blst: set-sell limited_by gas ev 0.0568 q 7.1983 (iteration 1)
- wighawag/hardhat-deploy: set-sell limited_by gas ev 0.0342 q 5.3402 (iteration 1)
- ethstaker/eth-docker: set-sell limited_by gas ev 0.0214 q 4.3828 (iteration 1)
- DefiLlama/DefiLlama-Adapters: set-sell limited_by gas ev 0.0200 q 3.2692 (iteration 1)
- DefiLlama/chainlist: merge-arb limited_by gas ev 0.0877 q 8.4437 (iteration 1)
- Certora/CertoraProver: set-sell limited_by gas ev 0.0000 q 0.1081 (iteration 1)
- Plonky3/Plonky3: set-sell limited_by gas ev 0.0291 q 4.6275 (iteration 1)
- intellij-solidity/intellij-solidity: set-sell limited_by gas ev 0.0623 q 6.8889 (iteration 1)
- wealdtech/ethdo: set-sell limited_by gas ev 0.0242 q 4.1101 (iteration 1)
- lambdaclass/lambdaworks: set-sell limited_by gas ev 0.0347 q 4.8786 (iteration 1)
- smartcontracts/simple-optimism-node: set-sell limited_by gas ev 0.0016 q 1.1117 (iteration 1)
- skalenetwork/libBLS: set-sell limited_by gas ev 0.0320 q 4.6905 (iteration 1)
- TrueBlocks/trueblocks-core: set-sell limited_by gas ev 0.0635 q 6.1931 (iteration 1)
- EspressoSystems/jellyfish: set-sell limited_by gas ev 0.0170 q 2.5343 (iteration 1)
- a16z/halmos: set-sell limited_by gas ev 0.0481 q 5.0900 (iteration 1)
- succinctlabs/op-succinct: set-sell limited_by gas ev 0.0169 q 2.7432 (iteration 1)
- succinctlabs/sp1: set-sell limited_by gas ev 0.0155 q 3.5927 (iteration 1)
- otterscan/otterscan: set-sell limited_by gas ev 0.0269 q 4.3923 (iteration 1)
- lambdaclass/ethrex: set-sell limited_by gas ev 0.0045 q 1.7363 (iteration 1)
- NethermindEth/juno: set-sell limited_by gas ev 0.0264 q 3.6939 (iteration 1)
- 0xMiden/miden-vm: set-sell limited_by gas ev 0.0830 q 7.2496 (iteration 1)
- edb-rs/edb: set-sell limited_by gas ev 0.0560 q 6.4335 (iteration 1)
- evmts/tevm-monorepo: set-sell limited_by gas ev 0.0454 q 4.8245 (iteration 1)
- succinctlabs/rsp: set-sell limited_by gas ev 0.1767 q 9.4598 (iteration 1)
- aestus-relay/mev-boost-relay: set-sell limited_by gas ev 0.0602 q 4.2420 (iteration 1)
- ethstaker/ethstaker-deposit-cli: set-sell limited_by gas ev 0.0155 q 3.1380 (iteration 1)
- dl-solarity/solidity-lib: set-sell limited_by gas ev 0.2039 q 11.4841 (iteration 1)
- risc0/risc0-ethereum: set-sell limited_by gas ev 0.0652 q 7.1435 (iteration 1)
- powdr-labs/powdr: set-sell limited_by gas ev 0.1057 q 9.0264 (iteration 1)
- axiom-crypto/snark-verifier: set-sell limited_by gas ev 0.0235 q 3.9485 (iteration 1)
- swiss-knife-xyz/swiss-knife: set-sell limited_by gas ev 0.0659 q 6.3321 (iteration 1)
- a16z/helios: set-sell limited_by gas ev 0.0000 q 0.1673 (iteration 1)
- apeworx/ape: set-sell limited_by gas ev 0.0262 q 4.2269 (iteration 1)
- chainsafe/lodestar: directional UP limited_by gas ev 0.0380 stake 6.1619 (iteration 1)
- consensys/teku: set-sell limited_by gas ev 0.0376 q 4.6964 (iteration 1)
- erigontech/erigon: set-sell limited_by gas ev 0.0288 q 4.4130 (iteration 1)
- eth-infinitism/account-abstraction: merge-arb limited_by volume-min ev -0.0000 q 0.0000 (iteration 1)
- eth-infinitism/account-abstraction: pair limited_by gas gain 0.0010 q 0.8855 (iteration 1)
- ethereum-lists/chains: set-sell limited_by gas ev 0.0075 q 2.4625 (iteration 1)
- ethereum/consensus-specs: merge-arb limited_by gas ev 0.0600 q 5.3476 (iteration 1)
- ethereum/eips: set-sell limited_by gas ev 0.0000 q 0.1317 (iteration 1)
- ipsilon/evmone: merge-arb limited_by gas ev 0.0336 q 5.3281 (iteration 1)
- ethereum/execution-apis: set-sell limited_by gas ev 0.0272 q 2.9887 (iteration 1)
- ethereum/go-ethereum: pair limited_by gas gain 0.0005 q 0.5659 (iteration 1)
- remix-project-org/remix-project: set-sell limited_by gas ev 0.0161 q 3.4405 (iteration 1)
- argotorg/solidity: set-sell limited_by gas ev 0.0713 q 7.2850 (iteration 1)
- argotorg/sourcify: set-sell limited_by gas ev 0.0000 q 0.0769 (iteration 1)
- ethereum/web3.py: directional DOWN limited_by gas ev 0.0429 stake 2.0593 (iteration 1)
- ethers-io/ethers.js: set-sell limited_by gas ev 0.0666 q 6.7606 (iteration 1)
- foundry-rs/foundry: merge-arb limited_by volume-min ev 0.0000 q 0.0000 (iteration 1)
- foundry-rs/foundry: pair limited_by gas gain 0.0689 q 7.5829 (iteration 1)
- grandinetech/grandine: set-sell limited_by gas ev 0.0623 q 6.5984 (iteration 1)
- hyperledger-web3j/web3j: set-sell limited_by gas ev 0.0253 q 4.2076 (iteration 1)
- hyperledger/besu: set-sell limited_by gas ev 0.0332 q 4.8374 (iteration 1)
- nethereum/nethereum: set-sell limited_by gas ev 0.0090 q 2.5001 (iteration 1)
- nethermindeth/nethermind: set-sell limited_by gas ev 0.0249 q 4.3295 (iteration 1)
- nomicfoundation/hardhat: merge-arb limited_by gas ev 0.0111 q 2.5954 (iteration 1)
- openzeppelin/openzeppelin-contracts: set-sell limited_by gas ev 0.0503 q 5.9489 (iteration 1)
- paradigmxyz/reth: merge-arb limited_by gas ev 0.0530 q 5.8657 (iteration 1)
- OffchainLabs/prysm: merge-arb limited_by gas ev 0.0941 q 7.7971 (iteration 1)
- safe-global/safe-smart-account: set-sell limited_by gas ev 0.0310 q 5.3953 (iteration 1)
- scaffold-eth/scaffold-eth-2: set-sell limited_by gas ev 0.0200 q 4.0765 (iteration 1)
- sigp/lighthouse: set-sell limited_by gas ev 0.0644 q 6.2624 (iteration 1)
- status-im/nimbus-eth2: set-sell limited_by gas ev 0.0544 q 5.5237 (iteration 1)
- vyperlang/titanoboa: set-sell limited_by gas ev 0.1842 q 10.8184 (iteration 1)
- vyperlang/vyper: set-sell limited_by gas ev 0.0006 q 0.6126 (iteration 1)
- wevm/viem: set-sell limited_by gas ev 0.1260 q 8.5711 (iteration 1)
- ethdebug/format: set-sell limited_by gas ev 0.0000 q 0.0247 (iteration 1)
- argotorg/act: set-sell limited_by gas ev 0.0594 q 6.2184 (iteration 1)
- ethpandaops/ethereum-package: set-sell limited_by gas ev 0.1252 q 8.8615 (iteration 1)
- ethpandaops/ethereum-helm-charts: set-sell limited_by gas ev 0.0133 q 3.2694 (iteration 1)
- ethpandaops/checkpointz: set-sell limited_by gas ev 0.0203 q 4.2080 (iteration 1)
- lambdaclass/lambda_ethereum_consensus: set-sell limited_by gas ev 0.0071 q 2.2225 (iteration 1)
- LFDT-web3j/web3j: directional UP limited_by gas ev 0.0000 stake 0.0480 (iteration 2)
- arkworks-rs/algebra: directional UP limited_by gas ev 0.0169 stake 4.1757 (iteration 2)
- protofire/solhint: directional UP limited_by gas ev 0.0209 stake 4.4526 (iteration 2)
- l2beat/l2beat: directional UP limited_by gas ev 0.0470 stake 6.8180 (iteration 2)
- flashbots/mev-boost: directional UP limited_by gas ev 0.0000 stake 0.0450 (iteration 2)
- flashbots/mev-boost-relay: directional UP limited_by gas ev 0.0000 stake 0.0400 (iteration 2)
- libp2p/libp2p: directional UP limited_by gas ev 0.0114 stake 3.3720 (iteration 2)
- supranational/blst: directional UP limited_by gas ev 0.0000 stake 0.0450 (iteration 2)
- ethstaker/eth-docker: directional UP limited_by gas ev 0.0048 stake 1.7380 (iteration 2)
- DefiLlama/DefiLlama-Adapters: directional DOWN limited_by gas ev 0.0455 stake 1.6449 (iteration 2)
- DefiLlama/chainlist: pair limited_by gas gain 0.0877 q 8.4437 (iteration 2)
- Certora/CertoraProver: directional UP limited_by gas ev 0.0008 stake 0.8799 (iteration 2)
- TrueBlocks/trueblocks-core: directional UP limited_by gas ev 0.0233 stake 4.9506 (iteration 2)
- EspressoSystems/jellyfish: directional UP limited_by gas ev 0.0141 stake 3.5697 (iteration 2)
- a16z/halmos: directional UP limited_by gas ev 0.0055 stake 2.3029 (iteration 2)
- succinctlabs/op-succinct: directional UP limited_by gas ev 0.0440 stake 6.0857 (iteration 2)
- NethermindEth/juno: directional UP limited_by gas ev 0.0186 stake 4.2532 (iteration 2)
- evmts/tevm-monorepo: directional DOWN limited_by gas ev 0.0203 stake 1.2431 (iteration 2)
- ethereum/consensus-specs: pair limited_by gas gain 0.0600 q 5.3476 (iteration 2)
- ethereum/eips: directional DOWN limited_by gas ev 0.0292 stake 0.7009 (iteration 2)
- ipsilon/evmone: pair limited_by gas gain 0.0336 q 5.3281 (iteration 2)
- ethereum/execution-apis: directional UP limited_by gas ev 0.0472 stake 6.9737 (iteration 2)
- ethereum/go-ethereum: directional DOWN limited_by gas ev 0.0050 stake 0.4440 (iteration 2)
- remix-project-org/remix-project: directional DOWN limited_by gas ev 0.0109 stake 0.7599 (iteration 2)
- argotorg/solidity: directional UP limited_by gas ev 0.0095 stake 3.1301 (iteration 2)
- argotorg/sourcify: directional UP limited_by gas ev 0.0080 stake 2.7058 (iteration 2)
- hyperledger/besu: directional UP limited_by gas ev 0.0434 stake 6.5259 (iteration 2)
- nethermindeth/nethermind: directional UP limited_by gas ev 0.0092 stake 2.9073 (iteration 2)
- nomicfoundation/hardhat: pair limited_by gas gain 0.0111 q 2.5954 (iteration 2)
- paradigmxyz/reth: pair limited_by gas gain 0.0530 q 5.8657 (iteration 2)
- OffchainLabs/prysm: pair limited_by gas gain 0.0941 q 7.7971 (iteration 2)
- scaffold-eth/scaffold-eth-2: directional DOWN limited_by gas ev 0.0328 stake 2.4233 (iteration 2)
- wevm/viem: directional UP limited_by gas ev 0.0128 stake 3.5904 (iteration 2)
- argotorg/act: directional UP limited_by gas ev 0.0334 stake 5.7570 (iteration 2)
- paradigmxyz/reth: directional UP limited_by gas ev 0.0372 stake 6.1077 (iteration 3)
- paradigmxyz/reth: directional DOWN limited_by gas ev 0.0193 stake 0.9065 (iteration 4)

## Class vs the candidates.json snapshot (pools[].price): 0 market(s) whose class differs

- live classes: {"set-sell":83,"sub1":9,"band":6}

## No row (skipped): 36 markets

- LFDT-web3j/web3j: spot sum 1.017807; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0506 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0000 repo tokens vs gas 0.0472
- arkworks-rs/algebra: spot sum 1.020676; p = [0.15000000000000002, 0.85, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0746 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0169 repo tokens vs gas 0.0472
- protofire/solhint: spot sum 1.016092; p = [0.25, 0.75, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0405 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0209 repo tokens vs gas 0.0472
- l2beat/l2beat: spot sum 1.016549; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0446 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0470 repo tokens vs gas 0.0472
- Vectorized/solady: spot sum 1.025626; p = [0.25, 0.75, 0]; neither side clears p(1-f) > price; set-sell dropped by step 7 (limited_by gas): ev 0.0699 repo tokens vs gas 0.3306
- flashbots/mev-boost: spot sum 1.009182; p = [0.09999999999999998, 0.9, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0181 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0000 repo tokens vs gas 0.0472
- flashbots/mev-boost-relay: spot sum 1.017228; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0471 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0000 repo tokens vs gas 0.0472
- libp2p/libp2p: spot sum 1.011330; p = [0.15000000000000002, 0.85, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0279 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0114 repo tokens vs gas 0.0472
- supranational/blst: spot sum 1.015976; p = [0.09999999999999998, 0.9, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0568 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0000 repo tokens vs gas 0.0472
- ethstaker/eth-docker: spot sum 1.009882; p = [0.4, 0.6, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0214 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0048 repo tokens vs gas 0.0472
- DefiLlama/DefiLlama-Adapters: spot sum 1.012384; p = [0.30000000000000004, 0.7, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0200 repo tokens vs gas 0.3306; directional DOWN dropped by step 7 (limited_by gas): ev 0.0455 repo tokens vs gas 0.0472
- Certora/CertoraProver: spot sum 1.000397; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0000 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0008 repo tokens vs gas 0.0472
- TrueBlocks/trueblocks-core: spot sum 1.020847; p = [0.15000000000000002, 0.85, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0635 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0233 repo tokens vs gas 0.0472
- EspressoSystems/jellyfish: spot sum 1.013611; p = [0.35, 0.65, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0170 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0141 repo tokens vs gas 0.0472
- a16z/halmos: spot sum 1.019159; p = [0.25, 0.75, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0481 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0055 repo tokens vs gas 0.0472
- succinctlabs/op-succinct: spot sum 1.012469; p = [0.4, 0.6, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0169 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0440 repo tokens vs gas 0.0472
- NethermindEth/juno: spot sum 1.014507; p = [0.25, 0.75, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0264 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0186 repo tokens vs gas 0.0472
- evmts/tevm-monorepo: spot sum 1.019073; p = [0.35, 0.65, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0454 repo tokens vs gas 0.3306; directional DOWN dropped by step 7 (limited_by gas): ev 0.0203 repo tokens vs gas 0.0472
- aestus-relay/mev-boost-relay: spot sum 1.028996; p = [0.30000000000000004, 0.7, 0]; neither side clears p(1-f) > price; set-sell dropped by step 7 (limited_by gas): ev 0.0602 repo tokens vs gas 0.3306
- risc0/risc0-ethereum: spot sum 1.018464; p = [0.30000000000000004, 0.7, 0]; neither side clears p(1-f) > price; set-sell dropped by step 7 (limited_by gas): ev 0.0652 repo tokens vs gas 0.3306
- chainsafe/lodestar: spot sum 0.999959; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; sum within [1-f, 1/(1-f)] so neither 3a nor 3b applies; directional UP dropped by step 7 (limited_by gas): ev 0.0380 repo tokens vs gas 0.0472
- ethereum/eips: spot sum 1.000431; p = [0.09999999999999998, 0.9, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0000 repo tokens vs gas 0.3306; directional DOWN dropped by step 7 (limited_by gas): ev 0.0292 repo tokens vs gas 0.0472
- ethereum/execution-apis: spot sum 1.018564; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0272 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0472 repo tokens vs gas 0.0472
- ethereum/go-ethereum: spot sum 0.998089; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; pair dropped by step 7 (limited_by gas): gain 0.0005 repo tokens vs gas 0.0945; directional DOWN dropped by step 7 (limited_by gas): ev 0.0050 repo tokens vs gas 0.0472
- remix-project-org/remix-project: spot sum 1.009470; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0161 repo tokens vs gas 0.3306; directional DOWN dropped by step 7 (limited_by gas): ev 0.0109 repo tokens vs gas 0.0472
- argotorg/solidity: spot sum 1.019836; p = [0.15000000000000002, 0.85, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0713 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0095 repo tokens vs gas 0.0472
- argotorg/sourcify: spot sum 1.000301; p = [0.25, 0.75, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0000 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0080 repo tokens vs gas 0.0472
- ethereum/web3.py: spot sum 0.999948; p = [0.30000000000000004, 0.7, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; sum within [1-f, 1/(1-f)] so neither 3a nor 3b applies; directional DOWN dropped by step 7 (limited_by gas): ev 0.0429 repo tokens vs gas 0.0472
- hyperledger/besu: spot sum 1.013908; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0332 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0434 repo tokens vs gas 0.0472
- nethermindeth/nethermind: spot sum 1.011664; p = [0.25, 0.75, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0249 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0092 repo tokens vs gas 0.0472
- paradigmxyz/reth: spot sum 0.981979; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; merge-arb dropped by step 7 (limited_by gas): ev 0.0530 repo tokens vs gas 0.3306; pair dropped by step 7 (limited_by gas): gain 0.0530 repo tokens vs gas 0.0945; directional UP dropped by step 7 (limited_by gas): ev 0.0372 repo tokens vs gas 0.0472; directional DOWN dropped by step 7 (limited_by gas): ev 0.0193 repo tokens vs gas 0.0472
- scaffold-eth/scaffold-eth-2: spot sum 1.009923; p = [0.35, 0.65, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0200 repo tokens vs gas 0.3306; directional DOWN dropped by step 7 (limited_by gas): ev 0.0328 repo tokens vs gas 0.0472
- vyperlang/vyper: spot sum 1.002189; p = [0.19999999999999996, 0.8, 0]; neither side clears p(1-f) > price; set-sell dropped by step 7 (limited_by gas): ev 0.0006 repo tokens vs gas 0.3306
- wevm/viem: spot sum 1.029943; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.1260 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0128 repo tokens vs gas 0.0472
- argotorg/act: spot sum 1.019366; p = [0.19999999999999996, 0.8, 0]; no side clears p(1-f) > price at the final prices except the directional row(s) dropped by step 7 below; set-sell dropped by step 7 (limited_by gas): ev 0.0594 repo tokens vs gas 0.3306; directional UP dropped by step 7 (limited_by gas): ev 0.0334 repo tokens vs gas 0.0472
- ethpandaops/ethereum-package: spot sum 1.028659; p = [0.35, 0.65, 0]; neither side clears p(1-f) > price; set-sell dropped by step 7 (limited_by gas): ev 0.1252 repo tokens vs gas 0.3306

**Totals:** 69 rows over 62 markets; sum ev = 49.3952 repo tokens (different tokens per market) => expected_value 0.504032 sUSDS at 1/98.
