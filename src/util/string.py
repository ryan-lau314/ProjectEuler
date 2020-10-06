def is_palindrome(n):
    """
    Tests if the input is a palindrome.
    Input can be either a number or a string.
    """
    if isinstance(n, int):
        return __is_palindrome(str(n))
    return __is_palindrome(n)


def __is_palindrome(s):
    return s == s[::-1]


def next_permutation(array):
    i = __find_rightmost_rise(array)

    if i is None:
        return False

    j = __find_next_largest_number_index_after_ith(array, i)
    array[i], array[j] = array[j], array[i]
    array[i + 1 :] = array[i + 1 :][::-1]
    return True


def __find_rightmost_rise(array):
    """
    Finds the largest i such that array[i] < array[i + 1].
    If there is no such i, return None.
    """
    if len(array) == 1:
        return None

    i = len(array) - 2
    while i >= 0:
        if array[i] < array[i + 1]:
            return i
        i -= 1

    return None


def __find_next_largest_number_index_after_ith(array, i):
    """
    Finds the largest j such that array[j] > array[i].
    """
    for j in range(len(array) - 1, 0, -1):
        if array[j] > array[i]:
            return j
