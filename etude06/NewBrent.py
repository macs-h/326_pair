#!/usr/bin/env python3.6

# E6 - Loopy Numbers
#
# @author Max Huang
# @author Sam Paterson
# @since 10 September 2018
# @version 1

longestCycle = 0
numberOfCycles = 0
factor_table = []
values = []

def cycle_floyd(f, x0):
    tortoise = f(x0) # f(x0) is the element/node next to x0.
    hare = f(f(x0))
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))

    # Find the position μ of first repetition.
    mu = 0
    tortoise = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)   # Hare and tortoise move at same speed
        mu += 1

    lam = 1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        lam += 1

    return lam, mu


def cycle_floyd_test(startingVal):
    global longestCycle, factor_table, values


    currVal = 0
    prevVal = startingVal
    prev = []
    while starin not in prev:
        currVal = sum(factors(prevVal))
        prev.append(currVal)
        values.append(currVal)
        print("currentVal:",currVal)
        prevVal = currVal
    print(values)
    x0 = startingVal
    lam, mu = cycle_floyd(f1, x0)

    print("Cycle len:", lam)
        # # print("Cycle starts with: {} at index {}".format(factor_table[mu], mu))
        # print("Factor table:", factor_table)

        # if lam > longestCycle:
        #     longestCycle = lam
        #     print("Longest =", lam)

    return


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



def f1(i):
    global values
    print(values)
    return values

    # global factor_table

    # tmp = sum(factors(i))
    # print("sum result: {}".format(tmp))
    # factor_table.append(tmp)
    # return tmp


if ( __name__ == '__main__' ):
    import time
    start_time = time.time()

    # for i in range (2,10000):
    #     print(">", i)
    #     cycle_floyd_test(i)
    cycle_floyd_test(1264460)
    # print(factors(276))

    print("--- %.4f seconds ---" % (time.time() - start_time))