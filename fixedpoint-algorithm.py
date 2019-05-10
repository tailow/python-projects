point = float(input("point: "))

iterations = int(input("iter: "))

x = point


def f(x):
    return -pow(abs(3 * x - 5), float(1)/3)


for i in range(iterations):
    x = f(x)

print(x)