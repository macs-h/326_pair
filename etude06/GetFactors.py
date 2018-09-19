#! /usr/bin/env python3.6
import sys

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

for line in sys.stdin:
    print(factors(int(line)))
    print()