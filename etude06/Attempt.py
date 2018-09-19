#!/usr/bin/env python3.6

# E6 - Loopy Numbers
#
# @author Max Huang
# @author Sam Paterson
# @since 06 September 2018
# @version 1

import time
from functools import reduce

def is_happy(n, factors):
    return n == sum(factors)

def trial_division(n):
    originalNumber = n
    factors = []

    while n%2 == 0:
        # if number is divisible by 2, add `2` to array
        factors.append(2)
        # Divide number by 2
        n/=2

    # The number is not divisble by 2. Any further factors must be odd so
    # start at 3 and then add 2 each time.
    f=3

    # while factor is less than sqrt(n), do:
    while (f * f <= n):
        if (n % f == 0):
            # If number is divisible by factor, add factor to array
            factors.append(f)
            # Divide number by factor
            n /= f
        else:
            # Number is NOT divisible by factor
            f += 2
    if n != 1:
        factors.append(n)

    if originalNumber in factors:
        factors.remove(originalNumber)
    return factors
# print(trial_division(396))
# print(is_happy(6, trial_division(6)))

values = []

start_time = time.time()

for i in range(1, 10):
    p_factors = trial_division(i)
    sum_factors = sum(p_factors)
    print("%s  --> %s\t%s" % (i, sum_factors, p_factors))

    # values.append([i, sum(tmp)])

#! -----------------------------------------------------------------------------
def factors(n):
    setOfFactors = set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    setOfFactors.remove(n)
    return setOfFactors


#TODO: For each number from 1 -> 9,000,000, find any loops

loop_nums = []
next_num = 0
original = 1264460
count = 0
# while count < 28:
while count < 10:
    if count == 0:
        next_num = original
        loop_nums.append(next_num)
        print("Starting:", next_num)
    count+= 1

    t = factors(next_num)
    print(t)
    next_num = sum(t)
    loop_nums.append(next_num)
    print("Next:", next_num)


#! -----------------------------------------------------------------------------

print("--- %.4f seconds ---" % (time.time() - start_time))
print(loop_nums)

# print()
# print(values)
def is_loopy(path):
    tortoise = path[0] # slow pointer, starts at the beginning of the list
    hare = path[0] # fast pointer, also starts at the beginning of the list
    end = path[-1] # point to the last node
    while True:
        print(hare)
        if hare == end:
            return False
        hare = path[hare[1]]    # move the fast pointer to the next node
        print(hare)
        if hare == end:
            return False
        hare = path[hare[1]] # move the fast pointer to gain twice the speed
        print(hare)
        tortoise = path[tortoise[1]]    # move the slow pointer to the next node
        print(tortoise)
        if hare == tortoise:
            return True

# print(is_loopy(values))

# print(is_loopy(loop_nums))