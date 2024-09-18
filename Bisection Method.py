def bisection_method(func, a, b, tol):
    if func(a) * func(b) >= 0:
        print("Bisection method fails.")
        return None
    c = a
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if func(c) == 0.0:
            break
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    return c
def func(x):
    return x**3 - x - 2
a = 1
b = 2
tol = 1e-5
root = bisection_method(func, a, b, tol)
print(f"The root is: {root}")
