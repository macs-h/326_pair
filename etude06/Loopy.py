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
        return 0,0

    while ( tortoise != hare ):
        tortoise = f ( tortoise )
        hare = f ( f ( hare ) )

        # if noLoop or hare > 9000000:
        if noLoop or hare > upperLimit:
            return 0,0

    mu = 0
    # tortoise = x0

    # while ( tortoise != hare ):
    #     tortoise = f ( tortoise )
        # hare = f ( hare )
        # mu = mu + 1

    lam = 1
    hare = f ( tortoise )
    while ( tortoise != hare ):
        hare = f ( hare )
        lam += 1

    return lam, mu

#*****************************************************************************80

def f1 ( i ) :
    global currentLoopNums, noLoopNums, noLoop
    global factorisedBefore
    global previousLoops
    global seenBefore

    # value = sum(factors(i))+1

    if i in factorisedBefore:
        value = factorisedBefore[i]
    else:
        value = sum(factors(i))+1
        # print(value)
        factorisedBefore[i] = value
        # print("i: {}\nv: {}\n".format(i, value))
        # print(i)
    
    # print(value)

    # if i in previousLoops:
    #     noLoop = True
    #     return 0
    if i in seenBefore:
        noLoop = True
        return 0


    # if value in noLoopNums or value in previousLoopNums or value <= 1:
    # if i in noLoopNums:
    #     noLoop = True
    #     return 0

    currentLoopNums[i] = i

    return value

#*****************************************************************************80

# def factors(n):
#     setOfFactors = set(
#         reduce(
#             list.__add__,
#             ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0),
#             []
#         ))
#     if len(setOfFactors) > 0:
#         setOfFactors.remove(n)
#     else:
#         setOfFactors = set([1])
#     return setOfFactors

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
        setOfFactors = set([1])
    return setOfFactors

#*****************************************************************************80

def getTime(time_elapsed):
    hours, rem = divmod(time_elapsed, 3600)
    minutes, seconds = divmod(rem, 60)
    return "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds)

#*****************************************************************************80

if ( __name__ == '__main__' ):

    # noLoop = False

    #&--------------------------------------------------------------------------
    #& Things to memoise:
    #&
    #& If number already seen or part of previously seen loop, stop.
    #&--------------------------------------------------------------------------
    # previousLoopNums = {1}
    currentLoopNums = {}
    noLoopNums = {1:1}

    longestCycle = 0
    numCycles = 0
    cycleArray = []

    factorisedBefore = {}
    previousLoops = {}
    seenBefore = {}

    start_time = time.time()

    startNum = 2
    endNum = 30

    for i in range (startNum, endNum):
        if i % 10000 == 0:
            print("--- {}\t at: {} ---".format(getTime(time.time() - start_time), i))

        noLoop = False
        cycleLen, tmp = cycle_floyd(f1, i, endNum)

        # noLoopNums[i] = i
        # noLoopNums.update(currentLoopNums)
        # currentLoopNums = {}
        seenBefore.update(currentLoopNums)

        if cycleLen != 0:
            # previousLoops.update(currentLoopNums)
        # if cycleLen > 1:
            numCycles += 1

            if cycleLen > longestCycle:
                # print(cycleLen)
                longestCycle = cycleLen

        currentLoopNums = {}

    print("-----\nRange:\t{} to {}".format(startNum, endNum))
    print("Time:\t{}".format(getTime(time.time() - start_time)))
    print("Cycles:\t{}\nMax:\t{}\n-----".format(numCycles, longestCycle))
