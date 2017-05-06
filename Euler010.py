
import math
from numba import jit
import timeit

start = timeit.default_timer()

@jit
def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

@jit
def run(num):
    sum_prime = 2 + 3 + 5+ 7 + 11 + 13+ 17+ 19 +23 + 29
    for i in range(29, num+1):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 11 != 0 and i % 13 != 0 and i % 17 != 0 and i % 19 != 0 and i % 23 != 0 and i % 29 != 0 :
            if is_prime(i):
                sum_prime += i
    num += 2
    return sum_prime


print(run(2000000))
stop = timeit.default_timer()
print("실행시간: " + str(stop - start))


