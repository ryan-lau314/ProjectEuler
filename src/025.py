from util.fib import  fib

if __name__ == '__main__':
    i = 0
    generator = fib()
    curr_fib = next(generator)

    while len(str(curr_fib)) < 1000:
        curr_fib = next(generator)
        i += 1
    
    print(f"{i}: {curr_fib}")
