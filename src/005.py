from util.factor import lcm

if __name__ == "__main__":
    numbers = [i for i in range(1, 21)]
    print(lcm(*numbers))
