def p53():
    count = 0
    DP = [[0 for _ in range(101)] for _ in range(101)]
    for n in range(1, 101):
        for r in range(n + 1):
            if n == 1 or r == 0 or r == n:
                DP[n][r] = 1
            else:
                DP[n][r] = DP[n - 1][r] + DP[n - 1][r - 1]

            if DP[n][r] > 1_000_000:
                count += 1

    print(count)


if __name__ == "__main__":
    p53()