#!/usr/bin/env python3.6

import time
from functools import reduce
def trial_division(n):
    a = [1]
    while n%2 == 0:
        a.append(2)
        n/=2
    f=3
    while f * f <= n:
        if (n % f == 0):
            a.append(f)
            n /= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    #Only odd number is possible
    return a


tmpList = trial_division(50)
print(tmpList)
print(reduce(lambda x, y: x*y, tmpList))

start_time = time.time()


# for i in range(1,100000):
#     # print("%s\t%s" % (i, trial_division(i)))
#     trial_division(i)

print("--- %.3f seconds ---" % (time.time() - start_time))