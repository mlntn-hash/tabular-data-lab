## L11 — numpy-basics

**What I built:** Implemented `mean`, `std`, `covariance`, and `pearson_correlation`
from scratch using plain Python loops (no `np.mean`/`np.std`/etc.), then verified
each against NumPy's reference implementation.

**What I learned:**
- mean = sum / n; std = sqrt(mean of squared deviations from mean)
- covariance measures how two variables move together: positive = same direction,
  negative = opposite direction
- pearson correlation = cov(X,Y) / (std(X) * std(Y)) — normalizes covariance to [-1, 1]
- np.cov() defaults to ddof=1 (sample, divides by n-1), not ddof=0 (population,
  divides by n) — need to pass ddof=0 explicitly to match a from-scratch
  implementation that divides by n
- np.cov() and np.corrcoef() return a 2x2 matrix, not a single number — need [0, 1]
  to get the actual covariance/correlation between the two variables

**Where I got stuck:** Forgot to index into the matrix result of np.cov/np.corrcoef
when formatting with f-strings — got a TypeError trying to format a whole array as
a float.

**Time spent:** ~1.5 hours

## L12 — broadcasting-drill

**What I built:** Normalized a 100x5 matrix both column-wise and row-wise
(subtract mean, divide by std) using pure NumPy broadcasting — no loops.

**What I learned:**
- Broadcasting compares shapes right-to-left; dimensions must either match
  or one of them must be 1
- Column-wise normalization "just works": (100,5) and (5,) broadcast fine,
  because the last dimension matches (5 == 5)
- Row-wise normalization fails by default: (100,5) and (100,) don't broadcast,
  because comparing right-to-left gives 5 vs 100 — no match
- Fix: use keepdims=True when computing mean/std along axis=1, turning shape
  (100,) into (100, 1) — now broadcasting works because 1 is a special
  "stretch to fit" value

**Where I got stuck:** Forgot keepdims when normalizing by rows, got
`ValueError: operands could not be broadcast together with shapes (100,5) (100,)`

**Time spent:** ~60 minutes

## L13 — image-as-array

**What I built:** Loaded an image via PIL, converted it to a NumPy array,
implemented greyscale conversion (luminance formula), 90° rotation, and a
manual 3x3 box-blur convolution — all without built-in PIL filters.

**What I learned:**
- An image is just a NumPy array: shape (height, width, 3) for RGB —
  PIL reports size as (width, height), NumPy reports shape as (height, width, channels)
  — opposite order, a common source of confusion
- Greyscale isn't a simple average of R,G,B — the standard luminance formula
  weights channels differently (0.299*R + 0.587*G + 0.114*B) because the eye
  perceives green as brighter than blue at the same intensity
- Convolution = sliding a small kernel (3x3) over the image, multiplying
  element-wise and summing, to compute each output pixel from its neighborhood
- Edge pixels need special handling (no full 3x3 neighborhood available) —
  here just skipped/left at 0 for simplicity; real libraries use padding

**Where I got stuck:** Renamed the loop variable from `i` to `y` in the outer
loop but forgot to update it inside the loop body — got `NameError: name 'i'
is not defined`. Reminder: loop variable name must match everywhere it's used.

**Time spent:** ~40 minutes

## L14 — pandas-warmup

**What I built:** Loaded Titanic dataset, explored structure with .info()
and .describe(), computed survival rates by sex, class, age group,
and sex+class combination using groupby + agg.

**What I learned:**
- groupby splits the dataframe into buckets by unique values,
  agg computes multiple aggregations at once (mean/count/sum)
- mean of a 0/1 column = survival rate directly
- pd.cut creates categorical bins from a numeric column
- groupby with a list of columns creates multi-level groups
- observed=True needed when grouping by pd.Categorical/pd.cut columns
- NaN values in Age (177 of 891) automatically drop from groupby —
  need to mention this in analysis conclusions

**Key findings:**
- Women survived at 74%, men at 19%
- 1st class: 63%, 2nd: 47%, 3rd: 24%
- Children (58%) survived more than seniors (23%)
- Women in 3rd class (50%) survived more than men in 1st class (37%)
  — gender mattered more than social class

**Where I got stuck:** Passed two separate string arguments to groupby
instead of a list — groupby(["A", "B"]), not groupby("A", "B")

**Time spent:** ~30 minutes

## L15 — pivot-melt

**What I built:** Created sample data in long format (user_id, date, metric, value),
converted to wide format via pivot_table, then back to long via melt.

**What I learned:**
- Long format: one row per observation — good for groupby, charts, databases
- Wide format: one row per entity, metrics as columns — good for ML, reports
- pivot_table: index = row keys, columns = what becomes new columns,
  values = what fills the cells, aggfunc = how to handle duplicates
- melt: reverse of pivot — id_vars stay, value_vars fold into rows
- NaN appears in wide format when a combination doesn't exist in the original data
- dropna needed after melt to remove those artificial NaN rows

**Where I got stuck:** —

**Time spent:** ~20 minutes

## Task 16 — Time Series Resample

- Converted a string datetime column to `datetime` using `pd.to_datetime()`.
- Set the datetime column as a `DatetimeIndex`.
- Used `resample("5min").ohlc()` to aggregate 1-minute tick data into 5-minute OHLC candles.
- Learned that `resample()` works only with a `DatetimeIndex`.
- Time spent: 20 min.