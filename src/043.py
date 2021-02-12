PRIMES = [2, 3, 5, 7, 11, 13, 17]


def find_pandigital_numbers():
    pandigital_numbers = []
    backtrack(0, 0, [True for _ in range(10)], pandigital_numbers)
    return pandigital_numbers


def backtrack(level, number, have_digit, pandigital_numbers):
    if level >= 10:
        pandigital_numbers.append(number)
        return

    for i in range(10):
        next_number = number * 10 + i
        if have_digit[i] and is_substring_divisible(level, next_number):
            have_digit[i] = False
            backtrack(level + 1, next_number, have_digit, pandigital_numbers)
            have_digit[i] = True


def is_substring_divisible(level, number):
    return level < 3 or number % 1000 % PRIMES[level - 3] == 0


if __name__ == "__main__":
    pandigital_numbers = find_pandigital_numbers()
    print(sum(pandigital_numbers))