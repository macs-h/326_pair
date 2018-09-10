def cycle_brent ( f, x0 ):
     # Main phase of algorithm: finding a repetition x_i = x_2i.
    # The hare moves twice as quickly as the tortoise and
    # the distance between them increases by 1 at each step.
    # Eventually they will both be inside the cycle and then,
    # at some point, the distance between them will be
    # divisible by the period λ.
    tortoise = f(x0) # f(x0) is the element/node next to x0.
    hare = f(f(x0))
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))

    # At this point the tortoise position, ν, which is also equal
    # to the distance between hare and tortoise, is divisible by
    # the period λ. So hare moving in circle one step at a time,
    # and tortoise (reset to x0) moving towards the circle, will
    # intersect at the beginning of the circle. Because the
    # distance between them is constant at 2ν, a multiple of λ,
    # they will agree as soon as the tortoise reaches index μ.

    # Find the position μ of first repetition.
    mu = 0
    tortoise = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)   # Hare and tortoise move at same speed
        mu += 1

    # Find the length of the shortest cycle starting from x_μ
    # The hare moves one step at a time while tortoise is still.
    # lam is incremented until λ is found.
    lam = 1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        lam += 1

    return lam, mu
#   power = 1
#   lam = 1
#   tortoise = x0
#   hare = f ( x0 )

#   while ( tortoise != hare ):
#     if ( power == lam ):
#       tortoise = hare
#       power = power * 2
#       lam = 0
#     hare = f ( hare )
#     lam = lam + 1

#   mu = 0
#   tortoise = x0
#   hare = x0

#   for i in range ( 0, lam ):
#     hare = f ( hare )

#   while ( tortoise != hare ):
#     tortoise = f ( tortoise )
#     hare = f ( hare )
#     mu = mu + 1

#   return lam, mu


factor_table = []

def cycle_brent_test01 ( starting_val ):
  import platform

  print()

  # Starting value
#   x0 = 1264460
  x0 = starting_val
  factor_table.append(x0)
  print ( 'Starting argument X0 = %d' % ( x0 ) )

  lam, mu = cycle_brent ( f1, x0 )

  print("Cycle len:", lam)
  print("Cycle starts with:", factor_table[mu])
  print("Factor table:", factor_table)

  return


def factors(n):
    from functools import reduce

    setOfFactors = set(
        reduce(
            list.__add__,
            ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0),
            []
        ))
    print("removing {} from {}".format(n, setOfFactors))
    if len(setOfFactors) > 0:
        setOfFactors.remove(n)
    else:
        setOfFactors = set([1])
    return setOfFactors


def f1 ( i ) :
    global factor_table

    tmp = sum(factors(i))
    print("sum result: {}".format(tmp))
    factor_table.append(tmp)
    return tmp
    # return value


if ( __name__ == '__main__' ):
    # for i in range (6,10):
        # cycle_brent_test01 (i)
    # cycle_brent_test01(6)

    # num = 1264460
    num = 7
    print(factors(num))
    print(f1(num))
    print(cycle_brent(f1, num))
