from util.timer import timing


@timing
def sum_of_multiples_below_n(n):
    sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


@timing
def sum_of_multiples_below_n_optimised(n):
    return (
        _sum_of_multiples_of_m_from_1_to_n(3, n)
        + _sum_of_multiples_of_m_from_1_to_n(5, n)
        - _sum_of_multiples_of_m_from_1_to_n(15, n)
    )


def _sum_of_multiples_of_m_from_1_to_n(m, n):
    if n < m:
        return 0
    return (m + (n - 1) // m * m) * ((n - 1) // m) // 2


if __name__ == "__main__":
    answer = sum_of_multiples_below_n(1000)
    answer = sum_of_multiples_below_n_optimised(1000)
    print(answer)
