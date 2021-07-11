def p055():
    print(sum([1 for n in range(1, 10000) if is_lychrel(n)]))


def is_lychrel(n):
    for _ in range(50):
        n += reverse(n)
        if is_palindrome(n):
            return False
    return True


def reverse(n):
    r = 0
    while n > 0:
        r *= 10
        r += n % 10
        n //= 10
    return r


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    p055()
