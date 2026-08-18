# New gas proposal

_Generated 2026-08-18 11:24:51Z · fork `osaka` · anchor_rate 100 Mgas/s_

**Summary:** 12 parameters proposed — 9 increased, 3 decreased, 0 new, 0 unresolved · 3 warnings · 0 poor-fit selections

## Contents

- [Proposed parameters](#proposed-gas-parameters)
- [Client comparison](#client-comparison)
- [Worst-case provenance](#worst-case-provenance-per-gas-param)
- [Warnings](#warnings)
- [Poor-fit selections](#poor-fit-selections)

## Proposed gas parameters

| Gas param | Current gas | Proposed gas | Diff | Diff % |
| --- | --- | --- | --- | --- |
| COLD_STORAGE_ACCESS | 2100 | 2268 | +168 | +8% |
| COLD_STORAGE_WRITE | 5000 | 17696 | +12696 | +254% |
| WARM_ACCESS | 100 | 28 | -72 | -72% |
| COLD_ACCOUNT_NOCODE_ACCESS | 2600 | 2244 | -356 | -14% |
| COLD_ACCOUNT_NOCODE_WRITE | 9300 | 35171 | +25871 | +278% |
| COLD_ACCOUNT_CODE_ACCESS | 2600 | 3517 | +917 | +35% |
| COLD_ACCOUNT_CODE_WRITE | 9300 | 7163 | -2137 | -23% |
| STORAGE_WRITE | 2800 | 15428 | +12628 | +451% |
| ACCOUNT_WRITE | 6700 | 32927 | +26227 | +391% |
| REFUND_STORAGE_CLEAR | 4800 | 16989 | +12189 | +254% |
| TX_ACCESS_LIST_STORAGE_KEY | 1900 | 2268 | +368 | +19% |
| TX_ACCESS_LIST_ADDRESS | 2400 | 3517 | +1117 | +47% |

## Client comparison

Worst client vs. second-worst client per gas parameter. The `Ratio` column is `worst gas / second-worst gas` — values close to 1× mean the worst case sits next to the rest of the field, while large ratios flag the worst client as an outlier.

| Gas param | Worst client | Worst gas | Second-worst client | Second-worst gas | Ratio |
| --- | --- | --- | --- | --- | --- |
| COLD_STORAGE_ACCESS | geth | 2268 | besu | 1557 | 1.46× |
| COLD_STORAGE_WRITE | erigon | 17696 | geth | 12682 | 1.40× |
| WARM_ACCESS | nethermind | 28 | geth | 17 | 1.65× |
| COLD_ACCOUNT_NOCODE_ACCESS | geth | 2244 | besu | 1803 | 1.24× |
| COLD_ACCOUNT_NOCODE_WRITE | erigon | 35171 | besu | 13927 | 2.53× |
| COLD_ACCOUNT_CODE_ACCESS | erigon | 3517 | besu | 2324 | 1.51× |
| COLD_ACCOUNT_CODE_WRITE | besu | 7163 | nethermind | 5052 | 1.42× |

Per-client proposed gas for each parameter. Cells are colored by `log2(proposed / current)` — red means the proposal is more expensive than the current gas cost, green means cheaper, and white sits at unchanged. Annotations show the absolute proposed gas value; blank rows are parameters with no prior baseline (see warnings below).

![](figs/proposal/heatmap.png)

## Worst-case provenance per gas param

One collapsible block per gas parameter showing every per-client candidate that the worst-case selector saw. Rows are model combos (the source regression's `test_name`, `target_opcode`, `model_coef_name`, and any `model_by` factors — components constant within a parameter are dropped from the label). Cells carry each candidate's proposed gas; the cell the per-client selector picked is outlined in black. Colors are `log2(proposed / current)` against that parameter's baseline on a per-parameter symmetric scale.

<details>
<summary><code>COLD_STORAGE_ACCESS</code> — 4 combos × 5 clients</summary>

![](figs/proposal/provenance__COLD_STORAGE_ACCESS.png)

</details>

<details>
<summary><code>COLD_STORAGE_WRITE</code> — 2 combos × 5 clients</summary>

![](figs/proposal/provenance__COLD_STORAGE_WRITE.png)

</details>

<details>
<summary><code>WARM_ACCESS</code> — 8 combos × 5 clients</summary>

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
<summary><code>COLD_ACCOUNT_NOCODE_ACCESS</code> — 16 combos × 5 clients</summary>

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
<summary><code>COLD_ACCOUNT_NOCODE_WRITE</code> — 4 combos × 5 clients</summary>

| Label | Combo |
| --- | --- |
| `M1` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=CALL |
| `M2` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=CALL |
| `M3` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=CALLCODE |
| `M4` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=CALLCODE |

![](figs/proposal/provenance__COLD_ACCOUNT_NOCODE_WRITE.png)

</details>

<details>
<summary><code>COLD_ACCOUNT_CODE_ACCESS</code> — 24 combos × 5 clients</summary>

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
<summary><code>COLD_ACCOUNT_CODE_WRITE</code> — 6 combos × 5 clients</summary>

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

**Clients with no estimations at all:** `ethrex`. These configured clients produced no fits for any gas parameter — check that the runtimes CSV contains their rows and that the fixture-name conventions match. Inspect the `evm_gasfit` warnings in `meta.json` for the cause.

### Missing glue adjustments

<details>
<summary><b>Priced glue opcodes with a poor fit</b> — 135 (glue_opcode, client) fits skipped</summary>

`p_value >= glue_contribution_p_value_threshold` (0.05) or `rsquared < glue_contribution_rsquared_threshold` (0.5) — the contribution of these (glue_opcode, client) fits was **skipped** when computing the glue adjustment, so the listed gas params carry a target coefficient that is not net of this glue opcode's runtime on the affected clients. See `glue_opcodes_autogenerated_report.md` for per-fit metrics.

| Glue opcode | Affected clients | Affected gas params |
| --- | --- | --- |
| `ADD` | `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE` |
| `AND` | `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | — |
| `CALLDATACOPY` | `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | — |
| `CALLDATALOAD` | `erigon` (R²), `ethrex` (R²), `geth` (R²), `nethermind` (both), `reth` (both) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE` |
| `CALLDATASIZE` | `besu` (p-value), `erigon` (both), `ethrex` (R²), `geth` (R²), `reth` (R²) | — |
| `DIV` | `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | — |
| `DUP` | `besu` (p-value), `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (p-value), `reth` (both) | `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE` |
| `EXP` | `nethermind` (both) | — |
| `GAS` | `besu` (p-value), `erigon` (both), `ethrex` (R²), `geth` (R²), `reth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS`, `WARM_ACCESS` |
| `GT` | `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS` |
| `ISZERO` | `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | — |
| `JUMP` | `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | — |
| `JUMPDEST` | `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE` |
| `JUMPI` | `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE` |
| `KECCAK256` | `erigon` (R²), `ethrex` (both), `geth` (R²), `nethermind` (both), `reth` (both) | — |
| `LT` | `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE` |
| `MLOAD` | `besu` (p-value), `erigon` (R²), `ethrex` (R²), `geth` (R²), `reth` (R²) | `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `WARM_ACCESS` |
| `MSTORE` | `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE` |
| `MSTORE8` | `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE` |
| `MUL` | `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | — |
| `PC` | `ethrex` (R²), `geth` (R²), `nethermind` (R²) | `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS` |
| `PUSH` | `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (p-value), `reth` (both) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_CODE_WRITE`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE`, `WARM_ACCESS` |
| `PUSH0` | `besu` (p-value), `erigon` (both), `ethrex` (R²), `geth` (both), `reth` (R²) | — |
| `RETURNDATASIZE` | `erigon` (both), `ethrex` (R²), `geth` (R²), `nethermind` (R²), `reth` (R²) | — |
| `SELFBALANCE` | `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | — |
| `STATICCALL` | `besu` (p-value), `erigon` (both), `ethrex` (both), `geth` (R²), `reth` (R²) | — |
| `SUB` | `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_ACCOUNT_NOCODE_WRITE`, `COLD_STORAGE_ACCESS` |
| `SWAP` | `erigon` (both), `ethrex` (both), `geth` (both), `nethermind` (both), `reth` (both) | `COLD_STORAGE_ACCESS`, `COLD_STORAGE_WRITE` |

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
<summary><code>WARM_ACCESS</code> — 4 weak combos</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_ext_account_query_warm` | `CALLCODE` | `target_coef` | `param_opcode=CALLCODE` | `nethermind` (R²) |
| `test_ext_account_query_warm` | `DELEGATECALL` | `target_coef` | `param_opcode=DELEGATECALL` | `nethermind` (R²) |
| `test_ext_account_query_warm` | `EXTCODEHASH` | `target_coef` | `param_opcode=EXTCODEHASH` | `reth` (R²) |
| `test_ext_account_query_warm` | `EXTCODESIZE` | `target_coef` | `param_opcode=EXTCODESIZE` | `reth` (R²) |

</details>
