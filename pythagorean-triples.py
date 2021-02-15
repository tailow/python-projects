import math

max_b = 20


class Triple:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def print_triple(self):
        print("%s, %s, %s" % (self.a, self.b, self.c))


triples = []

for b in range(max_b + 1):
    for a in range(1, b):
        if math.sqrt(a ** 2 + b ** 2) == int(math.sqrt(a ** 2 + b ** 2)):
            triples.append(Triple(a, b, int(math.sqrt(a ** 2 + b ** 2))))

for triple in triples:
    triple.print_triple()
