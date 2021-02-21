def gen_pandigital_for_seed(seed):
    pandigital = ""
    i = 1
    while len(pandigital) < 9:
        pandigital = pandigital + str(seed * i)
        i += 1
    return pandigital if is_pandigital(pandigital) else None


def is_pandigital(str):
    return "".join(sorted(str)) == "123456789"


if __name__ == "__main__":
    best_pandigital = 123456789

    for seed in range(1, 10000):
        pandigital = gen_pandigital_for_seed(seed)
        if pandigital and int(pandigital) > best_pandigital:
            best_pandigital = int(pandigital)
            print(f"Record update: {seed} generates {pandigital}!")
