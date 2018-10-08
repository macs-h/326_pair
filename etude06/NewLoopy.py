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
        return 0,0

    while ( tortoise != hare ):
        tortoise = f ( tortoise )
        hare = f ( f ( hare ) )

        if noLoop or hare > upperLimit:
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

def getTime(time_elapsed):
    hours, rem = divmod(time_elapsed, 3600)
    minutes, seconds = divmod(rem, 60)
    return "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds)

#*****************************************************************************80

#!----------------------------------------------------------------------------80
def sumPrimeFactors(primeFactorDict, initialVal):
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

    return int(returnVal)



def sumFactorsOf(n):
    global seenPrimes

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

        fullArray[i] = sumFactorsOf(i)

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

    # print(seenPrimes)
    print("-----\nRange:\t{} to {}".format(startNum, endNum))
    print("Time:\t{}".format(getTime(time.time() - start_time)))
    print("Cycles:\t{}\nMax:\t{}\n-----".format(loopCount, longestCycle))

    #!--------------------------------------------------------------------------


