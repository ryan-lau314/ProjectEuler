from sympy import sieve
from itertools import accumulate

MAX_VALUE = 1_000_000

prime_list = [i for i in sieve.primerange(1, MAX_VALUE)]
prime_acc = [0] + list(accumulate(prime_list))
prime_set = set(prime_list)


def p050():
    n = len(prime_list)
    largest_prime = prime_list[n - 1]

    for l in range(n, 0, -1):
        for i in range(0, n - l + 1):
            prime_sum = sublist_sum(i, i + l - 1)

            # Terminate early when the prime sum is larger than the largest prime.
            # Prime sums at later i's are larger, therefore not helpful.
            if prime_sum > largest_prime:
                break

            # Use set instead of list for faster searching
            if prime_sum in prime_set:
                return (prime_sum, i, l)


def sublist_sum(i, j):
    if i == 0:
        return prime_acc[j]
    return prime_acc[j] - prime_acc[i - 1]


if __name__ == "__main__":
    s, i, l = p050()
    print(f"{s} = {prime_list[i]} + ... + {prime_list[i + l - 1]} ({l} primes)")
