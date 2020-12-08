import math 

def sum_of_factorial_of_digits(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += math.factorial(digit)
        n //= 10
    return sum

if __name__ == '__main__':
    answer = sum([n for n in range(10, 2540160) if n == sum_of_factorial_of_digits(n)])
    print(answer)
