from util.factor import divisors


def is_abundant(n):
    return sum(divisors(n)) - n > n


if __name__ == "__main__":
    abundant_numbers = [i for i in range(1, 28124) if is_abundant(i)]

    abundant_sums = set()
    for i in abundant_numbers:
        for j in abundant_numbers:
            if i + j <= 28123 and i + j not in abundant_sums:
                abundant_sums.add(i + j)

    non_abundant_sums = [i for i in range(1, 28124) if i not in abundant_sums]
    print(sum(non_abundant_sums))
