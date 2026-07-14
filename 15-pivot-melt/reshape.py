import pandas as pd
import numpy as np

np.random.seed(42)

df_long = pd.DataFrame({
    "user_id": [1,1,1,2,2,2,3,3,3],
    "date": ['2024-01-01', '2024-01-01', '2024-01-02',
                '2024-01-01', '2024-01-01', '2024-01-02',
                '2024-01-01', '2024-01-01', '2024-01-02'],
    "metric": ['sales', 'clicks', 'sales',
                'sales', 'clicks', 'clicks',
                'sales', 'clicks', 'sales'],
    "value": [100, 50, 120, 200, 80, 90, 150, 60, 170]
})
print("LONG_FORMAT")
print(df_long)
print(f"SHAPE: {df_long.shape}")

df_wide = df_long.pivot_table(
    index=["user_id", "date"],
    columns="metric",
    values="value",
    aggfunc="sum"
)

df_wide = df_wide.reset_index()
df_wide.columns.name = None

print("WIDE_FORMAT")
print(df_wide)
print(f"SHAPE: {df_wide.shape}")

df_long_again = df_wide.melt(
    id_vars=["user_id", "date"],
    value_vars=["sales", "clicks"],
    var_name="metric",
    value_name="value"
)

df_long_again = df_long_again.dropna(subset=["value"])

df_long_again = df_long_again.sort_values(['user_id', 'date']).reset_index(drop=True)

print("BACK TO LONG_FORMAT")
print(df_long_again)
print(f"SHAPE: {df_long_again.shape}")