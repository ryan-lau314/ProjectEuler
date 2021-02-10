from itertools import permutations
from functools import reduce
from sympy.ntheory import isprime


def largest_pandigital_prime(n):
    for tuple in permutations(reversed(range(1, n + 1))):
        number = tuple_to_number(tuple)
        if isprime(number):
            return number
    return None


def tuple_to_number(tuple):
    return reduce(lambda acc, digit: acc * 10 + digit, tuple)


if __name__ == "__main__":
    for n in range(7, 0, -1):
        potential_prime = largest_pandigital_prime(n)
        if potential_prime:
            print(potential_prime)
            break
