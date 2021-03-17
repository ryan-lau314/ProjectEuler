from itertools import count


def triangle():
    for i in count(1):
        yield i * (i + 1) // 2


def pentagon():
    for i in count(1):
        yield i * (3 * i - 1) // 2


def hexagon():
    for i in count(1):
        yield i * (2 * i - 1)


def merge(first_gen, second_gen):
    first = next(first_gen)
    second = next(second_gen)
    while True:
        if first < second:
            first = next(first_gen)
        elif first > second:
            second = next(second_gen)
        else:
            yield first
            first = next(first_gen)
            second = next(second_gen)


if __name__ == "__main__":
    common_generator = merge(merge(triangle(), pentagon()), hexagon())
    next(common_generator)
    print(next(common_generator))