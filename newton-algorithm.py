x = float(input("x: "))
iterations = int(input("iterations: "))


def f(x):
    return (4 * x - 1) / (x**2 + 1)


def derivative(x):
    return (-4*x**2+2*x+4) / (x**2+1)**2


def tangent(x):
    return x - f(x) / derivative(x)


for i in range(iterations):
    x = tangent(x)
    print(str(i + 1) + ": " + str(x))
