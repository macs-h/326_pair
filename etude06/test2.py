''' Mersenne primes and perfect numbers '''

def primes(n):
    """ Return a list of primes < n """
    # From http://stackoverflow.com/a/3035188/4014959
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n - i*i - 1) // (2*i) + 1)
    return [2] + [2*i + 1 for i in range(1, n//2) if sieve[i]]

def lucas_lehmer(p):
    ''' The Lucas-Lehmer primality test for Mersenne primes.
        See https://en.wikipedia.org/wiki/Mersenne_prime#Searching_for_Mersenne_primes
    '''
    m = (1 << p) - 1
    s = 4
    for i in range(p - 2):
        s = (s * s - 2) % m
    return s == 0 and m or 0

#Lucas-Lehmer doesn't work on 2 because it's even, so we just print it manually :)
print('1 2\n3\n6\n')
count = 1
for p in primes(1280):
    m = lucas_lehmer(p)
    if m:
        count += 1
        n = m << (p - 1)
        print(count, p)
        print(m)
        print(n, '\n')