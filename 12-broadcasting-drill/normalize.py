import numpy as np

np.random.seed(42)
A = np.random.randn(100,5)

col_mean = A.mean(axis=0)
col_std = A.std(axis=0)

print("col_mean:", col_mean)
print("col_std:", col_std)

rows_mean = A.mean(axis=1, keepdims=True)
rows_std = A.std(axis=1, keepdims=True)

print("row_mean:", rows_mean)
print("row_std:", rows_std)

A_norm_cols = (A - col_mean)/col_std

print("A_norm_cols shape:", A_norm_cols.shape)
print("new col mean:", A_norm_cols.mean(axis=0))
print("new col stds:", A_norm_cols.std(axis=0))

A_norm_rows = (A - rows_mean)/rows_std

print("A_norm_rows shape:", A_norm_rows.shape)
print("new row mean:", A_norm_rows.mean(axis=1)[:5])
print("new row stds:", A_norm_rows.std(axis=1)[:5])