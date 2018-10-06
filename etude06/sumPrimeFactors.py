#! /usr/bin/env python3

from itertools import chain, cycle, accumulate
from collections import defaultdict

def factors_new(n):
    #   factors = set()
    #   for x in range(1, int(n**0.5) + 1):
    #     if n % x == 0:
    #       factors.add(x)
    #       factors.add(n//x)
    #   return (factors)
    def prime_powers(n):
        # c goes through 2, 3, 5, then the infinite (6n+1, 6n+5) series
        for c in accumulate(chain([2, 1, 2], cycle([2,4]))):
            if c*c > n: break
            if n%c: continue
            d,p = (), c
            while not n%c:
                n,p,d = n//c, p*c, d + (p,)
            yield(d)
        if n > 1: yield((n,))

    r = [1]
    for e in prime_powers(n):
        r += [a*b for a in r for b in e]
    return r

# def primeFactors(n):
#     from collections import defaultdict
#     pf = defaultdict(lambda: 0)
#     # pf = {}
#     # Print the number of two's that divide n
#     while n % 2 == 0:
#         # print (2)
#         pf[2]+=1
#         n = n / 2

#     # n must be odd at this point
#     # so a skip of 2 ( i = i + 2) can be used
#     for i in range(3,int(n**0.5)+1,2):

#         # while i divides n , print i ad divide n
#         while n % i== 0:
#             # print (i)
#             # print(i)
#             pf[i] += 1
#             # pf.append(i)
#             n = n / i

#     # Condition if n is a prime
#     # number greater than 2
#     if n > 2:
#         # print (n)
#         print(n)
#         pf[n] += 1
#         # pf.append(n)

#     return dict(pf)
#     # return pf

# def ffs(num):
#     from collections import defaultdict
#     factors = defaultdict(lambda: 0)
#     n = 2

#     while num != 1:
#         while num % n == 0:
#             factors[n] += 1
#             num /= n
#         n += 1

#     return dict(factors)


def sumFactorsOf(n):
    initialVal = n
    returnVal = 1
    pf = defaultdict(lambda: 0)

    while n % 2 == 0:
        pf[2]+=1
        n = n / 2

    for i in range(3,int(n**0.5)+1,2):
        # while i divides n , print i ad divide n
        while n % i== 0:
            pf[i] += 1
            n = n / i

    if n > 2:
        # print(n)
        pf[n] += 1

    primeFactorDict = dict(pf)


    for key in primeFactorDict:
        print("key: {}  val:{}".format(key, primeFactorDict[key]))
        val = primeFactorDict[key]

        tempVal = 0
        for power in range(val+1):
            tempVal += key**power

        returnVal *= tempVal

    returnVal -= initialVal
    if returnVal == 1:
        print("PRIME")
    return returnVal


if (__name__ == '__main__'):
    # factors of 12: [1, 2, 3, 4, 6]  = 16
    # primeFactors = [2, 2, 3] # prime factors of 12


    # print(sumPrimeFactors(primeFactors) == 16)

    print("----")
    # factors = factors_new(108)
    # print(factors)
    # print(primeFactors(108))
    # print( sum(factors_new(108)) -108)

    for i in range(1, 12):
        print("Num: {}".format(i))
        print("Result: {}".format(sumFactorsOf(i)))
        print("---")
    # print(ffs(108))