if __name__ == "__main__":
    total = 1
    for i in range(1, 501):
        upper_right = (2 * i + 1) ** 2
        total += upper_right * 4 - 12 * i
    print(total)
