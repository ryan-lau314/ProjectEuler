from util.string import is_palindrome

def base10_to_base2(base10):
    return bin(base10)[2:]

if __name__ == '__main__':
    solution = sum([number for number in range(1, 1_000_000) if is_palindrome(number) and is_palindrome(base10_to_base2(number))])
    print(solution)
