# Goals — anchor-rate sweep (20260922T091625Z_22c2404b9ce3f47c)

Ad-hoc what-if, not part of the generated site. One Goals-page *Per-client detail* table per candidate `anchor_rate`, all from the committed latest run `data/runs/20260922T091625Z_22c2404b9ce3f47c` — the 100 Mgas/s table is what the live page shows, the rest are hypotheticals.

Gas scales linearly with the anchor: `new_gas = runtime_ms × anchor_rate`, verified exact (<1e-11) over all 389 candidate fits in `new_gas_all_params.csv`, and `new_gas_rounded` is a ceiling. The glue adjustment is a measured runtime subtraction and the worst-case selector compares runtimes, so neither moves with the anchor — the winning model combo per (param, client) is identical at every rate below. So each table is `ceil(new_gas_decimal × rate/100)`, re-derived from the decimals rather than rescaling the rounded values.

The **goal targets do not scale** (`GOAL_SPECS` in `scripts/build_site.py`), and neither does the access component subtracted from the write goals. Lowering the anchor therefore only moves the estimates: each table reads "at this throughput goal, can clients hit these fixed costs?"

Values are the Goals page's effective numbers — write goals have the bundled cold-access component subtracted (`STORAGE_WRITE` − 2,100, `ACCOUNT_WRITE` − 3,000) and are floored at 0. Marks follow the page's three cell colours: ✅ clears (green), ⚠️ fails by up to 100% over goal (yellow), ❌ fails by more than 100% over (red). `COLD_ACCOUNT_ACCESS` and `ACCOUNT_WRITE` require *both* the CODE and NOCODE row to clear.

## 1. 100 Mgas/s — current, as rendered on the live page

| Goal | besu | erigon | ethrex | geth | nethermind | reth |
|---|---|---|---|---|---|---|
| **COLD_STORAGE_ACCESS** (goal 2,100) | 2,894 ⚠️ | 384 ✅ | 736 ✅ | 2,232 ⚠️ | 764 ✅ | 547 ✅ |
| **STORAGE_WRITE** (goal 10,000) | 12,579 ⚠️ | 14,639 ⚠️ | 343 ✅ | 11,751 ⚠️ | 3,081 ✅ | 9,374 ✅ |
| **COLD_ACCOUNT_ACCESS (CODE)** (goal 3,000) | 3,522 ⚠️ | 1,570 ✅ | 1,149 ✅ | 4,628 ⚠️ | 348 ✅ | 519 ✅ |
| **COLD_ACCOUNT_ACCESS (NOCODE)** (goal 3,000) | 2,414 ✅ | 447 ✅ | 927 ✅ | 2,225 ✅ | 363 ✅ | 538 ✅ |
| **ACCOUNT_WRITE (CODE)** (goal 9,000) | 9,272 ⚠️ | 4,435 ✅ | 77 ✅ | 12,455 ⚠️ | 2,858 ✅ | 9,974 ⚠️ |
| **ACCOUNT_WRITE (NOCODE)** (goal 9,000) | 20,993 ❌ | 16,897 ⚠️ | 642 ✅ | 9,440 ⚠️ | 6,031 ✅ | 11,617 ⚠️ |
| **WARM_ACCESS** (goal 100) | 96 ✅ | 9 ✅ | 13 ✅ | 23 ✅ | 32 ✅ | 7 ✅ |

Raw estimates behind the write rows (pre-subtraction): `COLD_STORAGE_WRITE` besu 14,679 / erigon 16,739 / ethrex 2,443 / geth 13,851 / nethermind 5,181 / reth 11,474; `COLD_ACCOUNT_CODE_WRITE` besu 12,272 / erigon 7,435 / ethrex 3,077 / geth 15,455 / nethermind 5,858 / reth 12,974; `COLD_ACCOUNT_NOCODE_WRITE` besu 23,993 / erigon 19,897 / ethrex 3,642 / geth 12,440 / nethermind 9,031 / reth 14,617.

## 2. 75 Mgas/s

| Goal | besu | erigon | ethrex | geth | nethermind | reth |
|---|---|---|---|---|---|---|
| **COLD_STORAGE_ACCESS** (goal 2,100) | 2,171 ⚠️ | 288 ✅ | 552 ✅ | 1,674 ✅ | 573 ✅ | 411 ✅ |
| **STORAGE_WRITE** (goal 10,000) | 8,909 ✅ | 10,454 ⚠️ | 0 ✅ | 8,289 ✅ | 1,786 ✅ | 6,505 ✅ |
| **COLD_ACCOUNT_ACCESS (CODE)** (goal 3,000) | 2,642 ✅ | 1,178 ✅ | 862 ✅ | 3,471 ⚠️ | 261 ✅ | 389 ✅ |
| **COLD_ACCOUNT_ACCESS (NOCODE)** (goal 3,000) | 1,811 ✅ | 335 ✅ | 695 ✅ | 1,669 ✅ | 272 ✅ | 404 ✅ |
| **ACCOUNT_WRITE (CODE)** (goal 9,000) | 6,204 ✅ | 2,577 ✅ | 0 ✅ | 8,591 ✅ | 1,393 ✅ | 6,731 ✅ |
| **ACCOUNT_WRITE (NOCODE)** (goal 9,000) | 14,995 ⚠️ | 11,923 ⚠️ | 0 ✅ | 6,330 ✅ | 3,774 ✅ | 7,963 ✅ |
| **WARM_ACCESS** (goal 100) | 72 ✅ | 7 ✅ | 10 ✅ | 18 ✅ | 24 ✅ | 5 ✅ |

Raw estimates behind the write rows (pre-subtraction): `COLD_STORAGE_WRITE` besu 11,009 / erigon 12,554 / ethrex 1,832 / geth 10,389 / nethermind 3,886 / reth 8,605; `COLD_ACCOUNT_CODE_WRITE` besu 9,204 / erigon 5,577 / ethrex 2,308 / geth 11,591 / nethermind 4,393 / reth 9,731; `COLD_ACCOUNT_NOCODE_WRITE` besu 17,995 / erigon 14,923 / ethrex 2,732 / geth 9,330 / nethermind 6,774 / reth 10,963.

## 3. 60 Mgas/s

| Goal | besu | erigon | ethrex | geth | nethermind | reth |
|---|---|---|---|---|---|---|
| **COLD_STORAGE_ACCESS** (goal 2,100) | 1,737 ✅ | 231 ✅ | 442 ✅ | 1,340 ✅ | 459 ✅ | 329 ✅ |
| **STORAGE_WRITE** (goal 10,000) | 6,707 ✅ | 7,943 ✅ | 0 ✅ | 6,211 ✅ | 1,009 ✅ | 4,784 ✅ |
| **COLD_ACCOUNT_ACCESS (CODE)** (goal 3,000) | 2,114 ✅ | 942 ✅ | 690 ✅ | 2,777 ✅ | 209 ✅ | 311 ✅ |
| **COLD_ACCOUNT_ACCESS (NOCODE)** (goal 3,000) | 1,449 ✅ | 268 ✅ | 556 ✅ | 1,335 ✅ | 218 ✅ | 323 ✅ |
| **ACCOUNT_WRITE (CODE)** (goal 9,000) | 4,363 ✅ | 1,461 ✅ | 0 ✅ | 6,273 ✅ | 515 ✅ | 4,785 ✅ |
| **ACCOUNT_WRITE (NOCODE)** (goal 9,000) | 11,396 ⚠️ | 8,938 ✅ | 0 ✅ | 4,464 ✅ | 2,419 ✅ | 5,770 ✅ |
| **WARM_ACCESS** (goal 100) | 58 ✅ | 6 ✅ | 8 ✅ | 14 ✅ | 19 ✅ | 4 ✅ |

Raw estimates behind the write rows (pre-subtraction): `COLD_STORAGE_WRITE` besu 8,807 / erigon 10,043 / ethrex 1,466 / geth 8,311 / nethermind 3,109 / reth 6,884; `COLD_ACCOUNT_CODE_WRITE` besu 7,363 / erigon 4,461 / ethrex 1,846 / geth 9,273 / nethermind 3,515 / reth 7,785; `COLD_ACCOUNT_NOCODE_WRITE` besu 14,396 / erigon 11,938 / ethrex 2,186 / geth 7,464 / nethermind 5,419 / reth 8,770.

## 4. 50 Mgas/s

| Goal | besu | erigon | ethrex | geth | nethermind | reth |
|---|---|---|---|---|---|---|
| **COLD_STORAGE_ACCESS** (goal 2,100) | 1,447 ✅ | 192 ✅ | 368 ✅ | 1,116 ✅ | 382 ✅ | 274 ✅ |
| **STORAGE_WRITE** (goal 10,000) | 5,240 ✅ | 6,270 ✅ | 0 ✅ | 4,826 ✅ | 491 ✅ | 3,637 ✅ |
| **COLD_ACCOUNT_ACCESS (CODE)** (goal 3,000) | 1,761 ✅ | 785 ✅ | 575 ✅ | 2,314 ✅ | 174 ✅ | 260 ✅ |
| **COLD_ACCOUNT_ACCESS (NOCODE)** (goal 3,000) | 1,207 ✅ | 224 ✅ | 464 ✅ | 1,113 ✅ | 182 ✅ | 269 ✅ |
| **ACCOUNT_WRITE (CODE)** (goal 9,000) | 3,136 ✅ | 718 ✅ | 0 ✅ | 4,728 ✅ | 0 ✅ | 3,487 ✅ |
| **ACCOUNT_WRITE (NOCODE)** (goal 9,000) | 8,997 ✅ | 6,949 ✅ | 0 ✅ | 3,220 ✅ | 1,516 ✅ | 4,309 ✅ |
| **WARM_ACCESS** (goal 100) | 48 ✅ | 5 ✅ | 7 ✅ | 12 ✅ | 16 ✅ | 4 ✅ |

Raw estimates behind the write rows (pre-subtraction): `COLD_STORAGE_WRITE` besu 7,340 / erigon 8,370 / ethrex 1,222 / geth 6,926 / nethermind 2,591 / reth 5,737; `COLD_ACCOUNT_CODE_WRITE` besu 6,136 / erigon 3,718 / ethrex 1,539 / geth 7,728 / nethermind 2,929 / reth 6,487; `COLD_ACCOUNT_NOCODE_WRITE` besu 11,997 / erigon 9,949 / ethrex 1,821 / geth 6,220 / nethermind 4,516 / reth 7,309.

## 5. Clients clearing, by anchor rate

| Goal | 100 Mgas/s | 75 Mgas/s | 60 Mgas/s | 50 Mgas/s |
|---|---|---|---|---|
| **COLD_STORAGE_ACCESS** (goal 2,100) | 4 / 6 | 5 / 6 | 6 / 6 | 6 / 6 |
| **STORAGE_WRITE** (goal 10,000) | 3 / 6 | 5 / 6 | 6 / 6 | 6 / 6 |
| **COLD_ACCOUNT_ACCESS** (goal 3,000) | 4 / 6 | 5 / 6 | 6 / 6 | 6 / 6 |
| **ACCOUNT_WRITE** (goal 9,000) | 2 / 6 | 4 / 6 | 5 / 6 | 6 / 6 |
| **WARM_ACCESS** (goal 100) | 6 / 6 | 6 / 6 | 6 / 6 | 6 / 6 |

## 6. Highest anchor rate at which each client clears

The rate where a cell lands exactly on its goal, from `rate = 100 × (goal + subtract) / new_gas_decimal` (the binding variant for the two-variant goals). A client clears the goal at this rate and every rate below it; `>100` means it already clears at the live 100 Mgas/s anchor. Ignores the ceiling, so treat these as ±0.1 Mgas/s.

| Goal | besu | erigon | ethrex | geth | nethermind | reth |
|---|---|---|---|---|---|---|
| **COLD_STORAGE_ACCESS** (goal 2,100) | 72.6 | >100 | >100 | 94.1 | >100 | >100 |
| **STORAGE_WRITE** (goal 10,000) | 82.4 | 72.3 | >100 | 87.4 | >100 | >100 |
| **COLD_ACCOUNT_ACCESS** (goal 3,000) | 85.2 | >100 | >100 | 64.8 | >100 | >100 |
| **ACCOUNT_WRITE** (goal 9,000) | 50.0 | 60.3 | >100 | 77.6 | >100 | 82.1 |
| **WARM_ACCESS** (goal 100) | >100 | >100 | >100 | >100 | >100 | >100 |

Two readings worth pulling out:

- **besu `ACCOUNT_WRITE` (NOCODE) is the binding cell on the whole page** at every rate from 100 down to ~50: `COLD_ACCOUNT_NOCODE_WRITE` 23,993 at 100 Mgas/s, so it needs 50.0 Mgas/s to reach the 9,000 goal. 50 Mgas/s is essentially the exact rate at which the table first goes all-green (8,997 vs 9,000 — a 3-gas margin); at 60 Mgas/s it is the single remaining failure anywhere on the page.
- **The floor-at-0 artifact grows as the anchor drops.** ethrex's bundled write estimates fall below the *fixed* access targets subtracted from them, so its write cells read 0 and "clear" for an arithmetic reason rather than a measured one — one variant at 100 Mgas/s, all three by 75, with nethermind joining on `ACCOUNT_WRITE` (CODE) at 50. Below ~60 Mgas/s the write rows say noticeably less about client performance than the access rows do.
