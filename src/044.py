from itertools import count


def nth_pentagon(n):
    return n * (3 * n - 1) // 2


def is_pentagon(n):
    return (((24 * n + 1) ** 0.5) + 1) % 6 == 0


for i in count(2):
    P_i = nth_pentagon(i)
    for d in range(1, i):
        P_d = nth_pentagon(d)
        j, remainder = divmod(P_i - P_d, 3 * d)
        if remainder == 0 and is_pentagon(2 * nth_pentagon(j) + P_i):
            P_j = nth_pentagon(j)
            P_k = nth_pentagon(j) + P_i
            print(f"{P_k} - {P_j} = {P_i}")
            print(f"{P_j} + {P_k} = {P_j + P_k}")
            exit(0)
