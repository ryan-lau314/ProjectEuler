from sympy import sieve


def p049():
    prime_dict = {}

    for prime in sieve.primerange(1000, 9999):
        prime_key = key(prime)
        prime_dict.setdefault(prime_key, [])
        prime_dict[prime_key].append(prime)

    for primes in prime_dict.values():
        for sequence in arithmetic_subsequence(primes):
            print(sequence)


def key(prime):
    return "".join(sorted(str(prime)))


def arithmetic_subsequence(primes):
    n = len(primes)
    if n < 3:
        return

    last_value = primes[n - 1]
    for i in range(n):
        for j in range(i + 1, n):
            first_prime = primes[i]
            second_prime = primes[j]
            possible_prime = second_prime * 2 - first_prime

            if possible_prime in primes:
                yield (first_prime, second_prime, possible_prime)

            if possible_prime > last_value:
                break


if __name__ == "__main__":
    p049()