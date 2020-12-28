def uses_one_to_nine_exactly_once(*values):
    char_list = [char for value in values for char in str(value)]
    char_list.sort()
    return ''.join(char_list) == '123456789'

def is_pandigital(n):
    i = 1
    while i * i <= n:
        if n % i == 0:
            if uses_one_to_nine_exactly_once(n, i, n // i):
                print(f'{i} * {n // i} = {n}')
                return True
        i += 1
    return False


if __name__ == '__main__':
    print('Sum is', sum([n for n in range(1000, 10000) if is_pandigital(n)]))