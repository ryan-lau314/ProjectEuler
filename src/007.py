from util.factor import primes

if __name__ == "__main__":
    generator = primes()
    for i in range(10000):
        next(generator)
    print(next(generator))
