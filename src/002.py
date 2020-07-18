from util.fib import fib

if __name__ == "__main__":
    sum = 0
    for num in fib():
        if num > 4_000_000:
            break
        if num % 2 == 0:
            sum += num
    print(sum)
