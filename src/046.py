from sympy import sieve
from itertools import count


def odd_composite_generator():
    for n in count(9, 2):
        if n not in sieve:
            yield n


def satisfies_goldbach(n: int):
    i = 1
    while n > 2 * i * i:
        maybe_prime = n - 2 * i * i
        if maybe_prime in sieve:
            return (maybe_prime, i)
        i += 1
    return None


if __name__ == "__main__":
    gen = odd_composite_generator()
    while True:
        odd_composite = next(gen)
        tuple = satisfies_goldbach(odd_composite)
        if tuple:
            prime, i = tuple
            print(f"{odd_composite} = {prime} + 2 * {i}^2")
        else:
            print(f"{odd_composite} is not happy!")
            break