def gen_pandigital_for_number(n):
    pandigital = ""
    i = 1
    while len(pandigital) < 9:
        pandigital = pandigital + str(n * i)
        i += 1
    return pandigital if is_pandigital(pandigital) else None


def is_pandigital(str):
    if len(str) != 9 or "0" in str:
        return False
    exists = [False for _ in range(10)]
    for c in str:
        i = ord(c) - ord("0")
        if exists[i]:
            return False
        exists[i] = True
    return True


if __name__ == "__main__":
    best_pandigital = 123456789

    for n in range(1, 10000):
        pandigital = gen_pandigital_for_number(n)
        if pandigital and int(pandigital) > best_pandigital:
            best_pandigital = int(pandigital)
            print(f"Record update: {n} generates {pandigital}!")
