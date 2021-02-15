# PRIME CHECKER

import time
import math

start_time = time.time()

# pls don't go above 10 000 000
prime_count = 1000000


def check_primality(num):
    for divisor in range(2, int(math.sqrt(num))):
        if num % divisor == 0:
            return False
    return True


i = 3

while i < prime_count:
    print(i)

    i += 2

print("%s seconds" % (time.time() - start_time))
