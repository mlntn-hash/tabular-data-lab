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