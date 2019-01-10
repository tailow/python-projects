# PRIME CHECKER

import math

primes = [2]

# pls don't go above 10 000 000
prime_count = 1000000


def check_primality(num):
    for divisor in range(2, int(math.sqrt(num))):
        if num % divisor == 0:
            return False
    return True


i = 3

while i < prime_count:
    if check_primality(i):
        primes.append(i)
    i += 2

for prime in primes:
    print(prime)
