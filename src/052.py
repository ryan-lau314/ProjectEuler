from itertools import count


def p52():
    for num_of_digits in count(1):
        start = 10 ** (num_of_digits - 1)
        end = 10 ** num_of_digits // 6
        for n in range(start, end + 1):
            if is_permuted_multiple(n):
                print(n)
                return


def is_permuted_multiple(n):
    for factor in reversed(range(2, 7)):
        if not is_permutated_multiple_of(n, factor):
            return False
    return True


def is_permutated_multiple_of(n, factor):
    return sorted(str(n)) == sorted(str(n * factor))


if __name__ == "__main__":
    p52()