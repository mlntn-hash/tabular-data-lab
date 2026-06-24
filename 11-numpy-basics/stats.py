import numpy as np

def my_mean(x):
    total = 0
    for num in x:
        total += num
    return total/len(x)

x = np.array([1,2,3,4,5,6,7,8,9])
print(f"my_mean:", my_mean(x))
print(f"np.mean:", np.mean(x))

def my_std(x):
    m = my_mean(x)

    total_square_diff = 0
    for value in x:
        total_square_diff += (value - m)**2

    variance = total_square_diff / len(x)
    return variance ** 0.5

print(f"my_std:, {my_std(x):.3f}")
print(f"np.std:", np.std(x))

def my_covariance(x, y):
    mx = my_mean(x)
    my_ = my_mean(y)

    total = 0
    for i in range(len(x)):
        total += (x[i] -mx) * (y[i] -my_)

    return total/len(x)

x2 = np.array([1,2,3,4])
y2 = np.array([9,8,7,6])

print(f"my_covariance:, {my_covariance(x2, y2):.4f}")
print(f"np_cov:, {np.cov(x2, y2, ddof=0)[0, 1]:.4f}")
print(np.cov(x2, y2))
print(np.cov(x2, y2, ddof=0))

def my_pearson_correlation(x, y):
    cov = my_covariance(x, y)
    sx = my_std(x)
    sy_ = my_std(y)
    return cov / (sx * sy_)

print(f"my_person: {my_pearson_correlation(x2, y2):.4f}")
print(f"np_person: {np.corrcoef(x2, y2)[0, 1]:.4f}")


