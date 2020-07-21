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
