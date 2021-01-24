from util.factor import primes

LEFT_TRUNCATABLE = []
RIGHT_TRUNCATABLE = []


def is_left_truncatable(n):
    if n < 10 or str(n)[1:] in LEFT_TRUNCATABLE:
        LEFT_TRUNCATABLE.append(str(n))
        return True
    return False


def is_right_truncatable(n):
    if n < 10 or str(n)[:-1] in RIGHT_TRUNCATABLE:
        RIGHT_TRUNCATABLE.append(str(n))
        return True
    return False


if __name__ == "__main__":
    solution = []
    prime_gen = primes()

    while len(solution) < 11:
        n = next(prime_gen)
        left = is_left_truncatable(n)
        right = is_right_truncatable(n)
        if left and right and n > 10:
            solution.append(n)

    print(solution)
    print(sum(solution))