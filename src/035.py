from util.factor import primes_within_range

def rotate(number):
    number_string = str(number)
    return int(number_string[-1] + number_string[:-1])

def is_circular_prime(prime, primes):
    next_rotation = rotate(prime)
    while next_rotation != prime:
        if next_rotation not in primes:
            return False
        next_rotation = rotate(next_rotation)
    return True

if __name__ == '__main__':
    primes = set([prime for prime in primes_within_range(1_000_000)])
    circular_primes = [prime for prime in primes if is_circular_prime(prime, primes)]
    print(len(circular_primes))
    