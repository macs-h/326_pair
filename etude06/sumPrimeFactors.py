#! /usr/bin/env python3

import sys
from itertools import chain, cycle, accumulate
from collections import defaultdict
import time

def sumPrimeFactors(primeFactorDict, initialVal):
    s_time = time.time()
    returnVal = 1
    # Sum up the prime factors - mimics result of sum of natural factors
    for key in primeFactorDict:
        val = primeFactorDict[key]

        tempVal = 0
        for power in range(val+1):
            tempVal += key**power

        returnVal *= tempVal

    returnVal -= initialVal

    return int(returnVal)



def sumFactorsOf(n):
    global seenPrimes
    s_time = time.time()

    initialVal = n
    pf = defaultdict(lambda: 0)

    while n % 2 == 0:
        pf[2] += 1
        n /= 2

    if n == 1:
        print(dict(pf))
        return sumPrimeFactors(dict(pf), initialVal)

    lastKey = 3
    limit = int(initialVal / 2) + 1
    st_time = time.time()

    for key in seenPrimes:

        while n % key == 0:
            pf[key] += 1
            n /= key

        #& If the key is larger than half initial n, then break
        if key > limit:
            break


    if n == 1:
        print(dict(pf))
        return sumPrimeFactors(dict(pf), initialVal)


    # print("lastKey: {}".format(lastKey))
    # for i in range(3,int(n**0.5)+1,2):
    for i in range (lastKey, int(initialVal**0.5)+1,2):
        # & Check dictionary of primes and if a prime, break out here.
        # print(n, i)
        # print(i)
        while n % i == 0:
            pf[i] += 1
            n /= i


    #& If n is still larger than 2, n is a prime.
    if n > 2:
        pf[n] += 1
        seenPrimes[n] = n  #& n is prime so add to list of seen primes.

    print(dict(pf))
    return sumPrimeFactors(dict(pf), initialVal)


if (__name__ == '__main__'):

    seenPrimes = {}

    num = sys.argv[1]
    num = int(num)
    print(sumFactorsOf(num))

