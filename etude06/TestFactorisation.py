import time

def trial_division(n):
    a = []
    while n%2 == 0:
        a.append(2)
        n/=2
    f=3
    while f * f <= n:
        if (n % f == 0):
            a.append(f)
            n /= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    #Only odd number is possible
    return a


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


def printTime(time_elapsed):
    hours, rem = divmod(time_elapsed, 3600)
    minutes, seconds = divmod(rem, 60)

    print("--- Time:{:0>2}:{:0>2}:{:05.2f} ---".format(int(hours),int(minutes),seconds))


if ( __name__ == '__main__' ):
    
    print(sum(factors(50)))
    # checkStart = 2
    # checkEnd = 10000

    # start_time = time.time()
    # for i in range (checkStart, checkEnd):
    #     if i % (checkEnd//10) == 0:
    #         print(">", i)
    #         print(">>", sum(trial_division(i)))
    #     trial_division(i)

    # printTime(time.time() - start_time)

    # print("\n")

    # start_time = time.time()
    # for i in range (checkStart, checkEnd):
    #     if i % (checkEnd//10) == 0:
    #         print(">", i)
    #         print(">>", sum(factors(i)))
    #     factors(i)

    # printTime(time.time() - start_time)