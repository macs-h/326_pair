# from proper_divisors import proper_divs
# from functools import lru_cache

from math import sqrt
from functools import lru_cache, reduce
from collections import Counter
from itertools import product
 
 
MUL = int.__mul__
 
 
def prime_factors(n):
    'Map prime factors to their multiplicity for n'
    d = _divs(n)
    d = [] if d == [n] else (d[:-1] if d[-1] == d else d)
    pf = Counter(d)
    return dict(pf)
 
@lru_cache(maxsize=None)
def _divs(n):
    'Memoized recursive function returning prime factors of n as a list'
    for i in range(2, int(sqrt(n)+1)):
        d, m  = divmod(n, i)
        if not m:
            return [i] + _divs(d)
    return [n]
 
 
def proper_divs(n):
    '''Return the set of proper divisors of n.'''
    pf = prime_factors(n)
    pfactors, occurrences = pf.keys(), pf.values()
    multiplicities = product(*(range(oc + 1) for oc in occurrences))
    divs = {reduce(MUL, (pf**m for pf, m in zip(pfactors, multis)), 1)
            for multis in multiplicities}
    try:
        divs.remove(n)
    except KeyError:
        pass
    return divs or ({1} if n != 1 else set())
 
 
@lru_cache()
def pdsum(n): 
    return sum(proper_divs(n))
 
 
def aliquot(n, maxlen=16, maxterm=2**47):
    if n == 0:
        return 'terminating', [0]
    s, slen, new = [n], 1, n
    while slen <= maxlen and new < maxterm:
        new = pdsum(s[-1])
        if new in s:
            if s[0] == new:
                if slen == 1:
                    # return 'perfect', s
                    return 1
                elif slen == 2:
                    # return 'amicable', s
                    return 1
                else:
                    return 'sociable of length %i' % slen, s
            elif s[-1] == new:
                # return 'aspiring', s
                return 1
            else:
                # return 'cyclic back to %i' % new, s
                return 1
        elif new == 0:
            # return 'terminating', s + [0]
            return 1
        else:
            s.append(new)
            slen += 1
    else:
        # return 'non-terminating', s
        return 1
 
if __name__ == '__main__':
    # for n in range(1, 11): 
    #     print('%s: %r' % aliquot(n))
    # print()
    # for n in [11, 12, 28, 496, 220, 1184,  12496, 1264460, 790, 909, 562, 1064, 1488, 15355717786080]: 
    for n in range(0, 9000000):
        if aliquot(n) == 1:
            continue
        else:
            print('%s: %r' % aliquot(n))