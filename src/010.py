from util.factor import primes_within_range

if __name__ == "__main__":
    answer = sum([i for i in primes_within_range(2_000_000)])
    print(answer)
