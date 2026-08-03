# Runtime estimation report

Per-spec NNLS fits of `test_runtime_ms` against `opcount`, one row per (target opcode, test, model_by combo, client).

## Contents

- [SLOAD](#sload)
- [SSTORE](#sstore)
- [BALANCE](#balance)
- [CALL](#call)
- [CALLCODE](#callcode)
- [DELEGATECALL](#delegatecall)
- [EXTCODEHASH](#extcodehash)
- [EXTCODESIZE](#extcodesize)
- [STATICCALL](#staticcall)
- [EXTCODECOPY](#extcodecopy)

## SLOAD

### test_sload_bloated — combo `False`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9879 | 0.01623 | 1.00e-03 | [0.01591, 0.01655] |
| `erigon` | 55 | 0.997 | 0.006272 | 1.00e-03 | [0.006191, 0.006348] |
| `ethrex` | 77 | 0.9744 | 0.008506 | 1.00e-03 | [0.008333, 0.008596] |
| `geth` | 99 | 0.9729 | 0.02141 | 1.00e-03 | [0.02046, 0.02215] |
| `nethermind` | 77 | 0.9812 | 0.008958 | 1.00e-03 | [0.008683, 0.009239] |
| `reth` | 110 | 0.9843 | 0.003928 | 1.00e-03 | [0.003829, 0.004026] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.988
Model:                  NNLS                    Adj. R-squared:          0.988
No. Observations:       132                               RMSE:          37.23
Df Residuals:           130                                MAE:          28.80
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    263.7453     10.9277       0.001    243.2838    286.6814
       opcount      0.0162      0.0002       0.001      0.0159      0.0165
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SLOAD__test_sload_bloated__False__besu__regression.png)

![](figs/runtime/SLOAD__test_sload_bloated__False__besu__bootstrap.png)

![](figs/runtime/SLOAD__test_sload_bloated__False__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.997
Model:                  NNLS                    Adj. R-squared:          0.997
No. Observations:       55                                RMSE:           7.08
Df Residuals:           53                                 MAE:           5.62
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      4.9600      3.0338       0.081      0.0000     10.8761
       opcount      0.0063      0.0000       0.001      0.0062      0.0063
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SLOAD__test_sload_bloated__False__erigon__regression.png)

![](figs/runtime/SLOAD__test_sload_bloated__False__erigon__bootstrap.png)

![](figs/runtime/SLOAD__test_sload_bloated__False__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.974
Model:                  NNLS                    Adj. R-squared:          0.974
No. Observations:       77                                RMSE:          29.11
Df Residuals:           75                                 MAE:          24.39
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      2.1781       1.000      0.0000      8.0293
       opcount      0.0085      0.0001       0.001      0.0083      0.0086
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SLOAD__test_sload_bloated__False__ethrex__regression.png)

![](figs/runtime/SLOAD__test_sload_bloated__False__ethrex__bootstrap.png)

![](figs/runtime/SLOAD__test_sload_bloated__False__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.973
Model:                  NNLS                    Adj. R-squared:          0.973
No. Observations:       99                                RMSE:          74.00
Df Residuals:           97                                 MAE:          63.36
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    580.4101     25.7016       0.001    536.4329    638.8428
       opcount      0.0214      0.0004       0.001      0.0205      0.0221
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SLOAD__test_sload_bloated__False__geth__regression.png)

![](figs/runtime/SLOAD__test_sload_bloated__False__geth__bootstrap.png)

![](figs/runtime/SLOAD__test_sload_bloated__False__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          25.68
Df Residuals:           75                                 MAE:          20.93
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     80.0959      8.6416       0.001     63.0246     96.9879
       opcount      0.0090      0.0001       0.001      0.0087      0.0092
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SLOAD__test_sload_bloated__False__nethermind__regression.png)

![](figs/runtime/SLOAD__test_sload_bloated__False__nethermind__bootstrap.png)

![](figs/runtime/SLOAD__test_sload_bloated__False__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.984
Model:                  NNLS                    Adj. R-squared:          0.984
No. Observations:       110                               RMSE:          10.27
Df Residuals:           108                                MAE:           7.84
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     97.8807      3.1408       0.001     92.1351    103.8522
       opcount      0.0039      0.0001       0.001      0.0038      0.0040
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SLOAD__test_sload_bloated__False__reth__regression.png)

![](figs/runtime/SLOAD__test_sload_bloated__False__reth__bootstrap.png)

![](figs/runtime/SLOAD__test_sload_bloated__False__reth__diagnostics.png)

</details>

### test_sload_bloated — combo `True`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9907 | 0.01587 | 1.00e-03 | [0.01558, 0.01617] |
| `erigon` | 55 | 0.9977 | 0.006093 | 1.00e-03 | [0.006063, 0.006116] |
| `ethrex` | 77 | 0.9891 | 0.01316 | 1.00e-03 | [0.01306, 0.01326] |
| `geth` | 99 | 0.9743 | 0.02072 | 1.00e-03 | [0.01993, 0.02139] |
| `nethermind` | 77 | 0.9841 | 0.009018 | 1.00e-03 | [0.008745, 0.009286] |
| `reth` | 110 | 0.9814 | 0.004057 | 1.00e-03 | [0.003963, 0.004161] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.991
Model:                  NNLS                    Adj. R-squared:          0.991
No. Observations:       132                               RMSE:          31.82
Df Residuals:           130                                MAE:          23.97
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    267.1321      9.2311       0.001    248.1575    285.2346
       opcount      0.0159      0.0001       0.001      0.0156      0.0162
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SLOAD__test_sload_bloated__True__besu__regression.png)

![](figs/runtime/SLOAD__test_sload_bloated__True__besu__bootstrap.png)

![](figs/runtime/SLOAD__test_sload_bloated__True__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.998
Model:                  NNLS                    Adj. R-squared:          0.998
No. Observations:       55                                RMSE:           6.14
Df Residuals:           53                                 MAE:           5.13
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.3357       1.000      0.0000      1.1182
       opcount      0.0061      0.0000       0.001      0.0061      0.0061
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SLOAD__test_sload_bloated__True__erigon__regression.png)

![](figs/runtime/SLOAD__test_sload_bloated__True__erigon__bootstrap.png)

![](figs/runtime/SLOAD__test_sload_bloated__True__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.989
Model:                  NNLS                    Adj. R-squared:          0.989
No. Observations:       77                                RMSE:          29.25
Df Residuals:           75                                 MAE:          23.19
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.4507       1.000      0.0000      0.0000
       opcount      0.0132      0.0001       0.001      0.0131      0.0133
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SLOAD__test_sload_bloated__True__ethrex__regression.png)

![](figs/runtime/SLOAD__test_sload_bloated__True__ethrex__bootstrap.png)

![](figs/runtime/SLOAD__test_sload_bloated__True__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.974
Model:                  NNLS                    Adj. R-squared:          0.974
No. Observations:       99                                RMSE:          69.77
Df Residuals:           97                                 MAE:          60.65
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    583.1246     22.8890       0.001    541.8490    630.6861
       opcount      0.0207      0.0004       0.001      0.0199      0.0214
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SLOAD__test_sload_bloated__True__geth__regression.png)

![](figs/runtime/SLOAD__test_sload_bloated__True__geth__bootstrap.png)

![](figs/runtime/SLOAD__test_sload_bloated__True__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.984
Model:                  NNLS                    Adj. R-squared:          0.984
No. Observations:       77                                RMSE:          23.76
Df Residuals:           75                                 MAE:          18.67
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     48.8478      8.0778       0.001     33.4154     65.5931
       opcount      0.0090      0.0001       0.001      0.0087      0.0093
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SLOAD__test_sload_bloated__True__nethermind__regression.png)

![](figs/runtime/SLOAD__test_sload_bloated__True__nethermind__bootstrap.png)

![](figs/runtime/SLOAD__test_sload_bloated__True__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       110                               RMSE:          11.56
Df Residuals:           108                                MAE:           8.78
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     91.6272      3.1306       0.001     85.4935     97.7194
       opcount      0.0041      0.0001       0.001      0.0040      0.0042
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SLOAD__test_sload_bloated__True__reth__regression.png)

![](figs/runtime/SLOAD__test_sload_bloated__True__reth__bootstrap.png)

![](figs/runtime/SLOAD__test_sload_bloated__True__reth__diagnostics.png)

</details>

### test_sload_same_key_benchmark

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 264 | 0.4186 | 6.887e-05 | 1.00e-03 | [5.86e-05, 7.927e-05] |
| `erigon` | 110 | 0.855 | 1.582e-05 | 1.00e-03 | [1.431e-05, 1.738e-05] |
| `ethrex` | 154 | 0.8104 | 2.481e-05 | 1.00e-03 | [2.297e-05, 2.665e-05] |
| `geth` | 198 | 0.9364 | 4.733e-05 | 1.00e-03 | [4.554e-05, 4.92e-05] |
| `nethermind` | 154 | 0.6876 | 0.0001318 | 1.00e-03 | [0.0001179, 0.0001459] |
| `reth` | 220 | 0.452 | 8.31e-06 | 1.00e-03 | [7.151e-06, 9.509e-06] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.419
Model:                  NNLS                    Adj. R-squared:          0.416
No. Observations:       264                               RMSE:          51.28
Df Residuals:           262                                MAE:          40.33
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    126.6476     10.9017       0.001    105.5398    147.9106
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SLOAD__test_sload_same_key_benchmark__all__besu__regression.png)

![](figs/runtime/SLOAD__test_sload_same_key_benchmark__all__besu__bootstrap.png)

![](figs/runtime/SLOAD__test_sload_same_key_benchmark__all__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.855
Model:                  NNLS                    Adj. R-squared:          0.854
No. Observations:       110                               RMSE:           4.12
Df Residuals:           108                                MAE:           3.07
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     12.7888      1.6849       0.001      9.4845     16.0941
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SLOAD__test_sload_same_key_benchmark__all__erigon__regression.png)

![](figs/runtime/SLOAD__test_sload_same_key_benchmark__all__erigon__bootstrap.png)

![](figs/runtime/SLOAD__test_sload_same_key_benchmark__all__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.810
Model:                  NNLS                    Adj. R-squared:          0.809
No. Observations:       154                               RMSE:           7.58
Df Residuals:           152                                MAE:           5.90
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     16.0439      1.7487       0.001     12.5347     19.5371
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SLOAD__test_sload_same_key_benchmark__all__ethrex__regression.png)

![](figs/runtime/SLOAD__test_sload_same_key_benchmark__all__ethrex__bootstrap.png)

![](figs/runtime/SLOAD__test_sload_same_key_benchmark__all__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.936
Model:                  NNLS                    Adj. R-squared:          0.936
No. Observations:       198                               RMSE:           7.79
Df Residuals:           196                                MAE:           6.17
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     20.7510      1.8924       0.001     17.1068     24.3774
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SLOAD__test_sload_same_key_benchmark__all__geth__regression.png)

![](figs/runtime/SLOAD__test_sload_same_key_benchmark__all__geth__bootstrap.png)

![](figs/runtime/SLOAD__test_sload_same_key_benchmark__all__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.688
Model:                  NNLS                    Adj. R-squared:          0.686
No. Observations:       154                               RMSE:          56.12
Df Residuals:           152                                MAE:          36.80
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    128.4155     15.8295       0.001     97.2448    159.7043
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SLOAD__test_sload_same_key_benchmark__all__nethermind__regression.png)

![](figs/runtime/SLOAD__test_sload_same_key_benchmark__all__nethermind__bootstrap.png)

![](figs/runtime/SLOAD__test_sload_same_key_benchmark__all__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.452
Model:                  NNLS                    Adj. R-squared:          0.450
No. Observations:       220                               RMSE:           5.78
Df Residuals:           218                                MAE:           4.43
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      9.4651      1.1450       0.001      7.2497     11.6756
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SLOAD__test_sload_same_key_benchmark__all__reth__regression.png)

![](figs/runtime/SLOAD__test_sload_same_key_benchmark__all__reth__bootstrap.png)

![](figs/runtime/SLOAD__test_sload_same_key_benchmark__all__reth__diagnostics.png)

</details>

## SSTORE

### test_sstore_bloated — combo `False` — `presets[cold_storage_sstore_access]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.7981 | 0.01596 | 1.00e-03 | [0.01477, 0.01714] |
| `erigon` | 55 | 0.9971 | 0.006261 | 1.00e-03 | [0.006171, 0.006303] |
| `ethrex` | 77 | 0.9705 | 0.008411 | 1.00e-03 | [0.008278, 0.008519] |
| `geth` | 99 | 0.9743 | 0.02152 | 1.00e-03 | [0.02077, 0.02224] |
| `nethermind` | 77 | 0.9819 | 0.008657 | 1.00e-03 | [0.008408, 0.008899] |
| `reth` | 110 | 0.9816 | 0.003965 | 1.00e-03 | [0.003848, 0.004086] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.798
Model:                  NNLS                    Adj. R-squared:          0.797
No. Observations:       132                               RMSE:         167.09
Df Residuals:           130                                MAE:         145.02
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    542.6888     43.3526       0.001    458.9386    635.1418
       opcount      0.0160      0.0006       0.001      0.0148      0.0171
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__False__besu__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__besu__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.997
Model:                  NNLS                    Adj. R-squared:          0.997
No. Observations:       55                                RMSE:           7.06
Df Residuals:           53                                 MAE:           5.70
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      1.2249      2.0494       0.324      0.0000      6.6271
       opcount      0.0063      0.0000       0.001      0.0062      0.0063
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__False__erigon__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__erigon__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.971
Model:                  NNLS                    Adj. R-squared:          0.970
No. Observations:       77                                RMSE:          31.53
Df Residuals:           75                                 MAE:          24.98
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.8638       1.000      0.0000      2.1658
       opcount      0.0084      0.0001       0.001      0.0083      0.0085
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__False__ethrex__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__ethrex__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.974
Model:                  NNLS                    Adj. R-squared:          0.974
No. Observations:       99                                RMSE:          72.69
Df Residuals:           97                                 MAE:          59.56
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    581.8180     22.6342       0.001    539.9038    628.1256
       opcount      0.0215      0.0004       0.001      0.0208      0.0222
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__False__geth__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__geth__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       77                                RMSE:          24.48
Df Residuals:           75                                 MAE:          18.23
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     86.3936      8.1214       0.001     70.8493    102.9264
       opcount      0.0087      0.0001       0.001      0.0084      0.0089
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__False__nethermind__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__nethermind__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       110                               RMSE:          11.29
Df Residuals:           108                                MAE:           8.60
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     96.2000      3.5552       0.001     89.2942    103.2116
       opcount      0.0040      0.0001       0.001      0.0038      0.0041
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__False__reth__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__reth__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__reth__diagnostics.png)

</details>

### test_sstore_bloated — combo `True` — `presets[cold_storage_sstore_access]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8537 | 0.01985 | 1.00e-03 | [0.01857, 0.02119] |
| `erigon` | 55 | 0.9964 | 0.006054 | 1.00e-03 | [0.006018, 0.006083] |
| `ethrex` | 77 | 0.9807 | 0.0131 | 1.00e-03 | [0.01295, 0.01324] |
| `geth` | 99 | 0.9721 | 0.02067 | 1.00e-03 | [0.01987, 0.02136] |
| `nethermind` | 77 | 0.9877 | 0.009142 | 1.00e-03 | [0.008918, 0.009393] |
| `reth` | 110 | 0.9873 | 0.004062 | 1.00e-03 | [0.003959, 0.004159] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.854
Model:                  NNLS                    Adj. R-squared:          0.853
No. Observations:       132                               RMSE:         171.06
Df Residuals:           130                                MAE:         139.91
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    255.7700     39.6534       0.001    180.8497    334.9506
       opcount      0.0199      0.0007       0.001      0.0186      0.0212
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__True__besu__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__besu__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       55                                RMSE:           7.73
Df Residuals:           53                                 MAE:           6.40
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0061      0.0000       0.001      0.0060      0.0061
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__True__erigon__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__erigon__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.980
No. Observations:       77                                RMSE:          40.05
Df Residuals:           75                                 MAE:          31.92
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0131      0.0001       0.001      0.0129      0.0132
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__True__ethrex__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__ethrex__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.972
Model:                  NNLS                    Adj. R-squared:          0.972
No. Observations:       99                                RMSE:          72.92
Df Residuals:           97                                 MAE:          64.66
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    581.3024     24.8875       0.001    539.5430    634.0479
       opcount      0.0207      0.0004       0.001      0.0199      0.0214
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__True__geth__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__geth__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.988
Model:                  NNLS                    Adj. R-squared:          0.988
No. Observations:       77                                RMSE:          21.20
Df Residuals:           75                                 MAE:          17.11
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     26.5334      7.4027       0.001     11.4497     40.6135
       opcount      0.0091      0.0001       0.001      0.0089      0.0094
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__True__nethermind__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__nethermind__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.987
Model:                  NNLS                    Adj. R-squared:          0.987
No. Observations:       110                               RMSE:           9.60
Df Residuals:           108                                MAE:           7.56
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     93.9945      3.0007       0.001     88.2299    100.0954
       opcount      0.0041      0.0000       0.001      0.0040      0.0042
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__True__reth__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__reth__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__reth__diagnostics.png)

</details>

### test_sstore_bloated — combo `False` — `presets[cold_storage_sstore_write]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9055 | 0.1381 | 1.00e-03 | [0.1318, 0.1447] |
| `erigon` | 55 | 0.9961 | 0.2316 | 1.00e-03 | [0.2273, 0.2356] |
| `ethrex` | 77 | 1.11e-16 | 0 | 1.00e+00 | [0, 0] |
| `geth` | 99 | 0.8911 | 0.1347 | 1.00e-03 | [0.1252, 0.1443] |
| `nethermind` | 77 | 0.9659 | 0.07548 | 1.00e-03 | [0.07205, 0.07863] |
| `reth` | 110 | 0.8986 | 0.04119 | 1.00e-03 | [0.03836, 0.04387] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.906
Model:                  NNLS                    Adj. R-squared:          0.905
No. Observations:       132                               RMSE:          28.80
Df Residuals:           130                                MAE:          22.63
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     85.8977      6.8152       0.001     72.7433     98.8322
       opcount      0.1381      0.0033       0.001      0.1318      0.1447
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__False__besu__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__besu__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       55                                RMSE:           9.40
Df Residuals:           53                                 MAE:           7.50
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    144.2543      4.7362       0.001    135.8473    153.8983
       opcount      0.2316      0.0022       0.001      0.2273      0.2356
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__False__erigon__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__erigon__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.000
Model:                  NNLS                    Adj. R-squared:         -0.013
No. Observations:       77                                RMSE:         438.96
Df Residuals:           75                                 MAE:         426.80
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    832.8608     49.7662       0.001    731.1020    925.4442
       opcount      0.0000      0.0000       1.000      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__False__ethrex__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__ethrex__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.891
Model:                  NNLS                    Adj. R-squared:          0.890
No. Observations:       99                                RMSE:          30.43
Df Residuals:           97                                 MAE:          25.90
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    179.2414      9.9528       0.001    160.6233    198.8713
       opcount      0.1347      0.0048       0.001      0.1252      0.1443
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__False__geth__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__geth__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.966
Model:                  NNLS                    Adj. R-squared:          0.965
No. Observations:       77                                RMSE:           9.15
Df Residuals:           75                                 MAE:           6.94
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     57.1449      3.3127       0.001     51.0492     63.7687
       opcount      0.0755      0.0017       0.001      0.0720      0.0786
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__False__nethermind__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__nethermind__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.899
Model:                  NNLS                    Adj. R-squared:          0.898
No. Observations:       110                               RMSE:           8.94
Df Residuals:           108                                MAE:           6.61
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     49.4930      3.2465       0.001     43.4743     56.3338
       opcount      0.0412      0.0014       0.001      0.0384      0.0439
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__False__reth__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__reth__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__False__reth__diagnostics.png)

</details>

### test_sstore_bloated — combo `True` — `presets[cold_storage_sstore_write]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9775 | 0.0932 | 1.00e-03 | [0.09091, 0.09547] |
| `erigon` | 55 | 0.9904 | 0.1418 | 1.00e-03 | [0.138, 0.1456] |
| `ethrex` | 77 | 0.2401 | 0.01003 | 1.00e-03 | [0.006808, 0.01262] |
| `geth` | 99 | 0.9918 | 0.09248 | 1.00e-03 | [0.09055, 0.09421] |
| `nethermind` | 77 | 0.9728 | 0.05848 | 1.00e-03 | [0.05625, 0.0604] |
| `reth` | 110 | 0.9884 | 0.02709 | 1.00e-03 | [0.02663, 0.02759] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.977
Model:                  NNLS                    Adj. R-squared:          0.977
No. Observations:       132                               RMSE:          68.54
Df Residuals:           130                                MAE:          58.41
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    345.4943     17.6051       0.001    312.2457    379.3728
       opcount      0.0932      0.0012       0.001      0.0909      0.0955
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__True__besu__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__besu__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.990
Model:                  NNLS                    Adj. R-squared:          0.990
No. Observations:       55                                RMSE:          67.78
Df Residuals:           53                                 MAE:          60.72
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    547.6082     27.6143       0.001    494.9801    602.2389
       opcount      0.1418      0.0019       0.001      0.1380      0.1456
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__True__erigon__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__erigon__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.240
Model:                  NNLS                    Adj. R-squared:          0.230
No. Observations:       77                                RMSE:          86.44
Df Residuals:           75                                 MAE:          70.01
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    704.1671     27.3815       0.001    655.2748    763.8980
       opcount      0.0100      0.0015       0.001      0.0068      0.0126
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__True__ethrex__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__ethrex__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.992
Model:                  NNLS                    Adj. R-squared:          0.992
No. Observations:       99                                RMSE:          40.74
Df Residuals:           97                                 MAE:          34.38
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    495.8116     13.2839       0.001    471.2143    524.7788
       opcount      0.0925      0.0009       0.001      0.0905      0.0942
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__True__geth__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__geth__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.973
Model:                  NNLS                    Adj. R-squared:          0.972
No. Observations:       77                                RMSE:          47.34
Df Residuals:           75                                 MAE:          36.45
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    155.5479     15.4120       0.001    128.2200    188.0642
       opcount      0.0585      0.0011       0.001      0.0562      0.0604
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__True__nethermind__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__nethermind__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.988
Model:                  NNLS                    Adj. R-squared:          0.988
No. Observations:       110                               RMSE:          14.20
Df Residuals:           108                                MAE:          10.69
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    122.9355      4.0313       0.001    114.7963    131.0930
       opcount      0.0271      0.0002       0.001      0.0266      0.0276
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/SSTORE__test_sstore_bloated__True__reth__regression.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__reth__bootstrap.png)

![](figs/runtime/SSTORE__test_sstore_bloated__True__reth__diagnostics.png)

</details>

## BALANCE

### test_ext_account_query_warm — combo `BALANCE`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.3515 | 8.465e-05 | 1.00e-03 | [6.595e-05, 0.0001023] |
| `erigon` | 55 | 0.8709 | 1.98e-05 | 1.00e-03 | [1.784e-05, 2.172e-05] |
| `ethrex` | 77 | 0.7653 | 1.39e-05 | 1.00e-03 | [1.221e-05, 1.56e-05] |
| `geth` | 99 | 0.6207 | 1.786e-05 | 1.00e-03 | [1.467e-05, 2.09e-05] |
| `nethermind` | 77 | 0.6863 | 0.0001224 | 1.00e-03 | [0.0001036, 0.0001404] |
| `reth` | 110 | 0.5505 | 1.231e-05 | 1.00e-03 | [1.07e-05, 1.394e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.352
Model:                  NNLS                    Adj. R-squared:          0.347
No. Observations:       132                               RMSE:          67.25
Df Residuals:           130                                MAE:          49.25
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    193.8436     18.6526       0.001    158.7041    233.5793
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_ext_account_query_warm__BALANCE__besu__regression.png)

![](figs/runtime/BALANCE__test_ext_account_query_warm__BALANCE__besu__bootstrap.png)

![](figs/runtime/BALANCE__test_ext_account_query_warm__BALANCE__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.871
Model:                  NNLS                    Adj. R-squared:          0.868
No. Observations:       55                                RMSE:           4.46
Df Residuals:           53                                 MAE:           3.35
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     15.2891      1.8979       0.001     11.6690     19.0934
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_ext_account_query_warm__BALANCE__erigon__regression.png)

![](figs/runtime/BALANCE__test_ext_account_query_warm__BALANCE__erigon__bootstrap.png)

![](figs/runtime/BALANCE__test_ext_account_query_warm__BALANCE__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.765
Model:                  NNLS                    Adj. R-squared:          0.762
No. Observations:       77                                RMSE:           4.50
Df Residuals:           75                                 MAE:           3.51
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      9.6337      1.7409       0.001      6.1758     13.0008
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_ext_account_query_warm__BALANCE__ethrex__regression.png)

![](figs/runtime/BALANCE__test_ext_account_query_warm__BALANCE__ethrex__bootstrap.png)

![](figs/runtime/BALANCE__test_ext_account_query_warm__BALANCE__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.621
Model:                  NNLS                    Adj. R-squared:          0.617
No. Observations:       99                                RMSE:           8.17
Df Residuals:           97                                 MAE:           6.77
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     42.1157      3.1054       0.001     36.1309     48.0741
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_ext_account_query_warm__BALANCE__geth__regression.png)

![](figs/runtime/BALANCE__test_ext_account_query_warm__BALANCE__geth__bootstrap.png)

![](figs/runtime/BALANCE__test_ext_account_query_warm__BALANCE__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.686
Model:                  NNLS                    Adj. R-squared:          0.682
No. Observations:       77                                RMSE:          48.43
Df Residuals:           75                                 MAE:          30.22
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    133.4252     18.2186       0.001    101.0221    170.6921
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_ext_account_query_warm__BALANCE__nethermind__regression.png)

![](figs/runtime/BALANCE__test_ext_account_query_warm__BALANCE__nethermind__bootstrap.png)

![](figs/runtime/BALANCE__test_ext_account_query_warm__BALANCE__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.550
Model:                  NNLS                    Adj. R-squared:          0.546
No. Observations:       110                               RMSE:           6.51
Df Residuals:           108                                MAE:           5.05
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     11.3470      1.5326       0.001      8.4866     14.2248
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_ext_account_query_warm__BALANCE__reth__regression.png)

![](figs/runtime/BALANCE__test_ext_account_query_warm__BALANCE__reth__bootstrap.png)

![](figs/runtime/BALANCE__test_ext_account_query_warm__BALANCE__reth__diagnostics.png)

</details>

### test_account_access — combo `BALANCE_AccountMode.EXISTING_EOA`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9024 | 0.03207 | 1.00e-03 | [0.03029, 0.03367] |
| `erigon` | 55 | 0.9959 | 0.008412 | 1.00e-03 | [0.008366, 0.008459] |
| `ethrex` | 77 | 0.982 | 0.01823 | 1.00e-03 | [0.01759, 0.01891] |
| `geth` | 99 | 0.9969 | 0.02081 | 1.00e-03 | [0.02058, 0.02104] |
| `nethermind` | 77 | 0.9838 | 0.01077 | 1.00e-03 | [0.01043, 0.01111] |
| `reth` | 110 | 0.9827 | 0.004445 | 1.00e-03 | [0.004335, 0.004557] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.902
Model:                  NNLS                    Adj. R-squared:          0.902
No. Observations:       132                               RMSE:         217.76
Df Residuals:           130                                MAE:         204.18
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    239.9926     56.4992       0.001    134.2017    351.7851
       opcount      0.0321      0.0009       0.001      0.0303      0.0337
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_EOA__besu__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_EOA__besu__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_EOA__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       55                                RMSE:          11.56
Df Residuals:           53                                 MAE:           9.51
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0084      0.0000       0.001      0.0084      0.0085
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_EOA__erigon__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_EOA__erigon__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_EOA__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       77                                RMSE:          50.98
Df Residuals:           75                                 MAE:          45.19
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    226.0302     23.6555       0.001    180.3134    272.7324
       opcount      0.0182      0.0003       0.001      0.0176      0.0189
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_EOA__ethrex__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_EOA__ethrex__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_EOA__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.997
Model:                  NNLS                    Adj. R-squared:          0.997
No. Observations:       99                                RMSE:          23.88
Df Residuals:           97                                 MAE:          19.28
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    397.9811      7.4708       0.001    383.3288    413.0056
       opcount      0.0208      0.0001       0.001      0.0206      0.0210
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_EOA__geth__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_EOA__geth__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_EOA__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.984
Model:                  NNLS                    Adj. R-squared:          0.984
No. Observations:       77                                RMSE:          28.56
Df Residuals:           75                                 MAE:          22.34
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     88.3113     10.9986       0.001     67.1510    110.6875
       opcount      0.0108      0.0002       0.001      0.0104      0.0111
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_EOA__nethermind__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_EOA__nethermind__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_EOA__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.983
Model:                  NNLS                    Adj. R-squared:          0.983
No. Observations:       110                               RMSE:          12.18
Df Residuals:           108                                MAE:           9.78
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     99.9705      3.6418       0.001     92.9238    106.9524
       opcount      0.0044      0.0001       0.001      0.0043      0.0046
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_EOA__reth__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_EOA__reth__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_EOA__reth__diagnostics.png)

</details>

### test_account_access — combo `BALANCE_AccountMode.NON_EXISTING_ACCOUNT` — `presets[cold_account_nocode_access]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9114 | 0.03188 | 1.00e-03 | [0.03013, 0.03356] |
| `erigon` | 55 | 0.9953 | 0.007971 | 1.00e-03 | [0.007913, 0.008018] |
| `ethrex` | 77 | 0.9383 | 0.002276 | 1.00e-03 | [0.002137, 0.002416] |
| `geth` | 99 | 0.9973 | 0.01995 | 1.00e-03 | [0.01974, 0.02017] |
| `nethermind` | 77 | 0.9725 | 0.01039 | 1.00e-03 | [0.01002, 0.01078] |
| `reth` | 110 | 0.9819 | 0.004397 | 1.00e-03 | [0.004263, 0.004539] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.911
Model:                  NNLS                    Adj. R-squared:          0.911
No. Observations:       132                               RMSE:         205.21
Df Residuals:           130                                MAE:         191.28
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    215.6906     54.8941       0.001    109.1148    326.2775
       opcount      0.0319      0.0009       0.001      0.0301      0.0336
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__besu__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__besu__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.995
Model:                  NNLS                    Adj. R-squared:          0.995
No. Observations:       55                                RMSE:          11.76
Df Residuals:           53                                 MAE:           9.24
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0080      0.0000       0.001      0.0079      0.0080
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__erigon__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__erigon__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.938
Model:                  NNLS                    Adj. R-squared:          0.937
No. Observations:       77                                RMSE:          12.05
Df Residuals:           75                                 MAE:           9.43
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    124.0749      4.1955       0.001    115.6790    132.0513
       opcount      0.0023      0.0001       0.001      0.0021      0.0024
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.997
Model:                  NNLS                    Adj. R-squared:          0.997
No. Observations:       99                                RMSE:          21.55
Df Residuals:           97                                 MAE:          17.41
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    404.8755      7.1638       0.001    391.2822    418.7663
       opcount      0.0200      0.0001       0.001      0.0197      0.0202
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__geth__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__geth__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.973
Model:                  NNLS                    Adj. R-squared:          0.972
No. Observations:       77                                RMSE:          36.08
Df Residuals:           75                                 MAE:          27.30
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    105.0961     12.9259       0.001     79.5407    129.5486
       opcount      0.0104      0.0002       0.001      0.0100      0.0108
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       110                               RMSE:          12.32
Df Residuals:           108                                MAE:           9.47
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    101.3918      4.3239       0.001     92.6221    109.5483
       opcount      0.0044      0.0001       0.001      0.0043      0.0045
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__reth__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__reth__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__reth__diagnostics.png)

</details>

### test_account_access — combo `BALANCE_AccountMode.EXISTING_CONTRACT_DIFF_MAX`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8889 | 0.0444 | 1.00e-03 | [0.04173, 0.04703] |
| `erigon` | 55 | 0.9394 | 0.02414 | 1.00e-03 | [0.02261, 0.02556] |
| `ethrex` | 77 | 0.9808 | 0.01853 | 1.00e-03 | [0.01782, 0.0192] |
| `geth` | 99 | 0.9836 | 0.02103 | 1.00e-03 | [0.02031, 0.02173] |
| `nethermind` | 77 | 0.973 | 0.01175 | 1.00e-03 | [0.01131, 0.01222] |
| `reth` | 110 | 0.9924 | 0.02032 | 1.00e-03 | [0.01993, 0.02068] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.889
Model:                  NNLS                    Adj. R-squared:          0.888
No. Observations:       132                               RMSE:         319.16
Df Residuals:           130                                MAE:         262.60
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    828.0517     89.4074       0.001    655.9746    998.8496
       opcount      0.0444      0.0014       0.001      0.0417      0.0470
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.939
Model:                  NNLS                    Adj. R-squared:          0.938
No. Observations:       55                                RMSE:         124.65
Df Residuals:           53                                 MAE:         108.27
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    288.1052     58.0084       0.001    187.0824    408.2465
       opcount      0.0241      0.0008       0.001      0.0226      0.0256
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.980
No. Observations:       77                                RMSE:          52.79
Df Residuals:           75                                 MAE:          46.76
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    223.6683     25.4864       0.001    178.1340    275.2793
       opcount      0.0185      0.0004       0.001      0.0178      0.0192
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.984
Model:                  NNLS                    Adj. R-squared:          0.983
No. Observations:       99                                RMSE:          55.18
Df Residuals:           97                                 MAE:          40.68
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    312.6303     28.2144       0.001    258.9236    368.7557
       opcount      0.0210      0.0004       0.001      0.0203      0.0217
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.973
Model:                  NNLS                    Adj. R-squared:          0.973
No. Observations:       77                                RMSE:          39.78
Df Residuals:           75                                 MAE:          30.71
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    114.6838     14.4014       0.001     85.5003    141.7331
       opcount      0.0118      0.0002       0.001      0.0113      0.0122
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.992
Model:                  NNLS                    Adj. R-squared:          0.992
No. Observations:       110                               RMSE:          36.15
Df Residuals:           108                                MAE:          27.29
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    137.0920     13.3297       0.001    112.2493    164.4823
       opcount      0.0203      0.0002       0.001      0.0199      0.0207
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__diagnostics.png)

</details>

### test_account_access — combo `BALANCE_AccountMode.EXISTING_CONTRACT_MINIMAL`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8438 | 0.02635 | 1.00e-03 | [0.02448, 0.02826] |
| `erigon` | 55 | 0.9371 | 0.02381 | 1.00e-03 | [0.0221, 0.02522] |
| `ethrex` | 77 | 0.9809 | 0.01855 | 1.00e-03 | [0.01787, 0.01917] |
| `geth` | 99 | 0.996 | 0.01997 | 1.00e-03 | [0.01968, 0.02022] |
| `nethermind` | 77 | 0.9708 | 0.01113 | 1.00e-03 | [0.01076, 0.01152] |
| `reth` | 110 | 0.9802 | 0.004859 | 1.00e-03 | [0.004723, 0.004995] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.844
Model:                  NNLS                    Adj. R-squared:          0.843
No. Observations:       132                               RMSE:         230.48
Df Residuals:           130                                MAE:         215.40
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    346.6338     60.1084       0.001    228.9422    461.4735
       opcount      0.0264      0.0010       0.001      0.0245      0.0283
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.937
Model:                  NNLS                    Adj. R-squared:          0.936
No. Observations:       55                                RMSE:         125.40
Df Residuals:           53                                 MAE:         108.97
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    280.6998     57.2455       0.001    180.3325    405.0354
       opcount      0.0238      0.0008       0.001      0.0221      0.0252
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          52.65
Df Residuals:           75                                 MAE:          45.98
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    221.6662     23.9051       0.001    179.5466    270.8085
       opcount      0.0185      0.0003       0.001      0.0179      0.0192
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          25.76
Df Residuals:           97                                 MAE:          20.75
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    397.0927      8.9033       0.001    381.5073    416.3752
       opcount      0.0200      0.0001       0.001      0.0197      0.0202
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.971
Model:                  NNLS                    Adj. R-squared:          0.970
No. Observations:       77                                RMSE:          39.25
Df Residuals:           75                                 MAE:          31.46
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    142.5326     11.7309       0.001    120.4153    166.3214
       opcount      0.0111      0.0002       0.001      0.0108      0.0115
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.980
Model:                  NNLS                    Adj. R-squared:          0.980
No. Observations:       110                               RMSE:          14.06
Df Residuals:           108                                MAE:          11.37
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     87.6840      4.5665       0.001     79.1407     96.9594
       opcount      0.0049      0.0001       0.001      0.0047      0.0050
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__diagnostics.png)

</details>

### test_account_access — combo `BALANCE_AccountMode.EXISTING_CONTRACT_SAME_MAX`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.83 | 0.02647 | 1.00e-03 | [0.02463, 0.02836] |
| `erigon` | 55 | 0.9374 | 0.02385 | 1.00e-03 | [0.02218, 0.02524] |
| `ethrex` | 77 | 0.9809 | 0.01854 | 1.00e-03 | [0.01789, 0.0192] |
| `geth` | 99 | 0.9958 | 0.01993 | 1.00e-03 | [0.01965, 0.02018] |
| `nethermind` | 77 | 0.9789 | 0.01163 | 1.00e-03 | [0.01128, 0.01197] |
| `reth` | 110 | 0.9821 | 0.004817 | 1.00e-03 | [0.0047, 0.004938] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.830
Model:                  NNLS                    Adj. R-squared:          0.829
No. Observations:       132                               RMSE:         243.58
Df Residuals:           130                                MAE:         227.11
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    349.2422     60.1863       0.001    224.9271    465.5263
       opcount      0.0265      0.0010       0.001      0.0246      0.0284
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.937
Model:                  NNLS                    Adj. R-squared:          0.936
No. Observations:       55                                RMSE:         125.30
Df Residuals:           53                                 MAE:         108.92
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    276.1860     57.2930       0.001    176.1556    396.7848
       opcount      0.0239      0.0008       0.001      0.0222      0.0252
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          52.57
Df Residuals:           75                                 MAE:          46.98
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    221.3793     23.6199       0.001    175.8896    269.9365
       opcount      0.0185      0.0003       0.001      0.0179      0.0192
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          26.26
Df Residuals:           97                                 MAE:          21.72
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    396.9844      8.5175       0.001    381.7001    415.5806
       opcount      0.0199      0.0001       0.001      0.0197      0.0202
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.979
Model:                  NNLS                    Adj. R-squared:          0.979
No. Observations:       77                                RMSE:          34.71
Df Residuals:           75                                 MAE:          26.66
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    114.2191     12.0383       0.001     90.5911    137.7451
       opcount      0.0116      0.0002       0.001      0.0113      0.0120
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       110                               RMSE:          13.23
Df Residuals:           108                                MAE:          10.41
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     87.9884      3.9124       0.001     80.5301     95.6849
       opcount      0.0048      0.0001       0.001      0.0047      0.0049
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__diagnostics.png)

</details>

### test_account_access — combo `BALANCE_AccountMode.NON_EXISTING_ACCOUNT` — `models.custom[0]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9114 | 0.03188 | 1.00e-03 | [0.03013, 0.03356] |
| `erigon` | 55 | 0.9953 | 0.007971 | 1.00e-03 | [0.007913, 0.008018] |
| `ethrex` | 77 | 0.9383 | 0.002276 | 1.00e-03 | [0.002137, 0.002416] |
| `geth` | 99 | 0.9973 | 0.01995 | 1.00e-03 | [0.01974, 0.02017] |
| `nethermind` | 77 | 0.9725 | 0.01039 | 1.00e-03 | [0.01002, 0.01078] |
| `reth` | 110 | 0.9819 | 0.004397 | 1.00e-03 | [0.004263, 0.004539] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.911
Model:                  NNLS                    Adj. R-squared:          0.911
No. Observations:       132                               RMSE:         205.21
Df Residuals:           130                                MAE:         191.28
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    215.6906     54.8941       0.001    109.1148    326.2775
       opcount      0.0319      0.0009       0.001      0.0301      0.0336
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__besu__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__besu__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.995
Model:                  NNLS                    Adj. R-squared:          0.995
No. Observations:       55                                RMSE:          11.76
Df Residuals:           53                                 MAE:           9.24
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0080      0.0000       0.001      0.0079      0.0080
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__erigon__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__erigon__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.938
Model:                  NNLS                    Adj. R-squared:          0.937
No. Observations:       77                                RMSE:          12.05
Df Residuals:           75                                 MAE:           9.43
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    124.0749      4.1955       0.001    115.6790    132.0513
       opcount      0.0023      0.0001       0.001      0.0021      0.0024
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.997
Model:                  NNLS                    Adj. R-squared:          0.997
No. Observations:       99                                RMSE:          21.55
Df Residuals:           97                                 MAE:          17.41
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    404.8755      7.1638       0.001    391.2822    418.7663
       opcount      0.0200      0.0001       0.001      0.0197      0.0202
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__geth__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__geth__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.973
Model:                  NNLS                    Adj. R-squared:          0.972
No. Observations:       77                                RMSE:          36.08
Df Residuals:           75                                 MAE:          27.30
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    105.0961     12.9259       0.001     79.5407    129.5486
       opcount      0.0104      0.0002       0.001      0.0100      0.0108
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       110                               RMSE:          12.32
Df Residuals:           108                                MAE:           9.47
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    101.3918      4.3239       0.001     92.6221    109.5483
       opcount      0.0044      0.0001       0.001      0.0043      0.0045
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__reth__regression.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__reth__bootstrap.png)

![](figs/runtime/BALANCE__test_account_access__BALANCE_AccountMode_NON_EXISTING_ACCOUNT__reth__diagnostics.png)

</details>

## CALL

### test_ext_account_query_warm — combo `CALL`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.6373 | 0.0004188 | 1.00e-03 | [0.0003605, 0.0004708] |
| `erigon` | 55 | 0.926 | 0.0001165 | 1.00e-03 | [0.000108, 0.000125] |
| `ethrex` | 77 | 0.9463 | 9.428e-05 | 1.00e-03 | [8.911e-05, 9.932e-05] |
| `geth` | 99 | 0.9433 | 0.0001325 | 1.00e-03 | [0.0001263, 0.0001391] |
| `nethermind` | 77 | 0.8742 | 0.000359 | 1.00e-03 | [0.0003311, 0.0003864] |
| `reth` | 110 | 0.9394 | 5.838e-05 | 1.00e-03 | [5.567e-05, 6.128e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.637
Model:                  NNLS                    Adj. R-squared:          0.635
No. Observations:       132                               RMSE:         159.67
Df Residuals:           130                                MAE:         121.84
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    669.5003     45.2301       0.001    586.5851    762.0959
       opcount      0.0004      0.0000       0.001      0.0004      0.0005
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_ext_account_query_warm__CALL__besu__regression.png)

![](figs/runtime/CALL__test_ext_account_query_warm__CALL__besu__bootstrap.png)

![](figs/runtime/CALL__test_ext_account_query_warm__CALL__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.926
Model:                  NNLS                    Adj. R-squared:          0.925
No. Observations:       55                                RMSE:          16.65
Df Residuals:           53                                 MAE:          13.81
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     33.7495      7.2737       0.001     20.0439     48.1946
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_ext_account_query_warm__CALL__erigon__regression.png)

![](figs/runtime/CALL__test_ext_account_query_warm__CALL__erigon__bootstrap.png)

![](figs/runtime/CALL__test_ext_account_query_warm__CALL__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.946
Model:                  NNLS                    Adj. R-squared:          0.946
No. Observations:       77                                RMSE:          11.35
Df Residuals:           75                                 MAE:           9.37
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     46.2367      4.1680       0.001     38.1041     54.9302
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_ext_account_query_warm__CALL__ethrex__regression.png)

![](figs/runtime/CALL__test_ext_account_query_warm__CALL__ethrex__bootstrap.png)

![](figs/runtime/CALL__test_ext_account_query_warm__CALL__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.943
Model:                  NNLS                    Adj. R-squared:          0.943
No. Observations:       99                                RMSE:          16.42
Df Residuals:           97                                 MAE:          12.77
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     47.2950      5.3201       0.001     37.3225     58.1605
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_ext_account_query_warm__CALL__geth__regression.png)

![](figs/runtime/CALL__test_ext_account_query_warm__CALL__geth__bootstrap.png)

![](figs/runtime/CALL__test_ext_account_query_warm__CALL__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.874
Model:                  NNLS                    Adj. R-squared:          0.873
No. Observations:       77                                RMSE:          68.82
Df Residuals:           75                                 MAE:          50.88
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    237.7322     24.7069       0.001    192.8647    284.6407
       opcount      0.0004      0.0000       0.001      0.0003      0.0004
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_ext_account_query_warm__CALL__nethermind__regression.png)

![](figs/runtime/CALL__test_ext_account_query_warm__CALL__nethermind__bootstrap.png)

![](figs/runtime/CALL__test_ext_account_query_warm__CALL__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.939
Model:                  NNLS                    Adj. R-squared:          0.939
No. Observations:       110                               RMSE:           7.49
Df Residuals:           108                                MAE:           5.94
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     25.1596      2.4793       0.001     20.3404     29.8218
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_ext_account_query_warm__CALL__reth__regression.png)

![](figs/runtime/CALL__test_ext_account_query_warm__CALL__reth__bootstrap.png)

![](figs/runtime/CALL__test_ext_account_query_warm__CALL__reth__diagnostics.png)

</details>

### test_account_access — combo `CALL_AccountMode.EXISTING_EOA` — `presets[cold_account_nocode_access]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9069 | 0.03391 | 1.00e-03 | [0.03219, 0.03577] |
| `erigon` | 55 | 0.9965 | 0.008692 | 1.00e-03 | [0.008646, 0.008736] |
| `ethrex` | 77 | 0.9818 | 0.01835 | 1.00e-03 | [0.01774, 0.01897] |
| `geth` | 99 | 0.9958 | 0.02101 | 1.00e-03 | [0.02075, 0.02126] |
| `nethermind` | 77 | 0.9715 | 0.01093 | 1.00e-03 | [0.01052, 0.01138] |
| `reth` | 110 | 0.9777 | 0.004759 | 1.00e-03 | [0.004617, 0.004899] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.907
Model:                  NNLS                    Adj. R-squared:          0.906
No. Observations:       132                               RMSE:         223.18
Df Residuals:           130                                MAE:         203.57
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    315.3350     59.6878       0.001    201.2761    421.2183
       opcount      0.0339      0.0009       0.001      0.0322      0.0358
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__besu__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__besu__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.997
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       55                                RMSE:          10.79
Df Residuals:           53                                 MAE:           9.24
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0087      0.0000       0.001      0.0086      0.0087
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__erigon__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__erigon__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       77                                RMSE:          51.26
Df Residuals:           75                                 MAE:          45.21
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    227.6326     22.9920       0.001    181.7989    271.6624
       opcount      0.0184      0.0003       0.001      0.0177      0.0190
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__ethrex__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__ethrex__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          27.93
Df Residuals:           97                                 MAE:          23.04
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    402.2064      8.6719       0.001    386.0550    419.1422
       opcount      0.0210      0.0001       0.001      0.0207      0.0213
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__geth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__geth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.971
Model:                  NNLS                    Adj. R-squared:          0.971
No. Observations:       77                                RMSE:          38.48
Df Residuals:           75                                 MAE:          29.14
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    108.1632     13.3971       0.001     82.6770    134.7877
       opcount      0.0109      0.0002       0.001      0.0105      0.0114
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__nethermind__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__nethermind__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.978
Model:                  NNLS                    Adj. R-squared:          0.978
No. Observations:       110                               RMSE:          14.75
Df Residuals:           108                                MAE:          11.83
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     99.3597      4.5232       0.001     90.8069    108.4872
       opcount      0.0048      0.0001       0.001      0.0046      0.0049
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__reth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__reth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__reth__diagnostics.png)

</details>

### test_account_access — combo `CALL_AccountMode.NON_EXISTING_ACCOUNT` — `presets[cold_account_nocode_access]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8981 | 0.0334 | 1.00e-03 | [0.03154, 0.03521] |
| `erigon` | 55 | 0.9936 | 0.008314 | 1.00e-03 | [0.008249, 0.008374] |
| `ethrex` | 77 | 0.9669 | 0.00246 | 1.00e-03 | [0.002356, 0.002568] |
| `geth` | 99 | 0.9957 | 0.02069 | 1.00e-03 | [0.02038, 0.02096] |
| `nethermind` | 77 | 0.9851 | 0.01087 | 1.00e-03 | [0.01056, 0.01119] |
| `reth` | 110 | 0.9826 | 0.004481 | 1.00e-03 | [0.004369, 0.004597] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.898
Model:                  NNLS                    Adj. R-squared:          0.897
No. Observations:       132                               RMSE:         231.05
Df Residuals:           130                                MAE:         216.15
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    391.7732     61.8925       0.001    269.0330    511.1143
       opcount      0.0334      0.0009       0.001      0.0315      0.0352
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__besu__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__besu__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.994
Model:                  NNLS                    Adj. R-squared:          0.993
No. Observations:       55                                RMSE:          14.28
Df Residuals:           53                                 MAE:          11.82
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0083      0.0000       0.001      0.0082      0.0084
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.967
Model:                  NNLS                    Adj. R-squared:          0.966
No. Observations:       77                                RMSE:           9.35
Df Residuals:           75                                 MAE:           7.93
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    117.9447      3.3061       0.001    111.4095    124.4757
       opcount      0.0025      0.0001       0.001      0.0024      0.0026
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          27.84
Df Residuals:           97                                 MAE:          22.18
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    388.7103      9.0974       0.001    371.8382    408.7596
       opcount      0.0207      0.0001       0.001      0.0204      0.0210
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__geth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__geth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.985
Model:                  NNLS                    Adj. R-squared:          0.985
No. Observations:       77                                RMSE:          27.49
Df Residuals:           75                                 MAE:          23.21
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    103.4762     10.5576       0.001     82.6607    123.5186
       opcount      0.0109      0.0002       0.001      0.0106      0.0112
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.983
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       110                               RMSE:          12.25
Df Residuals:           108                                MAE:           9.94
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    104.3896      3.7154       0.001     97.1654    111.7209
       opcount      0.0045      0.0001       0.001      0.0044      0.0046
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__reth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__reth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__reth__diagnostics.png)

</details>

### test_account_access — combo `CALL_AccountMode.EXISTING_EOA` — `presets[cold_account_nocode_write]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9656 | 0.117 | 1.00e-03 | [0.1131, 0.1212] |
| `erigon` | 55 | 0.9903 | 0.1486 | 1.00e-03 | [0.1443, 0.1529] |
| `ethrex` | 77 | 0.9915 | 0.03608 | 1.00e-03 | [0.03537, 0.03682] |
| `geth` | 99 | 0.9972 | 0.1027 | 1.00e-03 | [0.1015, 0.1039] |
| `nethermind` | 77 | 0.9792 | 0.06534 | 1.00e-03 | [0.06313, 0.06768] |
| `reth` | 110 | 0.9887 | 0.0343 | 1.00e-03 | [0.03359, 0.03505] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.966
Model:                  NNLS                    Adj. R-squared:          0.965
No. Observations:       132                               RMSE:         104.28
Df Residuals:           130                                MAE:          90.33
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    322.4523     30.7628       0.001    261.7857    384.0511
       opcount      0.1170      0.0020       0.001      0.1131      0.1212
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__besu__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__besu__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.990
Model:                  NNLS                    Adj. R-squared:          0.990
No. Observations:       55                                RMSE:          69.66
Df Residuals:           53                                 MAE:          58.66
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    506.0957     30.2184       0.001    446.2050    564.1082
       opcount      0.1486      0.0022       0.001      0.1443      0.1529
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__erigon__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__erigon__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.991
Model:                  NNLS                    Adj. R-squared:          0.991
No. Observations:       77                                RMSE:          15.80
Df Residuals:           75                                 MAE:          12.64
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    284.4040      4.8435       0.001    274.9004    293.7525
       opcount      0.0361      0.0004       0.001      0.0354      0.0368
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__ethrex__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__ethrex__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.997
Model:                  NNLS                    Adj. R-squared:          0.997
No. Observations:       99                                RMSE:          25.66
Df Residuals:           97                                 MAE:          20.36
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    394.9779      8.8101       0.001    378.1891    413.4410
       opcount      0.1027      0.0006       0.001      0.1015      0.1039
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__geth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__geth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.979
Model:                  NNLS                    Adj. R-squared:          0.979
No. Observations:       77                                RMSE:          44.98
Df Residuals:           75                                 MAE:          35.07
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    182.8859     14.7395       0.001    155.2952    212.2066
       opcount      0.0653      0.0011       0.001      0.0631      0.0677
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__nethermind__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__nethermind__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.989
Model:                  NNLS                    Adj. R-squared:          0.989
No. Observations:       110                               RMSE:          17.30
Df Residuals:           108                                MAE:          14.16
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    101.9993      5.6343       0.001     90.8353    113.1107
       opcount      0.0343      0.0004       0.001      0.0336      0.0351
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__reth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__reth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_EOA__reth__diagnostics.png)

</details>

### test_account_access — combo `CALL_AccountMode.NON_EXISTING_ACCOUNT` — `presets[cold_account_nocode_write]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8599 | 0.179 | 1.00e-03 | [0.1644, 0.1944] |
| `erigon` | 55 | 0.9886 | 0.2745 | 1.00e-03 | [0.2657, 0.2826] |
| `ethrex` | 77 | 0.8225 | 0.0482 | 1.00e-03 | [0.04244, 0.05395] |
| `geth` | 99 | 0.9844 | 0.159 | 1.00e-03 | [0.1547, 0.163] |
| `nethermind` | 77 | 0.8977 | 0.09912 | 1.00e-03 | [0.09135, 0.1076] |
| `reth` | 110 | 0.8983 | 0.05438 | 1.00e-03 | [0.05078, 0.05775] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.860
Model:                  NNLS                    Adj. R-squared:          0.859
No. Observations:       132                               RMSE:          24.90
Df Residuals:           130                                MAE:          19.82
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     70.8872      7.0867       0.001     57.1010     84.3282
       opcount      0.1790      0.0077       0.001      0.1644      0.1944
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__besu__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__besu__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.989
Model:                  NNLS                    Adj. R-squared:          0.988
No. Observations:       55                                RMSE:          10.18
Df Residuals:           53                                 MAE:           8.77
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     95.2677      4.2087       0.001     87.2662    104.2974
       opcount      0.2745      0.0042       0.001      0.2657      0.2826
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.822
Model:                  NNLS                    Adj. R-squared:          0.820
No. Observations:       77                                RMSE:           7.72
Df Residuals:           75                                 MAE:           6.19
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    228.6784      3.2171       0.001    222.6458    235.2481
       opcount      0.0482      0.0029       0.001      0.0424      0.0539
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.984
Model:                  NNLS                    Adj. R-squared:          0.984
No. Observations:       99                                RMSE:           6.89
Df Residuals:           97                                 MAE:           5.53
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     41.0963      2.2590       0.001     36.6716     45.7252
       opcount      0.1590      0.0021       0.001      0.1547      0.1630
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__geth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__geth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.898
Model:                  NNLS                    Adj. R-squared:          0.896
No. Observations:       77                                RMSE:          11.53
Df Residuals:           75                                 MAE:           7.67
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     25.0800      4.0673       0.001     16.7675     33.3598
       opcount      0.0991      0.0040       0.001      0.0914      0.1076
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.898
Model:                  NNLS                    Adj. R-squared:          0.897
No. Observations:       110                               RMSE:           6.31
Df Residuals:           108                                MAE:           5.22
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     16.2181      1.9607       0.001     12.5049     20.0542
       opcount      0.0544      0.0018       0.001      0.0508      0.0577
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__reth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__reth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__reth__diagnostics.png)

</details>

### test_account_access — combo `CALL_AccountMode.EXISTING_CONTRACT_DIFF_MAX` — `models.custom[0]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8886 | 0.04706 | 1.00e-03 | [0.04427, 0.04966] |
| `erigon` | 55 | 0.8993 | 0.1558 | 1.00e-03 | [0.1402, 0.1672] |
| `ethrex` | 77 | 0.9971 | 0.1006 | 1.00e-03 | [0.09946, 0.1018] |
| `geth` | 99 | 0.9352 | 0.04195 | 1.00e-03 | [0.03959, 0.04469] |
| `nethermind` | 77 | 0.9143 | 0.0368 | 1.00e-03 | [0.03413, 0.03969] |
| `reth` | 110 | 0.9956 | 0.0236 | 1.00e-03 | [0.02331, 0.0239] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.889
Model:                  NNLS                    Adj. R-squared:          0.888
No. Observations:       132                               RMSE:         337.01
Df Residuals:           130                                MAE:         282.38
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    897.2382     87.4597       0.001    730.9394   1068.4426
       opcount      0.0471      0.0014       0.001      0.0443      0.0497
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.899
Model:                  NNLS                    Adj. R-squared:          0.897
No. Observations:       55                                RMSE:        1054.18
Df Residuals:           53                                 MAE:         909.26
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    907.8150    489.0553       0.014     89.6678   2047.3720
       opcount      0.1558      0.0068       0.001      0.1402      0.1672
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.997
Model:                  NNLS                    Adj. R-squared:          0.997
No. Observations:       77                                RMSE:         110.41
Df Residuals:           75                                 MAE:          90.05
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    438.3104     39.5365       0.001    369.2868    522.5263
       opcount      0.1006      0.0006       0.001      0.0995      0.1018
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.935
Model:                  NNLS                    Adj. R-squared:          0.935
No. Observations:       99                                RMSE:         223.29
Df Residuals:           97                                 MAE:         185.63
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const   1319.5267     89.8722       0.001   1133.7237   1485.8905
       opcount      0.0420      0.0013       0.001      0.0396      0.0447
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.914
Model:                  NNLS                    Adj. R-squared:          0.913
No. Observations:       77                                RMSE:         227.91
Df Residuals:           75                                 MAE:         189.79
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    692.0943    105.8503       0.001    484.7322    895.0365
       opcount      0.0368      0.0015       0.001      0.0341      0.0397
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       110                               RMSE:          31.81
Df Residuals:           108                                MAE:          26.55
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    146.8274      9.4638       0.001    128.9419    165.8723
       opcount      0.0236      0.0001       0.001      0.0233      0.0239
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__diagnostics.png)

</details>

### test_account_access — combo `CALL_AccountMode.EXISTING_CONTRACT_MINIMAL` — `models.custom[0]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8621 | 0.02778 | 1.00e-03 | [0.02594, 0.02964] |
| `erigon` | 55 | 0.938 | 0.02467 | 1.00e-03 | [0.02295, 0.02611] |
| `ethrex` | 77 | 0.9814 | 0.01871 | 1.00e-03 | [0.01809, 0.01937] |
| `geth` | 99 | 0.996 | 0.02025 | 1.00e-03 | [0.01994, 0.02054] |
| `nethermind` | 77 | 0.9777 | 0.01289 | 1.00e-03 | [0.01246, 0.01332] |
| `reth` | 110 | 0.9801 | 0.005287 | 1.00e-03 | [0.005135, 0.005435] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.862
Model:                  NNLS                    Adj. R-squared:          0.861
No. Observations:       132                               RMSE:         224.69
Df Residuals:           130                                MAE:         210.19
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    402.9250     59.8446       0.001    289.2964    523.2041
       opcount      0.0278      0.0010       0.001      0.0259      0.0296
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.938
Model:                  NNLS                    Adj. R-squared:          0.937
No. Observations:       55                                RMSE:         128.27
Df Residuals:           53                                 MAE:         110.92
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    298.2313     58.3485       0.001    190.4175    418.5778
       opcount      0.0247      0.0008       0.001      0.0230      0.0261
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          52.14
Df Residuals:           75                                 MAE:          45.78
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    220.7017     23.7882       0.001    174.8109    268.0117
       opcount      0.0187      0.0003       0.001      0.0181      0.0194
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          26.04
Df Residuals:           97                                 MAE:          21.46
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    412.1455      9.7555       0.001    394.6213    432.3102
       opcount      0.0203      0.0002       0.001      0.0199      0.0205
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.978
Model:                  NNLS                    Adj. R-squared:          0.977
No. Observations:       77                                RMSE:          39.36
Df Residuals:           75                                 MAE:          29.92
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    109.2420     12.8554       0.001     84.6250    133.7048
       opcount      0.0129      0.0002       0.001      0.0125      0.0133
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.980
Model:                  NNLS                    Adj. R-squared:          0.980
No. Observations:       110                               RMSE:          15.22
Df Residuals:           108                                MAE:          12.15
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     93.5817      4.3893       0.001     85.3866    102.0455
       opcount      0.0053      0.0001       0.001      0.0051      0.0054
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__diagnostics.png)

</details>

### test_account_access — combo `CALL_AccountMode.EXISTING_CONTRACT_SAME_MAX` — `models.custom[0]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8517 | 0.02787 | 1.00e-03 | [0.026, 0.02967] |
| `erigon` | 55 | 0.925 | 0.03492 | 1.00e-03 | [0.03202, 0.03723] |
| `ethrex` | 77 | 0.981 | 0.01871 | 1.00e-03 | [0.01802, 0.01941] |
| `geth` | 99 | 0.9953 | 0.02042 | 1.00e-03 | [0.02012, 0.02072] |
| `nethermind` | 77 | 0.9846 | 0.01268 | 1.00e-03 | [0.01229, 0.01307] |
| `reth` | 110 | 0.9802 | 0.00526 | 1.00e-03 | [0.005099, 0.005403] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.852
Model:                  NNLS                    Adj. R-squared:          0.851
No. Observations:       132                               RMSE:         235.13
Df Residuals:           130                                MAE:         219.78
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    418.6077     62.2407       0.001    306.0877    547.7801
       opcount      0.0279      0.0010       0.001      0.0260      0.0297
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.925
Model:                  NNLS                    Adj. R-squared:          0.924
No. Observations:       55                                RMSE:         201.07
Df Residuals:           53                                 MAE:         174.34
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    331.0882     94.2978       0.001    168.5466    543.6901
       opcount      0.0349      0.0013       0.001      0.0320      0.0372
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          52.65
Df Residuals:           75                                 MAE:          46.75
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    226.6079     24.5762       0.001    179.2116    278.1680
       opcount      0.0187      0.0003       0.001      0.0180      0.0194
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.995
Model:                  NNLS                    Adj. R-squared:          0.995
No. Observations:       99                                RMSE:          28.32
Df Residuals:           97                                 MAE:          22.27
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    403.8894      9.4596       0.001    386.7597    423.0072
       opcount      0.0204      0.0002       0.001      0.0201      0.0207
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.985
Model:                  NNLS                    Adj. R-squared:          0.984
No. Observations:       77                                RMSE:          32.11
Df Residuals:           75                                 MAE:          25.81
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    136.1405     12.9854       0.001    110.3901    162.5341
       opcount      0.0127      0.0002       0.001      0.0123      0.0131
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.980
Model:                  NNLS                    Adj. R-squared:          0.980
No. Observations:       110                               RMSE:          15.13
Df Residuals:           108                                MAE:          12.15
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     93.8357      4.8744       0.001     84.7767    103.6518
       opcount      0.0053      0.0001       0.001      0.0051      0.0054
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__diagnostics.png)

</details>

### test_account_access — combo `CALL_AccountMode.NON_EXISTING_ACCOUNT` — `models.custom[0]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8981 | 0.0334 | 1.00e-03 | [0.03154, 0.03521] |
| `erigon` | 55 | 0.9936 | 0.008314 | 1.00e-03 | [0.008249, 0.008374] |
| `ethrex` | 77 | 0.9669 | 0.00246 | 1.00e-03 | [0.002356, 0.002568] |
| `geth` | 99 | 0.9957 | 0.02069 | 1.00e-03 | [0.02038, 0.02096] |
| `nethermind` | 77 | 0.9851 | 0.01087 | 1.00e-03 | [0.01056, 0.01119] |
| `reth` | 110 | 0.9826 | 0.004481 | 1.00e-03 | [0.004369, 0.004597] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.898
Model:                  NNLS                    Adj. R-squared:          0.897
No. Observations:       132                               RMSE:         231.05
Df Residuals:           130                                MAE:         216.15
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    391.7732     61.8925       0.001    269.0330    511.1143
       opcount      0.0334      0.0009       0.001      0.0315      0.0352
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__besu__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__besu__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.994
Model:                  NNLS                    Adj. R-squared:          0.993
No. Observations:       55                                RMSE:          14.28
Df Residuals:           53                                 MAE:          11.82
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0083      0.0000       0.001      0.0082      0.0084
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.967
Model:                  NNLS                    Adj. R-squared:          0.966
No. Observations:       77                                RMSE:           9.35
Df Residuals:           75                                 MAE:           7.93
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    117.9447      3.3061       0.001    111.4095    124.4757
       opcount      0.0025      0.0001       0.001      0.0024      0.0026
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          27.84
Df Residuals:           97                                 MAE:          22.18
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    388.7103      9.0974       0.001    371.8382    408.7596
       opcount      0.0207      0.0001       0.001      0.0204      0.0210
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__geth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__geth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.985
Model:                  NNLS                    Adj. R-squared:          0.985
No. Observations:       77                                RMSE:          27.49
Df Residuals:           75                                 MAE:          23.21
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    103.4762     10.5576       0.001     82.6607    123.5186
       opcount      0.0109      0.0002       0.001      0.0106      0.0112
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.983
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       110                               RMSE:          12.25
Df Residuals:           108                                MAE:           9.94
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    104.3896      3.7154       0.001     97.1654    111.7209
       opcount      0.0045      0.0001       0.001      0.0044      0.0046
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__reth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__reth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__reth__diagnostics.png)

</details>

### test_account_access — combo `CALL_AccountMode.EXISTING_CONTRACT_DIFF_MAX` — `models.custom[1]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9582 | 0.145 | 1.00e-03 | [0.1396, 0.1505] |
| `erigon` | 55 | 0.9727 | 0.2874 | 1.00e-03 | [0.2743, 0.2988] |
| `ethrex` | 77 | 0.9915 | 0.1331 | 1.00e-03 | [0.1302, 0.136] |
| `geth` | 99 | 0.9905 | 0.1308 | 1.00e-03 | [0.128, 0.1337] |
| `nethermind` | 77 | 0.9625 | 0.08967 | 1.00e-03 | [0.08534, 0.09415] |
| `reth` | 110 | 0.9899 | 0.05753 | 1.00e-03 | [0.05639, 0.05863] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.958
Model:                  NNLS                    Adj. R-squared:          0.958
No. Observations:       132                               RMSE:         142.60
Df Residuals:           130                                MAE:         120.91
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    239.5383     36.3480       0.001    167.9128    311.4117
       opcount      0.1450      0.0028       0.001      0.1396      0.1505
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.973
Model:                  NNLS                    Adj. R-squared:          0.972
No. Observations:       55                                RMSE:         226.70
Df Residuals:           53                                 MAE:         193.68
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const   1095.4013     97.6029       0.001    915.7387   1304.9087
       opcount      0.2874      0.0062       0.001      0.2743      0.2988
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.991
Model:                  NNLS                    Adj. R-squared:          0.991
No. Observations:       77                                RMSE:          58.13
Df Residuals:           75                                 MAE:          47.81
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    252.0983     19.3842       0.001    213.4706    288.3508
       opcount      0.1331      0.0015       0.001      0.1302      0.1360
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.991
Model:                  NNLS                    Adj. R-squared:          0.990
No. Observations:       99                                RMSE:          60.24
Df Residuals:           97                                 MAE:          48.93
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    543.3848     23.4310       0.001    500.3764    589.8155
       opcount      0.1308      0.0014       0.001      0.1280      0.1337
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.963
Model:                  NNLS                    Adj. R-squared:          0.962
No. Observations:       77                                RMSE:          83.30
Df Residuals:           75                                 MAE:          65.25
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    137.0491     29.6400       0.001     76.8461    192.3193
       opcount      0.0897      0.0023       0.001      0.0853      0.0942
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.990
Model:                  NNLS                    Adj. R-squared:          0.990
No. Observations:       110                               RMSE:          27.39
Df Residuals:           108                                MAE:          20.97
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    121.0481      8.4835       0.001    105.2041    137.5563
       opcount      0.0575      0.0006       0.001      0.0564      0.0586
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__diagnostics.png)

</details>

### test_account_access — combo `CALL_AccountMode.EXISTING_CONTRACT_MINIMAL` — `models.custom[1]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9577 | 0.1152 | 1.00e-03 | [0.1107, 0.1198] |
| `erigon` | 55 | 0.9941 | 0.1634 | 1.00e-03 | [0.1593, 0.1673] |
| `ethrex` | 77 | 0.9924 | 0.03619 | 1.00e-03 | [0.0356, 0.03678] |
| `geth` | 99 | 0.9971 | 0.1035 | 1.00e-03 | [0.1023, 0.1046] |
| `nethermind` | 77 | 0.972 | 0.06993 | 1.00e-03 | [0.06692, 0.0731] |
| `reth` | 110 | 0.9906 | 0.03496 | 1.00e-03 | [0.03434, 0.03567] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.958
Model:                  NNLS                    Adj. R-squared:          0.957
No. Observations:       132                               RMSE:         113.94
Df Residuals:           130                                MAE:          97.46
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    269.1170     31.2805       0.001    209.9870    331.5574
       opcount      0.1152      0.0024       0.001      0.1107      0.1198
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.994
Model:                  NNLS                    Adj. R-squared:          0.994
No. Observations:       55                                RMSE:          59.20
Df Residuals:           53                                 MAE:          49.05
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    751.8567     28.2813       0.001    700.1167    808.1761
       opcount      0.1634      0.0021       0.001      0.1593      0.1673
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.992
Model:                  NNLS                    Adj. R-squared:          0.992
No. Observations:       77                                RMSE:          14.94
Df Residuals:           75                                 MAE:          11.87
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    277.1753      4.5914       0.001    268.3159    286.1036
       opcount      0.0362      0.0003       0.001      0.0356      0.0368
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.997
Model:                  NNLS                    Adj. R-squared:          0.997
No. Observations:       99                                RMSE:          26.07
Df Residuals:           97                                 MAE:          20.12
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    379.7714      8.1731       0.001    364.8911    396.9269
       opcount      0.1035      0.0006       0.001      0.1023      0.1046
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.972
Model:                  NNLS                    Adj. R-squared:          0.972
No. Observations:       77                                RMSE:          55.81
Df Residuals:           75                                 MAE:          42.52
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    136.2534     22.6265       0.001     90.7985    180.2351
       opcount      0.0699      0.0016       0.001      0.0669      0.0731
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.991
Model:                  NNLS                    Adj. R-squared:          0.990
No. Observations:       110                               RMSE:          16.06
Df Residuals:           108                                MAE:          12.77
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     94.0277      4.9735       0.001     84.6367    103.9996
       opcount      0.0350      0.0003       0.001      0.0343      0.0357
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__diagnostics.png)

</details>

### test_account_access — combo `CALL_AccountMode.EXISTING_CONTRACT_SAME_MAX` — `models.custom[1]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9565 | 0.1153 | 1.00e-03 | [0.111, 0.1199] |
| `erigon` | 55 | 0.9935 | 0.1719 | 1.00e-03 | [0.1674, 0.176] |
| `ethrex` | 77 | 0.99 | 0.0359 | 1.00e-03 | [0.03524, 0.03659] |
| `geth` | 99 | 0.9969 | 0.1033 | 1.00e-03 | [0.1021, 0.1045] |
| `nethermind` | 77 | 0.9749 | 0.06874 | 1.00e-03 | [0.06642, 0.07083] |
| `reth` | 110 | 0.9892 | 0.03571 | 1.00e-03 | [0.03485, 0.03648] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.957
Model:                  NNLS                    Adj. R-squared:          0.956
No. Observations:       132                               RMSE:         115.75
Df Residuals:           130                                MAE:          98.98
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    275.5244     32.6473       0.001    212.9750    337.3243
       opcount      0.1153      0.0023       0.001      0.1110      0.1199
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.993
Model:                  NNLS                    Adj. R-squared:          0.993
No. Observations:       55                                RMSE:          65.70
Df Residuals:           53                                 MAE:          54.11
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    783.5344     30.6444       0.001    727.5260    849.9121
       opcount      0.1719      0.0022       0.001      0.1674      0.1760
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.990
Model:                  NNLS                    Adj. R-squared:          0.990
No. Observations:       77                                RMSE:          17.00
Df Residuals:           75                                 MAE:          13.29
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    283.7673      5.3992       0.001    272.9902    293.8998
       opcount      0.0359      0.0004       0.001      0.0352      0.0366
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.997
Model:                  NNLS                    Adj. R-squared:          0.997
No. Observations:       99                                RMSE:          26.90
Df Residuals:           97                                 MAE:          21.48
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    382.3665      8.3384       0.001    366.2372    399.9427
       opcount      0.1033      0.0006       0.001      0.1021      0.1045
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.975
Model:                  NNLS                    Adj. R-squared:          0.975
No. Observations:       77                                RMSE:          51.93
Df Residuals:           75                                 MAE:          39.55
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    150.3634     15.3210       0.001    120.9128    179.2472
       opcount      0.0687      0.0011       0.001      0.0664      0.0708
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.989
Model:                  NNLS                    Adj. R-squared:          0.989
No. Observations:       110                               RMSE:          17.57
Df Residuals:           108                                MAE:          12.67
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     89.1352      6.9057       0.001     76.8719    103.7866
       opcount      0.0357      0.0004       0.001      0.0349      0.0365
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__diagnostics.png)

</details>

### test_account_access — combo `CALL_AccountMode.NON_EXISTING_ACCOUNT` — `models.custom[1]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8599 | 0.179 | 1.00e-03 | [0.1644, 0.1944] |
| `erigon` | 55 | 0.9886 | 0.2745 | 1.00e-03 | [0.2657, 0.2826] |
| `ethrex` | 77 | 0.8225 | 0.0482 | 1.00e-03 | [0.04244, 0.05395] |
| `geth` | 99 | 0.9844 | 0.159 | 1.00e-03 | [0.1547, 0.163] |
| `nethermind` | 77 | 0.8977 | 0.09912 | 1.00e-03 | [0.09135, 0.1076] |
| `reth` | 110 | 0.8983 | 0.05438 | 1.00e-03 | [0.05078, 0.05775] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.860
Model:                  NNLS                    Adj. R-squared:          0.859
No. Observations:       132                               RMSE:          24.90
Df Residuals:           130                                MAE:          19.82
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     70.8872      7.0867       0.001     57.1010     84.3282
       opcount      0.1790      0.0077       0.001      0.1644      0.1944
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__besu__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__besu__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.989
Model:                  NNLS                    Adj. R-squared:          0.988
No. Observations:       55                                RMSE:          10.18
Df Residuals:           53                                 MAE:           8.77
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     95.2677      4.2087       0.001     87.2662    104.2974
       opcount      0.2745      0.0042       0.001      0.2657      0.2826
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.822
Model:                  NNLS                    Adj. R-squared:          0.820
No. Observations:       77                                RMSE:           7.72
Df Residuals:           75                                 MAE:           6.19
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    228.6784      3.2171       0.001    222.6458    235.2481
       opcount      0.0482      0.0029       0.001      0.0424      0.0539
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.984
Model:                  NNLS                    Adj. R-squared:          0.984
No. Observations:       99                                RMSE:           6.89
Df Residuals:           97                                 MAE:           5.53
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     41.0963      2.2590       0.001     36.6716     45.7252
       opcount      0.1590      0.0021       0.001      0.1547      0.1630
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__geth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__geth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.898
Model:                  NNLS                    Adj. R-squared:          0.896
No. Observations:       77                                RMSE:          11.53
Df Residuals:           75                                 MAE:           7.67
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     25.0800      4.0673       0.001     16.7675     33.3598
       opcount      0.0991      0.0040       0.001      0.0914      0.1076
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.898
Model:                  NNLS                    Adj. R-squared:          0.897
No. Observations:       110                               RMSE:           6.31
Df Residuals:           108                                MAE:           5.22
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     16.2181      1.9607       0.001     12.5049     20.0542
       opcount      0.0544      0.0018       0.001      0.0508      0.0577
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__reth__regression.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__reth__bootstrap.png)

![](figs/runtime/CALL__test_account_access__CALL_AccountMode_NON_EXISTING_ACCOUNT__reth__diagnostics.png)

</details>

## CALLCODE

### test_ext_account_query_warm — combo `CALLCODE`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.6007 | 0.0004009 | 1.00e-03 | [0.0003467, 0.0004625] |
| `erigon` | 55 | 0.9455 | 6.546e-05 | 1.00e-03 | [6.169e-05, 6.95e-05] |
| `ethrex` | 77 | 0.9269 | 9.804e-05 | 1.00e-03 | [9.228e-05, 0.0001038] |
| `geth` | 99 | 0.9468 | 0.0001856 | 1.00e-03 | [0.000176, 0.0001956] |
| `nethermind` | 77 | 0.6442 | 0.0002006 | 1.00e-03 | [0.0001623, 0.0002407] |
| `reth` | 110 | 0.9243 | 5.878e-05 | 1.00e-03 | [5.589e-05, 6.15e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.601
Model:                  NNLS                    Adj. R-squared:          0.598
No. Observations:       132                               RMSE:         165.20
Df Residuals:           130                                MAE:         127.70
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    666.1717     46.2816       0.001    578.7993    755.4101
       opcount      0.0004      0.0000       0.001      0.0003      0.0005
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_ext_account_query_warm__CALLCODE__besu__regression.png)

![](figs/runtime/CALLCODE__test_ext_account_query_warm__CALLCODE__besu__bootstrap.png)

![](figs/runtime/CALLCODE__test_ext_account_query_warm__CALLCODE__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.945
Model:                  NNLS                    Adj. R-squared:          0.944
No. Observations:       55                                RMSE:           7.95
Df Residuals:           53                                 MAE:           6.00
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     20.4851      2.7687       0.001     14.7772     25.7656
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_ext_account_query_warm__CALLCODE__erigon__regression.png)

![](figs/runtime/CALLCODE__test_ext_account_query_warm__CALLCODE__erigon__bootstrap.png)

![](figs/runtime/CALLCODE__test_ext_account_query_warm__CALLCODE__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.927
Model:                  NNLS                    Adj. R-squared:          0.926
No. Observations:       77                                RMSE:          13.92
Df Residuals:           75                                 MAE:          10.99
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     40.4507      4.5198       0.001     31.9699     49.4785
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_ext_account_query_warm__CALLCODE__ethrex__regression.png)

![](figs/runtime/CALLCODE__test_ext_account_query_warm__CALLCODE__ethrex__bootstrap.png)

![](figs/runtime/CALLCODE__test_ext_account_query_warm__CALLCODE__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.947
Model:                  NNLS                    Adj. R-squared:          0.946
No. Observations:       99                                RMSE:          22.24
Df Residuals:           97                                 MAE:          16.73
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     29.5504      7.3453       0.001     15.4541     43.6462
       opcount      0.0002      0.0000       0.001      0.0002      0.0002
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_ext_account_query_warm__CALLCODE__geth__regression.png)

![](figs/runtime/CALLCODE__test_ext_account_query_warm__CALLCODE__geth__bootstrap.png)

![](figs/runtime/CALLCODE__test_ext_account_query_warm__CALLCODE__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.644
Model:                  NNLS                    Adj. R-squared:          0.639
No. Observations:       77                                RMSE:          75.34
Df Residuals:           75                                 MAE:          56.39
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    170.9623     31.0912       0.001    110.7651    233.2307
       opcount      0.0002      0.0000       0.001      0.0002      0.0002
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_ext_account_query_warm__CALLCODE__nethermind__regression.png)

![](figs/runtime/CALLCODE__test_ext_account_query_warm__CALLCODE__nethermind__bootstrap.png)

![](figs/runtime/CALLCODE__test_ext_account_query_warm__CALLCODE__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.924
Model:                  NNLS                    Adj. R-squared:          0.924
No. Observations:       110                               RMSE:           8.50
Df Residuals:           108                                MAE:           6.17
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     21.8783      2.3636       0.001     17.4649     26.7148
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_ext_account_query_warm__CALLCODE__reth__regression.png)

![](figs/runtime/CALLCODE__test_ext_account_query_warm__CALLCODE__reth__bootstrap.png)

![](figs/runtime/CALLCODE__test_ext_account_query_warm__CALLCODE__reth__diagnostics.png)

</details>

### test_account_access — combo `CALLCODE_AccountMode.EXISTING_EOA` — `presets[cold_account_nocode_access]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8986 | 0.03344 | 1.00e-03 | [0.03157, 0.03538] |
| `erigon` | 55 | 0.9959 | 0.008168 | 1.00e-03 | [0.008118, 0.008214] |
| `ethrex` | 77 | 0.9812 | 0.01828 | 1.00e-03 | [0.01764, 0.01896] |
| `geth` | 99 | 0.996 | 0.02125 | 1.00e-03 | [0.02097, 0.02157] |
| `nethermind` | 77 | 0.9838 | 0.01107 | 1.00e-03 | [0.01073, 0.01144] |
| `reth` | 110 | 0.977 | 0.004485 | 1.00e-03 | [0.004353, 0.004618] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.899
Model:                  NNLS                    Adj. R-squared:          0.898
No. Observations:       132                               RMSE:         230.67
Df Residuals:           130                                MAE:         213.71
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    296.1206     60.3611       0.001    174.1646    412.9811
       opcount      0.0334      0.0010       0.001      0.0316      0.0354
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__besu__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__besu__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       55                                RMSE:          11.14
Df Residuals:           53                                 MAE:           9.08
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0082      0.0000       0.001      0.0081      0.0082
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__erigon__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__erigon__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          52.03
Df Residuals:           75                                 MAE:          45.82
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    232.3033     24.5823       0.001    184.1541    281.0519
       opcount      0.0183      0.0003       0.001      0.0176      0.0190
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__ethrex__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__ethrex__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          27.59
Df Residuals:           97                                 MAE:          22.93
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    392.9246      9.1993       0.001    375.3754    410.6841
       opcount      0.0213      0.0001       0.001      0.0210      0.0216
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__geth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__geth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.984
Model:                  NNLS                    Adj. R-squared:          0.984
No. Observations:       77                                RMSE:          29.15
Df Residuals:           75                                 MAE:          22.44
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     78.2317     11.4799       0.001     55.5839    100.6592
       opcount      0.0111      0.0002       0.001      0.0107      0.0114
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__nethermind__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__nethermind__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.977
Model:                  NNLS                    Adj. R-squared:          0.977
No. Observations:       110                               RMSE:          14.14
Df Residuals:           108                                MAE:          11.25
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    102.5786      4.4298       0.001     94.1705    111.3215
       opcount      0.0045      0.0001       0.001      0.0044      0.0046
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__reth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__reth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__reth__diagnostics.png)

</details>

### test_account_access — combo `CALLCODE_AccountMode.NON_EXISTING_ACCOUNT` — `presets[cold_account_nocode_access]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9119 | 0.03272 | 1.00e-03 | [0.03109, 0.0346] |
| `erigon` | 55 | 0.9958 | 0.007987 | 1.00e-03 | [0.007936, 0.008033] |
| `ethrex` | 77 | 0.9654 | 0.002608 | 1.00e-03 | [0.002497, 0.002731] |
| `geth` | 99 | 0.9959 | 0.02131 | 1.00e-03 | [0.02102, 0.02161] |
| `nethermind` | 77 | 0.9814 | 0.01061 | 1.00e-03 | [0.01032, 0.01093] |
| `reth` | 110 | 0.9751 | 0.004419 | 1.00e-03 | [0.00428, 0.004551] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.912
Model:                  NNLS                    Adj. R-squared:          0.911
No. Observations:       132                               RMSE:         208.84
Df Residuals:           130                                MAE:         194.35
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    299.0950     57.4105       0.001    181.5305    403.2972
       opcount      0.0327      0.0009       0.001      0.0311      0.0346
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__besu__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__besu__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       55                                RMSE:          10.99
Df Residuals:           53                                 MAE:           8.84
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0080      0.0000       0.001      0.0079      0.0080
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__erigon__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__erigon__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.965
Model:                  NNLS                    Adj. R-squared:          0.965
No. Observations:       77                                RMSE:          10.14
Df Residuals:           75                                 MAE:           8.29
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    109.1003      3.9253       0.001    101.0885    116.8300
       opcount      0.0026      0.0001       0.001      0.0025      0.0027
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          27.92
Df Residuals:           97                                 MAE:          23.03
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    396.4650      9.6515       0.001    377.8520    416.1590
       opcount      0.0213      0.0001       0.001      0.0210      0.0216
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__geth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__geth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          29.99
Df Residuals:           75                                 MAE:          23.04
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     95.8272      9.6547       0.001     76.4629    113.7154
       opcount      0.0106      0.0002       0.001      0.0103      0.0109
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.975
Model:                  NNLS                    Adj. R-squared:          0.975
No. Observations:       110                               RMSE:          14.50
Df Residuals:           108                                MAE:          11.84
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    102.9138      4.2320       0.001     95.0896    111.2922
       opcount      0.0044      0.0001       0.001      0.0043      0.0046
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__reth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__reth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__reth__diagnostics.png)

</details>

### test_account_access — combo `CALLCODE_AccountMode.EXISTING_EOA` — `presets[cold_account_nocode_write]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8231 | 0.03823 | 1.00e-03 | [0.03479, 0.0413] |
| `erigon` | 55 | 0.9883 | 0.00766 | 1.00e-03 | [0.007481, 0.007828] |
| `ethrex` | 77 | 0.9823 | 0.0188 | 1.00e-03 | [0.01822, 0.01949] |
| `geth` | 99 | 0.986 | 0.03124 | 1.00e-03 | [0.03052, 0.03198] |
| `nethermind` | 77 | 0.9693 | 0.01377 | 1.00e-03 | [0.01317, 0.01426] |
| `reth` | 110 | 0.9396 | 0.006271 | 1.00e-03 | [0.005919, 0.006622] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.823
Model:                  NNLS                    Adj. R-squared:          0.822
No. Observations:       132                               RMSE:          83.70
Df Residuals:           130                                MAE:          74.25
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     46.1742     21.6357       0.011      5.8375     89.5979
       opcount      0.0382      0.0017       0.001      0.0348      0.0413
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__besu__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__besu__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.988
Model:                  NNLS                    Adj. R-squared:          0.988
No. Observations:       55                                RMSE:           3.93
Df Residuals:           53                                 MAE:           2.61
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      4.0801      1.4405       0.001      1.5401      6.8973
       opcount      0.0077      0.0001       0.001      0.0075      0.0078
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__erigon__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__erigon__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       77                                RMSE:          11.91
Df Residuals:           75                                 MAE:           9.91
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    136.6831      5.3435       0.001    125.7959    146.6663
       opcount      0.0188      0.0003       0.001      0.0182      0.0195
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__ethrex__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__ethrex__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.986
Model:                  NNLS                    Adj. R-squared:          0.986
No. Observations:       99                                RMSE:          17.61
Df Residuals:           97                                 MAE:          14.28
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     90.2528      6.1287       0.001     78.1880    102.3354
       opcount      0.0312      0.0004       0.001      0.0305      0.0320
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__geth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__geth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.969
Model:                  NNLS                    Adj. R-squared:          0.969
No. Observations:       77                                RMSE:          11.57
Df Residuals:           75                                 MAE:           8.76
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     39.4828      4.2892       0.001     32.0634     49.0211
       opcount      0.0138      0.0003       0.001      0.0132      0.0143
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__nethermind__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__nethermind__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.940
Model:                  NNLS                    Adj. R-squared:          0.939
No. Observations:       110                               RMSE:           7.51
Df Residuals:           108                                MAE:           6.04
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     38.8326      2.7931       0.001     33.4922     44.6162
       opcount      0.0063      0.0002       0.001      0.0059      0.0066
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__reth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__reth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_EOA__reth__diagnostics.png)

</details>

### test_account_access — combo `CALLCODE_AccountMode.NON_EXISTING_ACCOUNT` — `presets[cold_account_nocode_write]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8269 | 0.03801 | 1.00e-03 | [0.03456, 0.04095] |
| `erigon` | 55 | 0.9933 | 0.007398 | 1.00e-03 | [0.007247, 0.007559] |
| `ethrex` | 77 | 0.684 | 0.002105 | 1.00e-03 | [0.001805, 0.002396] |
| `geth` | 99 | 0.9923 | 0.03276 | 1.00e-03 | [0.0321, 0.0334] |
| `nethermind` | 77 | 0.9484 | 0.0136 | 1.00e-03 | [0.01292, 0.01429] |
| `reth` | 110 | 0.9229 | 0.006277 | 1.00e-03 | [0.005936, 0.006635] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.827
Model:                  NNLS                    Adj. R-squared:          0.826
No. Observations:       132                               RMSE:          82.15
Df Residuals:           130                                MAE:          73.68
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     40.5407     20.9028       0.028      0.0000     84.2772
       opcount      0.0380      0.0016       0.001      0.0346      0.0409
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__besu__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__besu__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.993
Model:                  NNLS                    Adj. R-squared:          0.993
No. Observations:       55                                RMSE:           2.88
Df Residuals:           53                                 MAE:           2.20
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      5.0110      1.0990       0.001      2.8576      7.2447
       opcount      0.0074      0.0001       0.001      0.0072      0.0076
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__erigon__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__erigon__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.684
Model:                  NNLS                    Adj. R-squared:          0.680
No. Observations:       77                                RMSE:           6.76
Df Residuals:           75                                 MAE:           5.56
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    128.1923      2.1819       0.001    123.8577    132.4820
       opcount      0.0021      0.0001       0.001      0.0018      0.0024
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.992
Model:                  NNLS                    Adj. R-squared:          0.992
No. Observations:       99                                RMSE:          13.63
Df Residuals:           97                                 MAE:          10.91
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     66.7566      4.5210       0.001     58.0024     76.0002
       opcount      0.0328      0.0003       0.001      0.0321      0.0334
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__geth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__geth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.948
Model:                  NNLS                    Adj. R-squared:          0.948
No. Observations:       77                                RMSE:          14.98
Df Residuals:           75                                 MAE:          11.28
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     38.3452      4.8286       0.001     29.1536     47.8694
       opcount      0.0136      0.0003       0.001      0.0129      0.0143
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.923
Model:                  NNLS                    Adj. R-squared:          0.922
No. Observations:       110                               RMSE:           8.57
Df Residuals:           108                                MAE:           6.64
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     38.5604      2.5269       0.001     33.7574     43.5964
       opcount      0.0063      0.0002       0.001      0.0059      0.0066
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__reth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__reth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__reth__diagnostics.png)

</details>

### test_account_access — combo `CALLCODE_AccountMode.EXISTING_CONTRACT_DIFF_MAX` — `models.custom[0]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8821 | 0.04609 | 1.00e-03 | [0.04321, 0.0489] |
| `erigon` | 55 | 0.9015 | 0.1553 | 1.00e-03 | [0.1417, 0.1669] |
| `ethrex` | 77 | 0.9971 | 0.1009 | 1.00e-03 | [0.09949, 0.1021] |
| `geth` | 99 | 0.9362 | 0.04192 | 1.00e-03 | [0.03962, 0.04461] |
| `nethermind` | 77 | 0.9119 | 0.03619 | 1.00e-03 | [0.03339, 0.0391] |
| `reth` | 110 | 0.9955 | 0.02265 | 1.00e-03 | [0.02242, 0.02294] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.882
Model:                  NNLS                    Adj. R-squared:          0.881
No. Observations:       132                               RMSE:         340.69
Df Residuals:           130                                MAE:         283.15
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    914.4245     91.3216       0.001    731.3679   1091.2595
       opcount      0.0461      0.0015       0.001      0.0432      0.0489
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.901
Model:                  NNLS                    Adj. R-squared:          0.900
No. Observations:       55                                RMSE:        1038.39
Df Residuals:           53                                 MAE:         898.20
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    892.3621    477.5231       0.020     20.7211   1899.4198
       opcount      0.1553      0.0065       0.001      0.1417      0.1669
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.997
Model:                  NNLS                    Adj. R-squared:          0.997
No. Observations:       77                                RMSE:         110.00
Df Residuals:           75                                 MAE:          88.82
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    434.4635     42.4805       0.001    360.0115    523.7395
       opcount      0.1009      0.0007       0.001      0.0995      0.1021
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.936
Model:                  NNLS                    Adj. R-squared:          0.936
No. Observations:       99                                RMSE:         221.28
Df Residuals:           97                                 MAE:         186.03
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const   1315.6563     88.3679       0.001   1124.8194   1480.1521
       opcount      0.0419      0.0013       0.001      0.0396      0.0446
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.912
Model:                  NNLS                    Adj. R-squared:          0.911
No. Observations:       77                                RMSE:         227.40
Df Residuals:           75                                 MAE:         185.71
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    745.9480    105.4960       0.001    540.6259    955.8820
       opcount      0.0362      0.0015       0.001      0.0334      0.0391
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.995
Model:                  NNLS                    Adj. R-squared:          0.995
No. Observations:       110                               RMSE:          30.91
Df Residuals:           108                                MAE:          22.55
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    143.6481      7.5117       0.001    127.5826    157.1272
       opcount      0.0226      0.0001       0.001      0.0224      0.0229
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__diagnostics.png)

</details>

### test_account_access — combo `CALLCODE_AccountMode.EXISTING_CONTRACT_MINIMAL` — `models.custom[0]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8363 | 0.02813 | 1.00e-03 | [0.02609, 0.0303] |
| `erigon` | 55 | 0.9371 | 0.02444 | 1.00e-03 | [0.02276, 0.02585] |
| `ethrex` | 77 | 0.9827 | 0.01877 | 1.00e-03 | [0.01815, 0.01946] |
| `geth` | 99 | 0.9966 | 0.02046 | 1.00e-03 | [0.02022, 0.02072] |
| `nethermind` | 77 | 0.9731 | 0.01275 | 1.00e-03 | [0.01225, 0.01323] |
| `reth` | 110 | 0.9767 | 0.004853 | 1.00e-03 | [0.004694, 0.004997] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.836
Model:                  NNLS                    Adj. R-squared:          0.835
No. Observations:       132                               RMSE:         251.60
Df Residuals:           130                                MAE:         235.62
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    375.4797     65.4980       0.001    244.7475    502.4186
       opcount      0.0281      0.0011       0.001      0.0261      0.0303
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.937
Model:                  NNLS                    Adj. R-squared:          0.936
No. Observations:       55                                RMSE:         128.03
Df Residuals:           53                                 MAE:         112.47
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    286.7104     56.0751       0.001    186.6814    407.7676
       opcount      0.0244      0.0008       0.001      0.0228      0.0259
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.983
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       77                                RMSE:          50.34
Df Residuals:           75                                 MAE:          44.35
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    215.3976     23.1465       0.001    168.6119    261.4874
       opcount      0.0188      0.0003       0.001      0.0182      0.0195
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.997
Model:                  NNLS                    Adj. R-squared:          0.997
No. Observations:       99                                RMSE:          24.21
Df Residuals:           97                                 MAE:          19.37
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    394.6030      7.8745       0.001    379.2371    409.6079
       opcount      0.0205      0.0001       0.001      0.0202      0.0207
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.973
Model:                  NNLS                    Adj. R-squared:          0.973
No. Observations:       77                                RMSE:          42.85
Df Residuals:           75                                 MAE:          29.74
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    118.7732     15.6896       0.001     88.8525    150.6066
       opcount      0.0127      0.0003       0.001      0.0123      0.0132
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.977
Model:                  NNLS                    Adj. R-squared:          0.977
No. Observations:       110                               RMSE:          15.14
Df Residuals:           108                                MAE:          12.22
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     91.3825      4.7563       0.001     82.7482    101.3169
       opcount      0.0049      0.0001       0.001      0.0047      0.0050
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__diagnostics.png)

</details>

### test_account_access — combo `CALLCODE_AccountMode.EXISTING_CONTRACT_SAME_MAX` — `models.custom[0]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8346 | 0.02808 | 1.00e-03 | [0.02601, 0.03027] |
| `erigon` | 55 | 0.9284 | 0.03486 | 1.00e-03 | [0.03216, 0.03708] |
| `ethrex` | 77 | 0.9814 | 0.01877 | 1.00e-03 | [0.0181, 0.01942] |
| `geth` | 99 | 0.9955 | 0.02047 | 1.00e-03 | [0.0202, 0.02075] |
| `nethermind` | 77 | 0.9828 | 0.01247 | 1.00e-03 | [0.01211, 0.01283] |
| `reth` | 110 | 0.9798 | 0.004951 | 1.00e-03 | [0.004811, 0.005108] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.835
Model:                  NNLS                    Adj. R-squared:          0.833
No. Observations:       132                               RMSE:         252.74
Df Residuals:           130                                MAE:         237.27
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    376.4160     66.9315       0.001    238.9661    505.5841
       opcount      0.0281      0.0011       0.001      0.0260      0.0303
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.928
Model:                  NNLS                    Adj. R-squared:          0.927
No. Observations:       55                                RMSE:         195.81
Df Residuals:           53                                 MAE:         169.50
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    311.2989     89.6446       0.001    142.5328    501.5737
       opcount      0.0349      0.0012       0.001      0.0322      0.0371
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          52.25
Df Residuals:           75                                 MAE:          46.05
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    221.7557     24.2266       0.001    176.2392    268.8777
       opcount      0.0188      0.0003       0.001      0.0181      0.0194
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          27.68
Df Residuals:           97                                 MAE:          22.65
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    395.3899      8.7411       0.001    378.5350    412.1471
       opcount      0.0205      0.0001       0.001      0.0202      0.0207
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.983
Model:                  NNLS                    Adj. R-squared:          0.983
No. Observations:       77                                RMSE:          33.34
Df Residuals:           75                                 MAE:          24.95
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    141.4225     12.4862       0.001    118.6247    167.0891
       opcount      0.0125      0.0002       0.001      0.0121      0.0128
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.980
Model:                  NNLS                    Adj. R-squared:          0.980
No. Observations:       110                               RMSE:          14.36
Df Residuals:           108                                MAE:          10.91
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     86.2122      4.3092       0.001     77.4587     94.2951
       opcount      0.0050      0.0001       0.001      0.0048      0.0051
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__diagnostics.png)

</details>

### test_account_access — combo `CALLCODE_AccountMode.NON_EXISTING_ACCOUNT` — `models.custom[0]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9119 | 0.03272 | 1.00e-03 | [0.03109, 0.0346] |
| `erigon` | 55 | 0.9958 | 0.007987 | 1.00e-03 | [0.007936, 0.008033] |
| `ethrex` | 77 | 0.9654 | 0.002608 | 1.00e-03 | [0.002497, 0.002731] |
| `geth` | 99 | 0.9959 | 0.02131 | 1.00e-03 | [0.02102, 0.02161] |
| `nethermind` | 77 | 0.9814 | 0.01061 | 1.00e-03 | [0.01032, 0.01093] |
| `reth` | 110 | 0.9751 | 0.004419 | 1.00e-03 | [0.00428, 0.004551] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.912
Model:                  NNLS                    Adj. R-squared:          0.911
No. Observations:       132                               RMSE:         208.84
Df Residuals:           130                                MAE:         194.35
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    299.0950     57.4105       0.001    181.5305    403.2972
       opcount      0.0327      0.0009       0.001      0.0311      0.0346
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__besu__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__besu__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       55                                RMSE:          10.99
Df Residuals:           53                                 MAE:           8.84
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0080      0.0000       0.001      0.0079      0.0080
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__erigon__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__erigon__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.965
Model:                  NNLS                    Adj. R-squared:          0.965
No. Observations:       77                                RMSE:          10.14
Df Residuals:           75                                 MAE:           8.29
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    109.1003      3.9253       0.001    101.0885    116.8300
       opcount      0.0026      0.0001       0.001      0.0025      0.0027
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          27.92
Df Residuals:           97                                 MAE:          23.03
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    396.4650      9.6515       0.001    377.8520    416.1590
       opcount      0.0213      0.0001       0.001      0.0210      0.0216
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__geth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__geth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          29.99
Df Residuals:           75                                 MAE:          23.04
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     95.8272      9.6547       0.001     76.4629    113.7154
       opcount      0.0106      0.0002       0.001      0.0103      0.0109
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.975
Model:                  NNLS                    Adj. R-squared:          0.975
No. Observations:       110                               RMSE:          14.50
Df Residuals:           108                                MAE:          11.84
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    102.9138      4.2320       0.001     95.0896    111.2922
       opcount      0.0044      0.0001       0.001      0.0043      0.0046
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__reth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__reth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__reth__diagnostics.png)

</details>

### test_account_access — combo `CALLCODE_AccountMode.EXISTING_CONTRACT_DIFF_MAX` — `models.custom[1]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8801 | 0.05791 | 1.00e-03 | [0.05407, 0.06172] |
| `erigon` | 55 | 0.9002 | 0.1538 | 1.00e-03 | [0.1396, 0.1652] |
| `ethrex` | 77 | 0.9881 | 0.1086 | 1.00e-03 | [0.1059, 0.1113] |
| `geth` | 99 | 0.9485 | 0.06266 | 1.00e-03 | [0.05917, 0.06591] |
| `nethermind` | 77 | 0.9056 | 0.04598 | 1.00e-03 | [0.04253, 0.04938] |
| `reth` | 110 | 0.9812 | 0.02479 | 1.00e-03 | [0.02407, 0.02556] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.880
Model:                  NNLS                    Adj. R-squared:          0.879
No. Observations:       132                               RMSE:         100.60
Df Residuals:           130                                MAE:          83.65
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    170.0728     28.0634       0.001    115.7758    220.0256
       opcount      0.0579      0.0021       0.001      0.0541      0.0617
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.900
Model:                  NNLS                    Adj. R-squared:          0.898
No. Observations:       55                                RMSE:         240.97
Df Residuals:           53                                 MAE:         210.92
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    477.4868    113.6356       0.001    290.2433    729.8606
       opcount      0.1538      0.0066       0.001      0.1396      0.1652
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.988
Model:                  NNLS                    Adj. R-squared:          0.988
No. Observations:       77                                RMSE:          56.19
Df Residuals:           75                                 MAE:          47.79
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    212.1505     19.9084       0.001    173.4381    252.5835
       opcount      0.1086      0.0014       0.001      0.1059      0.1113
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.949
Model:                  NNLS                    Adj. R-squared:          0.948
No. Observations:       99                                RMSE:          68.72
Df Residuals:           97                                 MAE:          57.74
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    381.6583     28.6073       0.001    327.9717    437.8056
       opcount      0.0627      0.0018       0.001      0.0592      0.0659
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.906
Model:                  NNLS                    Adj. R-squared:          0.904
No. Observations:       77                                RMSE:          69.87
Df Residuals:           75                                 MAE:          57.86
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    128.8170     28.1580       0.001     76.7194    186.9008
       opcount      0.0460      0.0018       0.001      0.0425      0.0494
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       110                               RMSE:          16.16
Df Residuals:           108                                MAE:          11.75
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     70.2476      4.9531       0.001     59.8580     80.1663
       opcount      0.0248      0.0004       0.001      0.0241      0.0256
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__diagnostics.png)

</details>

### test_account_access — combo `CALLCODE_AccountMode.EXISTING_CONTRACT_MINIMAL` — `models.custom[1]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.7873 | 0.03671 | 1.00e-03 | [0.03321, 0.0395] |
| `erigon` | 55 | 0.9056 | 0.02389 | 1.00e-03 | [0.02167, 0.02575] |
| `ethrex` | 77 | 0.9749 | 0.01878 | 1.00e-03 | [0.01799, 0.01956] |
| `geth` | 99 | 0.9904 | 0.03027 | 1.00e-03 | [0.02962, 0.03091] |
| `nethermind` | 77 | 0.9649 | 0.01527 | 1.00e-03 | [0.01466, 0.01597] |
| `reth` | 110 | 0.9459 | 0.006491 | 1.00e-03 | [0.006203, 0.006764] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.787
Model:                  NNLS                    Adj. R-squared:          0.786
No. Observations:       132                               RMSE:          89.82
Df Residuals:           130                                MAE:          80.46
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     31.4155     22.2063       0.089      0.0000     80.4038
       opcount      0.0367      0.0017       0.001      0.0332      0.0395
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.906
Model:                  NNLS                    Adj. R-squared:          0.904
No. Observations:       55                                RMSE:          36.31
Df Residuals:           53                                 MAE:          29.02
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    251.9566     17.5194       0.001    220.5427    291.0912
       opcount      0.0239      0.0010       0.001      0.0217      0.0257
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.975
Model:                  NNLS                    Adj. R-squared:          0.975
No. Observations:       77                                RMSE:          14.19
Df Residuals:           75                                 MAE:          12.32
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    140.7796      6.2067       0.001    128.8049    153.5761
       opcount      0.0188      0.0004       0.001      0.0180      0.0196
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.990
Model:                  NNLS                    Adj. R-squared:          0.990
No. Observations:       99                                RMSE:          14.03
Df Residuals:           97                                 MAE:          10.86
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     90.2569      5.1177       0.001     80.5897    100.7538
       opcount      0.0303      0.0003       0.001      0.0296      0.0309
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.965
Model:                  NNLS                    Adj. R-squared:          0.964
No. Observations:       77                                RMSE:          13.70
Df Residuals:           75                                 MAE:          10.72
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     55.1912      4.4804       0.001     45.9555     63.8200
       opcount      0.0153      0.0003       0.001      0.0147      0.0160
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.946
Model:                  NNLS                    Adj. R-squared:          0.945
No. Observations:       110                               RMSE:           7.30
Df Residuals:           108                                MAE:           6.05
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     36.3953      2.2328       0.001     32.2423     40.7220
       opcount      0.0065      0.0001       0.001      0.0062      0.0068
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__diagnostics.png)

</details>

### test_account_access — combo `CALLCODE_AccountMode.EXISTING_CONTRACT_SAME_MAX` — `models.custom[1]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.7979 | 0.03595 | 1.00e-03 | [0.03236, 0.03896] |
| `erigon` | 55 | 0.9126 | 0.03441 | 1.00e-03 | [0.03155, 0.03679] |
| `ethrex` | 77 | 0.9756 | 0.01881 | 1.00e-03 | [0.01806, 0.01959] |
| `geth` | 99 | 0.9898 | 0.03053 | 1.00e-03 | [0.02986, 0.03126] |
| `nethermind` | 77 | 0.9657 | 0.01517 | 1.00e-03 | [0.0146, 0.01572] |
| `reth` | 110 | 0.9502 | 0.006694 | 1.00e-03 | [0.006349, 0.007002] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.798
Model:                  NNLS                    Adj. R-squared:          0.796
No. Observations:       132                               RMSE:          85.18
Df Residuals:           130                                MAE:          76.30
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     36.4512     21.8654       0.053      0.0000     81.1015
       opcount      0.0360      0.0017       0.001      0.0324      0.0390
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.913
Model:                  NNLS                    Adj. R-squared:          0.911
No. Observations:       55                                RMSE:          50.13
Df Residuals:           53                                 MAE:          41.14
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    245.0234     23.4097       0.001    203.6863    295.2673
       opcount      0.0344      0.0013       0.001      0.0315      0.0368
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.976
Model:                  NNLS                    Adj. R-squared:          0.975
No. Observations:       77                                RMSE:          14.01
Df Residuals:           75                                 MAE:          11.86
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    143.2886      6.3610       0.001    131.8660    155.7353
       opcount      0.0188      0.0004       0.001      0.0181      0.0196
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.990
Model:                  NNLS                    Adj. R-squared:          0.990
No. Observations:       99                                RMSE:          14.56
Df Residuals:           97                                 MAE:          11.63
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     86.1498      5.9722       0.001     74.5801     97.5603
       opcount      0.0305      0.0004       0.001      0.0299      0.0313
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.966
Model:                  NNLS                    Adj. R-squared:          0.965
No. Observations:       77                                RMSE:          13.47
Df Residuals:           75                                 MAE:          10.51
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     56.9399      4.4012       0.001     48.7718     66.0894
       opcount      0.0152      0.0003       0.001      0.0146      0.0157
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.950
Model:                  NNLS                    Adj. R-squared:          0.950
No. Observations:       110                               RMSE:           7.21
Df Residuals:           108                                MAE:           5.91
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     36.3927      2.5748       0.001     31.7593     41.5603
       opcount      0.0067      0.0002       0.001      0.0063      0.0070
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__diagnostics.png)

</details>

### test_account_access — combo `CALLCODE_AccountMode.NON_EXISTING_ACCOUNT` — `models.custom[1]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8269 | 0.03801 | 1.00e-03 | [0.03456, 0.04095] |
| `erigon` | 55 | 0.9933 | 0.007398 | 1.00e-03 | [0.007247, 0.007559] |
| `ethrex` | 77 | 0.684 | 0.002105 | 1.00e-03 | [0.001805, 0.002396] |
| `geth` | 99 | 0.9923 | 0.03276 | 1.00e-03 | [0.0321, 0.0334] |
| `nethermind` | 77 | 0.9484 | 0.0136 | 1.00e-03 | [0.01292, 0.01429] |
| `reth` | 110 | 0.9229 | 0.006277 | 1.00e-03 | [0.005936, 0.006635] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.827
Model:                  NNLS                    Adj. R-squared:          0.826
No. Observations:       132                               RMSE:          82.15
Df Residuals:           130                                MAE:          73.68
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     40.5407     20.9028       0.028      0.0000     84.2772
       opcount      0.0380      0.0016       0.001      0.0346      0.0409
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__besu__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__besu__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.993
Model:                  NNLS                    Adj. R-squared:          0.993
No. Observations:       55                                RMSE:           2.88
Df Residuals:           53                                 MAE:           2.20
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      5.0110      1.0990       0.001      2.8576      7.2447
       opcount      0.0074      0.0001       0.001      0.0072      0.0076
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__erigon__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__erigon__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.684
Model:                  NNLS                    Adj. R-squared:          0.680
No. Observations:       77                                RMSE:           6.76
Df Residuals:           75                                 MAE:           5.56
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    128.1923      2.1819       0.001    123.8577    132.4820
       opcount      0.0021      0.0001       0.001      0.0018      0.0024
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.992
Model:                  NNLS                    Adj. R-squared:          0.992
No. Observations:       99                                RMSE:          13.63
Df Residuals:           97                                 MAE:          10.91
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     66.7566      4.5210       0.001     58.0024     76.0002
       opcount      0.0328      0.0003       0.001      0.0321      0.0334
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__geth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__geth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.948
Model:                  NNLS                    Adj. R-squared:          0.948
No. Observations:       77                                RMSE:          14.98
Df Residuals:           75                                 MAE:          11.28
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     38.3452      4.8286       0.001     29.1536     47.8694
       opcount      0.0136      0.0003       0.001      0.0129      0.0143
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.923
Model:                  NNLS                    Adj. R-squared:          0.922
No. Observations:       110                               RMSE:           8.57
Df Residuals:           108                                MAE:           6.64
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     38.5604      2.5269       0.001     33.7574     43.5964
       opcount      0.0063      0.0002       0.001      0.0059      0.0066
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__reth__regression.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__reth__bootstrap.png)

![](figs/runtime/CALLCODE__test_account_access__CALLCODE_AccountMode_NON_EXISTING_ACCOUNT__reth__diagnostics.png)

</details>

## DELEGATECALL

### test_ext_account_query_warm — combo `DELEGATECALL`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.7259 | 0.0004434 | 1.00e-03 | [0.0004007, 0.000487] |
| `erigon` | 55 | 0.9239 | 5.929e-05 | 1.00e-03 | [5.47e-05, 6.406e-05] |
| `ethrex` | 77 | 0.9355 | 9.641e-05 | 1.00e-03 | [9.065e-05, 0.0001017] |
| `geth` | 99 | 0.9508 | 0.0001499 | 1.00e-03 | [0.0001422, 0.0001577] |
| `nethermind` | 77 | 0.9207 | 0.0004925 | 1.00e-03 | [0.0004579, 0.0005329] |
| `reth` | 110 | 0.9388 | 5.433e-05 | 1.00e-03 | [5.176e-05, 5.669e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.726
Model:                  NNLS                    Adj. R-squared:          0.724
No. Observations:       132                               RMSE:         141.10
Df Residuals:           130                                MAE:         106.83
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    539.9041     35.2881       0.001    472.3617    613.1542
       opcount      0.0004      0.0000       0.001      0.0004      0.0005
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_ext_account_query_warm__DELEGATECALL__besu__regression.png)

![](figs/runtime/DELEGATECALL__test_ext_account_query_warm__DELEGATECALL__besu__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_ext_account_query_warm__DELEGATECALL__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.924
Model:                  NNLS                    Adj. R-squared:          0.922
No. Observations:       55                                RMSE:           8.81
Df Residuals:           53                                 MAE:           6.42
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     27.0164      3.6959       0.001     19.6275     34.2965
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_ext_account_query_warm__DELEGATECALL__erigon__regression.png)

![](figs/runtime/DELEGATECALL__test_ext_account_query_warm__DELEGATECALL__erigon__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_ext_account_query_warm__DELEGATECALL__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.936
Model:                  NNLS                    Adj. R-squared:          0.935
No. Observations:       77                                RMSE:          13.11
Df Residuals:           75                                 MAE:          10.25
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     41.8201      4.7980       0.001     32.9833     51.4747
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_ext_account_query_warm__DELEGATECALL__ethrex__regression.png)

![](figs/runtime/DELEGATECALL__test_ext_account_query_warm__DELEGATECALL__ethrex__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_ext_account_query_warm__DELEGATECALL__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.951
Model:                  NNLS                    Adj. R-squared:          0.950
No. Observations:       99                                RMSE:          17.66
Df Residuals:           97                                 MAE:          14.10
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     47.6529      6.2832       0.001     35.8662     59.5922
       opcount      0.0001      0.0000       0.001      0.0001      0.0002
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_ext_account_query_warm__DELEGATECALL__geth__regression.png)

![](figs/runtime/DELEGATECALL__test_ext_account_query_warm__DELEGATECALL__geth__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_ext_account_query_warm__DELEGATECALL__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.921
Model:                  NNLS                    Adj. R-squared:          0.920
No. Observations:       77                                RMSE:          74.84
Df Residuals:           75                                 MAE:          59.24
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    207.4498     28.8892       0.001    148.2128    260.9227
       opcount      0.0005      0.0000       0.001      0.0005      0.0005
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_ext_account_query_warm__DELEGATECALL__nethermind__regression.png)

![](figs/runtime/DELEGATECALL__test_ext_account_query_warm__DELEGATECALL__nethermind__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_ext_account_query_warm__DELEGATECALL__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.939
Model:                  NNLS                    Adj. R-squared:          0.938
No. Observations:       110                               RMSE:           7.18
Df Residuals:           108                                MAE:           5.64
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     24.3195      2.1823       0.001     20.1337     28.9064
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_ext_account_query_warm__DELEGATECALL__reth__regression.png)

![](figs/runtime/DELEGATECALL__test_ext_account_query_warm__DELEGATECALL__reth__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_ext_account_query_warm__DELEGATECALL__reth__diagnostics.png)

</details>

### test_account_access — combo `DELEGATECALL_AccountMode.EXISTING_EOA`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9017 | 0.03351 | 1.00e-03 | [0.03166, 0.03543] |
| `erigon` | 55 | 0.9961 | 0.008211 | 1.00e-03 | [0.008164, 0.008257] |
| `ethrex` | 77 | 0.9814 | 0.01832 | 1.00e-03 | [0.01767, 0.01896] |
| `geth` | 99 | 0.9965 | 0.02114 | 1.00e-03 | [0.02087, 0.02138] |
| `nethermind` | 77 | 0.985 | 0.01102 | 1.00e-03 | [0.01069, 0.01137] |
| `reth` | 110 | 0.9781 | 0.004489 | 1.00e-03 | [0.004356, 0.004618] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.902
Model:                  NNLS                    Adj. R-squared:          0.901
No. Observations:       132                               RMSE:         227.42
Df Residuals:           130                                MAE:         211.67
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    284.0898     60.2236       0.001    159.6335    398.1671
       opcount      0.0335      0.0010       0.001      0.0317      0.0354
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_EOA__besu__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_EOA__besu__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_EOA__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       55                                RMSE:          10.95
Df Residuals:           53                                 MAE:           9.31
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0082      0.0000       0.001      0.0082      0.0083
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_EOA__erigon__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_EOA__erigon__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_EOA__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          51.88
Df Residuals:           75                                 MAE:          45.68
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    227.9318     23.9295       0.001    181.6624    276.0262
       opcount      0.0183      0.0003       0.001      0.0177      0.0190
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_EOA__ethrex__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_EOA__ethrex__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_EOA__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          25.85
Df Residuals:           97                                 MAE:          20.49
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    389.4846      8.0553       0.001    374.8802    406.2575
       opcount      0.0211      0.0001       0.001      0.0209      0.0214
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_EOA__geth__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_EOA__geth__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_EOA__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.985
Model:                  NNLS                    Adj. R-squared:          0.985
No. Observations:       77                                RMSE:          27.99
Df Residuals:           75                                 MAE:          23.42
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     93.0322     11.8271       0.001     69.5223    115.7958
       opcount      0.0110      0.0002       0.001      0.0107      0.0114
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_EOA__nethermind__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_EOA__nethermind__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_EOA__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.978
Model:                  NNLS                    Adj. R-squared:          0.978
No. Observations:       110                               RMSE:          13.82
Df Residuals:           108                                MAE:          10.61
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     99.7196      4.3640       0.001     91.4620    108.3633
       opcount      0.0045      0.0001       0.001      0.0044      0.0046
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_EOA__reth__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_EOA__reth__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_EOA__reth__diagnostics.png)

</details>

### test_account_access — combo `DELEGATECALL_AccountMode.NON_EXISTING_ACCOUNT` — `presets[cold_account_nocode_access]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9136 | 0.03269 | 1.00e-03 | [0.03095, 0.0344] |
| `erigon` | 55 | 0.9959 | 0.008028 | 1.00e-03 | [0.007981, 0.008074] |
| `ethrex` | 77 | 0.9582 | 0.002529 | 1.00e-03 | [0.002408, 0.002656] |
| `geth` | 99 | 0.9948 | 0.02102 | 1.00e-03 | [0.0207, 0.0213] |
| `nethermind` | 77 | 0.9826 | 0.01048 | 1.00e-03 | [0.01014, 0.01082] |
| `reth` | 110 | 0.9766 | 0.004528 | 1.00e-03 | [0.004382, 0.004681] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.914
Model:                  NNLS                    Adj. R-squared:          0.913
No. Observations:       132                               RMSE:         206.67
Df Residuals:           130                                MAE:         193.53
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    286.6230     57.7412       0.001    173.9368    397.2989
       opcount      0.0327      0.0009       0.001      0.0309      0.0344
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__besu__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__besu__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       55                                RMSE:          10.95
Df Residuals:           53                                 MAE:           8.65
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0080      0.0000       0.001      0.0080      0.0081
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.958
Model:                  NNLS                    Adj. R-squared:          0.958
No. Observations:       77                                RMSE:          10.86
Df Residuals:           75                                 MAE:           8.92
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    116.3860      3.8851       0.001    108.7578    123.7424
       opcount      0.0025      0.0001       0.001      0.0024      0.0027
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.995
Model:                  NNLS                    Adj. R-squared:          0.995
No. Observations:       99                                RMSE:          31.12
Df Residuals:           97                                 MAE:          24.94
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    409.3314     10.0058       0.001    392.0963    430.3496
       opcount      0.0210      0.0002       0.001      0.0207      0.0213
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__geth__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__geth__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.983
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       77                                RMSE:          28.66
Df Residuals:           75                                 MAE:          23.83
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    118.1085     11.4225       0.001     96.7325    139.6271
       opcount      0.0105      0.0002       0.001      0.0101      0.0108
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.977
Model:                  NNLS                    Adj. R-squared:          0.976
No. Observations:       110                               RMSE:          14.42
Df Residuals:           108                                MAE:          10.92
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     96.8511      4.1402       0.001     88.3715    104.9734
       opcount      0.0045      0.0001       0.001      0.0044      0.0047
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__reth__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__reth__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__reth__diagnostics.png)

</details>

### test_account_access — combo `DELEGATECALL_AccountMode.EXISTING_CONTRACT_DIFF_MAX`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.87 | 0.0463 | 1.00e-03 | [0.0433, 0.04901] |
| `erigon` | 55 | 0.9007 | 0.155 | 1.00e-03 | [0.1414, 0.166] |
| `ethrex` | 77 | 0.9977 | 0.1024 | 1.00e-03 | [0.1012, 0.1035] |
| `geth` | 99 | 0.9339 | 0.04166 | 1.00e-03 | [0.03904, 0.04425] |
| `nethermind` | 77 | 0.9076 | 0.0379 | 1.00e-03 | [0.03485, 0.04105] |
| `reth` | 110 | 0.9851 | 0.02249 | 1.00e-03 | [0.02199, 0.02322] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.870
Model:                  NNLS                    Adj. R-squared:          0.869
No. Observations:       132                               RMSE:         362.29
Df Residuals:           130                                MAE:         308.08
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    914.1564     93.9946       0.001    736.7571   1099.8795
       opcount      0.0463      0.0015       0.001      0.0433      0.0490
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.901
Model:                  NNLS                    Adj. R-squared:          0.899
No. Observations:       55                                RMSE:        1041.83
Df Residuals:           53                                 MAE:         901.25
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    908.1678    483.4129       0.015     99.2466   1920.5291
       opcount      0.1550      0.0066       0.001      0.1414      0.1660
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.998
Model:                  NNLS                    Adj. R-squared:          0.998
No. Observations:       77                                RMSE:          99.04
Df Residuals:           75                                 MAE:          79.02
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    322.1447     34.5908       0.001    257.7385    392.1486
       opcount      0.1024      0.0006       0.001      0.1012      0.1035
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.934
Model:                  NNLS                    Adj. R-squared:          0.933
No. Observations:       99                                RMSE:         224.42
Df Residuals:           97                                 MAE:         188.57
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const   1323.4084     94.0206       0.001   1143.3790   1511.0561
       opcount      0.0417      0.0013       0.001      0.0390      0.0443
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.908
Model:                  NNLS                    Adj. R-squared:          0.906
No. Observations:       77                                RMSE:         244.74
Df Residuals:           75                                 MAE:         206.48
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    648.4111    110.6486       0.001    435.1512    879.0294
       opcount      0.0379      0.0016       0.001      0.0348      0.0411
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.985
Model:                  NNLS                    Adj. R-squared:          0.985
No. Observations:       110                               RMSE:          56.00
Df Residuals:           108                                MAE:          30.22
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    159.2239     16.7248       0.001    121.5842    188.6466
       opcount      0.0225      0.0003       0.001      0.0220      0.0232
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__diagnostics.png)

</details>

### test_account_access — combo `DELEGATECALL_AccountMode.EXISTING_CONTRACT_MINIMAL`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8337 | 0.0278 | 1.00e-03 | [0.02568, 0.02992] |
| `erigon` | 55 | 0.9371 | 0.02423 | 1.00e-03 | [0.02243, 0.0257] |
| `ethrex` | 77 | 0.9822 | 0.01872 | 1.00e-03 | [0.01806, 0.01938] |
| `geth` | 99 | 0.9967 | 0.02037 | 1.00e-03 | [0.02015, 0.02061] |
| `nethermind` | 77 | 0.9814 | 0.01256 | 1.00e-03 | [0.0122, 0.01296] |
| `reth` | 110 | 0.9791 | 0.004906 | 1.00e-03 | [0.004764, 0.005045] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.834
Model:                  NNLS                    Adj. R-squared:          0.832
No. Observations:       132                               RMSE:         251.29
Df Residuals:           130                                MAE:         235.05
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    394.0430     64.8313       0.001    267.1772    526.1752
       opcount      0.0278      0.0011       0.001      0.0257      0.0299
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.937
Model:                  NNLS                    Adj. R-squared:          0.936
No. Observations:       55                                RMSE:         127.03
Df Residuals:           53                                 MAE:         110.42
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    295.3743     58.4711       0.001    192.6717    420.7692
       opcount      0.0242      0.0008       0.001      0.0224      0.0257
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       77                                RMSE:          51.02
Df Residuals:           75                                 MAE:          44.91
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    217.7700     23.6936       0.001    172.8744    265.1410
       opcount      0.0187      0.0003       0.001      0.0181      0.0194
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.997
Model:                  NNLS                    Adj. R-squared:          0.997
No. Observations:       99                                RMSE:          23.71
Df Residuals:           97                                 MAE:          17.95
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    396.1633      8.0079       0.001    381.1215    412.2435
       opcount      0.0204      0.0001       0.001      0.0201      0.0206
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          34.99
Df Residuals:           75                                 MAE:          28.20
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    134.5949     13.8731       0.001    108.2221    160.7677
       opcount      0.0126      0.0002       0.001      0.0122      0.0130
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.979
Model:                  NNLS                    Adj. R-squared:          0.979
No. Observations:       110                               RMSE:          14.51
Df Residuals:           108                                MAE:          11.46
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     87.8563      4.2653       0.001     79.8109     96.6501
       opcount      0.0049      0.0001       0.001      0.0048      0.0050
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__diagnostics.png)

</details>

### test_account_access — combo `DELEGATECALL_AccountMode.EXISTING_CONTRACT_SAME_MAX`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8388 | 0.02797 | 1.00e-03 | [0.02587, 0.03002] |
| `erigon` | 55 | 0.9232 | 0.03457 | 1.00e-03 | [0.03167, 0.03693] |
| `ethrex` | 77 | 0.9817 | 0.01876 | 1.00e-03 | [0.0181, 0.01944] |
| `geth` | 99 | 0.9954 | 0.02011 | 1.00e-03 | [0.01982, 0.02037] |
| `nethermind` | 77 | 0.9801 | 0.01257 | 1.00e-03 | [0.01213, 0.01294] |
| `reth` | 110 | 0.9795 | 0.004941 | 1.00e-03 | [0.004795, 0.005095] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.839
Model:                  NNLS                    Adj. R-squared:          0.838
No. Observations:       132                               RMSE:         248.22
Df Residuals:           130                                MAE:         233.26
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    383.4393     64.9945       0.001    259.3919    512.7420
       opcount      0.0280      0.0011       0.001      0.0259      0.0300
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.923
Model:                  NNLS                    Adj. R-squared:          0.922
No. Observations:       55                                RMSE:         201.84
Df Residuals:           53                                 MAE:         174.22
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    329.2028     93.7740       0.001    165.4197    537.0102
       opcount      0.0346      0.0013       0.001      0.0317      0.0369
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          51.87
Df Residuals:           75                                 MAE:          46.32
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    221.1307     23.9110       0.001    176.7257    269.9802
       opcount      0.0188      0.0003       0.001      0.0181      0.0194
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.995
Model:                  NNLS                    Adj. R-squared:          0.995
No. Observations:       99                                RMSE:          27.63
Df Residuals:           97                                 MAE:          22.72
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    413.0852      9.1932       0.001    397.3253    432.0779
       opcount      0.0201      0.0001       0.001      0.0198      0.0204
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.980
Model:                  NNLS                    Adj. R-squared:          0.980
No. Observations:       77                                RMSE:          36.29
Df Residuals:           75                                 MAE:          28.21
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    135.5856     14.6100       0.001    108.5287    164.6216
       opcount      0.0126      0.0002       0.001      0.0121      0.0129
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.980
Model:                  NNLS                    Adj. R-squared:          0.979
No. Observations:       110                               RMSE:          14.46
Df Residuals:           108                                MAE:          11.11
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     84.8585      4.4869       0.001     75.7691     93.4414
       opcount      0.0049      0.0001       0.001      0.0048      0.0051
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__diagnostics.png)

</details>

### test_account_access — combo `DELEGATECALL_AccountMode.NON_EXISTING_ACCOUNT` — `models.custom[0]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9136 | 0.03269 | 1.00e-03 | [0.03095, 0.0344] |
| `erigon` | 55 | 0.9959 | 0.008028 | 1.00e-03 | [0.007981, 0.008074] |
| `ethrex` | 77 | 0.9582 | 0.002529 | 1.00e-03 | [0.002408, 0.002656] |
| `geth` | 99 | 0.9948 | 0.02102 | 1.00e-03 | [0.0207, 0.0213] |
| `nethermind` | 77 | 0.9826 | 0.01048 | 1.00e-03 | [0.01014, 0.01082] |
| `reth` | 110 | 0.9766 | 0.004528 | 1.00e-03 | [0.004382, 0.004681] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.914
Model:                  NNLS                    Adj. R-squared:          0.913
No. Observations:       132                               RMSE:         206.67
Df Residuals:           130                                MAE:         193.53
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    286.6230     57.7412       0.001    173.9368    397.2989
       opcount      0.0327      0.0009       0.001      0.0309      0.0344
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__besu__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__besu__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       55                                RMSE:          10.95
Df Residuals:           53                                 MAE:           8.65
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0080      0.0000       0.001      0.0080      0.0081
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.958
Model:                  NNLS                    Adj. R-squared:          0.958
No. Observations:       77                                RMSE:          10.86
Df Residuals:           75                                 MAE:           8.92
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    116.3860      3.8851       0.001    108.7578    123.7424
       opcount      0.0025      0.0001       0.001      0.0024      0.0027
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.995
Model:                  NNLS                    Adj. R-squared:          0.995
No. Observations:       99                                RMSE:          31.12
Df Residuals:           97                                 MAE:          24.94
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    409.3314     10.0058       0.001    392.0963    430.3496
       opcount      0.0210      0.0002       0.001      0.0207      0.0213
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__geth__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__geth__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.983
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       77                                RMSE:          28.66
Df Residuals:           75                                 MAE:          23.83
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    118.1085     11.4225       0.001     96.7325    139.6271
       opcount      0.0105      0.0002       0.001      0.0101      0.0108
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.977
Model:                  NNLS                    Adj. R-squared:          0.976
No. Observations:       110                               RMSE:          14.42
Df Residuals:           108                                MAE:          10.92
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     96.8511      4.1402       0.001     88.3715    104.9734
       opcount      0.0045      0.0001       0.001      0.0044      0.0047
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__reth__regression.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__reth__bootstrap.png)

![](figs/runtime/DELEGATECALL__test_account_access__DELEGATECALL_AccountMode_NON_EXISTING_ACCOUNT__reth__diagnostics.png)

</details>

## EXTCODEHASH

### test_ext_account_query_warm — combo `EXTCODEHASH`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.4312 | 7.683e-05 | 1.00e-03 | [6e-05, 9.333e-05] |
| `erigon` | 55 | 0.9168 | 3.211e-05 | 1.00e-03 | [2.933e-05, 3.513e-05] |
| `ethrex` | 77 | 0.8196 | 1.493e-05 | 1.00e-03 | [1.325e-05, 1.671e-05] |
| `geth` | 99 | 0.9032 | 3.799e-05 | 1.00e-03 | [3.558e-05, 4.073e-05] |
| `nethermind` | 77 | 0.9248 | 0.000243 | 1.00e-03 | [0.0002273, 0.0002584] |
| `reth` | 110 | 0.6493 | 1.355e-05 | 1.00e-03 | [1.182e-05, 1.54e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.431
Model:                  NNLS                    Adj. R-squared:          0.427
No. Observations:       132                               RMSE:          51.62
Df Residuals:           130                                MAE:          42.32
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    206.7266     16.5631       0.001    174.2385    240.8986
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_ext_account_query_warm__EXTCODEHASH__besu__regression.png)

![](figs/runtime/EXTCODEHASH__test_ext_account_query_warm__EXTCODEHASH__besu__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_ext_account_query_warm__EXTCODEHASH__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.917
Model:                  NNLS                    Adj. R-squared:          0.915
No. Observations:       55                                RMSE:           5.66
Df Residuals:           53                                 MAE:           4.71
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     18.2744      2.7590       0.001     12.6963     23.7560
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_ext_account_query_warm__EXTCODEHASH__erigon__regression.png)

![](figs/runtime/EXTCODEHASH__test_ext_account_query_warm__EXTCODEHASH__erigon__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_ext_account_query_warm__EXTCODEHASH__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.820
Model:                  NNLS                    Adj. R-squared:          0.817
No. Observations:       77                                RMSE:           4.10
Df Residuals:           75                                 MAE:           2.93
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      7.1216      1.5283       0.001      4.2269     10.2794
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_ext_account_query_warm__EXTCODEHASH__ethrex__regression.png)

![](figs/runtime/EXTCODEHASH__test_ext_account_query_warm__EXTCODEHASH__ethrex__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_ext_account_query_warm__EXTCODEHASH__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.903
Model:                  NNLS                    Adj. R-squared:          0.902
No. Observations:       99                                RMSE:           7.27
Df Residuals:           97                                 MAE:           5.74
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     23.7931      2.4200       0.001     18.7977     28.1612
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_ext_account_query_warm__EXTCODEHASH__geth__regression.png)

![](figs/runtime/EXTCODEHASH__test_ext_account_query_warm__EXTCODEHASH__geth__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_ext_account_query_warm__EXTCODEHASH__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.925
Model:                  NNLS                    Adj. R-squared:          0.924
No. Observations:       77                                RMSE:          40.53
Df Residuals:           75                                 MAE:          33.80
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    173.7287     15.5033       0.001    145.2003    204.2774
       opcount      0.0002      0.0000       0.001      0.0002      0.0003
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_ext_account_query_warm__EXTCODEHASH__nethermind__regression.png)

![](figs/runtime/EXTCODEHASH__test_ext_account_query_warm__EXTCODEHASH__nethermind__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_ext_account_query_warm__EXTCODEHASH__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.649
Model:                  NNLS                    Adj. R-squared:          0.646
No. Observations:       110                               RMSE:           5.82
Df Residuals:           108                                MAE:           4.63
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     11.8977      1.6940       0.001      8.2741     15.0013
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_ext_account_query_warm__EXTCODEHASH__reth__regression.png)

![](figs/runtime/EXTCODEHASH__test_ext_account_query_warm__EXTCODEHASH__reth__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_ext_account_query_warm__EXTCODEHASH__reth__diagnostics.png)

</details>

### test_account_access — combo `EXTCODEHASH_AccountMode.EXISTING_EOA`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9001 | 0.03216 | 1.00e-03 | [0.03031, 0.03387] |
| `erigon` | 55 | 0.9917 | 0.008692 | 1.00e-03 | [0.008626, 0.00877] |
| `ethrex` | 77 | 0.9824 | 0.01815 | 1.00e-03 | [0.01751, 0.01881] |
| `geth` | 99 | 0.9975 | 0.02085 | 1.00e-03 | [0.02064, 0.02105] |
| `nethermind` | 77 | 0.9801 | 0.0106 | 1.00e-03 | [0.01017, 0.011] |
| `reth` | 110 | 0.9858 | 0.004495 | 1.00e-03 | [0.004402, 0.004601] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.900
Model:                  NNLS                    Adj. R-squared:          0.899
No. Observations:       132                               RMSE:         221.23
Df Residuals:           130                                MAE:         208.47
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    234.7069     57.3442       0.001    127.4948    350.0330
       opcount      0.0322      0.0009       0.001      0.0303      0.0339
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_EOA__besu__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_EOA__besu__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_EOA__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.992
Model:                  NNLS                    Adj. R-squared:          0.992
No. Observations:       55                                RMSE:          16.87
Df Residuals:           53                                 MAE:          10.93
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0087      0.0000       0.001      0.0086      0.0088
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_EOA__erigon__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_EOA__erigon__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_EOA__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       77                                RMSE:          50.22
Df Residuals:           75                                 MAE:          44.41
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    230.5795     24.2459       0.001    182.8124    278.0865
       opcount      0.0182      0.0003       0.001      0.0175      0.0188
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_EOA__ethrex__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_EOA__ethrex__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_EOA__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.998
Model:                  NNLS                    Adj. R-squared:          0.998
No. Observations:       99                                RMSE:          21.38
Df Residuals:           97                                 MAE:          16.79
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    398.4196      7.0675       0.001    385.1706    412.7035
       opcount      0.0208      0.0001       0.001      0.0206      0.0210
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_EOA__geth__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_EOA__geth__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_EOA__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.980
Model:                  NNLS                    Adj. R-squared:          0.980
No. Observations:       77                                RMSE:          31.19
Df Residuals:           75                                 MAE:          24.19
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    108.2335     14.0320       0.001     82.9158    140.2032
       opcount      0.0106      0.0002       0.001      0.0102      0.0110
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_EOA__nethermind__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_EOA__nethermind__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_EOA__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.986
Model:                  NNLS                    Adj. R-squared:          0.986
No. Observations:       110                               RMSE:          11.13
Df Residuals:           108                                MAE:           9.00
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     97.5497      3.3183       0.001     90.9291    103.8837
       opcount      0.0045      0.0001       0.001      0.0044      0.0046
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_EOA__reth__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_EOA__reth__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_EOA__reth__diagnostics.png)

</details>

### test_account_access — combo `EXTCODEHASH_AccountMode.NON_EXISTING_ACCOUNT` — `presets[cold_account_nocode_access]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9124 | 0.03176 | 1.00e-03 | [0.03002, 0.03353] |
| `erigon` | 55 | 0.9936 | 0.007803 | 1.00e-03 | [0.007747, 0.007858] |
| `ethrex` | 77 | 0.959 | 0.002413 | 1.00e-03 | [0.002293, 0.00253] |
| `geth` | 99 | 0.9965 | 0.02016 | 1.00e-03 | [0.01991, 0.0204] |
| `nethermind` | 77 | 0.977 | 0.01074 | 1.00e-03 | [0.01039, 0.0111] |
| `reth` | 110 | 0.9766 | 0.004395 | 1.00e-03 | [0.004264, 0.004525] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.912
Model:                  NNLS                    Adj. R-squared:          0.912
No. Observations:       132                               RMSE:         203.24
Df Residuals:           130                                MAE:         190.86
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    227.0005     56.7871       0.001    112.4729    337.1885
       opcount      0.0318      0.0009       0.001      0.0300      0.0335
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__besu__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__besu__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.994
Model:                  NNLS                    Adj. R-squared:          0.993
No. Observations:       55                                RMSE:          13.54
Df Residuals:           53                                 MAE:          11.62
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0078      0.0000       0.001      0.0077      0.0079
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__erigon__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__erigon__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.959
Model:                  NNLS                    Adj. R-squared:          0.958
No. Observations:       77                                RMSE:          10.31
Df Residuals:           75                                 MAE:           8.60
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    117.1988      3.8215       0.001    109.9136    124.5841
       opcount      0.0024      0.0001       0.001      0.0023      0.0025
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__ethrex__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__ethrex__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.997
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          24.57
Df Residuals:           97                                 MAE:          19.54
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    386.4755      8.0180       0.001    371.9390    402.5634
       opcount      0.0202      0.0001       0.001      0.0199      0.0204
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__geth__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__geth__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.977
Model:                  NNLS                    Adj. R-squared:          0.977
No. Observations:       77                                RMSE:          34.02
Df Residuals:           75                                 MAE:          26.22
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     92.7876     11.4187       0.001     70.4713    116.0742
       opcount      0.0107      0.0002       0.001      0.0104      0.0111
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__nethermind__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__nethermind__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.977
Model:                  NNLS                    Adj. R-squared:          0.976
No. Observations:       110                               RMSE:          14.04
Df Residuals:           108                                MAE:          11.02
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    103.6408      4.2119       0.001     95.3256    111.9915
       opcount      0.0044      0.0001       0.001      0.0043      0.0045
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__reth__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__reth__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__reth__diagnostics.png)

</details>

### test_account_access — combo `EXTCODEHASH_AccountMode.EXISTING_CONTRACT_DIFF_MAX`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.893 | 0.04488 | 1.00e-03 | [0.04212, 0.04748] |
| `erigon` | 55 | 0.9368 | 0.02443 | 1.00e-03 | [0.02283, 0.0258] |
| `ethrex` | 77 | 0.9821 | 0.01854 | 1.00e-03 | [0.01788, 0.01922] |
| `geth` | 99 | 0.9961 | 0.01965 | 1.00e-03 | [0.01939, 0.0199] |
| `nethermind` | 77 | 0.9686 | 0.01172 | 1.00e-03 | [0.01123, 0.01219] |
| `reth` | 110 | 0.9917 | 0.01995 | 1.00e-03 | [0.01961, 0.02028] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.893
Model:                  NNLS                    Adj. R-squared:          0.892
No. Observations:       132                               RMSE:         315.88
Df Residuals:           130                                MAE:         260.78
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    795.6981     87.3201       0.001    621.5013    968.9964
       opcount      0.0449      0.0014       0.001      0.0421      0.0475
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.937
Model:                  NNLS                    Adj. R-squared:          0.936
No. Observations:       55                                RMSE:         128.97
Df Residuals:           53                                 MAE:         112.44
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    287.9576     55.9005       0.001    191.3039    406.2342
       opcount      0.0244      0.0008       0.001      0.0228      0.0258
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       77                                RMSE:          50.93
Df Residuals:           75                                 MAE:          44.60
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    224.7037     23.6349       0.001    179.5225    271.8436
       opcount      0.0185      0.0003       0.001      0.0179      0.0192
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          24.95
Df Residuals:           97                                 MAE:          19.92
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    416.0943      8.9407       0.001    399.3740    433.9502
       opcount      0.0197      0.0001       0.001      0.0194      0.0199
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.969
Model:                  NNLS                    Adj. R-squared:          0.968
No. Observations:       77                                RMSE:          42.88
Df Residuals:           75                                 MAE:          33.60
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    138.0131     14.5697       0.001    110.0837    166.1429
       opcount      0.0117      0.0003       0.001      0.0112      0.0122
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.992
Model:                  NNLS                    Adj. R-squared:          0.992
No. Observations:       110                               RMSE:          37.05
Df Residuals:           108                                MAE:          26.91
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    167.1656     10.6114       0.001    146.9197    188.8680
       opcount      0.0199      0.0002       0.001      0.0196      0.0203
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__diagnostics.png)

</details>

### test_account_access — combo `EXTCODEHASH_AccountMode.EXISTING_CONTRACT_MINIMAL`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8335 | 0.02659 | 1.00e-03 | [0.02468, 0.02851] |
| `erigon` | 55 | 0.94 | 0.02409 | 1.00e-03 | [0.02242, 0.02542] |
| `ethrex` | 77 | 0.9818 | 0.01851 | 1.00e-03 | [0.0179, 0.01917] |
| `geth` | 99 | 0.9952 | 0.01988 | 1.00e-03 | [0.01962, 0.02018] |
| `nethermind` | 77 | 0.9814 | 0.01157 | 1.00e-03 | [0.01116, 0.01195] |
| `reth` | 110 | 0.9837 | 0.004778 | 1.00e-03 | [0.004644, 0.004908] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.834
Model:                  NNLS                    Adj. R-squared:          0.832
No. Observations:       132                               RMSE:         241.55
Df Residuals:           130                                MAE:         226.48
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    339.2034     60.4042       0.001    220.4384    459.9718
       opcount      0.0266      0.0010       0.001      0.0247      0.0285
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.940
Model:                  NNLS                    Adj. R-squared:          0.939
No. Observations:       55                                RMSE:         123.72
Df Residuals:           53                                 MAE:         108.14
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    276.0549     55.2922       0.001    180.3734    393.7411
       opcount      0.0241      0.0008       0.001      0.0224      0.0254
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       77                                RMSE:          51.26
Df Residuals:           75                                 MAE:          45.19
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    223.8939     23.2175       0.001    177.5790    267.7147
       opcount      0.0185      0.0003       0.001      0.0179      0.0192
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.995
Model:                  NNLS                    Adj. R-squared:          0.995
No. Observations:       99                                RMSE:          28.15
Df Residuals:           97                                 MAE:          23.09
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    403.8889      9.7044       0.001    384.6740    423.4765
       opcount      0.0199      0.0001       0.001      0.0196      0.0202
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          32.34
Df Residuals:           75                                 MAE:          25.46
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    133.4446     12.2196       0.001    109.7377    158.4202
       opcount      0.0116      0.0002       0.001      0.0112      0.0119
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.984
Model:                  NNLS                    Adj. R-squared:          0.984
No. Observations:       110                               RMSE:          12.51
Df Residuals:           108                                MAE:           9.94
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     90.0225      4.1271       0.001     82.4810     98.3024
       opcount      0.0048      0.0001       0.001      0.0046      0.0049
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__diagnostics.png)

</details>

### test_account_access — combo `EXTCODEHASH_AccountMode.EXISTING_CONTRACT_SAME_MAX`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8373 | 0.02627 | 1.00e-03 | [0.02429, 0.0282] |
| `erigon` | 55 | 0.9393 | 0.0239 | 1.00e-03 | [0.02218, 0.02532] |
| `ethrex` | 77 | 0.9812 | 0.01855 | 1.00e-03 | [0.01789, 0.01917] |
| `geth` | 99 | 0.9922 | 0.01978 | 1.00e-03 | [0.0194, 0.02011] |
| `nethermind` | 77 | 0.9761 | 0.01178 | 1.00e-03 | [0.01138, 0.01219] |
| `reth` | 110 | 0.9821 | 0.004789 | 1.00e-03 | [0.004674, 0.004911] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.837
Model:                  NNLS                    Adj. R-squared:          0.836
No. Observations:       132                               RMSE:         235.45
Df Residuals:           130                                MAE:         220.63
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    354.7880     60.5965       0.001    240.3908    478.9246
       opcount      0.0263      0.0010       0.001      0.0243      0.0282
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.939
Model:                  NNLS                    Adj. R-squared:          0.938
No. Observations:       55                                RMSE:         123.48
Df Residuals:           53                                 MAE:         108.15
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    288.9563     57.7900       0.001    189.0297    419.7462
       opcount      0.0239      0.0008       0.001      0.0222      0.0253
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          52.25
Df Residuals:           75                                 MAE:          46.09
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    220.7102     24.2801       0.001    175.7320    268.2551
       opcount      0.0186      0.0003       0.001      0.0179      0.0192
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.992
Model:                  NNLS                    Adj. R-squared:          0.992
No. Observations:       99                                RMSE:          35.59
Df Residuals:           97                                 MAE:          23.92
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    413.3847     12.4606       0.001    392.3082    439.6233
       opcount      0.0198      0.0002       0.001      0.0194      0.0201
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.976
Model:                  NNLS                    Adj. R-squared:          0.976
No. Observations:       77                                RMSE:          37.52
Df Residuals:           75                                 MAE:          30.79
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    130.3393     13.4072       0.001    105.2371    157.4611
       opcount      0.0118      0.0002       0.001      0.0114      0.0122
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       110                               RMSE:          13.13
Df Residuals:           108                                MAE:          10.49
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     90.4530      3.9332       0.001     82.8227     97.6782
       opcount      0.0048      0.0001       0.001      0.0047      0.0049
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__diagnostics.png)

</details>

### test_account_access — combo `EXTCODEHASH_AccountMode.NON_EXISTING_ACCOUNT` — `models.custom[0]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9124 | 0.03176 | 1.00e-03 | [0.03002, 0.03353] |
| `erigon` | 55 | 0.9936 | 0.007803 | 1.00e-03 | [0.007747, 0.007858] |
| `ethrex` | 77 | 0.959 | 0.002413 | 1.00e-03 | [0.002293, 0.00253] |
| `geth` | 99 | 0.9965 | 0.02016 | 1.00e-03 | [0.01991, 0.0204] |
| `nethermind` | 77 | 0.977 | 0.01074 | 1.00e-03 | [0.01039, 0.0111] |
| `reth` | 110 | 0.9766 | 0.004395 | 1.00e-03 | [0.004264, 0.004525] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.912
Model:                  NNLS                    Adj. R-squared:          0.912
No. Observations:       132                               RMSE:         203.24
Df Residuals:           130                                MAE:         190.86
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    227.0005     56.7871       0.001    112.4729    337.1885
       opcount      0.0318      0.0009       0.001      0.0300      0.0335
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__besu__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__besu__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.994
Model:                  NNLS                    Adj. R-squared:          0.993
No. Observations:       55                                RMSE:          13.54
Df Residuals:           53                                 MAE:          11.62
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0078      0.0000       0.001      0.0077      0.0079
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__erigon__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__erigon__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.959
Model:                  NNLS                    Adj. R-squared:          0.958
No. Observations:       77                                RMSE:          10.31
Df Residuals:           75                                 MAE:           8.60
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    117.1988      3.8215       0.001    109.9136    124.5841
       opcount      0.0024      0.0001       0.001      0.0023      0.0025
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__ethrex__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__ethrex__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.997
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          24.57
Df Residuals:           97                                 MAE:          19.54
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    386.4755      8.0180       0.001    371.9390    402.5634
       opcount      0.0202      0.0001       0.001      0.0199      0.0204
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__geth__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__geth__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.977
Model:                  NNLS                    Adj. R-squared:          0.977
No. Observations:       77                                RMSE:          34.02
Df Residuals:           75                                 MAE:          26.22
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     92.7876     11.4187       0.001     70.4713    116.0742
       opcount      0.0107      0.0002       0.001      0.0104      0.0111
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__nethermind__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__nethermind__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.977
Model:                  NNLS                    Adj. R-squared:          0.976
No. Observations:       110                               RMSE:          14.04
Df Residuals:           108                                MAE:          11.02
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    103.6408      4.2119       0.001     95.3256    111.9915
       opcount      0.0044      0.0001       0.001      0.0043      0.0045
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__reth__regression.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__reth__bootstrap.png)

![](figs/runtime/EXTCODEHASH__test_account_access__EXTCODEHASH_AccountMode_NON_EXISTING_ACCOUNT__reth__diagnostics.png)

</details>

## EXTCODESIZE

### test_ext_account_query_warm — combo `EXTCODESIZE`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.3813 | 0.000144 | 1.00e-03 | [0.000111, 0.000178] |
| `erigon` | 55 | 0.8648 | 2.138e-05 | 1.00e-03 | [1.943e-05, 2.359e-05] |
| `ethrex` | 77 | 0.742 | 1.825e-05 | 1.00e-03 | [1.612e-05, 2.082e-05] |
| `geth` | 99 | 0.07771 | 1.122e-05 | 1.00e-03 | [3.394e-06, 2.029e-05] |
| `nethermind` | 77 | 0.6857 | 0.0002076 | 1.00e-03 | [0.000172, 0.0002427] |
| `reth` | 110 | 0.4111 | 1.063e-05 | 1.00e-03 | [8.944e-06, 1.244e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.381
Model:                  NNLS                    Adj. R-squared:          0.377
No. Observations:       132                               RMSE:          55.73
Df Residuals:           130                                MAE:          46.03
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    132.6814     16.4525       0.001     99.0126    164.4268
       opcount      0.0001      0.0000       0.001      0.0001      0.0002
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_ext_account_query_warm__EXTCODESIZE__besu__regression.png)

![](figs/runtime/EXTCODESIZE__test_ext_account_query_warm__EXTCODESIZE__besu__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_ext_account_query_warm__EXTCODESIZE__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.865
Model:                  NNLS                    Adj. R-squared:          0.862
No. Observations:       55                                RMSE:           2.57
Df Residuals:           53                                 MAE:           1.99
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      7.8742      0.9685       0.001      5.8193      9.6147
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_ext_account_query_warm__EXTCODESIZE__erigon__regression.png)

![](figs/runtime/EXTCODESIZE__test_ext_account_query_warm__EXTCODESIZE__erigon__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_ext_account_query_warm__EXTCODESIZE__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.742
Model:                  NNLS                    Adj. R-squared:          0.739
No. Observations:       77                                RMSE:           3.27
Df Residuals:           75                                 MAE:           2.64
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      3.8318      1.0319       0.001      1.8167      5.8986
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_ext_account_query_warm__EXTCODESIZE__ethrex__regression.png)

![](figs/runtime/EXTCODESIZE__test_ext_account_query_warm__EXTCODESIZE__ethrex__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_ext_account_query_warm__EXTCODESIZE__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.078
Model:                  NNLS                    Adj. R-squared:          0.068
No. Observations:       99                                RMSE:          11.74
Df Residuals:           97                                 MAE:           9.10
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     48.7579      4.9589       0.001     38.6602     57.6972
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_ext_account_query_warm__EXTCODESIZE__geth__regression.png)

![](figs/runtime/EXTCODESIZE__test_ext_account_query_warm__EXTCODESIZE__geth__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_ext_account_query_warm__EXTCODESIZE__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.686
Model:                  NNLS                    Adj. R-squared:          0.681
No. Observations:       77                                RMSE:          42.68
Df Residuals:           75                                 MAE:          28.68
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     89.6312     17.7892       0.001     56.2891    125.6288
       opcount      0.0002      0.0000       0.001      0.0002      0.0002
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_ext_account_query_warm__EXTCODESIZE__nethermind__regression.png)

![](figs/runtime/EXTCODESIZE__test_ext_account_query_warm__EXTCODESIZE__nethermind__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_ext_account_query_warm__EXTCODESIZE__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.411
Model:                  NNLS                    Adj. R-squared:          0.406
No. Observations:       110                               RMSE:           3.86
Df Residuals:           108                                MAE:           2.86
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      5.8712      0.8336       0.001      4.2915      7.5060
       opcount      0.0000      0.0000       0.001      0.0000      0.0000
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_ext_account_query_warm__EXTCODESIZE__reth__regression.png)

![](figs/runtime/EXTCODESIZE__test_ext_account_query_warm__EXTCODESIZE__reth__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_ext_account_query_warm__EXTCODESIZE__reth__diagnostics.png)

</details>

### test_account_access — combo `EXTCODESIZE_AccountMode.EXISTING_EOA`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8987 | 0.03239 | 1.00e-03 | [0.03032, 0.0343] |
| `erigon` | 55 | 0.9951 | 0.007998 | 1.00e-03 | [0.007948, 0.008042] |
| `ethrex` | 77 | 0.9806 | 0.0183 | 1.00e-03 | [0.01768, 0.01895] |
| `geth` | 99 | 0.9969 | 0.02086 | 1.00e-03 | [0.02064, 0.02108] |
| `nethermind` | 77 | 0.977 | 0.01072 | 1.00e-03 | [0.01038, 0.0111] |
| `reth` | 110 | 0.9787 | 0.004503 | 1.00e-03 | [0.004376, 0.004636] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.899
Model:                  NNLS                    Adj. R-squared:          0.898
No. Observations:       132                               RMSE:         217.43
Df Residuals:           130                                MAE:         202.64
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    217.7220     60.2968       0.001     98.2031    334.7644
       opcount      0.0324      0.0010       0.001      0.0303      0.0343
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_EOA__besu__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_EOA__besu__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_EOA__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.995
Model:                  NNLS                    Adj. R-squared:          0.995
No. Observations:       55                                RMSE:          11.57
Df Residuals:           53                                 MAE:           9.61
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0133       1.000      0.0000      0.0000
       opcount      0.0080      0.0000       0.001      0.0079      0.0080
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_EOA__erigon__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_EOA__erigon__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_EOA__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.980
No. Observations:       77                                RMSE:          51.52
Df Residuals:           75                                 MAE:          46.26
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    213.8813     22.3641       0.001    170.8121    257.5847
       opcount      0.0183      0.0003       0.001      0.0177      0.0190
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_EOA__ethrex__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_EOA__ethrex__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_EOA__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.997
Model:                  NNLS                    Adj. R-squared:          0.997
No. Observations:       99                                RMSE:          23.20
Df Residuals:           97                                 MAE:          18.75
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    390.3141      7.7262       0.001    375.5482    406.5263
       opcount      0.0209      0.0001       0.001      0.0206      0.0211
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_EOA__geth__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_EOA__geth__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_EOA__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.977
Model:                  NNLS                    Adj. R-squared:          0.977
No. Observations:       77                                RMSE:          32.88
Df Residuals:           75                                 MAE:          25.43
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     92.9219     11.8895       0.001     69.4671    115.9268
       opcount      0.0107      0.0002       0.001      0.0104      0.0111
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_EOA__nethermind__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_EOA__nethermind__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_EOA__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.979
Model:                  NNLS                    Adj. R-squared:          0.978
No. Observations:       110                               RMSE:          13.30
Df Residuals:           108                                MAE:          10.35
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     96.4396      4.1523       0.001     88.0864    104.4223
       opcount      0.0045      0.0001       0.001      0.0044      0.0046
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_EOA__reth__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_EOA__reth__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_EOA__reth__diagnostics.png)

</details>

### test_account_access — combo `EXTCODESIZE_AccountMode.NON_EXISTING_ACCOUNT` — `presets[cold_account_nocode_access]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8983 | 0.03156 | 1.00e-03 | [0.02977, 0.03337] |
| `erigon` | 55 | 0.9933 | 0.00778 | 1.00e-03 | [0.007718, 0.007834] |
| `ethrex` | 77 | 0.9538 | 0.002419 | 1.00e-03 | [0.002291, 0.002546] |
| `geth` | 99 | 0.9958 | 0.0203 | 1.00e-03 | [0.02001, 0.02057] |
| `nethermind` | 77 | 0.9817 | 0.01057 | 1.00e-03 | [0.01023, 0.01094] |
| `reth` | 110 | 0.9787 | 0.00441 | 1.00e-03 | [0.004297, 0.004537] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.898
Model:                  NNLS                    Adj. R-squared:          0.897
No. Observations:       132                               RMSE:         212.36
Df Residuals:           130                                MAE:         196.13
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    251.9743     55.4745       0.001    138.8488    354.5821
       opcount      0.0316      0.0009       0.001      0.0298      0.0334
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__besu__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__besu__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.993
Model:                  NNLS                    Adj. R-squared:          0.993
No. Observations:       55                                RMSE:          13.40
Df Residuals:           53                                 MAE:          11.19
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0078      0.0000       0.001      0.0077      0.0078
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__erigon__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__erigon__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.954
Model:                  NNLS                    Adj. R-squared:          0.953
No. Observations:       77                                RMSE:          10.64
Df Residuals:           75                                 MAE:           8.50
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    113.7293      3.8818       0.001    106.1551    121.4056
       opcount      0.0024      0.0001       0.001      0.0023      0.0025
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          26.21
Df Residuals:           97                                 MAE:          21.25
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    382.9513      8.9918       0.001    366.6415    401.7907
       opcount      0.0203      0.0001       0.001      0.0200      0.0206
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__geth__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__geth__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          28.89
Df Residuals:           75                                 MAE:          24.00
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     87.6898     11.0186       0.001     65.4168    107.8622
       opcount      0.0106      0.0002       0.001      0.0102      0.0109
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.979
Model:                  NNLS                    Adj. R-squared:          0.978
No. Observations:       110                               RMSE:          13.02
Df Residuals:           108                                MAE:           9.71
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    102.3247      3.8578       0.001     94.5040    109.7071
       opcount      0.0044      0.0001       0.001      0.0043      0.0045
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__reth__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__reth__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__reth__diagnostics.png)

</details>

### test_account_access — combo `EXTCODESIZE_AccountMode.EXISTING_CONTRACT_DIFF_MAX`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8917 | 0.04477 | 1.00e-03 | [0.04189, 0.04751] |
| `erigon` | 55 | 0.899 | 0.1441 | 1.00e-03 | [0.1307, 0.1547] |
| `ethrex` | 77 | 0.9968 | 0.1 | 1.00e-03 | [0.09858, 0.1013] |
| `geth` | 99 | 0.938 | 0.04184 | 1.00e-03 | [0.03917, 0.04432] |
| `nethermind` | 77 | 0.928 | 0.03598 | 1.00e-03 | [0.03347, 0.03861] |
| `reth` | 110 | 0.9959 | 0.02247 | 1.00e-03 | [0.02219, 0.02276] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.892
Model:                  NNLS                    Adj. R-squared:          0.891
No. Observations:       132                               RMSE:         307.36
Df Residuals:           130                                MAE:         256.32
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    781.9027     87.6832       0.001    620.5924    961.2178
       opcount      0.0448      0.0014       0.001      0.0419      0.0475
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.899
Model:                  NNLS                    Adj. R-squared:          0.897
No. Observations:       55                                RMSE:         950.96
Df Residuals:           53                                 MAE:         824.19
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    872.8213    449.2427       0.013    113.1092   1809.8005
       opcount      0.1441      0.0063       0.001      0.1307      0.1547
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.997
Model:                  NNLS                    Adj. R-squared:          0.997
No. Observations:       77                                RMSE:         111.92
Df Residuals:           75                                 MAE:          90.45
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    444.5370     42.9719       0.001    367.9065    533.6409
       opcount      0.1000      0.0007       0.001      0.0986      0.1013
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.938
Model:                  NNLS                    Adj. R-squared:          0.937
No. Observations:       99                                RMSE:         211.81
Df Residuals:           97                                 MAE:         179.04
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const   1267.3353     88.0998       0.001   1094.0173   1458.5300
       opcount      0.0418      0.0013       0.001      0.0392      0.0443
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.928
Model:                  NNLS                    Adj. R-squared:          0.927
No. Observations:       77                                RMSE:         197.44
Df Residuals:           75                                 MAE:         166.92
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    610.3246     92.0799       0.001    431.6284    791.7922
       opcount      0.0360      0.0013       0.001      0.0335      0.0386
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       110                               RMSE:          28.45
Df Residuals:           108                                MAE:          21.01
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    149.2346      9.0502       0.001    132.2996    167.3143
       opcount      0.0225      0.0001       0.001      0.0222      0.0228
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__diagnostics.png)

</details>

### test_account_access — combo `EXTCODESIZE_AccountMode.EXISTING_CONTRACT_MINIMAL`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8372 | 0.0264 | 1.00e-03 | [0.02444, 0.02842] |
| `erigon` | 55 | 0.9364 | 0.02374 | 1.00e-03 | [0.02203, 0.02512] |
| `ethrex` | 77 | 0.982 | 0.0186 | 1.00e-03 | [0.01795, 0.01924] |
| `geth` | 99 | 0.9964 | 0.0199 | 1.00e-03 | [0.01963, 0.02016] |
| `nethermind` | 77 | 0.9703 | 0.0117 | 1.00e-03 | [0.01132, 0.01214] |
| `reth` | 110 | 0.9853 | 0.004859 | 1.00e-03 | [0.004734, 0.004982] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.837
Model:                  NNLS                    Adj. R-squared:          0.836
No. Observations:       132                               RMSE:         229.34
Df Residuals:           130                                MAE:         214.33
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    338.8734     58.1210       0.001    221.8135    451.7552
       opcount      0.0264      0.0010       0.001      0.0244      0.0284
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.936
Model:                  NNLS                    Adj. R-squared:          0.935
No. Observations:       55                                RMSE:         121.92
Df Residuals:           53                                 MAE:         105.32
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    281.6913     55.1562       0.001    185.4131    403.9803
       opcount      0.0237      0.0008       0.001      0.0220      0.0251
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       77                                RMSE:          49.54
Df Residuals:           75                                 MAE:          44.02
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    217.0286     22.9245       0.001    174.5815    263.3305
       opcount      0.0186      0.0003       0.001      0.0179      0.0192
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          23.69
Df Residuals:           97                                 MAE:          19.25
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    405.4007      8.1012       0.001    390.9009    421.8726
       opcount      0.0199      0.0001       0.001      0.0196      0.0202
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.970
Model:                  NNLS                    Adj. R-squared:          0.970
No. Observations:       77                                RMSE:          40.29
Df Residuals:           75                                 MAE:          32.35
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    121.0463     13.0912       0.001     94.0778    146.5984
       opcount      0.0117      0.0002       0.001      0.0113      0.0121
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.985
Model:                  NNLS                    Adj. R-squared:          0.985
No. Observations:       110                               RMSE:          11.69
Df Residuals:           108                                MAE:           9.60
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     84.7572      3.8598       0.001     77.1559     92.7283
       opcount      0.0049      0.0001       0.001      0.0047      0.0050
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__diagnostics.png)

</details>

### test_account_access — combo `EXTCODESIZE_AccountMode.EXISTING_CONTRACT_SAME_MAX`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8388 | 0.02676 | 1.00e-03 | [0.02466, 0.02876] |
| `erigon` | 55 | 0.9374 | 0.02382 | 1.00e-03 | [0.02222, 0.02521] |
| `ethrex` | 77 | 0.9816 | 0.01853 | 1.00e-03 | [0.01793, 0.0192] |
| `geth` | 99 | 0.995 | 0.01997 | 1.00e-03 | [0.01964, 0.02026] |
| `nethermind` | 77 | 0.9726 | 0.01161 | 1.00e-03 | [0.01122, 0.01202] |
| `reth` | 110 | 0.981 | 0.004768 | 1.00e-03 | [0.004658, 0.004879] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.839
Model:                  NNLS                    Adj. R-squared:          0.838
No. Observations:       132                               RMSE:         231.06
Df Residuals:           130                                MAE:         215.57
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    323.3719     60.3637       0.001    211.4272    441.3864
       opcount      0.0268      0.0011       0.001      0.0247      0.0288
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.937
Model:                  NNLS                    Adj. R-squared:          0.936
No. Observations:       55                                RMSE:         121.24
Df Residuals:           53                                 MAE:         104.11
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    282.5433     55.2622       0.001    185.6032    394.4470
       opcount      0.0238      0.0008       0.001      0.0222      0.0252
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          50.03
Df Residuals:           75                                 MAE:          44.14
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    221.3448     22.6794       0.001    176.1187    264.6523
       opcount      0.0185      0.0003       0.001      0.0179      0.0192
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.995
Model:                  NNLS                    Adj. R-squared:          0.995
No. Observations:       99                                RMSE:          27.95
Df Residuals:           97                                 MAE:          22.73
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    395.9109      9.8488       0.001    378.0221    417.6454
       opcount      0.0200      0.0002       0.001      0.0196      0.0203
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.973
Model:                  NNLS                    Adj. R-squared:          0.972
No. Observations:       77                                RMSE:          38.40
Df Residuals:           75                                 MAE:          29.27
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    125.9844     12.7675       0.001    101.4158    154.5838
       opcount      0.0116      0.0002       0.001      0.0112      0.0120
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       110                               RMSE:          13.06
Df Residuals:           108                                MAE:          10.08
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     92.6753      3.5829       0.001     85.9568     99.9640
       opcount      0.0048      0.0001       0.001      0.0047      0.0049
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__diagnostics.png)

</details>

### test_account_access — combo `EXTCODESIZE_AccountMode.NON_EXISTING_ACCOUNT` — `models.custom[0]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8983 | 0.03156 | 1.00e-03 | [0.02977, 0.03337] |
| `erigon` | 55 | 0.9933 | 0.00778 | 1.00e-03 | [0.007718, 0.007834] |
| `ethrex` | 77 | 0.9538 | 0.002419 | 1.00e-03 | [0.002291, 0.002546] |
| `geth` | 99 | 0.9958 | 0.0203 | 1.00e-03 | [0.02001, 0.02057] |
| `nethermind` | 77 | 0.9817 | 0.01057 | 1.00e-03 | [0.01023, 0.01094] |
| `reth` | 110 | 0.9787 | 0.00441 | 1.00e-03 | [0.004297, 0.004537] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.898
Model:                  NNLS                    Adj. R-squared:          0.897
No. Observations:       132                               RMSE:         212.36
Df Residuals:           130                                MAE:         196.13
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    251.9743     55.4745       0.001    138.8488    354.5821
       opcount      0.0316      0.0009       0.001      0.0298      0.0334
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__besu__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__besu__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.993
Model:                  NNLS                    Adj. R-squared:          0.993
No. Observations:       55                                RMSE:          13.40
Df Residuals:           53                                 MAE:          11.19
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0078      0.0000       0.001      0.0077      0.0078
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__erigon__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__erigon__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.954
Model:                  NNLS                    Adj. R-squared:          0.953
No. Observations:       77                                RMSE:          10.64
Df Residuals:           75                                 MAE:           8.50
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    113.7293      3.8818       0.001    106.1551    121.4056
       opcount      0.0024      0.0001       0.001      0.0023      0.0025
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          26.21
Df Residuals:           97                                 MAE:          21.25
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    382.9513      8.9918       0.001    366.6415    401.7907
       opcount      0.0203      0.0001       0.001      0.0200      0.0206
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__geth__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__geth__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          28.89
Df Residuals:           75                                 MAE:          24.00
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     87.6898     11.0186       0.001     65.4168    107.8622
       opcount      0.0106      0.0002       0.001      0.0102      0.0109
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.979
Model:                  NNLS                    Adj. R-squared:          0.978
No. Observations:       110                               RMSE:          13.02
Df Residuals:           108                                MAE:           9.71
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    102.3247      3.8578       0.001     94.5040    109.7071
       opcount      0.0044      0.0001       0.001      0.0043      0.0045
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__reth__regression.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__reth__bootstrap.png)

![](figs/runtime/EXTCODESIZE__test_account_access__EXTCODESIZE_AccountMode_NON_EXISTING_ACCOUNT__reth__diagnostics.png)

</details>

## STATICCALL

### test_ext_account_query_warm — combo `STATICCALL`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.6823 | 0.00038 | 1.00e-03 | [0.0003317, 0.0004266] |
| `erigon` | 55 | 0.9334 | 6.854e-05 | 1.00e-03 | [6.32e-05, 7.31e-05] |
| `ethrex` | 77 | 0.9507 | 9.434e-05 | 1.00e-03 | [8.928e-05, 9.977e-05] |
| `geth` | 99 | 0.9448 | 0.0001759 | 1.00e-03 | [0.0001682, 0.000184] |
| `nethermind` | 77 | 0.878 | 0.0003535 | 1.00e-03 | [0.0003228, 0.0003841] |
| `reth` | 110 | 0.88 | 5.066e-05 | 1.00e-03 | [4.738e-05, 5.417e-05] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.682
Model:                  NNLS                    Adj. R-squared:          0.680
No. Observations:       132                               RMSE:         134.28
Df Residuals:           130                                MAE:         106.55
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    610.4007     39.3889       0.001    535.4728    692.8060
       opcount      0.0004      0.0000       0.001      0.0003      0.0004
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_ext_account_query_warm__STATICCALL__besu__regression.png)

![](figs/runtime/STATICCALL__test_ext_account_query_warm__STATICCALL__besu__bootstrap.png)

![](figs/runtime/STATICCALL__test_ext_account_query_warm__STATICCALL__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.933
Model:                  NNLS                    Adj. R-squared:          0.932
No. Observations:       55                                RMSE:           9.48
Df Residuals:           53                                 MAE:           7.31
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     37.4952      4.4739       0.001     29.3915     46.9137
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_ext_account_query_warm__STATICCALL__erigon__regression.png)

![](figs/runtime/STATICCALL__test_ext_account_query_warm__STATICCALL__erigon__bootstrap.png)

![](figs/runtime/STATICCALL__test_ext_account_query_warm__STATICCALL__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.951
Model:                  NNLS                    Adj. R-squared:          0.950
No. Observations:       77                                RMSE:          11.12
Df Residuals:           75                                 MAE:           9.01
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     44.7968      4.1994       0.001     36.5231     53.1631
       opcount      0.0001      0.0000       0.001      0.0001      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_ext_account_query_warm__STATICCALL__ethrex__regression.png)

![](figs/runtime/STATICCALL__test_ext_account_query_warm__STATICCALL__ethrex__bootstrap.png)

![](figs/runtime/STATICCALL__test_ext_account_query_warm__STATICCALL__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.945
Model:                  NNLS                    Adj. R-squared:          0.944
No. Observations:       99                                RMSE:          22.02
Df Residuals:           97                                 MAE:          16.55
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     56.2809      6.5983       0.001     43.6215     69.1411
       opcount      0.0002      0.0000       0.001      0.0002      0.0002
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_ext_account_query_warm__STATICCALL__geth__regression.png)

![](figs/runtime/STATICCALL__test_ext_account_query_warm__STATICCALL__geth__bootstrap.png)

![](figs/runtime/STATICCALL__test_ext_account_query_warm__STATICCALL__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.878
Model:                  NNLS                    Adj. R-squared:          0.876
No. Observations:       77                                RMSE:          68.26
Df Residuals:           75                                 MAE:          55.00
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    229.8987     28.6232       0.001    177.5955    289.5333
       opcount      0.0004      0.0000       0.001      0.0003      0.0004
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_ext_account_query_warm__STATICCALL__nethermind__regression.png)

![](figs/runtime/STATICCALL__test_ext_account_query_warm__STATICCALL__nethermind__bootstrap.png)

![](figs/runtime/STATICCALL__test_ext_account_query_warm__STATICCALL__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.880
Model:                  NNLS                    Adj. R-squared:          0.879
No. Observations:       110                               RMSE:           9.69
Df Residuals:           108                                MAE:           7.42
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     34.2779      3.3311       0.001     27.6420     40.4959
       opcount      0.0001      0.0000       0.001      0.0000      0.0001
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_ext_account_query_warm__STATICCALL__reth__regression.png)

![](figs/runtime/STATICCALL__test_ext_account_query_warm__STATICCALL__reth__bootstrap.png)

![](figs/runtime/STATICCALL__test_ext_account_query_warm__STATICCALL__reth__diagnostics.png)

</details>

### test_account_access — combo `STATICCALL_AccountMode.EXISTING_EOA`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9091 | 0.03369 | 1.00e-03 | [0.03182, 0.03544] |
| `erigon` | 55 | 0.9955 | 0.008606 | 1.00e-03 | [0.008551, 0.008659] |
| `ethrex` | 77 | 0.9825 | 0.01839 | 1.00e-03 | [0.01776, 0.01905] |
| `geth` | 99 | 0.9969 | 0.02114 | 1.00e-03 | [0.02088, 0.02143] |
| `nethermind` | 77 | 0.9807 | 0.0109 | 1.00e-03 | [0.01055, 0.01125] |
| `reth` | 110 | 0.9702 | 0.004651 | 1.00e-03 | [0.004519, 0.004799] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.909
Model:                  NNLS                    Adj. R-squared:          0.908
No. Observations:       132                               RMSE:         218.93
Df Residuals:           130                                MAE:         203.24
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    316.0138     59.4023       0.001    200.4851    433.9810
       opcount      0.0337      0.0009       0.001      0.0318      0.0354
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_EOA__besu__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_EOA__besu__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_EOA__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.995
Model:                  NNLS                    Adj. R-squared:          0.995
No. Observations:       55                                RMSE:          12.27
Df Residuals:           53                                 MAE:          10.03
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0086      0.0000       0.001      0.0086      0.0087
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_EOA__erigon__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_EOA__erigon__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_EOA__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       77                                RMSE:          50.49
Df Residuals:           75                                 MAE:          44.40
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    225.8665     23.9220       0.001    177.7463    270.9703
       opcount      0.0184      0.0003       0.001      0.0178      0.0191
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_EOA__ethrex__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_EOA__ethrex__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_EOA__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.997
Model:                  NNLS                    Adj. R-squared:          0.997
No. Observations:       99                                RMSE:          24.27
Df Residuals:           97                                 MAE:          19.26
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    400.6952      9.0321       0.001    382.4079    419.1677
       opcount      0.0211      0.0001       0.001      0.0209      0.0214
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_EOA__geth__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_EOA__geth__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_EOA__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.980
No. Observations:       77                                RMSE:          31.43
Df Residuals:           75                                 MAE:          24.80
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    102.7091     10.6800       0.001     82.0292    123.5486
       opcount      0.0109      0.0002       0.001      0.0106      0.0113
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_EOA__nethermind__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_EOA__nethermind__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_EOA__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.970
Model:                  NNLS                    Adj. R-squared:          0.970
No. Observations:       110                               RMSE:          16.77
Df Residuals:           108                                MAE:          12.40
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    109.6952      4.6585       0.001    100.3998    118.8607
       opcount      0.0047      0.0001       0.001      0.0045      0.0048
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_EOA__reth__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_EOA__reth__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_EOA__reth__diagnostics.png)

</details>

### test_account_access — combo `STATICCALL_AccountMode.NON_EXISTING_ACCOUNT` — `presets[cold_account_nocode_access]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9002 | 0.03348 | 1.00e-03 | [0.03145, 0.03549] |
| `erigon` | 55 | 0.9958 | 0.008721 | 1.00e-03 | [0.008671, 0.008771] |
| `ethrex` | 77 | 0.9651 | 0.00262 | 1.00e-03 | [0.002513, 0.002731] |
| `geth` | 99 | 0.9962 | 0.02161 | 1.00e-03 | [0.0213, 0.02193] |
| `nethermind` | 77 | 0.9746 | 0.01075 | 1.00e-03 | [0.01039, 0.01117] |
| `reth` | 110 | 0.9757 | 0.004462 | 1.00e-03 | [0.004306, 0.004628] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.900
Model:                  NNLS                    Adj. R-squared:          0.899
No. Observations:       132                               RMSE:         229.18
Df Residuals:           130                                MAE:         214.29
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    363.8872     65.6575       0.001    233.2772    491.8147
       opcount      0.0335      0.0010       0.001      0.0315      0.0355
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__besu__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__besu__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       55                                RMSE:          11.86
Df Residuals:           53                                 MAE:           9.53
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0087      0.0000       0.001      0.0087      0.0088
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.965
Model:                  NNLS                    Adj. R-squared:          0.965
No. Observations:       77                                RMSE:          10.24
Df Residuals:           75                                 MAE:           8.44
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    110.1344      3.3769       0.001    103.3579    116.6195
       opcount      0.0026      0.0001       0.001      0.0025      0.0027
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          27.49
Df Residuals:           97                                 MAE:          21.42
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    398.0493      9.7951       0.001    379.2648    417.7261
       opcount      0.0216      0.0002       0.001      0.0213      0.0219
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__geth__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__geth__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.975
Model:                  NNLS                    Adj. R-squared:          0.974
No. Observations:       77                                RMSE:          35.65
Df Residuals:           75                                 MAE:          29.10
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    111.0433     12.2693       0.001     86.3994    134.8906
       opcount      0.0108      0.0002       0.001      0.0104      0.0112
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.976
Model:                  NNLS                    Adj. R-squared:          0.975
No. Observations:       110                               RMSE:          14.47
Df Residuals:           108                                MAE:          10.47
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    104.4487      4.5808       0.001     95.3192    113.3987
       opcount      0.0045      0.0001       0.001      0.0043      0.0046
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__reth__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__reth__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__reth__diagnostics.png)

</details>

### test_account_access — combo `STATICCALL_AccountMode.EXISTING_CONTRACT_DIFF_MAX`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8893 | 0.04751 | 1.00e-03 | [0.04454, 0.05021] |
| `erigon` | 55 | 0.8994 | 0.1555 | 1.00e-03 | [0.1417, 0.1669] |
| `ethrex` | 77 | 0.9976 | 0.101 | 1.00e-03 | [0.09994, 0.1021] |
| `geth` | 99 | 0.9362 | 0.04165 | 1.00e-03 | [0.0391, 0.04417] |
| `nethermind` | 77 | 0.9098 | 0.03694 | 1.00e-03 | [0.03424, 0.03968] |
| `reth` | 110 | 0.9954 | 0.02368 | 1.00e-03 | [0.02339, 0.02398] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.889
Model:                  NNLS                    Adj. R-squared:          0.888
No. Observations:       132                               RMSE:         339.27
Df Residuals:           130                                MAE:         282.15
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    851.2606     91.5118       0.001    686.0951   1038.3779
       opcount      0.0475      0.0015       0.001      0.0445      0.0502
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.899
Model:                  NNLS                    Adj. R-squared:          0.898
No. Observations:       55                                RMSE:        1052.47
Df Residuals:           53                                 MAE:         909.85
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    906.3559    473.9314       0.020     53.7803   1883.8779
       opcount      0.1555      0.0065       0.001      0.1417      0.1669
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.998
Model:                  NNLS                    Adj. R-squared:          0.998
No. Observations:       77                                RMSE:         100.83
Df Residuals:           75                                 MAE:          81.02
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    446.6078     36.8965       0.001    376.4028    524.2565
       opcount      0.1010      0.0005       0.001      0.0999      0.1021
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.936
Model:                  NNLS                    Adj. R-squared:          0.936
No. Observations:       99                                RMSE:         220.01
Df Residuals:           97                                 MAE:         182.63
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const   1325.9773     91.6560       0.001   1155.3644   1506.3855
       opcount      0.0417      0.0013       0.001      0.0391      0.0442
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.910
Model:                  NNLS                    Adj. R-squared:          0.909
No. Observations:       77                                RMSE:         235.46
Df Residuals:           75                                 MAE:         197.45
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    700.5761     97.9311       0.001    508.2522    894.0264
       opcount      0.0369      0.0014       0.001      0.0342      0.0397
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.995
Model:                  NNLS                    Adj. R-squared:          0.995
No. Observations:       110                               RMSE:          32.67
Df Residuals:           108                                MAE:          26.82
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    137.2703      9.1339       0.001    119.0717    154.9947
       opcount      0.0237      0.0002       0.001      0.0234      0.0240
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__diagnostics.png)

</details>

### test_account_access — combo `STATICCALL_AccountMode.EXISTING_CONTRACT_MINIMAL`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8559 | 0.02798 | 1.00e-03 | [0.02616, 0.03004] |
| `erigon` | 55 | 0.9376 | 0.02456 | 1.00e-03 | [0.02276, 0.02594] |
| `ethrex` | 77 | 0.9818 | 0.01872 | 1.00e-03 | [0.01811, 0.0194] |
| `geth` | 99 | 0.9961 | 0.02023 | 1.00e-03 | [0.01995, 0.0205] |
| `nethermind` | 77 | 0.9797 | 0.01265 | 1.00e-03 | [0.01226, 0.01309] |
| `reth` | 110 | 0.9777 | 0.005193 | 1.00e-03 | [0.005071, 0.00532] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.856
Model:                  NNLS                    Adj. R-squared:          0.855
No. Observations:       132                               RMSE:         232.34
Df Residuals:           130                                MAE:         218.48
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    395.1396     61.5656       0.001    268.8694    509.8825
       opcount      0.0280      0.0010       0.001      0.0262      0.0300
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.938
Model:                  NNLS                    Adj. R-squared:          0.936
No. Observations:       55                                RMSE:         128.23
Df Residuals:           53                                 MAE:         110.59
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    301.7190     60.7847       0.001    200.3280    440.4044
       opcount      0.0246      0.0008       0.001      0.0228      0.0259
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       77                                RMSE:          51.53
Df Residuals:           75                                 MAE:          45.79
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    219.1807     23.3488       0.001    173.2950    264.0622
       opcount      0.0187      0.0003       0.001      0.0181      0.0194
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          25.63
Df Residuals:           97                                 MAE:          20.67
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    410.5354      9.1563       0.001    393.2171    429.0515
       opcount      0.0202      0.0001       0.001      0.0199      0.0205
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.980
Model:                  NNLS                    Adj. R-squared:          0.979
No. Observations:       77                                RMSE:          36.87
Df Residuals:           75                                 MAE:          28.55
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    126.9510     13.0108       0.001     99.5011    151.6024
       opcount      0.0126      0.0002       0.001      0.0123      0.0131
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.978
Model:                  NNLS                    Adj. R-squared:          0.977
No. Observations:       110                               RMSE:          15.87
Df Residuals:           108                                MAE:          12.05
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     97.4029      3.8531       0.001     89.9569    105.0411
       opcount      0.0052      0.0001       0.001      0.0051      0.0053
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__diagnostics.png)

</details>

### test_account_access — combo `STATICCALL_AccountMode.EXISTING_CONTRACT_SAME_MAX`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8511 | 0.02778 | 1.00e-03 | [0.02574, 0.02961] |
| `erigon` | 55 | 0.9243 | 0.03508 | 1.00e-03 | [0.03232, 0.03736] |
| `ethrex` | 77 | 0.9812 | 0.01878 | 1.00e-03 | [0.01807, 0.01947] |
| `geth` | 99 | 0.9961 | 0.0203 | 1.00e-03 | [0.02004, 0.02057] |
| `nethermind` | 77 | 0.9826 | 0.0124 | 1.00e-03 | [0.01203, 0.0128] |
| `reth` | 110 | 0.9829 | 0.005168 | 1.00e-03 | [0.005059, 0.005297] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.851
Model:                  NNLS                    Adj. R-squared:          0.850
No. Observations:       132                               RMSE:         235.23
Df Residuals:           130                                MAE:         221.31
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    408.9938     60.7457       0.001    289.5932    527.5140
       opcount      0.0278      0.0010       0.001      0.0257      0.0296
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.924
Model:                  NNLS                    Adj. R-squared:          0.923
No. Observations:       55                                RMSE:         203.21
Df Residuals:           53                                 MAE:         173.85
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    320.9428     91.3941       0.001    164.5099    520.9135
       opcount      0.0351      0.0013       0.001      0.0323      0.0374
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          52.63
Df Residuals:           75                                 MAE:          45.95
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    219.8042     25.0156       0.001    174.1111    269.2799
       opcount      0.0188      0.0004       0.001      0.0181      0.0195
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          25.71
Df Residuals:           97                                 MAE:          21.24
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    406.9206      8.5623       0.001    389.9467    423.6550
       opcount      0.0203      0.0001       0.001      0.0200      0.0206
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.983
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       77                                RMSE:          33.42
Df Residuals:           75                                 MAE:          27.03
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    147.1394     13.3523       0.001    120.9365    172.9034
       opcount      0.0124      0.0002       0.001      0.0120      0.0128
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.983
Model:                  NNLS                    Adj. R-squared:          0.983
No. Observations:       110                               RMSE:          13.79
Df Residuals:           108                                MAE:          10.84
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     98.8077      3.7713       0.001     91.6136    106.4753
       opcount      0.0052      0.0001       0.001      0.0051      0.0053
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__diagnostics.png)

</details>

### test_account_access — combo `STATICCALL_AccountMode.NON_EXISTING_ACCOUNT` — `models.custom[0]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.9002 | 0.03348 | 1.00e-03 | [0.03145, 0.03549] |
| `erigon` | 55 | 0.9958 | 0.008721 | 1.00e-03 | [0.008671, 0.008771] |
| `ethrex` | 77 | 0.9651 | 0.00262 | 1.00e-03 | [0.002513, 0.002731] |
| `geth` | 99 | 0.9962 | 0.02161 | 1.00e-03 | [0.0213, 0.02193] |
| `nethermind` | 77 | 0.9746 | 0.01075 | 1.00e-03 | [0.01039, 0.01117] |
| `reth` | 110 | 0.9757 | 0.004462 | 1.00e-03 | [0.004306, 0.004628] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.900
Model:                  NNLS                    Adj. R-squared:          0.899
No. Observations:       132                               RMSE:         229.18
Df Residuals:           130                                MAE:         214.29
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    363.8872     65.6575       0.001    233.2772    491.8147
       opcount      0.0335      0.0010       0.001      0.0315      0.0355
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__besu__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__besu__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       55                                RMSE:          11.86
Df Residuals:           53                                 MAE:           9.53
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0087      0.0000       0.001      0.0087      0.0088
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.965
Model:                  NNLS                    Adj. R-squared:          0.965
No. Observations:       77                                RMSE:          10.24
Df Residuals:           75                                 MAE:           8.44
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    110.1344      3.3769       0.001    103.3579    116.6195
       opcount      0.0026      0.0001       0.001      0.0025      0.0027
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          27.49
Df Residuals:           97                                 MAE:          21.42
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    398.0493      9.7951       0.001    379.2648    417.7261
       opcount      0.0216      0.0002       0.001      0.0213      0.0219
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__geth__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__geth__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.975
Model:                  NNLS                    Adj. R-squared:          0.974
No. Observations:       77                                RMSE:          35.65
Df Residuals:           75                                 MAE:          29.10
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    111.0433     12.2693       0.001     86.3994    134.8906
       opcount      0.0108      0.0002       0.001      0.0104      0.0112
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.976
Model:                  NNLS                    Adj. R-squared:          0.975
No. Observations:       110                               RMSE:          14.47
Df Residuals:           108                                MAE:          10.47
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    104.4487      4.5808       0.001     95.3192    113.3987
       opcount      0.0045      0.0001       0.001      0.0043      0.0046
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__reth__regression.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__reth__bootstrap.png)

![](figs/runtime/STATICCALL__test_account_access__STATICCALL_AccountMode_NON_EXISTING_ACCOUNT__reth__diagnostics.png)

</details>

## EXTCODECOPY

### test_account_access — combo `EXTCODECOPY_AccountMode.EXISTING_EOA`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8965 | 0.03249 | 1.00e-03 | [0.03066, 0.03443] |
| `erigon` | 55 | 0.9909 | 0.008018 | 1.00e-03 | [0.007953, 0.008088] |
| `ethrex` | 77 | 0.9813 | 0.01821 | 1.00e-03 | [0.01755, 0.01887] |
| `geth` | 99 | 0.9952 | 0.02134 | 1.00e-03 | [0.02105, 0.02163] |
| `nethermind` | 77 | 0.9813 | 0.01077 | 1.00e-03 | [0.01042, 0.01115] |
| `reth` | 110 | 0.9839 | 0.004556 | 1.00e-03 | [0.004459, 0.004652] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.897
Model:                  NNLS                    Adj. R-squared:          0.896
No. Observations:       132                               RMSE:         213.72
Df Residuals:           130                                MAE:         199.67
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    221.5485     56.7370       0.001    107.4221    329.2081
       opcount      0.0325      0.0010       0.001      0.0307      0.0344
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_EOA__besu__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_EOA__besu__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_EOA__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.991
Model:                  NNLS                    Adj. R-squared:          0.991
No. Observations:       55                                RMSE:          15.26
Df Residuals:           53                                 MAE:          10.14
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.1437       1.000      0.0000      0.0000
       opcount      0.0080      0.0000       0.001      0.0080      0.0081
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_EOA__erigon__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_EOA__erigon__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_EOA__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          48.66
Df Residuals:           75                                 MAE:          43.10
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    220.8600     22.5314       0.001    176.6894    266.7560
       opcount      0.0182      0.0003       0.001      0.0176      0.0189
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_EOA__ethrex__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_EOA__ethrex__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_EOA__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.995
Model:                  NNLS                    Adj. R-squared:          0.995
No. Observations:       99                                RMSE:          28.85
Df Residuals:           97                                 MAE:          21.55
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    397.0871     10.1329       0.001    379.3721    418.5159
       opcount      0.0213      0.0001       0.001      0.0210      0.0216
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_EOA__geth__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_EOA__geth__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_EOA__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          28.76
Df Residuals:           75                                 MAE:          23.36
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     90.6789     11.6232       0.001     68.4999    112.5262
       opcount      0.0108      0.0002       0.001      0.0104      0.0112
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_EOA__nethermind__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_EOA__nethermind__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_EOA__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.984
Model:                  NNLS                    Adj. R-squared:          0.984
No. Observations:       110                               RMSE:          11.30
Df Residuals:           108                                MAE:           8.90
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     93.0026      3.1894       0.001     87.1639     99.7902
       opcount      0.0046      0.0000       0.001      0.0045      0.0047
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_EOA__reth__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_EOA__reth__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_EOA__reth__diagnostics.png)

</details>

### test_account_access — combo `EXTCODECOPY_AccountMode.NON_EXISTING_ACCOUNT` — `presets[cold_account_nocode_access]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.912 | 0.03191 | 1.00e-03 | [0.03027, 0.03356] |
| `erigon` | 55 | 0.9929 | 0.007788 | 1.00e-03 | [0.007721, 0.007845] |
| `ethrex` | 77 | 0.9562 | 0.00249 | 1.00e-03 | [0.002376, 0.002613] |
| `geth` | 99 | 0.9961 | 0.02061 | 1.00e-03 | [0.02031, 0.02088] |
| `nethermind` | 77 | 0.9779 | 0.01076 | 1.00e-03 | [0.01039, 0.01111] |
| `reth` | 110 | 0.9769 | 0.00449 | 1.00e-03 | [0.004363, 0.004624] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.912
Model:                  NNLS                    Adj. R-squared:          0.911
No. Observations:       132                               RMSE:         191.99
Df Residuals:           130                                MAE:         180.66
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    226.7828     51.1633       0.001    123.4383    325.3103
       opcount      0.0319      0.0008       0.001      0.0303      0.0336
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__besu__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__besu__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.993
Model:                  NNLS                    Adj. R-squared:          0.993
No. Observations:       55                                RMSE:          13.49
Df Residuals:           53                                 MAE:          11.74
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0078      0.0000       0.001      0.0077      0.0078
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__erigon__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__erigon__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.956
Model:                  NNLS                    Adj. R-squared:          0.956
No. Observations:       77                                RMSE:          10.32
Df Residuals:           75                                 MAE:           8.24
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    110.7922      3.4455       0.001    103.4905    117.0504
       opcount      0.0025      0.0001       0.001      0.0024      0.0026
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__ethrex__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__ethrex__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          24.95
Df Residuals:           97                                 MAE:          19.46
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    389.4173      8.8558       0.001    373.2052    407.9819
       opcount      0.0206      0.0001       0.001      0.0203      0.0209
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__geth__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__geth__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.978
Model:                  NNLS                    Adj. R-squared:          0.978
No. Observations:       77                                RMSE:          31.36
Df Residuals:           75                                 MAE:          25.13
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     85.5002     10.9818       0.001     64.4084    108.1859
       opcount      0.0108      0.0002       0.001      0.0104      0.0111
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__nethermind__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__nethermind__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.977
Model:                  NNLS                    Adj. R-squared:          0.977
No. Observations:       110                               RMSE:          13.37
Df Residuals:           108                                MAE:          10.13
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     98.5052      3.5223       0.001     91.8571    105.4322
       opcount      0.0045      0.0001       0.001      0.0044      0.0046
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__reth__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__reth__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__reth__diagnostics.png)

</details>

### test_account_access — combo `EXTCODECOPY_AccountMode.EXISTING_CONTRACT_DIFF_MAX`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8942 | 0.04533 | 1.00e-03 | [0.04272, 0.04798] |
| `erigon` | 55 | 0.902 | 0.1448 | 1.00e-03 | [0.1318, 0.1554] |
| `ethrex` | 77 | 0.9976 | 0.1013 | 1.00e-03 | [0.1001, 0.1026] |
| `geth` | 99 | 0.9348 | 0.04218 | 1.00e-03 | [0.03949, 0.04481] |
| `nethermind` | 77 | 0.9293 | 0.03711 | 1.00e-03 | [0.03482, 0.03954] |
| `reth` | 110 | 0.9956 | 0.02265 | 1.00e-03 | [0.02238, 0.02294] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.894
Model:                  NNLS                    Adj. R-squared:          0.893
No. Observations:       132                               RMSE:         297.57
Df Residuals:           130                                MAE:         248.50
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    745.7626     76.5604       0.001    586.4230    894.9525
       opcount      0.0453      0.0013       0.001      0.0427      0.0480
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_DIFF_MAX__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.902
Model:                  NNLS                    Adj. R-squared:          0.900
No. Observations:       55                                RMSE:         910.70
Df Residuals:           53                                 MAE:         783.84
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    838.1536    413.4274       0.012     67.4957   1742.3484
       opcount      0.1448      0.0059       0.001      0.1318      0.1554
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_DIFF_MAX__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.998
Model:                  NNLS                    Adj. R-squared:          0.998
No. Observations:       77                                RMSE:          94.48
Df Residuals:           75                                 MAE:          77.00
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    374.1865     37.9574       0.001    302.9746    452.1378
       opcount      0.1013      0.0006       0.001      0.1001      0.1026
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_DIFF_MAX__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.935
Model:                  NNLS                    Adj. R-squared:          0.934
No. Observations:       99                                RMSE:         212.57
Df Residuals:           97                                 MAE:         178.63
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const   1250.9809     90.2346       0.001   1079.5826   1421.4738
       opcount      0.0422      0.0014       0.001      0.0395      0.0448
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_DIFF_MAX__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.929
Model:                  NNLS                    Adj. R-squared:          0.928
No. Observations:       77                                RMSE:         195.31
Df Residuals:           75                                 MAE:         168.74
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    526.3623     82.4098       0.001    368.0539    688.4494
       opcount      0.0371      0.0012       0.001      0.0348      0.0395
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_DIFF_MAX__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       110                               RMSE:          28.57
Df Residuals:           108                                MAE:          20.97
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    136.4885      8.2746       0.001    121.3531    152.0236
       opcount      0.0226      0.0002       0.001      0.0224      0.0229
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_DIFF_MAX__reth__diagnostics.png)

</details>

### test_account_access — combo `EXTCODECOPY_AccountMode.EXISTING_CONTRACT_MINIMAL`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8377 | 0.02717 | 1.00e-03 | [0.02509, 0.02913] |
| `erigon` | 55 | 0.9384 | 0.02381 | 1.00e-03 | [0.02213, 0.0252] |
| `ethrex` | 77 | 0.9822 | 0.01865 | 1.00e-03 | [0.01798, 0.01929] |
| `geth` | 99 | 0.996 | 0.02046 | 1.00e-03 | [0.02021, 0.02071] |
| `nethermind` | 77 | 0.9706 | 0.01159 | 1.00e-03 | [0.01114, 0.01206] |
| `reth` | 110 | 0.9805 | 0.004916 | 1.00e-03 | [0.004775, 0.005062] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.838
Model:                  NNLS                    Adj. R-squared:          0.836
No. Observations:       132                               RMSE:         228.20
Df Residuals:           130                                MAE:         212.04
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    304.4162     57.1788       0.001    193.6807    421.9737
       opcount      0.0272      0.0010       0.001      0.0251      0.0291
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_MINIMAL__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.938
Model:                  NNLS                    Adj. R-squared:          0.937
No. Observations:       55                                RMSE:         116.36
Df Residuals:           53                                 MAE:         101.80
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    276.4000     54.0972       0.001    185.7621    395.1992
       opcount      0.0238      0.0008       0.001      0.0221      0.0252
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_MINIMAL__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.982
Model:                  NNLS                    Adj. R-squared:          0.982
No. Observations:       77                                RMSE:          47.97
Df Residuals:           75                                 MAE:          42.45
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    212.9121     22.0686       0.001    172.0326    257.9613
       opcount      0.0186      0.0003       0.001      0.0180      0.0193
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_MINIMAL__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          24.59
Df Residuals:           97                                 MAE:          19.34
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    385.2437      7.5925       0.001    369.7996    400.6700
       opcount      0.0205      0.0001       0.001      0.0202      0.0207
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_MINIMAL__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.971
Model:                  NNLS                    Adj. R-squared:          0.970
No. Observations:       77                                RMSE:          38.48
Df Residuals:           75                                 MAE:          28.93
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    126.6634     13.3533       0.001     99.9577    151.6178
       opcount      0.0116      0.0002       0.001      0.0111      0.0121
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_MINIMAL__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.980
No. Observations:       110                               RMSE:          13.23
Df Residuals:           108                                MAE:          10.19
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     86.0501      4.1330       0.001     78.1970     94.2636
       opcount      0.0049      0.0001       0.001      0.0048      0.0051
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_MINIMAL__reth__diagnostics.png)

</details>

### test_account_access — combo `EXTCODECOPY_AccountMode.EXISTING_CONTRACT_SAME_MAX`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.8298 | 0.02668 | 1.00e-03 | [0.02463, 0.0287] |
| `erigon` | 55 | 0.9388 | 0.02396 | 1.00e-03 | [0.02239, 0.02536] |
| `ethrex` | 77 | 0.9811 | 0.01858 | 1.00e-03 | [0.01792, 0.01925] |
| `geth` | 99 | 0.9952 | 0.02015 | 1.00e-03 | [0.01982, 0.02046] |
| `nethermind` | 77 | 0.9799 | 0.01199 | 1.00e-03 | [0.0116, 0.01236] |
| `reth` | 110 | 0.9829 | 0.004985 | 1.00e-03 | [0.004848, 0.005129] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.830
Model:                  NNLS                    Adj. R-squared:          0.828
No. Observations:       132                               RMSE:         230.64
Df Residuals:           130                                MAE:         215.55
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    333.2305     58.8670       0.001    224.7271    443.6926
       opcount      0.0267      0.0010       0.001      0.0246      0.0287
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_SAME_MAX__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.939
Model:                  NNLS                    Adj. R-squared:          0.938
No. Observations:       55                                RMSE:         116.76
Df Residuals:           53                                 MAE:         101.36
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    271.1421     52.9697       0.001    179.2219    376.2548
       opcount      0.0240      0.0008       0.001      0.0224      0.0254
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_SAME_MAX__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.981
Model:                  NNLS                    Adj. R-squared:          0.981
No. Observations:       77                                RMSE:          49.17
Df Residuals:           75                                 MAE:          43.78
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    217.2860     22.2783       0.001    173.1777    261.1074
       opcount      0.0186      0.0003       0.001      0.0179      0.0193
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_SAME_MAX__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.995
Model:                  NNLS                    Adj. R-squared:          0.995
No. Observations:       99                                RMSE:          26.76
Df Residuals:           97                                 MAE:          20.90
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    394.4144      9.6745       0.001    376.1417    413.2571
       opcount      0.0201      0.0002       0.001      0.0198      0.0205
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_SAME_MAX__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.980
Model:                  NNLS                    Adj. R-squared:          0.980
No. Observations:       77                                RMSE:          32.79
Df Residuals:           75                                 MAE:          25.40
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    114.0419     12.5700       0.001     90.2004    139.0477
       opcount      0.0120      0.0002       0.001      0.0116      0.0124
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_SAME_MAX__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.983
Model:                  NNLS                    Adj. R-squared:          0.983
No. Observations:       110                               RMSE:          12.53
Df Residuals:           108                                MAE:           9.77
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     79.4259      4.2573       0.001     71.1232     87.6516
       opcount      0.0050      0.0001       0.001      0.0048      0.0051
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_EXISTING_CONTRACT_SAME_MAX__reth__diagnostics.png)

</details>

### test_account_access — combo `EXTCODECOPY_AccountMode.NON_EXISTING_ACCOUNT` — `models.custom[0]`

| client | nobs | R² | target_coef (ms) | p-value | 95% CI |
| --- | --- | --- | --- | --- | --- |
| `besu` | 132 | 0.912 | 0.03191 | 1.00e-03 | [0.03027, 0.03356] |
| `erigon` | 55 | 0.9929 | 0.007788 | 1.00e-03 | [0.007721, 0.007845] |
| `ethrex` | 77 | 0.9562 | 0.00249 | 1.00e-03 | [0.002376, 0.002613] |
| `geth` | 99 | 0.9961 | 0.02061 | 1.00e-03 | [0.02031, 0.02088] |
| `nethermind` | 77 | 0.9779 | 0.01076 | 1.00e-03 | [0.01039, 0.01111] |
| `reth` | 110 | 0.9769 | 0.00449 | 1.00e-03 | [0.004363, 0.004624] |

<details><summary>besu — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.912
Model:                  NNLS                    Adj. R-squared:          0.911
No. Observations:       132                               RMSE:         191.99
Df Residuals:           130                                MAE:         180.66
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    226.7828     51.1633       0.001    123.4383    325.3103
       opcount      0.0319      0.0008       0.001      0.0303      0.0336
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__besu__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__besu__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__besu__diagnostics.png)

</details>

<details><summary>erigon — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.993
Model:                  NNLS                    Adj. R-squared:          0.993
No. Observations:       55                                RMSE:          13.49
Df Residuals:           53                                 MAE:          11.74
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const      0.0000      0.0000       1.000      0.0000      0.0000
       opcount      0.0078      0.0000       0.001      0.0077      0.0078
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__erigon__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__erigon__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__erigon__diagnostics.png)

</details>

<details><summary>ethrex — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.956
Model:                  NNLS                    Adj. R-squared:          0.956
No. Observations:       77                                RMSE:          10.32
Df Residuals:           75                                 MAE:           8.24
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    110.7922      3.4455       0.001    103.4905    117.0504
       opcount      0.0025      0.0001       0.001      0.0024      0.0026
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__ethrex__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__ethrex__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__ethrex__diagnostics.png)

</details>

<details><summary>geth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.996
Model:                  NNLS                    Adj. R-squared:          0.996
No. Observations:       99                                RMSE:          24.95
Df Residuals:           97                                 MAE:          19.46
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const    389.4173      8.8558       0.001    373.2052    407.9819
       opcount      0.0206      0.0001       0.001      0.0203      0.0209
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__geth__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__geth__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__geth__diagnostics.png)

</details>

<details><summary>nethermind — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.978
Model:                  NNLS                    Adj. R-squared:          0.978
No. Observations:       77                                RMSE:          31.36
Df Residuals:           75                                 MAE:          25.13
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     85.5002     10.9818       0.001     64.4084    108.1859
       opcount      0.0108      0.0002       0.001      0.0104      0.0111
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__nethermind__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__nethermind__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__nethermind__diagnostics.png)

</details>

<details><summary>reth — NNLS regression summary</summary>

```
==============================================================================
                           NNLS Regression Results                            
==============================================================================
Dep. Variable:          test_runtime_ms              R-squared:          0.977
Model:                  NNLS                    Adj. R-squared:          0.977
No. Observations:       110                               RMSE:          13.37
Df Residuals:           108                                MAE:          10.13
Df Model:               1      
==============================================================================
                      coef     std err     P-value      [0.025      0.975]
------------------------------------------------------------------------------
         const     98.5052      3.5223       0.001     91.8571    105.4322
       opcount      0.0045      0.0001       0.001      0.0044      0.0046
==============================================================================
Notes: Non-negative least squares with bootstrap inference (1000 iterations)
==============================================================================
```

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__reth__regression.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__reth__bootstrap.png)

![](figs/runtime/EXTCODECOPY__test_account_access__EXTCODECOPY_AccountMode_NON_EXISTING_ACCOUNT__reth__diagnostics.png)

</details>
