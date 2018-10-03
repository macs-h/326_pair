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

    # print("------------------")
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

    global fullArray, noLoop
    global seenValues

    value = fullArray[i]

    if value in seenValues or value <= 1:
        noLoop = True

    return value

#*****************************************************************************80

def factors(n):
    if n%2==0:
        setOfFactors = set(
        reduce(
            list.__add__,
            ([i, n//i] for i in range(2, int(n**0.5) + 1) if n % i == 0),
            []
        ))
    else:

        setOfFactors = set(
            reduce(
            list.__add__,
            ([i, n//i] for i in range(3, int(n**0.5) + 1, 2) if n % i == 0),
            []
        ))
    if len(setOfFactors) == 0:
        setOfFactors = set([0])
    return setOfFactors

#*****************************************************************************80

def getTime(time_elapsed):
    hours, rem = divmod(time_elapsed, 3600)
    minutes, seconds = divmod(rem, 60)
    return "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds)

#*****************************************************************************80

#!----------------------------------------------------------------------------80
# def trial_division(n):
#     a = [1]
#     while n%2 == 0:
#         a.append(2)
#         n/=2
#     f=3
#     while f * f <= n:
#         if (n % f == 0):
#             a.append(f)
#             n /= f
#         else:
#             f += 2
#     # if n != 1:
#     #     a.append(n)
#     #Only odd number is possible
#     return a


#!----------------------------------------------------------------------------80

if ( __name__ == '__main__' ):


    longestCycle = 0
    numCycles = 0

    start_time = time.time()

    startNum = 2
    endNum = 1000000


    #!---
    fullArray = [0] * 9000000 # endNum

    perfectNumberCount = 0
    loopCount = 0
    seenValues = {0:0, 1:1}

    #!---

    #!--------------------------------------------------------------------------
    # Set up the array containing the sums.
    for i in range(startNum, endNum+1):
        if i % 100000 == 0:
            print("--- {}\t calc: {} ---".format(getTime(time.time() - start_time), i))

        fullArray[i] = sum(factors(i))+1

        # print(factors(i))
        # print("fullArray[{}] = {}".format(i, fullArray[i]))


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

    print("-----\nRange:\t{} to {}".format(startNum, endNum))
    print("Time:\t{}".format(getTime(time.time() - start_time)))
    print("Cycles:\t{}\nMax:\t{}\n-----".format(loopCount, longestCycle))

    #!--------------------------------------------------------------------------


    # for i in range (startNum, endNum):
    #     if i % 10000 == 0:
    #         print("--- {}\t at: {} ---".format(getTime(time.time() - start_time), i))

    #     noLoop = False
    #     cycleLen, tmp = cycle_floyd(f1, i, endNum)

    #     # noLoopNums[i] = i
    #     # noLoopNums.update(currentLoopNums)
    #     # currentLoopNums = {}
    #     seenBefore.update(currentLoopNums)

    #     if cycleLen != 0:
    #         # previousLoops.update(currentLoopNums)
    #     # if cycleLen > 1:
    #         numCycles += 1

    #         if cycleLen > longestCycle:
    #             # print(cycleLen)
    #             longestCycle = cycleLen

    #     currentLoopNums = {}

    # print("-----\nRange:\t{} to {}".format(startNum, endNum))
    # print("Time:\t{}".format(getTime(time.time() - start_time)))
    # print("Cycles:\t{}\nMax:\t{}\n-----".format(numCycles, longestCycle))
