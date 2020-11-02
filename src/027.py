from util.factor import sieve_of_eratosthenes

all_primes = set()
for index, num_of_factor in enumerate(sieve_of_eratosthenes(2001000)):
    if num_of_factor == 0 and index >= 2:
        all_primes.add(index)

possible_b = list(filter(lambda value: value < 1000, all_primes))


def consecutive_prime_count(a, b):
    """
    Consider the expression f(n) = n^2 + an + b.

    The function returns the largest N such that f(n) is prime for all n between 0 and N-1 inclusive.
    """
    n = 0
    while n * n + a * n + b in all_primes:
        n += 1
    return n


if __name__ == "__main__":
    max_consecutive_prime_count = 0
    optimal_a = 0
    optimal_b = 0

    for a in range(-999, 1000):
        for b in possible_b:
            count = consecutive_prime_count(a, b)

            if count > max_consecutive_prime_count:
                max_consecutive_prime_count = count
                optimal_a, optimal_b = a, b
                print(f"n^2 + {a}n + {b} => {count} terms")

    print(f"optimal_a * optimal_b = {optimal_a * optimal_b}")
