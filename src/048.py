MODULUS = 10_000_000_000

if __name__ == "__main__":
    sum = 0
    for i in range(1, 1001):
        sum = (sum + pow(i, i, 10_000_000_000)) % MODULUS
    print(sum)