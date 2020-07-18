def fib():
    first = 0
    second = 1
    while True:
        yield first
        first, second = second, first + second
