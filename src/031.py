COINS = [1, 2, 5, 10, 20, 50, 100, 200]
VALUE = 200

if __name__ == '__main__':
    DP = [[0 for _ in range(VALUE + 1)] for _ in range(len(COINS))]
    for i in range(len(COINS)):
        coin_value = COINS[i]
        for value in range(VALUE + 1):
            if i == 0:
                DP[i][value] = 1 if value % coin_value == 0 else 0
            else:
                DP[i][value] = DP[i-1][value]
                if coin_value <= value:
                    DP[i][value] += DP[i][value - coin_value]
    
print(f'There are {DP[len(COINS) - 1][VALUE]} way(s) to make {VALUE}p')