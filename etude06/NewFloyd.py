#! /usr/bin/env python3.6
#

import time

valueLessThanOne = False
valueAlreadyExists = False
noLoop = False
previousLoopNums = {}

def cycle_floyd ( f, x0, upperLimit):
    global valueLessThanOne, noLoop, valueAlreadyExists

    tortoise = f ( x0 )
    hare = f ( tortoise )

    while ( tortoise != hare ):#and not valueLessThanOne:
        tortoise = f ( tortoise )
        hare = f ( f ( hare ) )

        if hare > upperLimit:
        # if hare > 9000000:
            noLoop = True
            break
        if valueAlreadyExists or valueLessThanOne:
            noLoop = True
            break

    mu = 0
    tortoise = x0

    if noLoop or valueLessThanOne or valueAlreadyExists:
        return 0,0
    else:
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

def cycle_floyd_test02 (x0 , upperLimit) :
    # global valueLessThanOne, valueAlreadyExists

    lam, mu = cycle_floyd ( f2, x0, upperLimit )

    # if valueLessThanOne:
    #     lam = 0

    return lam

#*****************************************************************************80

def resetBools ():
    global valueAlreadyExists, valueLessThanOne, noLoop
    valueAlreadyExists = False
    valueLessThanOne = False
    noLoop = False

def getTime(time_elapsed):
    hours, rem = divmod(time_elapsed, 3600)
    minutes, seconds = divmod(rem, 60)
    return "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds)

def cycle_floyd_test ( ):
    global previousLoopNums
    longestCycle = 0
    numCycles = 0

    start_time = time.time()

    # startNum = 14310
    # endNum = 14320
    startNum = 2
    endNum = 1000000

    #? ----------------------------
    #? Stop checking at hard limit of iteration range.
    #? If loop hits '1', stop!
    #? A number can only be in a loop once! - check list of previous loopy numbers. If already in list, then counts at same loop. Same number cannot be in two different loops at the same time.
    #? ----------------------------

    for i in range (startNum, endNum):
        if i % 10000 == 0:
            print("--- {}\tat: {} ---".format(getTime(time.time() - start_time), i))

        # valueLessThanOne = False
        # noLoop = False
        resetBools()

        cycleLen = cycle_floyd_test02(i, endNum)
        if cycleLen != 0:
            previousLoopNums[i] = i
            numCycles += 1
            # print("> i: {}  \t\b\blen: {}".format(i, cycleLen), end="")
            # print("\tFactors: {}".format(factors(i)))
            if cycleLen > longestCycle:
                longestCycle = cycleLen


    print("-----\nRange:\t{} to {}".format(startNum, endNum))
    print("Time:\t{}".format(getTime(time.time() - start_time)))
    print("Cycles:\t{}\nMax:\t{}\n-----".format(numCycles, longestCycle))


    return


#*****************************************************************************80

def factors(n):
    from functools import reduce

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
array = []
def f2 ( i ) :
    global valueLessThanOne, valueAlreadyExists, previousLoopNums

    value = sum(factors(i))
    # print(value)
    # array.append(value)

    if value <= 1:
        valueLessThanOne = True
    if value in previousLoopNums:
        valueAlreadyExists = True

    return value


#*****************************************************************************80

if ( __name__ == '__main__' ):

    cycle_floyd_test ( )
