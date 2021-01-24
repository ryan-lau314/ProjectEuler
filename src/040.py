def champernowne_generator():
    # Generates the decimal part of the Champernowne's constant
    current = 1
    remainder = str(current)
    while True:
        if len(remainder) > 0:
            c = remainder[0]
            remainder = remainder[1:]
            yield c
        else:
            current += 1
            remainder = str(current)


if __name__ == "__main__":
    gen = champernowne_generator()

    product = 1
    for i in range(1, 1_000_001):
        c = next(gen)
        if i in [1, 10, 100, 1_000, 10_000, 100_000, 1_000_000]:
            print(f"Digit {i} has value {c}")
            product *= int(c)

    print(product)