def sum_of_fifth_powers_of_digits(n):
    total = 0
    while n > 0:
        last_digit = n % 10
        total += last_digit ** 5
        n //= 10
    return total


if __name__ == "__main__":
    total = 0
    for n in range(10, 354_295):
        if n == sum_of_fifth_powers_of_digits(n):
            total += n
            print(f"Solution found: {n}")
    print(f"Sum: {total}")