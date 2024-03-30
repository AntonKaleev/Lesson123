import math

def f(x):
    return math.sin(x)
def trapez(a, b, N, func):
    N = (b - a) / n
    integral = 0.5 * (func(a) + func(b))

    for i in range(1, n):
        integral += func(a + i * N)

    integral *= N
    return integral


a = 5
b = 7
n = 100
integral = trapez(a, b, n, f)

print(f"Приближенное значение определенного интеграла: {integral}")