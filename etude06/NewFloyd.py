#! /usr/bin/env python3.6
#

import time
from functools import reduce

def cycle_floyd ( f, x0, upperLimit):
    global noLoop


    tortoise = f ( x0 )
    hare = f ( tortoise )

    if noLoop:
        return 0,0

    while ( tortoise != hare ):#and not valueLessThanOne:
        tortoise = f ( tortoise )
        hare = f ( f ( hare ) )

        if noLoop or hare > 9000000:
            return 0,0

    mu = 0
    tortoise = x0

    while ( tortoise != hare ):
        tortoise = f ( tortoise )
        hare = f ( hare )
        mu = mu + 1

    lam = 1
    hare = f ( tortoise )
    while ( tortoise != hare ):
        hare = f ( hare )
        lam = lam + 1

    return lam, mu

#*****************************************************************************80

def f1 ( i ) :
    global currentLoopNums, noLoopNums, noLoop

    value = sum(factors(i))

    # if value in noLoopNums or value in previousLoopNums or value <= 1:
    if value in noLoopNums:
        noLoop = True

    currentLoopNums[value] = value

    return value

#*****************************************************************************80

def factors(n):
    setOfFactors = set(
        reduce(
            list.__add__,
            ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0),
            []
        ))
    if len(setOfFactors) > 0:
        setOfFactors.remove(n)
    else:
        setOfFactors = set([1])
    return setOfFactors

#*****************************************************************************80

def resetBools ():
    global  noLoop
    noLoop = False

def getTime(time_elapsed):
    hours, rem = divmod(time_elapsed, 3600)
    minutes, seconds = divmod(rem, 60)
    return "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds)

#*****************************************************************************80

if ( __name__ == '__main__' ):

    # noLoop = False

    #&----------------------------------------------------------------------------80
    #& Things to memoise:
    #&
    #& If number already seen or part of previously seen loop, stop.
    #&----------------------------------------------------------------------------80
    # previousLoopNums = {1}
    currentLoopNums = {}
    noLoopNums = {}

    longestCycle = 0
    numCycles = 0
    cycleArray = []

    start_time = time.time()

    # startNum = 14310
    # endNum = 14320
    startNum = 2
    endNum = 9000000

    #? ----------------------------
    #? Stop checking at hard limit of iteration range.
    #? If loop hits '1', stop!
    #? A number can only be in a loop once! - check list of previous loopy numbers. If already in list, then counts at same loop. Same number cannot be in two different loops at the same time.
    #? ----------------------------

    for i in range (startNum, endNum):
        if i % 100000 == 0:
            print("--- {}\tat: {} ---".format(getTime(time.time() - start_time), i))

        # resetBools()
        noLoop = False
        cycleLen, tmp = cycle_floyd(f1, i, endNum)

        noLoopNums.update(currentLoopNums)
        currentLoopNums = {}

        if cycleLen != 0:
            numCycles += 1

            if cycleLen > longestCycle:
                longestCycle = cycleLen

    print("-----\nRange:\t{} to {}".format(startNum, endNum))
    print("Time:\t{}".format(getTime(time.time() - start_time)))
    print("Cycles:\t{}\nMax:\t{}\n-----".format(numCycles, longestCycle))
