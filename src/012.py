from util.factor import num_of_divisors

if __name__ == "__main__":
    i = 2
    triangle = 1
    while num_of_divisors(triangle) <= 500:
        triangle += i
        i += 1
    print(triangle)
