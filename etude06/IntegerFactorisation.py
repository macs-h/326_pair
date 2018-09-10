#!/usr/bin/env python3.6

import time

def trial_division(n):
    a = []
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

# print(trial_division(99999))

start_time = time.time()


for i in range(1,100000):
    # print("%s\t%s" % (i, trial_division(i)))
    trial_division(i)

print("--- %.3f seconds ---" % (time.time() - start_time))