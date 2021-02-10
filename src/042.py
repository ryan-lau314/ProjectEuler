from sympy.ntheory.primetest import is_square
from urllib.request import urlopen


def is_triangle(n):
    return is_square(8 * n + 1)


def word_value(word):
    return sum([char_value(c) for c in word])


def char_value(c):
    return ord(c.upper()) - ord("A") + 1


if __name__ == "__main__":
    words = []
    data = urlopen("https://projecteuler.net/project/resources/p042_words.txt")
    for line in data:
        words += line.decode("utf-8").replace('"', "").split(",")

    print(sum([1 for word in words if is_triangle(word_value(word))]))
