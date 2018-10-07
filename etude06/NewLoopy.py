#! /usr/bin/env python3.6
#
# E6 - Loopy Numbers
#
# @author Max Huang
# @author Sam Paterson
# @since 06 September 2018
# @version 1

import time
from functools import reduce
from itertools import chain, cycle, accumulate
from collections import defaultdict

def cycle_floyd ( f, x0, upperLimit):
    global noLoop

    tortoise = f ( x0 )
    hare = f ( tortoise )

    if noLoop:
        # print("noloop returns")
        # print("\n---\nNOLOOP\n---\n")
        return 0,0

    while ( tortoise != hare ):
        tortoise = f ( tortoise )
        hare = f ( f ( hare ) )

        if noLoop or hare > upperLimit:
            # print(hare)
            # print("noloop returns in while")
            return 0,0

    mu = 0

    lam = 1
    hare = f ( tortoise )

    if tortoise == 0 or hare == 0:
        return 0,0
    while ( tortoise != hare ):
        hare = f ( hare )
        lam += 1
    # print("\n\tTOR: {}  HAR: {}".format(tortoise, hare))
    # print("\tfound loop of size {}\n".format(lam))
    return lam, mu

#*****************************************************************************80

def f1 ( i ) :

    global fullArray, noLoop, endNum
    global seenValues

    if i > endNum:
        noLoop = True
        value = 0
    else:
        value = fullArray[i]

    if value in seenValues or value <= 1:
        noLoop = True

    return value

#*****************************************************************************80

# def factors(n):
#     if n%2==0:
#         setOfFactors = set(
#         reduce(
#             list.__add__,
#             ([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0),
#             []
#         ))
#     else:

#         setOfFactors = set(
#             reduce(
#             list.__add__,
#             ([i, n//i] for i in range(3, int(n**0.5) + 1, 2) if n % i == 0),
#             []
#         ))
#     if len(setOfFactors) == 0:
#         setOfFactors = set([0])
#     return setOfFactors


# def factors_new(n):
#     #   factors = set()
#     #   for x in range(1, int(n**0.5) + 1):
#     #     if n % x == 0:
#     #       factors.add(x)
#     #       factors.add(n//x)
#     #   return (factors)
#     def prime_powers(n):
#         # c goes through 2, 3, 5, then the infinite (6n+1, 6n+5) series
#         for c in accumulate(chain([2, 1, 2], cycle([2,4]))):
#             if c*c > n: break
#             if n%c: continue
#             d,p = (), c
#             while not n%c:
#                 n,p,d = n//c, p*c, d + (p,)
#             yield(d)
#         if n > 1: yield((n,))

#     r = [1]
#     for e in prime_powers(n):
#         r += [a*b for a in r for b in e]
#     return r

#*****************************************************************************80

def getTime(time_elapsed):
    hours, rem = divmod(time_elapsed, 3600)
    minutes, seconds = divmod(rem, 60)
    return "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds)

#*****************************************************************************80

#!----------------------------------------------------------------------------80
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
    # print("{}  {}".format(initialVal, returnVal))

    #& Memoise any prime numbers that we come across
    # if returnVal == 1:
    #     seenPrimes[initialVal] = returnVal

    print("sumPrimeFactors:\t{}".format(time.time() - s_time))

    return int(returnVal)



def sumFactorsOf(n):
    global seenPrimes
    s_time = time.time()

    #?-----------------------
    #? If ever n == 1, factorisation is finished.
    #? If returnVal == initialVal, the number is a prime so memoise it
    #?-----------------------

    initialVal = n
    pf = defaultdict(lambda: 0)

    while n % 2 == 0:
        pf[2] += 1
        n /= 2

    if n == 1:
        # print("- 1 -")
        # print("fullArray[{}] = {}\n".format(initialVal, dict(pf)))
        return sumPrimeFactors(dict(pf), initialVal)


    #& Go through list of primes trying to factorise `n`.
    #& If can't factorise by the time the prime reaches sqrt(n), then n
    #& is a prime.
    lastKey = 3
    limit = int(initialVal / 2) + 1
    # print("-- limit for {} is {}".format(initialVal, limit))
    # print("n:",n)
    st_time = time.time()
    for key in seenPrimes:
        # print("--> seenPrimes:", key)

        while n % key == 0:
            pf[key] += 1
            n /= key
        # print("key:",key)
        # lastKey = key

        #& If the key is larger than half initial n, then break
        if key > limit:
            break

    print("for loop:\t\t{}".format(time.time() - st_time))

    if n == 1:
        # print("\t- 2 -")
        # print("fullArray[{}] = {}\n".format(initialVal, dict(pf)))
        return sumPrimeFactors(dict(pf), initialVal)


    # print("lastKey: {}".format(lastKey))
    # for i in range(3,int(n**0.5)+1,2):
    # for i in range (lastKey, int(initialVal**0.5)+1,2):
    #     # & Check dictionary of primes and if a prime, break out here.
    #     # print(n, i)
    #     print(i)
    #     while n % i == 0:
    #         pf[i] += 1
    #         n /= i

    #& If n is still larger than 2, n is a prime.
    if n > 2:
        pf[n] += 1
        seenPrimes[n] = n  #& n is prime so add to list of seen primes.

    # primeFactorDict = dict(pf)
    # print("---- end ----")
    # print("fullArray[{}] = {}\n".format(initialVal, dict(pf)))
    print("sumFactorsOf:\t{}".format(time.time() - s_time))
    return sumPrimeFactors(dict(pf), initialVal)




#!----------------------------------------------------------------------------80

if ( __name__ == '__main__' ):


    longestCycle = 0
    numCycles = 0

    start_time = time.time()

    startNum = 2
    endNum = 100000


    #!---
    fullArray = [0] * (endNum+1) # endNum

    seenPrimes = {}
    perfectNumberCount = 0
    loopCount = 0
    seenValues = {0:0, 1:1}

    #!---

    #!--------------------------------------------------------------------------
    # Set up the array containing the sums.
    for i in range(startNum, endNum+1):
        if i % 10000 == 0:
            print("--- {}\t calc: {} ---".format(getTime(time.time() - start_time), i))

        # fullArray[i] = sum(factors(i))+1
        # fullArray[i] = sum(factors_new(i)) - i
        print("Val:", i)
        fullArray[i] = sumFactorsOf(i)
        print("------------------------------")

        # print(factors_new(i))
        # print("fullArray[{}] = {}".format(i, fullArray[i]))

    print()

    # MAIN PROGRAM
    for i in range (startNum, endNum):
        if i % 100000 == 0:
            print("--- {}\t at: {} ---".format(getTime(time.time() - start_time), i))

        noLoop = False
        current = {}


        cycleLen, tmp = cycle_floyd(f1, i, endNum)
        seenValues[i] = i

        if cycleLen != 0:
            loopCount += 1

            if cycleLen > longestCycle:
                longestCycle = cycleLen

    print(seenPrimes)
    print("-----\nRange:\t{} to {}".format(startNum, endNum))
    print("Time:\t{}".format(getTime(time.time() - start_time)))
    print("Cycles:\t{}\nMax:\t{}\n-----".format(loopCount, longestCycle))

    #!--------------------------------------------------------------------------


