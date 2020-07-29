def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6


def square_of_sum(n):
    sum = (n * (n + 1)) // 2
    return sum * sum


if __name__ == "__main__":
    answer = square_of_sum(100) - sum_of_squares(100)
    print(answer)
