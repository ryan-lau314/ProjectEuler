from urllib.request import urlopen


def char_value(c):
    return ord(c.upper()) - ord("A") + 1


def word_value(word, position):
    return sum([char_value(c) for c in word]) * (position + 1)


if __name__ == "__main__":
    names = []
    data = urlopen("https://projecteuler.net/project/resources/p022_names.txt")
    for line in data:
        names += line.decode("utf-8").replace('"', "").split(",")

    names.sort()
    print(sum([word_value(name, i) for i, name in enumerate(names)]))
