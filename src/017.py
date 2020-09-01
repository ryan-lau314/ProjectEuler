DICT = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    15: "fifteen",
    18: "eighteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    80: "eighty",
}


def one_digit_to_words(n):
    return [DICT[n]]


def two_digit_to_words(n):
    # Special case: 1~13
    if n in DICT:
        return [DICT[n]]

    # Special case: 14~19
    if n < 20:
        return [DICT[n - 10] + "teen"]

    words = []
    tens = n // 10 * 10
    if tens in DICT:
        # Special tens: e.g. twenty, thirty
        words.append(DICT[tens])
    else:
        # Generic tens: e.g. sixty, seventy
        words.append(DICT[tens // 10] + "ty")

    # Add ones for those that are not multiples of ten
    if n % 10 != 0:
        words += one_digit_to_words(n % 10)

    return words


def three_digit_to_words(n):
    if n < 100:
        return two_digit_to_words(n)

    words = [DICT[n // 100], "hundred"]

    # Add "and xxx" for those that are not multiples of 100
    if n % 100 != 0:
        words += ["and"]
        words += two_digit_to_words(n % 100)

    return words


def four_digit_to_words(n):
    if n < 1000:
        return three_digit_to_words(n)

    words = [DICT[n // 1000], "thousand"]

    # Add "and xxx" for those that are not multiples of 1000
    if n % 1000 != 0:
        words += three_digit_to_words(n % 1000)

    return words


def word_length(words):
    return sum([len(word) for word in words])


if __name__ == "__main__":
    solution = 0
    for i in range(1, 1001):
        words = four_digit_to_words(i)
        solution += word_length(words)
    print(solution)
