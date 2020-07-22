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
