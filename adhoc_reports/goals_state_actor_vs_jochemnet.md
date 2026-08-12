# Goals — state-actor stateful suite vs. jochemnet (committed latest)

Ad-hoc comparison, not part of the generated site. Both runs share the same
compute suite (`3c6dc791050b116d`), fit.yaml, and 2026-08-09→2026-08-12 data
window, and differ only in the stateful suite:

- **jochemnet** (currently committed latest, `data/runs/20260812T052044Z_3c6dc791050b116d`) — suite `0d93b5bf3b970403`.
- **state-actor** (throwaway alt run, not archived) — suite `3f6a0898955dff4f`.

`ethrex` is excluded from both tables: it has no jochemnet fit at all, so there's
nothing to diff it against.

Anchor rate: 100 Mgas/s for both. Values are the same "effective" numbers the
Goals page shows — write goals have the bundled cold-access component
subtracted and are floored at 0. ✅ = clears the goal, ❌ = fails it.

## 1. Goals — per-client detail (state-actor suite)

| Goal | besu | erigon | geth | nethermind | reth |
|---|---|---|---|---|---|
| **COLD_STORAGE_ACCESS** (goal 2,100) | 1,627 ✅ | 649 ✅ | 2,149 ❌ | 819 ✅ | 407 ✅ |
| **STORAGE_WRITE** (goal 8,000) | 8,275 ❌ | 20,595 ❌ | 13,408 ❌ | 4,833 ✅ | 1,570 ✅ |
| **COLD_ACCOUNT_ACCESS (CODE)** (goal 3,000) | 4,635 ❌ | 14,598 ❌ | 4,182 ❌ | 2,754 ✅ | 2,304 ✅ |
| **COLD_ACCOUNT_ACCESS (NOCODE)** (goal 3,000) | 3,566 ❌ | 928 ✅ | 2,141 ✅ | 965 ✅ | 492 ✅ |
| **ACCOUNT_WRITE (CODE)** (goal 9,000) | 9,016 ❌ | 24,427 ❌ | 10,116 ❌ | 4,275 ✅ | 2,663 ✅ |
| **ACCOUNT_WRITE (NOCODE)** (goal 9,000) | 13,111 ❌ | 24,214 ❌ | 13,411 ❌ | 6,547 ✅ | 2,024 ✅ |
| **WARM_ACCESS** (goal 100) | 48 ✅ | 11 ✅ | 19 ✅ | 42 ✅ | 6 ✅ |

*(`COLD_ACCOUNT_ACCESS` and `ACCOUNT_WRITE` require both the CODE and NOCODE row to clear — e.g. erigon fails `COLD_ACCOUNT_ACCESS` overall because CODE fails even though NOCODE passes.)*

## 2. Diff vs. jochemnet (% change, state-actor vs. jochemnet)

| Goal | besu | erigon | geth | nethermind | reth |
|---|---|---|---|---|---|
| **COLD_STORAGE_ACCESS** | +7% | +2% | -6% | +5% | +171% |
| **STORAGE_WRITE** | +0% | +41% | +11% | +15% | +1% |
| **COLD_ACCOUNT_ACCESS (CODE)** | +106% | +6% | +88% | +64% | +7% |
| **COLD_ACCOUNT_ACCESS (NOCODE)** | +100% | +5% | -4% | +146% | +202% |
| **ACCOUNT_WRITE (CODE)** | +105% | +88% | +352% | +92% | +20% |
| **ACCOUNT_WRITE (NOCODE)** | +9% | -7% | +47% | +13% | +41% |
| **WARM_ACCESS** | +500% | +22% | +6% | -7% | -14% |

## Key takeaways

- **`COLD_STORAGE_ACCESS`, `STORAGE_WRITE`, and `WARM_ACCESS` are suite-insensitive.** Clearing counts are identical between suites (4/5, 2/5, 5/5) and the same clients pass/fail in each — the biggest single moves are reth's `COLD_STORAGE_ACCESS` (+171%) and besu's `WARM_ACCESS` (+500%), but both stay far under their goals either way.
- **`COLD_ACCOUNT_ACCESS` is the one goal that actually flips.** besu and geth clear it under jochemnet (4/5 clearing) but fail it under state-actor (2/5 clearing) — both flip because their CODE variant crosses the 3,000 goal (besu +106%, geth +88%).
- **`ACCOUNT_WRITE`'s overall clearing count is unchanged (2/5 under both, only nethermind and reth clear) — but that hides a real shift.** besu's and geth's `ACCOUNT_WRITE (CODE)` variant also flips from pass to fail under state-actor; it just doesn't move the combined result because their NOCODE variant was already failing under jochemnet.
- **erigon fails both `COLD_ACCOUNT_ACCESS` and `ACCOUNT_WRITE` under either suite** — its account-cost estimates are consistently far over goal regardless of which stateful suite is used.
- **Net effect:** the `COLD_ACCOUNT_*`/`ACCOUNT_WRITE` family is far more sensitive to the choice of stateful suite than `COLD_STORAGE_*`/`WARM_ACCESS` — worth treating those account-cost estimates as less settled before locking in goal targets or picking a suite to commit to.
