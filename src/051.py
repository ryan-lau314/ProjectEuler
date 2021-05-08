from itertools import count
from sympy import sieve


def p51():
    for num_of_digits in count(1):
        (
            largest_family_key,
            largest_family_values,
        ) = largest_prime_family_with_num_of_digits(num_of_digits)
        print(largest_family_key, largest_family_values)

        if len(largest_family_values) >= 8:
            break


def largest_prime_family_with_num_of_digits(num_of_digits):
    mask_to_primes = dict()
    for prime in primes_with_num_of_digits(num_of_digits):
        for mask in mask_prime(prime):
            if mask not in mask_to_primes:
                mask_to_primes[mask] = []
            mask_to_primes[mask].append(prime)

    largest_family_key = ""
    largest_family_values = []
    for family_key, family_values in mask_to_primes.items():
        if len(family_values) > len(largest_family_values) or (
            len(family_values) == len(largest_family_values)
            and min(family_values) < len(largest_family_values)
        ):
            largest_family_key = family_key
            largest_family_values = family_values

    return largest_family_key, largest_family_values


def primes_with_num_of_digits(num_of_digits):
    return [n for n in sieve.primerange(10 ** (num_of_digits - 1), 10 ** num_of_digits)]


def mask_prime(prime):
    masks = []
    for i in range(10):
        mask_prime_helper(str(prime), "", chr(ord("0") + i), masks)
    return masks


def mask_prime_helper(prime, mask, digit, masks):
    if len(prime) == len(mask):
        if prime != mask:
            masks += [mask]
    else:
        i = len(mask)
        c = prime[i]
        if c == digit:
            mask_prime_helper(prime, mask + "*", digit, masks)
        mask_prime_helper(prime, mask + c, digit, masks)


if __name__ == "__main__":
    p51()