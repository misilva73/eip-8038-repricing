# New gas proposal

_Generated 2026-08-03 08:22:26Z · fork `osaka` · anchor_rate 75 Mgas/s_

**Summary:** 12 parameters proposed — 8 increased, 4 decreased, 0 new, 0 unresolved · 4 warnings · 1 poor-fit selection

## Contents

- [Proposed parameters](#proposed-gas-parameters)
- [Client comparison](#client-comparison)
- [Worst-case provenance](#worst-case-provenance-per-gas-param)
- [Warnings](#warnings)
- [Poor-fit selections](#poor-fit-selections)

## Proposed gas parameters

| Gas param | Current gas | Proposed gas | Diff | Diff % |
| --- | --- | --- | --- | --- |
| COLD_STORAGE_ACCESS | 2100 | 1615 | -485 | -23% |
| COLD_STORAGE_WRITE | 5000 | 17371 | +12371 | +247% |
| WARM_ACCESS | 100 | 37 | -63 | -63% |
| COLD_ACCOUNT_NOCODE_ACCESS | 2600 | 2544 | -56 | -2% |
| COLD_ACCOUNT_NOCODE_WRITE | 9300 | 20589 | +11289 | +121% |
| COLD_ACCOUNT_CODE_ACCESS | 2600 | 11682 | +9082 | +349% |
| COLD_ACCOUNT_CODE_WRITE | 9300 | 21555 | +12255 | +132% |
| STORAGE_WRITE | 2800 | 15756 | +12956 | +463% |
| ACCOUNT_WRITE | 6700 | 18045 | +11345 | +169% |
| REFUND_STORAGE_CLEAR | 4800 | 16677 | +11877 | +247% |
| TX_ACCESS_LIST_STORAGE_KEY | 1900 | 1615 | -285 | -15% |
| TX_ACCESS_LIST_ADDRESS | 2400 | 11682 | +9282 | +387% |

## Client comparison

Worst client vs. second-worst client per gas parameter. The `Ratio` column is `worst gas / second-worst gas` — values close to 1× mean the worst case sits next to the rest of the field, while large ratios flag the worst client as an outlier.

| Gas param | Worst client | Worst gas | Second-worst client | Second-worst gas | Ratio |
| --- | --- | --- | --- | --- | --- |
| COLD_STORAGE_ACCESS | geth | 1615 | besu | 1489 | 1.08× |
| COLD_STORAGE_WRITE | erigon | 17371 | besu | 10354 | 1.68× |
| WARM_ACCESS | nethermind | 37 | besu | 34 | 1.09× |
| COLD_ACCOUNT_NOCODE_ACCESS | besu | 2544 | geth | 1621 | 1.57× |
| COLD_ACCOUNT_NOCODE_WRITE | erigon | 20589 | besu | 13426 | 1.53× |
| COLD_ACCOUNT_CODE_ACCESS | erigon | 11682 | ethrex | 7680 | 1.52× |
| COLD_ACCOUNT_CODE_WRITE | erigon | 21555 | besu | 13426 | 1.61× |

Per-client proposed gas for each parameter. Cells are colored by `log2(proposed / current)` — red means the proposal is more expensive than the current gas cost, green means cheaper, and white sits at unchanged. Annotations show the absolute proposed gas value; blank rows are parameters with no prior baseline (see warnings below).

![](figs/proposal/heatmap.png)

## Worst-case provenance per gas param

One collapsible block per gas parameter showing every per-client candidate that the worst-case selector saw. Rows are model combos (the source regression's `test_name`, `target_opcode`, `model_coef_name`, and any `model_by` factors — components constant within a parameter are dropped from the label). Cells carry each candidate's proposed gas; the cell the per-client selector picked is outlined in black. Colors are `log2(proposed / current)` against that parameter's baseline on a per-parameter symmetric scale.

<details>
<summary><code>COLD_STORAGE_ACCESS</code> — 4 combos × 6 clients</summary>

![](figs/proposal/provenance__COLD_STORAGE_ACCESS.png)

</details>

<details>
<summary><code>COLD_STORAGE_WRITE</code> — 2 combos × 6 clients</summary>

![](figs/proposal/provenance__COLD_STORAGE_WRITE.png)

</details>

<details>
<summary><code>WARM_ACCESS</code> — 8 combos × 6 clients</summary>

| Label | Combo |
| --- | --- |
| `M1` | test_name=test_ext_account_query_warm / target_opcode=BALANCE / model_coef_name=target_coef / param_opcode=BALANCE |
| `M2` | test_name=test_ext_account_query_warm / target_opcode=CALL / model_coef_name=target_coef / param_opcode=CALL |
| `M3` | test_name=test_ext_account_query_warm / target_opcode=CALLCODE / model_coef_name=target_coef / param_opcode=CALLCODE |
| `M4` | test_name=test_ext_account_query_warm / target_opcode=DELEGATECALL / model_coef_name=target_coef / param_opcode=DELEGATECALL |
| `M5` | test_name=test_ext_account_query_warm / target_opcode=EXTCODEHASH / model_coef_name=target_coef / param_opcode=EXTCODEHASH |
| `M6` | test_name=test_ext_account_query_warm / target_opcode=EXTCODESIZE / model_coef_name=target_coef / param_opcode=EXTCODESIZE |
| `M7` | test_name=test_ext_account_query_warm / target_opcode=STATICCALL / model_coef_name=target_coef / param_opcode=STATICCALL |
| `M8` | test_name=test_sload_same_key_benchmark / target_opcode=SLOAD / model_coef_name=target_coef |

![](figs/proposal/provenance__WARM_ACCESS.png)

</details>

<details>
<summary><code>COLD_ACCOUNT_NOCODE_ACCESS</code> — 16 combos × 6 clients</summary>

| Label | Combo |
| --- | --- |
| `M1` | test_name=test_account_access / target_opcode=BALANCE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=BALANCE |
| `M2` | test_name=test_account_access / target_opcode=BALANCE / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=BALANCE |
| `M3` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=CALL |
| `M4` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=CALL |
| `M5` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=CALLCODE |
| `M6` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=CALLCODE |
| `M7` | test_name=test_account_access / target_opcode=DELEGATECALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=DELEGATECALL |
| `M8` | test_name=test_account_access / target_opcode=DELEGATECALL / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=DELEGATECALL |
| `M9` | test_name=test_account_access / target_opcode=EXTCODECOPY / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=EXTCODECOPY |
| `M10` | test_name=test_account_access / target_opcode=EXTCODECOPY / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=EXTCODECOPY |
| `M11` | test_name=test_account_access / target_opcode=EXTCODEHASH / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=EXTCODEHASH |
| `M12` | test_name=test_account_access / target_opcode=EXTCODEHASH / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=EXTCODEHASH |
| `M13` | test_name=test_account_access / target_opcode=EXTCODESIZE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=EXTCODESIZE |
| `M14` | test_name=test_account_access / target_opcode=EXTCODESIZE / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=EXTCODESIZE |
| `M15` | test_name=test_account_access / target_opcode=STATICCALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=STATICCALL |
| `M16` | test_name=test_account_access / target_opcode=STATICCALL / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=STATICCALL |

![](figs/proposal/provenance__COLD_ACCOUNT_NOCODE_ACCESS.png)

</details>

<details>
<summary><code>COLD_ACCOUNT_NOCODE_WRITE</code> — 4 combos × 6 clients</summary>

| Label | Combo |
| --- | --- |
| `M1` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=CALL |
| `M2` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=CALL |
| `M3` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=CALLCODE |
| `M4` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=CALLCODE |

![](figs/proposal/provenance__COLD_ACCOUNT_NOCODE_WRITE.png)

</details>

<details>
<summary><code>COLD_ACCOUNT_CODE_ACCESS</code> — 32 combos × 6 clients</summary>

| Label | Combo |
| --- | --- |
| `M1` | test_name=test_account_access / target_opcode=BALANCE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX / param_opcode=BALANCE |
| `M2` | test_name=test_account_access / target_opcode=BALANCE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL / param_opcode=BALANCE |
| `M3` | test_name=test_account_access / target_opcode=BALANCE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX / param_opcode=BALANCE |
| `M4` | test_name=test_account_access / target_opcode=BALANCE / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=BALANCE |
| `M5` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX / param_opcode=CALL |
| `M6` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL / param_opcode=CALL |
| `M7` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX / param_opcode=CALL |
| `M8` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=CALL |
| `M9` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX / param_opcode=CALLCODE |
| `M10` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL / param_opcode=CALLCODE |
| `M11` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX / param_opcode=CALLCODE |
| `M12` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=CALLCODE |
| `M13` | test_name=test_account_access / target_opcode=DELEGATECALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX / param_opcode=DELEGATECALL |
| `M14` | test_name=test_account_access / target_opcode=DELEGATECALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL / param_opcode=DELEGATECALL |
| `M15` | test_name=test_account_access / target_opcode=DELEGATECALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX / param_opcode=DELEGATECALL |
| `M16` | test_name=test_account_access / target_opcode=DELEGATECALL / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=DELEGATECALL |
| `M17` | test_name=test_account_access / target_opcode=EXTCODECOPY / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX / param_opcode=EXTCODECOPY |
| `M18` | test_name=test_account_access / target_opcode=EXTCODECOPY / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL / param_opcode=EXTCODECOPY |
| `M19` | test_name=test_account_access / target_opcode=EXTCODECOPY / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX / param_opcode=EXTCODECOPY |
| `M20` | test_name=test_account_access / target_opcode=EXTCODECOPY / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=EXTCODECOPY |
| `M21` | test_name=test_account_access / target_opcode=EXTCODEHASH / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX / param_opcode=EXTCODEHASH |
| `M22` | test_name=test_account_access / target_opcode=EXTCODEHASH / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL / param_opcode=EXTCODEHASH |
| `M23` | test_name=test_account_access / target_opcode=EXTCODEHASH / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX / param_opcode=EXTCODEHASH |
| `M24` | test_name=test_account_access / target_opcode=EXTCODEHASH / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=EXTCODEHASH |
| `M25` | test_name=test_account_access / target_opcode=EXTCODESIZE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX / param_opcode=EXTCODESIZE |
| `M26` | test_name=test_account_access / target_opcode=EXTCODESIZE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL / param_opcode=EXTCODESIZE |
| `M27` | test_name=test_account_access / target_opcode=EXTCODESIZE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX / param_opcode=EXTCODESIZE |
| `M28` | test_name=test_account_access / target_opcode=EXTCODESIZE / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=EXTCODESIZE |
| `M29` | test_name=test_account_access / target_opcode=STATICCALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX / param_opcode=STATICCALL |
| `M30` | test_name=test_account_access / target_opcode=STATICCALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL / param_opcode=STATICCALL |
| `M31` | test_name=test_account_access / target_opcode=STATICCALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX / param_opcode=STATICCALL |
| `M32` | test_name=test_account_access / target_opcode=STATICCALL / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=STATICCALL |

![](figs/proposal/provenance__COLD_ACCOUNT_CODE_ACCESS.png)

</details>

<details>
<summary><code>COLD_ACCOUNT_CODE_WRITE</code> — 8 combos × 6 clients</summary>

| Label | Combo |
| --- | --- |
| `M1` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX / param_opcode=CALL |
| `M2` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL / param_opcode=CALL |
| `M3` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX / param_opcode=CALL |
| `M4` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=CALL |
| `M5` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX / param_opcode=CALLCODE |
| `M6` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL / param_opcode=CALLCODE |
| `M7` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX / param_opcode=CALLCODE |
| `M8` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=CALLCODE |

![](figs/proposal/provenance__COLD_ACCOUNT_CODE_WRITE.png)

</details>

## Warnings

### Missing parameters

_None._

### Incomplete client coverage

_None._

### Missing glue adjustments

<details>
<summary><b>Non-priced opcodes correlated with the target opcount</b> — 1 test affected</summary>

The target coefficient was left unadjusted for these. Consider adding them to the glue model or re-designing the test to isolate the target opcode.

| Test name | Non-priced opcodes |
| --- | --- |
| `test_account_access` | `SHA3` |

</details>

<details>
<summary><b>Priced glue opcodes with a poor fit</b> — 142 (glue_opcode, client) fits skipped</summary>

`p_value >= glue_contribution_p_value_threshold` (0.05) or `rsquared < glue_contribution_rsquared_threshold` (0.5) — the contribution of these (glue_opcode, client) fits was **skipped** when computing the glue adjustment, so the listed gas params carry a target coefficient that is not net of this glue opcode's runtime on the affected clients. See `glue_opcodes_autogenerated_report.md` for per-fit metrics.

| Glue opcode | Affected clients | Affected gas params |
| --- | --- | --- |
| `ADD` | `besu` (both), `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE` |
| `AND` | `besu` (both), `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | — |
| `CALLDATACOPY` | `besu` (both), `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | — |
| `CALLDATALOAD` | `besu` (both), `erigon` (R²), `ethrex` (R²), `geth` (R²), `nethermind` (R²), `reth` (both) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE` |
| `CALLDATASIZE` | `erigon` (R²), `geth` (R²), `reth` (R²) | — |
| `DIV` | `besu` (both), `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | — |
| `DUP` | `besu` (p-value), `erigon` (both), `ethrex` (p-value), `geth` (both), `nethermind` (p-value), `reth` (both) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE` |
| `EXP` | `nethermind` (both) | — |
| `GAS` | `erigon` (R²), `geth` (R²), `reth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS`, `WARM_ACCESS` |
| `GT` | `besu` (both), `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS` |
| `ISZERO` | `besu` (both), `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | — |
| `JUMP` | `besu` (both), `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | — |
| `JUMPDEST` | `besu` (both), `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE` |
| `JUMPI` | `besu` (both), `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE` |
| `LT` | `besu` (both), `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE` |
| `MLOAD` | `erigon` (R²), `geth` (R²), `reth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `WARM_ACCESS` |
| `MSTORE` | `besu` (both), `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE` |
| `MSTORE8` | `besu` (both), `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE` |
| `MUL` | `besu` (both), `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | — |
| `PC` | `besu` (R²), `ethrex` (R²), `geth` (R²), `nethermind` (R²), `reth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS` |
| `PUSH` | `besu` (p-value), `erigon` (both), `ethrex` (p-value), `geth` (both), `nethermind` (p-value), `reth` (both) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE`, `WARM_ACCESS` |
| `PUSH0` | `besu` (p-value), `erigon` (both), `geth` (both), `reth` (R²) | — |
| `RETURNDATASIZE` | `besu` (R²), `erigon` (R²), `ethrex` (R²), `geth` (R²), `nethermind` (R²), `reth` (R²) | — |
| `SELFBALANCE` | `besu` (both), `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | — |
| `STATICCALL` | `erigon` (both), `geth` (R²), `reth` (R²) | — |
| `SUB` | `besu` (both), `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS` |
| `SWAP` | `besu` (both), `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE` |

</details>

### Other

- derived: 'REFUND_STORAGE_CLEAR' shadows a raw fork field on 'osaka'
- derived: 'TX_ACCESS_LIST_STORAGE_KEY' shadows a raw fork field on 'osaka'
- derived: 'TX_ACCESS_LIST_ADDRESS' shadows a raw fork field on 'osaka'

## Poor-fit selections

Rows where the winning fit's p-value exceeded `modeling.poor_fit_p_value_threshold` (0.05) or its R² fell below `modeling.poor_fit_rsquared_threshold` (0.5). The failing threshold(s) are noted alongside each row; selections in `### Winners with poor fit` still drive the proposal, while `### Other weak candidates` lists losing candidates that the selector dropped in favor of a qualified alternative. See `runtime_estimation_autogenerated_report.md` for per-fit `runtime_ms`, `pvalue`, and `rsquared` metrics.

### Winners with poor fit

| Gas param | Client | Test | Target opcode | Coef | runtime_ms | pvalue | rsquared | Failed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `COLD_STORAGE_WRITE` | `ethrex` | `test_sstore_bloated` | `SSTORE` | `target_coef` | 0.01003 | 0.001 | 0.2401 | R² |

### Other weak candidates

<details>
<summary><code>COLD_STORAGE_WRITE</code> — 1 weak combo</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_sstore_bloated` | `SSTORE` | `target_coef` | — | `ethrex` (both) |

</details>

<details>
<summary><code>WARM_ACCESS</code> — 4 weak combos</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_ext_account_query_warm` | `BALANCE` | `target_coef` | `param_opcode=BALANCE` | `besu` (R²) |
| `test_ext_account_query_warm` | `EXTCODEHASH` | `target_coef` | `param_opcode=EXTCODEHASH` | `besu` (R²) |
| `test_ext_account_query_warm` | `EXTCODESIZE` | `target_coef` | `param_opcode=EXTCODESIZE` | `besu` (R²), `geth` (R²), `reth` (R²) |
| `test_sload_same_key_benchmark` | `SLOAD` | `target_coef` | — | `besu` (R²), `reth` (R²) |

</details>
