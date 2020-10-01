from util.factor import divisors


def sum_of_divisors(n):
    return sum(divisors(n)) - n


if __name__ == "__main__":
    total = 0

    for first in range(1, 10000):
        second = sum_of_divisors(first)
        if second > first and sum_of_divisors(second) == first:
            print(f"Pair found: ({first}, {second})")
            total += first + second

    print(total)
