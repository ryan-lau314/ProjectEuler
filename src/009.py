if __name__ == "__main__":
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = 1000 - a - b
            if c <= b:
                break
            if a * a + b * b > c * c:
                break
            if a * a + b * b == c * c:
                print(f"a = {a}, b = {b}, c = {c}.\na * b * c = {a*b*c}")
                exit(0)

