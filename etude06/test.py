def primes(known_primes=[7, 11, 13, 17, 19, 23, 29]):
    """
    Generate every prime number in ascending order
    """
    # 2, 3, 5 wheel
    yield from (2, 3, 5)
    yield from known_primes
    # The first time the generator runs, known_primes
    #   contains all primes such that  5 < p < 2 * 3 * 5
    # After each wheel cycle the list of known primes
    #   will be added to.
    # We need to figure out where to continue from,
    #   which is the next multiple of 30 higher than
    #   the last known_prime:
    base = 30 * (known_primes[-1] // 30 + 1)
    new_primes = []
    while True:
        # offs is chosen so  30*i + offs cannot be a multiple of 2, 3, or 5
        for offs in (1, 7, 11, 13, 17, 19, 23, 29):
            k = base + offs    # next prime candidate
            for p in known_primes:
                if not k % p:
                    # found a factor - not prime
                    break
                elif p*p > k:
                    # no smaller prime factors - found a new prime
                    new_primes.append(k)
                    break
        if new_primes:
            yield from new_primes
            known_primes.extend(new_primes)
            new_primes = []
        base += 30

def is_prime(n):
    for p in primes():
        if not n % p:
            # found a factor - not prime
            return False
        elif p * p > n:
            # no factors found - is prime
            return True


# search all numbers in [2..limit] for perfect numbers
# (ones whose proper divisors sum to the number)
# limit = int(input("enter upper limit for perfect number search: "))
limit = 9000000

for p in primes():
    pp = 2**p
    perfect = (pp - 1) * (pp // 2)
    if perfect > limit:
        break
    elif is_prime(pp - 1):
        print(perfect, "is a perfect number")