a = float(input("a: "))
b = float(input("b: "))

gap = float(input("minimum gap: "))

c = 0


def f(x):
    return x ** 2 - 5


while abs(b - a) > gap:
    c = 1 / 2 * (a + b)

    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

print(c)
