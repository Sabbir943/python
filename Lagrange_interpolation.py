
def lagrange_interpolation(x, y, x_new):
    n = len(x)
    result = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p *= (x_new - x[j]) / (x[i] - x[j])
        result += y[i] * p
    return result


x = [300, 304, 305, 307]
y = [2.4771, 2.4829, 2.4843, 2.4871]
x_new = 301
result = lagrange_interpolation(x, y, x_new)
print(result)