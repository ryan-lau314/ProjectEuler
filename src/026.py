from typing import Dict


def cycle_length(n: int) -> int:
    """
    Returns the length of the recurring cycle in the decimal representation of 1/n.

    If there is no recurring cycle, returns 0.
    """
    remainder: int = 10 % n
    counter: int = 1
    previousRemainders: Dict[int, int] = {1: 0}

    while remainder != 0 and remainder not in previousRemainders:
        previousRemainders[remainder] = counter
        counter += 1
        remainder = 10 * remainder % n

    if remainder == 0:
        return 0

    return counter - previousRemainders[remainder]


if __name__ == "__main__":
    max_cycle_length: int = 0
    max_cycle_length_index: int = 0

    for i in range(1, 1001):
        length = cycle_length(i)
        if length > max_cycle_length:
            max_cycle_length = length
            max_cycle_length_index = i

    print(f"Cycle length of 1/{max_cycle_length_index} = {max_cycle_length}")
