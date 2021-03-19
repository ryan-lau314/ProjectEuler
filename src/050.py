from sympy import sieve
from itertools import accumulate

MAX_VALUE = 1_000_000

if __name__ == "__main__":
    prime_list = [i for i in sieve.primerange(1, MAX_VALUE)]
    prime_acc = [0] + list(accumulate(prime_list))
    prime_set = set(prime_list)
    n = len(prime_list)

    max_chain_size = next(
        index for index, value in enumerate(prime_acc) if value > MAX_VALUE
    )

    for chain_size in range(max_chain_size, 0, -1):
        for i in range(0, n - chain_size):
            prime_sum = prime_acc[i + chain_size] - prime_acc[i]
            if prime_sum in prime_set:
                print(
                    f"{prime_sum} = {prime_list[i + 1]} + ... + {i + chain_size} ({chain_size} primes)"
                )
                exit(0)
