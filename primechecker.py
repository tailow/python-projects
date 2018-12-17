import time
import math
from matplotlib import pyplot as plt

primes = [2]
times = []

test_file = open("C:\\Users\\revit\\Desktop\\Projektit\\Python\\testproject\\testfile.txt", "w")

def check_primality(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
    return True


i = 3

while i < 1000000:
    if check_primality(i):
        primes.append(i)
    i += 2
    times.append(time.time())

    test_file.write("%s\n" % time.time())


plt.plot(times)
plt.show()