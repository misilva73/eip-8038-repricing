# New gas proposal

_Generated 2026-06-02 09:22:24Z · fork `osaka` · anchor_rate 100 Mgas/s_

**Summary:** 9 parameters proposed — 8 increased, 1 decreased, 0 new, 0 unresolved · 4 warnings · 0 poor-fit selections

## Contents

- [Proposed parameters](#proposed-gas-parameters)
- [Client comparison](#client-comparison)
- [Worst-case provenance](#worst-case-provenance-per-gas-param)
- [Warnings](#warnings)
- [Poor-fit selections](#poor-fit-selections)

## Proposed gas parameters

| Gas param | Current gas | Proposed gas | Diff | Diff % |
| --- | --- | --- | --- | --- |
| COLD_STORAGE_ACCESS | 2100 | 2536 | +436 | +21% |
| STORAGE_WRITE | 2800 | 17173 | +14373 | +513% |
| COLD_ACCOUNT_NOCODE_ACCESS | 2600 | 10221 | +7621 | +293% |
| ACCOUNT_WRITE | 6700 | 27736 | +21036 | +314% |
| COLD_ACCOUNT_CODE_ACCESS | 2600 | 10221 | +7621 | +293% |
| WARM_ACCESS | 100 | 73 | -27 | -27% |
| REFUND_STORAGE_CLEAR | 4800 | 18921 | +14121 | +294% |
| TX_ACCESS_LIST_STORAGE_KEY | 1900 | 2536 | +636 | +33% |
| TX_ACCESS_LIST_ADDRESS | 2400 | 10221 | +7821 | +326% |

## Client comparison

Worst client vs. second-worst client per gas parameter. The `Ratio` column is `worst gas / second-worst gas` — values close to 1× mean the worst case sits next to the rest of the field, while large ratios flag the worst client as an outlier.

| Gas param | Worst client | Worst gas | Second-worst client | Second-worst gas | Ratio |
| --- | --- | --- | --- | --- | --- |
| COLD_STORAGE_ACCESS | nethermind | 2536 | besu | 1723 | 1.47× |
| STORAGE_WRITE | reth | 17173 | erigon | 16263 | 1.06× |
| COLD_ACCOUNT_NOCODE_ACCESS | erigon | 10221 | reth | 3682 | 2.78× |
| ACCOUNT_WRITE | erigon | 27736 | reth | 16375 | 1.69× |
| COLD_ACCOUNT_CODE_ACCESS | erigon | 10221 | reth | 3682 | 2.78× |
| WARM_ACCESS | nethermind | 73 | besu | 62 | 1.18× |

Per-client proposed gas for each parameter. Cells are colored by `log2(proposed / current)` — red means the proposal is more expensive than the current gas cost, green means cheaper, and white sits at unchanged. Annotations show the absolute proposed gas value; blank rows are parameters with no prior baseline (see warnings below).

![](figs/proposal/heatmap.png)

## Worst-case provenance per gas param

One collapsible block per gas parameter showing every per-client candidate that the worst-case selector saw. Rows are model combos (the source regression's `test_name`, `target_opcode`, `model_coef_name`, and any `model_by` factors — components constant within a parameter are dropped from the label). Cells carry each candidate's proposed gas; the cell the per-client selector picked is outlined in black. Colors are `log2(proposed / current)` against that parameter's baseline on a per-parameter symmetric scale.

<details>
<summary><code>COLD_STORAGE_ACCESS</code> — 4 combos × 4 clients</summary>

![](figs/proposal/provenance__COLD_STORAGE_ACCESS.png)

</details>

<details>
<summary><code>STORAGE_WRITE</code> — 2 combos × 4 clients</summary>

![](figs/proposal/provenance__STORAGE_WRITE.png)

</details>

<details>
<summary><code>COLD_ACCOUNT_NOCODE_ACCESS</code> — 21 combos × 4 clients</summary>

| Label | Combo |
| --- | --- |
| `M1` | test_name=test_account_access / target_opcode=BALANCE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=BALANCE |
| `M2` | test_name=test_account_access / target_opcode=BALANCE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=BALANCE |
| `M3` | test_name=test_account_access / target_opcode=BALANCE / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=BALANCE |
| `M4` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=CALL |
| `M5` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=CALL |
| `M6` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=CALL |
| `M7` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=CALLCODE |
| `M8` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=CALLCODE |
| `M9` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=CALLCODE |
| `M10` | test_name=test_account_access / target_opcode=DELEGATECALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=DELEGATECALL |
| `M11` | test_name=test_account_access / target_opcode=DELEGATECALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=DELEGATECALL |
| `M12` | test_name=test_account_access / target_opcode=DELEGATECALL / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=DELEGATECALL |
| `M13` | test_name=test_account_access / target_opcode=EXTCODECOPY / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=EXTCODECOPY |
| `M14` | test_name=test_account_access / target_opcode=EXTCODECOPY / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=EXTCODECOPY |
| `M15` | test_name=test_account_access / target_opcode=EXTCODEHASH / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=EXTCODEHASH |
| `M16` | test_name=test_account_access / target_opcode=EXTCODEHASH / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=EXTCODEHASH |
| `M17` | test_name=test_account_access / target_opcode=EXTCODESIZE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=EXTCODESIZE |
| `M18` | test_name=test_account_access / target_opcode=EXTCODESIZE / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=EXTCODESIZE |
| `M19` | test_name=test_account_access / target_opcode=STATICCALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=STATICCALL |
| `M20` | test_name=test_account_access / target_opcode=STATICCALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=STATICCALL |
| `M21` | test_name=test_account_access / target_opcode=STATICCALL / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=STATICCALL |

![](figs/proposal/provenance__COLD_ACCOUNT_NOCODE_ACCESS.png)

</details>

<details>
<summary><code>ACCOUNT_WRITE</code> — 6 combos × 4 clients</summary>

| Label | Combo |
| --- | --- |
| `M1` | test_name=test_account_access / target_opcode=CALL / model_coef_name=update / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=CALL |
| `M2` | test_name=test_account_access / target_opcode=CALL / model_coef_name=update / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=CALL |
| `M3` | test_name=test_account_access / target_opcode=CALL / model_coef_name=update / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=CALL |
| `M4` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=update / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=CALLCODE |
| `M5` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=update / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=CALLCODE |
| `M6` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=update / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=CALLCODE |

![](figs/proposal/provenance__ACCOUNT_WRITE.png)

</details>

<details>
<summary><code>COLD_ACCOUNT_CODE_ACCESS</code> — 21 combos × 4 clients</summary>

| Label | Combo |
| --- | --- |
| `M1` | test_name=test_account_access / target_opcode=BALANCE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=BALANCE |
| `M2` | test_name=test_account_access / target_opcode=BALANCE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=BALANCE |
| `M3` | test_name=test_account_access / target_opcode=BALANCE / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=BALANCE |
| `M4` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=CALL |
| `M5` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=CALL |
| `M6` | test_name=test_account_access / target_opcode=CALL / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=CALL |
| `M7` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=CALLCODE |
| `M8` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=CALLCODE |
| `M9` | test_name=test_account_access / target_opcode=CALLCODE / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=CALLCODE |
| `M10` | test_name=test_account_access / target_opcode=DELEGATECALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=DELEGATECALL |
| `M11` | test_name=test_account_access / target_opcode=DELEGATECALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=DELEGATECALL |
| `M12` | test_name=test_account_access / target_opcode=DELEGATECALL / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=DELEGATECALL |
| `M13` | test_name=test_account_access / target_opcode=EXTCODECOPY / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=EXTCODECOPY |
| `M14` | test_name=test_account_access / target_opcode=EXTCODECOPY / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=EXTCODECOPY |
| `M15` | test_name=test_account_access / target_opcode=EXTCODEHASH / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=EXTCODEHASH |
| `M16` | test_name=test_account_access / target_opcode=EXTCODEHASH / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=EXTCODEHASH |
| `M17` | test_name=test_account_access / target_opcode=EXTCODESIZE / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=EXTCODESIZE |
| `M18` | test_name=test_account_access / target_opcode=EXTCODESIZE / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=EXTCODESIZE |
| `M19` | test_name=test_account_access / target_opcode=STATICCALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_CONTRACT / param_opcode=STATICCALL |
| `M20` | test_name=test_account_access / target_opcode=STATICCALL / model_coef_name=target_coef / param_account_mode=AccountMode.EXISTING_EOA / param_opcode=STATICCALL |
| `M21` | test_name=test_account_access / target_opcode=STATICCALL / model_coef_name=target_coef / param_account_mode=AccountMode.NON_EXISTING_ACCOUNT / param_opcode=STATICCALL |

![](figs/proposal/provenance__COLD_ACCOUNT_CODE_ACCESS.png)

</details>

<details>
<summary><code>WARM_ACCESS</code> — 8 combos × 4 clients</summary>

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

**Clients with no estimations at all:** `geth`. These configured clients produced no fits for any gas parameter — check that the runtimes CSV contains their rows and that the fixture-name conventions match. Inspect the `evm_gasfit` warnings in `meta.json` for the cause.

These gas parameters were fit by at least one client but not by every configured client — the listed clients produced no estimation, so the worst-case value was selected from a smaller pool. Inspect the `evm_gasfit` warnings in `meta.json` for the cause.

| Gas param | Missing clients |
| --- | --- |
| `COLD_STORAGE_ACCESS` | `geth` |
| `STORAGE_WRITE` | `geth` |
| `COLD_ACCOUNT_NOCODE_ACCESS` | `geth` |
| `ACCOUNT_WRITE` | `geth` |
| `COLD_ACCOUNT_CODE_ACCESS` | `geth` |
| `WARM_ACCESS` | `geth` |

### Missing glue adjustments

<details>
<summary><b>Non-priced opcodes correlated with the target opcount</b> — 1 test affected</summary>

The target coefficient was left unadjusted for these. Consider adding them to the glue model or re-designing the test to isolate the target opcode.

| Test name | Non-priced opcodes |
| --- | --- |
| `test_account_access` | `CLZ` |

</details>

<details>
<summary><b>Priced glue opcodes with a poor fit</b> — 51 (glue_opcode, client) fits skipped</summary>

`p_value >= glue_contribution_p_value_threshold` (0.05) or `rsquared < glue_contribution_rsquared_threshold` (0.5) — the contribution of these (glue_opcode, client) fits was **skipped** when computing the glue adjustment, so the listed gas params carry a target coefficient that is not net of this glue opcode's runtime on the affected clients. See `glue_opcodes_autogenerated_report.md` for per-fit metrics.

| Glue opcode | Affected clients | Affected gas params |
| --- | --- | --- |
| `ADD` | `geth` (R²), `nethermind` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_STORAGE_ACCESS` |
| `AND` | `geth` (R²), `nethermind` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_NOCODE_ACCESS` |
| `CALLDATACOPY` | `geth` (R²) | — |
| `CALLDATALOAD` | `besu` (both), `geth` (R²), `nethermind` (R²), `reth` (R²) | — |
| `CALLDATASIZE` | `erigon` (p-value), `geth` (R²), `nethermind` (p-value) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_NOCODE_ACCESS` |
| `DIV` | `geth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_NOCODE_ACCESS` |
| `DUP` | `geth` (R²), `nethermind` (p-value) | `COLD_STORAGE_ACCESS` |
| `EXP` | `geth` (R²), `nethermind` (both) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_NOCODE_ACCESS` |
| `GAS` | `erigon` (p-value), `geth` (R²), `nethermind` (p-value) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_STORAGE_ACCESS`, `WARM_ACCESS` |
| `GT` | `geth` (R²), `nethermind` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_STORAGE_ACCESS` |
| `ISZERO` | `geth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_NOCODE_ACCESS` |
| `JUMP` | `geth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_NOCODE_ACCESS` |
| `JUMPDEST` | `geth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_STORAGE_ACCESS` |
| `JUMPI` | `geth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_STORAGE_ACCESS` |
| `KECCAK256` | `besu` (R²), `geth` (R²), `nethermind` (both), `reth` (both) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_NOCODE_ACCESS` |
| `LT` | `geth` (R²) | `COLD_STORAGE_ACCESS` |
| `MLOAD` | `erigon` (p-value), `geth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_NOCODE_ACCESS`, `WARM_ACCESS` |
| `MSTORE` | `geth` (R²), `reth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_NOCODE_ACCESS` |
| `MSTORE8` | `geth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_NOCODE_ACCESS` |
| `MUL` | `geth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_NOCODE_ACCESS` |
| `PC` | `geth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_STORAGE_ACCESS` |
| `PUSH` | `erigon` (p-value), `geth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_STORAGE_ACCESS`, `WARM_ACCESS` |
| `PUSH0` | `erigon` (p-value), `geth` (both), `nethermind` (p-value) | — |
| `RETURNDATASIZE` | `geth` (R²) | — |
| `SELFBALANCE` | `besu` (R²), `geth` (R²) | — |
| `STATICCALL` | `erigon` (p-value), `geth` (both) | — |
| `SUB` | `geth` (R²) | `COLD_ACCOUNT_CODE_ACCESS`, `COLD_ACCOUNT_NOCODE_ACCESS`, `COLD_STORAGE_ACCESS` |
| `SWAP` | `geth` (R²), `nethermind` (R²) | — |

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
<summary><code>COLD_STORAGE_ACCESS</code> — 2 weak combos</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_sstore_bloated` | `SSTORE` | `target_coef` | `param_existing_slots=False` | `reth` (p-value) |
| `test_sstore_bloated` | `SSTORE` | `target_coef` | `param_existing_slots=True` | `erigon` (p-value), `reth` (p-value) |

</details>

<details>
<summary><code>COLD_ACCOUNT_NOCODE_ACCESS</code> — 2 weak combos</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_account_access` | `CALL` | `target_coef` | `param_account_mode=AccountMode.EXISTING_EOA` | `reth` (p-value) |
| `test_account_access` | `CALL` | `target_coef` | `param_account_mode=AccountMode.NON_EXISTING_ACCOUNT` | `reth` (R²) |

</details>

<details>
<summary><code>ACCOUNT_WRITE</code> — 4 weak combos</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_account_access` | `CALL` | `update` | `param_account_mode=AccountMode.NON_EXISTING_ACCOUNT` / `param_opcode=CALL` | `besu` (p-value), `reth` (R²) |
| `test_account_access` | `CALLCODE` | `update` | `param_account_mode=AccountMode.EXISTING_CONTRACT` / `param_opcode=CALLCODE` | `besu` (p-value), `erigon` (p-value), `nethermind` (p-value), `reth` (p-value) |
| `test_account_access` | `CALLCODE` | `update` | `param_account_mode=AccountMode.EXISTING_EOA` / `param_opcode=CALLCODE` | `besu` (p-value), `erigon` (p-value), `nethermind` (p-value), `reth` (p-value) |
| `test_account_access` | `CALLCODE` | `update` | `param_account_mode=AccountMode.NON_EXISTING_ACCOUNT` / `param_opcode=CALLCODE` | `besu` (p-value), `erigon` (p-value), `nethermind` (p-value), `reth` (p-value) |

</details>

<details>
<summary><code>COLD_ACCOUNT_CODE_ACCESS</code> — 2 weak combos</summary>

| Test | Target opcode | Coef | Combo | Failing clients |
| --- | --- | --- | --- | --- |
| `test_account_access` | `CALL` | `target_coef` | `param_account_mode=AccountMode.EXISTING_EOA` | `reth` (p-value) |
| `test_account_access` | `CALL` | `target_coef` | `param_account_mode=AccountMode.NON_EXISTING_ACCOUNT` | `reth` (R²) |

</details>
