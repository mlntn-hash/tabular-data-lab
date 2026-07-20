import pandas as pd

data = {
    "datetime": [
        "2026-01-01 09:00",
        "2026-01-01 09:01",
        "2026-01-01 09:02",
        "2026-01-01 09:03",
        "2026-01-01 09:04",
        "2026-01-01 09:05",
        "2026-01-01 09:06",
        "2026-01-01 09:07",
        "2026-01-01 09:08",
        "2026-01-01 09:09",
    ],
    "price": [
        100,
        101,
        99,
        103,
        104,
        105,
        103,
        107,
        106,
        101
    ]
}
df = pd.DataFrame(data)

print(df)
print(df.dtypes)

df["datetime"] = pd.to_datetime(df["datetime"])

print(df.dtypes)

df = df.set_index("datetime")
print(df)
print(type(df.index))

ohlc = df.resample("5min").ohlc()

print(ohlc)