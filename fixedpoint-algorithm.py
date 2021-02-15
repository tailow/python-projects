import math

point = float(input("point: "))

iterations = int(input("iter: "))

x = point


def f(x):
    return x + math.e ** -x - 0.7 * math.log(x)


for i in range(iterations):
    x = f(x)
    print(x)

print(x)
