# New gas proposal

_Generated 2026-07-06 08:06:50Z · fork `osaka` · anchor_rate 100 Mgas/s_

**Summary:** 12 parameters proposed — 10 increased, 2 decreased, 0 new, 0 unresolved · 4 warnings · 0 poor-fit selections

## Contents

- [Proposed parameters](#proposed-gas-parameters)
- [Client comparison](#client-comparison)
- [Worst-case provenance](#worst-case-provenance-per-gas-param)
- [Warnings](#warnings)
- [Poor-fit selections](#poor-fit-selections)

## Proposed gas parameters

| Gas param | Current gas | Proposed gas | Diff | Diff % |
| --- | --- | --- | --- | --- |
| COLD_STORAGE_ACCESS | 2100 | 2425 | +325 | +15% |
| COLD_STORAGE_WRITE | 5000 | 13530 | +8530 | +171% |
| COLD_ACCOUNT_NOCODE_ACCESS | 2600 | 2267 | -333 | -13% |
| COLD_ACCOUNT_CODE_ACCESS | 2600 | 2772 | +172 | +7% |
| COLD_ACCOUNT_NOCODE_WRITE | 9300 | 19738 | +10438 | +112% |
| COLD_ACCOUNT_CODE_WRITE | 9300 | 19738 | +10438 | +112% |
| WARM_ACCESS | 100 | 51 | -49 | -49% |
| STORAGE_WRITE | 2800 | 11105 | +8305 | +297% |
| ACCOUNT_WRITE | 6700 | 17471 | +10771 | +161% |
| REFUND_STORAGE_CLEAR | 4800 | 12989 | +8189 | +171% |
| TX_ACCESS_LIST_STORAGE_KEY | 1900 | 2425 | +525 | +28% |
| TX_ACCESS_LIST_ADDRESS | 2400 | 2772 | +372 | +16% |

## Client comparison

Worst client vs. second-worst client per gas parameter. The `Ratio` column is `worst gas / second-worst gas` — values close to 1× mean the worst case sits next to the rest of the field, while large ratios flag the worst client as an outlier.

| Gas param | Worst client | Worst gas | Second-worst client | Second-worst gas | Ratio |
| --- | --- | --- | --- | --- | --- |
| COLD_STORAGE_ACCESS | geth | 2425 | besu | 1519 | 1.60× |
| COLD_STORAGE_WRITE | geth | 13530 | erigon | 12198 | 1.11× |
| COLD_ACCOUNT_NOCODE_ACCESS | geth | 2267 | besu | 1589 | 1.43× |
| COLD_ACCOUNT_CODE_ACCESS | besu | 2772 | erigon | 2450 | 1.13× |
| COLD_ACCOUNT_NOCODE_WRITE | erigon | 19738 | geth | 9908 | 1.99× |
| COLD_ACCOUNT_CODE_WRITE | erigon | 19738 | geth | 9908 | 1.99× |
| WARM_ACCESS | besu | 51 | erigon | 49 | 1.04× |

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
<summary><code>COLD_ACCOUNT_NOCODE_ACCESS</code> — 13 combos × 6 clients</summary>

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
| `M9` | test_name=test_account_access / target_opcode=EXTCODECOPY / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=EXTCODECOPY |
| `M10` | test_name=test_account_access / target_opcode=EXTCODEHASH / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=EXTCODEHASH |
| `M11` | test_name=test_account_access / target_opcode=EXTCODESIZE / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=EXTCODESIZE |
| `M12` | test_name=test_account_access / target_opcode=STATICCALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=STATICCALL |
| `M13` | test_name=test_account_access / target_opcode=STATICCALL / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=STATICCALL |

![](figs/proposal/provenance__COLD_ACCOUNT_NOCODE_ACCESS.png)

</details>

<details>
<summary><code>COLD_ACCOUNT_CODE_ACCESS</code> — 16 combos × 6 clients</summary>

| Label | Combo |
| --- | --- |
| `M1` | test_name=test_account_access / target_opcode=BALANCE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=BALANCE |
| `M2` | test_name=test_account_access / target_opcode=BALANCE / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=BALANCE |
| `M3` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=CALL |
| `M4` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=CALL |
| `M5` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=CALLCODE |
| `M6` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=CALLCODE |
| `M7` | test_name=test_account_access / target_opcode=DELEGATECALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=DELEGATECALL |
| `M8` | test_name=test_account_access / target_opcode=DELEGATECALL / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=DELEGATECALL |
| `M9` | test_name=test_account_access / target_opcode=EXTCODECOPY / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=EXTCODECOPY |
| `M10` | test_name=test_account_access / target_opcode=EXTCODECOPY / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=EXTCODECOPY |
| `M11` | test_name=test_account_access / target_opcode=EXTCODEHASH / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=EXTCODEHASH |
| `M12` | test_name=test_account_access / target_opcode=EXTCODEHASH / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=EXTCODEHASH |
| `M13` | test_name=test_account_access / target_opcode=EXTCODESIZE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=EXTCODESIZE |
| `M14` | test_name=test_account_access / target_opcode=EXTCODESIZE / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=EXTCODESIZE |
| `M15` | test_name=test_account_access / target_opcode=STATICCALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=STATICCALL |
| `M16` | test_name=test_account_access / target_opcode=STATICCALL / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=STATICCALL |

![](figs/proposal/provenance__COLD_ACCOUNT_CODE_ACCESS.png)

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
<summary><code>COLD_ACCOUNT_CODE_WRITE</code> — 4 combos × 6 clients</summary>

| Label | Combo |
| --- | --- |
| `M1` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=CALL |
| `M2` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=CALL |
| `M3` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=CALLCODE |
| `M4` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=CALLCODE |

![](figs/proposal/provenance__COLD_ACCOUNT_CODE_WRITE.png)

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
| `M8` | test_name=test_storage_sload_same_key_benchmark / target_opcode=SLOAD / model_coef_name=target_coef |

![](figs/proposal/provenance__WARM_ACCESS.png)

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
| `test_account_access` | `CLZ` |

</details>

<details>
<summary><b>Priced glue opcodes with a poor fit</b> — 27 (glue_opcode, client) fits skipped</summary>

`p_value >= glue_contribution_p_value_threshold` (0.05) or `rsquared < glue_contribution_rsquared_threshold` (0.5) — the contribution of these (glue_opcode, client) fits was **skipped** when computing the glue adjustment, so the listed gas params carry a target coefficient that is not net of this glue opcode's runtime on the affected clients. See `glue_opcodes_autogenerated_report.md` for per-fit metrics.

| Glue opcode | Affected clients | Affected gas params |
| --- | --- | --- |
| `ADD` | `nethermind` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE` |
| `CALLDATALOAD` | `besu` (both), `erigon` (both), `ethrex` (R²), `geth` (R²), `nethermind` (R²), `reth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE` |
| `CALLDATASIZE` | `reth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE` |
| `DUP` | `reth` (R²) | `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE` |
| `EXP` | `nethermind` (both) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE` |
| `GAS` | `reth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS`, `WARM_ACCESS` |
| `GT` | `besu` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS` |
| `KECCAK256` | `besu` (R²), `erigon` (R²), `ethrex` (both), `geth` (R²), `nethermind` (both), `reth` (both) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE` |
| `LT` | `besu` (R²) | `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE` |
| `MLOAD` | `reth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `WARM_ACCESS` |
| `MSTORE` | `reth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE` |
| `PC` | `reth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS` |
| `PUSH` | `reth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE`, `WARM_ACCESS` |
| `PUSH0` | `reth` (R²) | — |
| `STATICCALL` | `reth` (R²) | — |
| `SWAP` | `besu` (R²), `reth` (R²) | `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE` |

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
| `test_sstore_bloated` | `SSTORE` | `target_coef` | — | `besu` (R²), `erigon` (both), `ethrex` (R²) |

</details>

<details>
<summary><code>COLD_ACCOUNT_NOCODE_ACCESS</code> — 1 weak combo</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_account_access` | `EXTCODECOPY` | `target_coef` | — | `besu` (R²), `ethrex` (R²) |

</details>

<details>
<summary><code>COLD_ACCOUNT_CODE_ACCESS</code> — 7 weak combos</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_account_access` | `CALL` | `target_coef` | `param_account_mode=AccountMode.EXISTING_CONTRACT` / `param_opcode=CALL` | `erigon` (R²) |
| `test_account_access` | `CALLCODE` | `target_coef` | `param_account_mode=AccountMode.EXISTING_CONTRACT` / `param_opcode=CALLCODE` | `erigon` (R²) |
| `test_account_access` | `DELEGATECALL` | `target_coef` | `param_account_mode=AccountMode.EXISTING_CONTRACT` / `param_opcode=DELEGATECALL` | `erigon` (R²) |
| `test_account_access` | `EXTCODECOPY` | `target_coef` | `param_account_mode=AccountMode.EXISTING_CONTRACT` / `param_opcode=EXTCODECOPY` | `besu` (R²) |
| `test_account_access` | `EXTCODECOPY` | `target_coef` | `param_account_mode=AccountMode.NON_EXISTING_ACCOUNT` / `param_opcode=EXTCODECOPY` | `besu` (R²), `ethrex` (R²) |
| `test_account_access` | `EXTCODESIZE` | `target_coef` | `param_account_mode=AccountMode.EXISTING_CONTRACT` / `param_opcode=EXTCODESIZE` | `erigon` (R²) |
| `test_account_access` | `STATICCALL` | `target_coef` | `param_account_mode=AccountMode.EXISTING_CONTRACT` / `param_opcode=STATICCALL` | `erigon` (R²) |

</details>

<details>
<summary><code>COLD_ACCOUNT_NOCODE_WRITE</code> — 3 weak combos</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_account_access` | `CALL` | `target_coef` | `param_account_mode=AccountMode.NON_EXISTING_ACCOUNT` / `param_opcode=CALL` | `besu` (R²), `ethrex` (R²) |
| `test_account_access` | `CALLCODE` | `target_coef` | `param_account_mode=AccountMode.EXISTING_EOA` / `param_opcode=CALLCODE` | `ethrex` (both) |
| `test_account_access` | `CALLCODE` | `target_coef` | `param_account_mode=AccountMode.NON_EXISTING_ACCOUNT` / `param_opcode=CALLCODE` | `besu` (R²), `ethrex` (R²), `reth` (R²) |

</details>

<details>
<summary><code>COLD_ACCOUNT_CODE_WRITE</code> — 3 weak combos</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_account_access` | `CALL` | `target_coef` | `param_account_mode=AccountMode.NON_EXISTING_ACCOUNT` / `param_opcode=CALL` | `besu` (R²), `ethrex` (R²) |
| `test_account_access` | `CALLCODE` | `target_coef` | `param_account_mode=AccountMode.EXISTING_CONTRACT` / `param_opcode=CALLCODE` | `erigon` (R²), `ethrex` (both) |
| `test_account_access` | `CALLCODE` | `target_coef` | `param_account_mode=AccountMode.NON_EXISTING_ACCOUNT` / `param_opcode=CALLCODE` | `besu` (R²), `ethrex` (R²), `reth` (R²) |

</details>

<details>
<summary><code>WARM_ACCESS</code> — 6 weak combos</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_ext_account_query_warm` | `BALANCE` | `target_coef` | `param_opcode=BALANCE` | `besu` (R²), `ethrex` (R²) |
| `test_ext_account_query_warm` | `CALLCODE` | `target_coef` | `param_opcode=CALLCODE` | `besu` (R²) |
| `test_ext_account_query_warm` | `DELEGATECALL` | `target_coef` | `param_opcode=DELEGATECALL` | `besu` (R²) |
| `test_ext_account_query_warm` | `EXTCODEHASH` | `target_coef` | `param_opcode=EXTCODEHASH` | `besu` (R²), `ethrex` (R²) |
| `test_ext_account_query_warm` | `EXTCODESIZE` | `target_coef` | `param_opcode=EXTCODESIZE` | `besu` (R²), `ethrex` (R²) |
| `test_storage_sload_same_key_benchmark` | `SLOAD` | `target_coef` | — | `besu` (R²) |

</details>
