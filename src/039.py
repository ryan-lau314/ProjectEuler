if __name__ == "__main__":
    # Maps permieters to valid triangle solutions
    D = {}

    for a in range(1, 1000 // 3 + 1):
        for b in range(a, (1000 - a) // 2 + 1):
            for c in range(b, 1001 - a - b):
                if a * a + b * b == c * c:
                    p = a + b + c
                    if p in D:
                        D[p].append((a, b, c))
                    else:
                        D[p] = [(a, b, c)]

    max_record = max(D.items(), key=(lambda item: len(item[1])))
    print(max_record)
    print(len(max_record[1]))