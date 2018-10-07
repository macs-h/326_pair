#!/usr/bin/env python3

from functools import reduce
import sys

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


if (__name__ == '__main__'):
    num = sys.argv[1]
    num = int(num)
    print(factors(num))

