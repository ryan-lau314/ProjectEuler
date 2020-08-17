if __name__ == "__main__":
    dp = [[0 for _ in range(21)] for _ in range(21)]

    for i in range(21):
        for j in range(21):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    print(dp[20][20])

