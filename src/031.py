COINS = [1, 2, 5, 10, 20, 50, 100, 200]
VALUE = 200

if __name__ == '__main__':
    DP = [[0 for _ in range(VALUE + 1)] for _ in range(len(COINS))]
    for i in range(len(COINS)):
        coin_value = COINS[i]
        for value in range(coin_value, VALUE + 1):
            if value == 0:
                DP[i][value] = 1
            elif value < coin_value:
                if i > 0:
                    DP[i][value] = DP[i-1][value]
                else:
                    DP[i][value] = 0
            else:
                if i > 0:
                    DP[i][value] = DP[i-1][value] + DP[i][value - coin_value]
                else:
                    DP[i][value] = DP[i][value - coin_value]
    
    print(f'There are {DP[len(COINS) - 1][VALUE]} way(s) to make {VALUE}p')