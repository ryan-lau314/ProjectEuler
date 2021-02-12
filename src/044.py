from itertools import count

cache = {}


def nth_pentagon(n):
    if n not in cache:
        cache[n] = n * (3 * n - 1) // 2
    return cache[n]


def is_pentagon(n):
    return (((24 * n + 1) ** 0.5) + 1) % 6 == 0


for i in count(1):
    large_pentagon = nth_pentagon(i)
    for j in range(1, i):
        small_pentagon = nth_pentagon(j)
        sum = small_pentagon + large_pentagon
        difference = large_pentagon - small_pentagon
        if is_pentagon(sum) and is_pentagon(difference):
            print(f"{large_pentagon} + {small_pentagon} = {sum}")
            print(f"{large_pentagon} - {small_pentagon} = {difference}")
            exit(0)
