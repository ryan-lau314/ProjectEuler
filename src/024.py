from util.string import next_permutation


if __name__ == "__main__":
    array = [str(i) for i in range(10)]
    for i in range(1_000_000 - 1):
        next_permutation(array)
    print("".join(array))
