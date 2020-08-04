from functools import reduce


def prime_factorisation(n):
    """
    Returns the prime factor form of a number.
    For example, input number 100 = 2^2 * 5^2 will be transformed to [(2, 2), (5, 2)].
    """
    factors = []
    curr_factor = 2
    exponent = 0
    while n > 1:
        while n % curr_factor == 0:
            n /= curr_factor
            exponent += 1

        if exponent > 0:
            factors.append((curr_factor, exponent))

        curr_factor += 1
        exponent = 0
    return factors


def primes():
    """
    Simple prime generator. Not very efficient.
    """
    yield 2
    primes = []
    test_prime = 3
    while True:
        is_prime = True
        for i in primes:
            if test_prime % i == 0:
                is_prime = False
                break

        if is_prime:
            yield test_prime
            primes.append(test_prime)

        test_prime += 2


def primes_within_range(n):
    for index, value in enumerate(sieve_of_eratosthenes(n)):
        if index >= 2 and value == 0:
            yield index


def sieve_of_eratosthenes(n):
    """
    Finds all prime numbers under n.
    Returns the array a[0...n-1]. 
    If number n is prime, a[n] = 0.
    If number n is composite, a[n] contains one of n's non-trivial factors.
    """
    sieve = [0 for _ in range(n)]
    wheel = __wheel_factors()
    factor = next(wheel)
    while factor * factor <= n:
        if sieve[factor] == 0:
            for i in range(factor * factor, n, factor):
                sieve[i] = factor
        factor = next(wheel)
    return sieve


def __wheel_factors():
    yield 2
    yield 3
    yield 5
    yield 7
    yield 11
    yield 13
    factor = 17
    while True:
        yield factor
        factor += 2


def lcm(*vals):
    """
    Returns the lowest common multiple of all values.
    """
    if len(vals) == 0:
        raise Exception("Please provide a value!")
    else:
        return reduce(__lcm, vals)


def gcd(*vals):
    """
    Returns the greatest common divisor of all values.
    """
    if len(vals) == 0:
        raise Exception("Please provide a value!")
    else:
        return reduce(__gcd, vals)


def __lcm(x, y):
    return x * y // __gcd(x, y)


def __gcd(x, y):
    if y == 0:
        return x
    return __gcd(y, x % y)

