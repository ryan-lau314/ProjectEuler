from itertools import count


def nth_pentagon(n):
    return n * (3 * n - 1) // 2


def is_pentagon(n):
    return (((24 * n + 1) ** 0.5) + 1) % 6 == 0


for d in count(2):
    D = nth_pentagon(d)
    for i in range(1, d):
        P_i = nth_pentagon(i)
        j, remainder = divmod(D - P_i, 3 * i)
        if remainder == 0 and is_pentagon(2 * nth_pentagon(j) + D):
            print(D)
            exit(0)
