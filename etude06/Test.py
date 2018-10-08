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
    global loopStart

    tortoise = f ( x0 )
    hare = f ( tortoise )

    if noLoop:
        return 0,0

    while ( tortoise != hare ):
        tortoise = f ( tortoise )
        hare = f ( f ( hare ) )

        if noLoop or tortoise > upperLimit:
            return 0,0
        if tortoise < x0:
            return 0,0

    mu = 0
    # tortoise = x0
    # while tortoise != hare:
    #     tortoise = f(tortoise)
    #     hare = f(hare)
    #     mu += 1


    # if tortoise == 0 or hare == 0:
    #     return 0,0

    lam = 1
    hare = f ( tortoise )
    while ( tortoise != hare ):
        hare = f ( hare )
        lam += 1
    # print("\n\tTOR: {}  HAR: {}".format(tortoise, hare))
    # print("\tfound loop of size {}\n".format(lam))

    loopStart[x0] = lam
    return lam, mu

#*****************************************************************************80

def f1 ( i ) :
    global fullArray, noLoop, endNum, currentNumber
    global seenValues
    global currentValues

    if i > endNum:
        noLoop = True
        value = 0
    else:
        value = fullArray[i]

    # if value in seenValues or value <= 1:
    #     noLoop = True

    if value in seenValues:# or value < i:
        noLoop = True
        value = 0


    return value

#*****************************************************************************80

def getTime(time_elapsed):
    hours, rem = divmod(time_elapsed, 3600)
    minutes, seconds = divmod(rem, 60)
    return "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds)

#*****************************************************************************80

#!----------------------------------------------------------------------------80
def sumPrimeFactors(primeFactorDict, initialVal):
    global seenFactors

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

#*****************************************************************************80

def sumFactorsOf(n):
    global primes
    global seenFactors


    initialVal = n
    pf = defaultdict(lambda: 0)

    # print("\n\n--- init val: {} ---".format(initialVal))

    while n % 2 == 0:
        pf[2] += 1
        n /= 2
        # if n in seenFactors and 2 in seenFactors[n]:
        #     pf[2] += seenFactors[n][2]
        #     break

    if n == 1:
        # seenFactors[initialVal].update(dict(pf))
        return sumPrimeFactors(dict(pf), initialVal)

    # limit = int(initialVal / 2) + 1
    limit = int(initialVal ** 0.5)

    for key in primes:
        while n % key == 0:
            pf[key] += 1
            n /= key
            # if n in seenFactors and key in seenFactors[n]:
            #     pf[key] += seenFactors[n][key]
            #     break

        #& If the key is larger than half initial n, then break
        if key > limit:
            # print("-- break key:", key)
            break

    if n == 1:
        # seenFactors[initialVal].update(dict(pf))
        return sumPrimeFactors(dict(pf), initialVal)

    #& If n is still larger than 2, n is a prime.
    if n > 2:
        pf[n] += 1


    # primeFactorDict = dict(pf)
    # print("---- end ----")
    # print("fullArray[{}] = {}\n".format(initialVal, dict(pf)))
    
    # seenFactors[initialVal].update(dict(pf))
    return sumPrimeFactors(dict(pf), initialVal)



def sieve_of_eratosthenes(max_integer):
    sieve = [True for _ in range(max_integer + 1)]
    sieve[0:1] = [False, False]
    for start in range(2, max_integer + 1):
        if sieve[start]:
            for i in range(2 * start, max_integer + 1, start):
                sieve[i] = False
    primes = []
    for i in range(2, max_integer + 1):
        if sieve[i]:
            primes.append(i)
    return primes


#!----------------------------------------------------------------------------80

if ( __name__ == '__main__' ):


    longestCycle = 0
    numCycles = 0

    start_time = time.time()

    startNum = 2
    endNum = 1000000
    currentNumber = 0

    #!---
    fullArray = [0] * (endNum+1) # endNum

    seenPrimes = {}
    perfectNumberCount = 0
    loopCount = 0
    seenValues = {0:0, 1:1}
    seenFactors = defaultdict(lambda: {})

    # loops = []
    loops = {}
    currentValues = {}
    # cLens = []
    loopStart = {}
    #!---

    #!--------------------------------------------------------------------------
    primes = sieve_of_eratosthenes(endNum)

    # Set up the array containing the sums.
    for i in range(startNum, endNum+1):
        if i % 100000 == 0:
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

        currentNumber = i
        cycleLen, tmp = cycle_floyd(f1, i, endNum)
        seenValues[i] = i

        if cycleLen > 1:
            loopCount += 1
            # cLens.append(cycleLen)
            # loops.append(i)
            loops[i] = cycleLen

            if cycleLen > longestCycle:
                longestCycle = cycleLen

    # print(primes)
    print("-----\nRange:\t{} to {}".format(startNum, endNum))
    print("Time:\t{}".format(getTime(time.time() - start_time)))
    print("Cycles:\t{}\nMax:\t{}\n-----".format(loopCount, longestCycle))
    print()
    print(loops)
    print()
    print(loopStart)
    print()
    print(len(loopStart))
    # print(cLens)
    #!--------------------------------------------------------------------------


