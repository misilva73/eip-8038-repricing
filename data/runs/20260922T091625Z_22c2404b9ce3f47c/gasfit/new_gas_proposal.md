# New gas proposal

_Generated 2026-09-22 13:08:14Z · fork `osaka` · anchor_rate 100 Mgas/s_

**Summary:** 12 parameters proposed — 10 increased, 2 decreased, 0 new, 0 unresolved · 3 warnings · 0 poor-fit selections

## Contents

- [Proposed parameters](#proposed-gas-parameters)
- [Client comparison](#client-comparison)
- [Worst-case provenance](#worst-case-provenance-per-gas-param)
- [Warnings](#warnings)
- [Poor-fit selections](#poor-fit-selections)

## Proposed gas parameters

| Gas param | Current gas | Proposed gas | Diff | Diff % |
| --- | --- | --- | --- | --- |
| COLD_STORAGE_ACCESS | 2100 | 2894 | +794 | +38% |
| COLD_STORAGE_WRITE | 5000 | 16739 | +11739 | +235% |
| WARM_ACCESS | 100 | 96 | -4 | -4% |
| COLD_ACCOUNT_NOCODE_ACCESS | 2600 | 2414 | -186 | -7% |
| COLD_ACCOUNT_NOCODE_WRITE | 9300 | 23993 | +14693 | +158% |
| COLD_ACCOUNT_CODE_ACCESS | 2600 | 4628 | +2028 | +78% |
| COLD_ACCOUNT_CODE_WRITE | 9300 | 15455 | +6155 | +66% |
| STORAGE_WRITE | 2800 | 13845 | +11045 | +394% |
| ACCOUNT_WRITE | 6700 | 21579 | +14879 | +222% |
| REFUND_STORAGE_CLEAR | 4800 | 16070 | +11270 | +235% |
| TX_ACCESS_LIST_STORAGE_KEY | 1900 | 2894 | +994 | +52% |
| TX_ACCESS_LIST_ADDRESS | 2400 | 4628 | +2228 | +93% |

## Client comparison

Worst client vs. second-worst client per gas parameter. The `Ratio` column is `worst gas / second-worst gas` — values close to 1× mean the worst case sits next to the rest of the field, while large ratios flag the worst client as an outlier.

| Gas param | Worst client | Worst gas | Second-worst client | Second-worst gas | Ratio |
| --- | --- | --- | --- | --- | --- |
| COLD_STORAGE_ACCESS | besu | 2894 | geth | 2232 | 1.30× |
| COLD_STORAGE_WRITE | erigon | 16739 | besu | 14679 | 1.14× |
| WARM_ACCESS | besu | 96 | nethermind | 32 | 3.00× |
| COLD_ACCOUNT_NOCODE_ACCESS | besu | 2414 | geth | 2225 | 1.08× |
| COLD_ACCOUNT_NOCODE_WRITE | besu | 23993 | erigon | 19897 | 1.21× |
| COLD_ACCOUNT_CODE_ACCESS | geth | 4628 | besu | 3522 | 1.31× |
| COLD_ACCOUNT_CODE_WRITE | geth | 15455 | reth | 12974 | 1.19× |

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
<summary><code>COLD_ACCOUNT_CODE_ACCESS</code> — 24 combos × 6 clients</summary>

| Label | Combo |
| --- | --- |
| `M1` | test_name=test_account_access / target_opcode=BALANCE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX / param_opcode=BALANCE |
| `M2` | test_name=test_account_access / target_opcode=BALANCE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL / param_opcode=BALANCE |
| `M3` | test_name=test_account_access / target_opcode=BALANCE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX / param_opcode=BALANCE |
| `M4` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX / param_opcode=CALL |
| `M5` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL / param_opcode=CALL |
| `M6` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX / param_opcode=CALL |
| `M7` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX / param_opcode=CALLCODE |
| `M8` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL / param_opcode=CALLCODE |
| `M9` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX / param_opcode=CALLCODE |
| `M10` | test_name=test_account_access / target_opcode=DELEGATECALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX / param_opcode=DELEGATECALL |
| `M11` | test_name=test_account_access / target_opcode=DELEGATECALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL / param_opcode=DELEGATECALL |
| `M12` | test_name=test_account_access / target_opcode=DELEGATECALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX / param_opcode=DELEGATECALL |
| `M13` | test_name=test_account_access / target_opcode=EXTCODECOPY / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX / param_opcode=EXTCODECOPY |
| `M14` | test_name=test_account_access / target_opcode=EXTCODECOPY / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL / param_opcode=EXTCODECOPY |
| `M15` | test_name=test_account_access / target_opcode=EXTCODECOPY / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX / param_opcode=EXTCODECOPY |
| `M16` | test_name=test_account_access / target_opcode=EXTCODEHASH / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX / param_opcode=EXTCODEHASH |
| `M17` | test_name=test_account_access / target_opcode=EXTCODEHASH / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL / param_opcode=EXTCODEHASH |
| `M18` | test_name=test_account_access / target_opcode=EXTCODEHASH / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX / param_opcode=EXTCODEHASH |
| `M19` | test_name=test_account_access / target_opcode=EXTCODESIZE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX / param_opcode=EXTCODESIZE |
| `M20` | test_name=test_account_access / target_opcode=EXTCODESIZE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL / param_opcode=EXTCODESIZE |
| `M21` | test_name=test_account_access / target_opcode=EXTCODESIZE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX / param_opcode=EXTCODESIZE |
| `M22` | test_name=test_account_access / target_opcode=STATICCALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX / param_opcode=STATICCALL |
| `M23` | test_name=test_account_access / target_opcode=STATICCALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL / param_opcode=STATICCALL |
| `M24` | test_name=test_account_access / target_opcode=STATICCALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX / param_opcode=STATICCALL |

![](figs/proposal/provenance__COLD_ACCOUNT_CODE_ACCESS.png)

</details>

<details>
<summary><code>COLD_ACCOUNT_CODE_WRITE</code> — 6 combos × 6 clients</summary>

| Label | Combo |
| --- | --- |
| `M1` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX / param_opcode=CALL |
| `M2` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL / param_opcode=CALL |
| `M3` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX / param_opcode=CALL |
| `M4` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX / param_opcode=CALLCODE |
| `M5` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL / param_opcode=CALLCODE |
| `M6` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX / param_opcode=CALLCODE |

![](figs/proposal/provenance__COLD_ACCOUNT_CODE_WRITE.png)

</details>

## Warnings

### Missing parameters

_None._

### Incomplete client coverage

_None._

### Missing glue adjustments

<details>
<summary><b>Priced glue opcodes with a poor fit</b> — 14 (glue_opcode, client) fits skipped</summary>

`p_value >= glue_contribution_p_value_threshold` (0.05) or `rsquared < glue_contribution_rsquared_threshold` (0.5) — the contribution of these (glue_opcode, client) fits was **skipped** when computing the glue adjustment, so the listed gas params carry a target coefficient that is not net of this glue opcode's runtime on the affected clients. See `glue_opcodes_autogenerated_report.md` for per-fit metrics.

| Glue opcode | Affected clients | Affected gas params |
| --- | --- | --- |
| `CALLDATALOAD` | `besu` (R²), `erigon` (R²), `ethrex` (R²), `geth` (R²), `nethermind` (R²), `reth` (both) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE` |
| `EXP` | `nethermind` (both) | — |
| `KECCAK256` | `besu` (R²), `erigon` (R²), `ethrex` (both), `geth` (R²), `nethermind` (both), `reth` (both) | — |
| `MSTORE` | `reth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE` |

</details>

### Other

- derived: 'REFUND_STORAGE_CLEAR' shadows a raw fork field on 'osaka'
- derived: 'TX_ACCESS_LIST_STORAGE_KEY' shadows a raw fork field on 'osaka'
- derived: 'TX_ACCESS_LIST_ADDRESS' shadows a raw fork field on 'osaka'

## Poor-fit selections

Rows where the winning fit's p-value exceeded `modeling.poor_fit_p_value_threshold` (0.05) or its R² fell below `modeling.poor_fit_rsquared_threshold` (0.5). The failing threshold(s) are noted alongside each row; selections in `### Winners with poor fit` still drive the proposal, while `### Other weak candidates` lists losing candidates that the selector dropped in favor of a qualified alternative. See `runtime_estimation_autogenerated_report.md` for per-fit `runtime_ms`, `pvalue`, and `rsquared` metrics.

### Winners with poor fit

_None._

### Other weak candidates

<details>
<summary><code>COLD_STORAGE_WRITE</code> — 1 weak combo</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_sstore_bloated` | `SSTORE` | `target_coef` | — | `ethrex` (both) |

</details>

<details>
<summary><code>WARM_ACCESS</code> — 1 weak combo</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_sload_same_key_benchmark` | `SLOAD` | `target_coef` | — | `besu` (R²) |

</details>

<details>
<summary><code>COLD_ACCOUNT_NOCODE_WRITE</code> — 1 weak combo</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_account_access` | `CALLCODE` | `target_coef` | — | `ethrex` (R²) |

</details>

<details>
<summary><code>COLD_ACCOUNT_CODE_ACCESS</code> — 6 weak combos</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_account_access` | `CALL` | `target_coef` | `param_opcode=CALL` | `nethermind` (R²), `reth` (R²) |
| `test_account_access` | `CALLCODE` | `target_coef` | `param_opcode=CALLCODE` | `nethermind` (R²), `reth` (R²) |
| `test_account_access` | `DELEGATECALL` | `target_coef` | `param_opcode=DELEGATECALL` | `nethermind` (R²), `reth` (R²) |
| `test_account_access` | `EXTCODECOPY` | `target_coef` | `param_opcode=EXTCODECOPY` | `nethermind` (R²), `reth` (R²) |
| `test_account_access` | `EXTCODESIZE` | `target_coef` | `param_opcode=EXTCODESIZE` | `nethermind` (R²), `reth` (R²) |
| `test_account_access` | `STATICCALL` | `target_coef` | `param_opcode=STATICCALL` | `nethermind` (R²), `reth` (R²) |

</details>

<details>
<summary><code>COLD_ACCOUNT_CODE_WRITE</code> — 3 weak combos</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_account_access` | `CALLCODE` | `target_coef` | `param_account_mode=AccountMode.EXISTING_CONTRACT_DIFF_MAX` | `reth` (R²) |
| `test_account_access` | `CALLCODE` | `target_coef` | `param_account_mode=AccountMode.EXISTING_CONTRACT_MINIMAL` | `ethrex` (both) |
| `test_account_access` | `CALLCODE` | `target_coef` | `param_account_mode=AccountMode.EXISTING_CONTRACT_SAME_MAX` | `ethrex` (both) |

</details>
