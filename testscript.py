import math

def sano(nimi, lause):
    print("%s sanoo: '%s'" % (nimi, lause))


sano("Pietari", "osaan käyttää funktioita")

sano("Tomi", "Pietari osaa käyttää funktioita")

sano("Kauko", "Kahden jännitelähteen potentiaalin summa on johtimen resistanssi")


def diameter(r):
    print(2*r)


def circ(r):
    print(2 * math.pi * r)


def f(x):
    return math.sin(x)


print(f(1))
print(f(4))