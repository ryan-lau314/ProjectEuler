memo = {}


def collatz_chain_length(n):
    if n in memo:
        return memo[n]

    if n == 1:
        length = 1
    elif n % 2 == 0:
        length = collatz_chain_length(n // 2) + 1
    else:
        length = collatz_chain_length(3 * n + 1) + 1

    memo[n] = length
    return length


if __name__ == "__main__":
    starting_number = 0
    max_chain_length = 0
    for i in range(1, 1_000_000):
        length = collatz_chain_length(i)
        if length > max_chain_length:
            starting_number, max_chain_length = (i, length)

    print(f"Starting number: {starting_number}\nChain length: {max_chain_length}")

