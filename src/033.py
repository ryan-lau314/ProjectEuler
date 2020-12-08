from fractions import Fraction

def is_curious_solution(A, B, a, b):
    return A != B and A >= 10 and B >= 10 and A < B and not (A % 10 == 0 and B % 10 == 0) and Fraction(A, B) == Fraction(a, b)

def get_curious_solutions(a, b, c):
    solutions = []
    # ca/cb = a/b
    if is_curious_solution(c * 10 + a, c * 10 + b, a, b):
        solutions.append((c * 10 + a, c * 10 + b))
        
    # ca/bc = a/b
    if is_curious_solution(c * 10 + a, b * 10 + c, a, b):
        solutions.append((c * 10 + a, b * 10 + c))
    
    # ac/cb = a/b
    if is_curious_solution(a * 10 + c, c * 10 + b, a, b):
        solutions.append((a * 10 + c, c * 10 + b))

    # ac/bc = a/b
    if is_curious_solution(a * 10 + c, b * 10 + c, a, b):
        solutions.append((a * 10 + c, b * 10 + c))

    return solutions

if __name__ == '__main__':
    curious_solutions = []

    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(10):
                curious_solutions += get_curious_solutions(a, b, c)

    product = Fraction(1, 1) 
    for solution in set(curious_solutions):
        numerator, denominator = solution
        product *= Fraction(numerator, denominator)

    print(product.denominator)