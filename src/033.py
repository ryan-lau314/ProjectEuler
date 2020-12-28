from fractions import Fraction

def is_curious_solution(A, B, a, b):
    return 1 if B >= 10 and A < B and not (A % 10 == 0 and B % 10 == 0) and Fraction(A, B) == Fraction(a, b) else 0

def curious_solution_count(a, b, c):
    # (ca/cb,ca/bc,ac/cb,ac/bc) = a/b
    return is_curious_solution(c * 10 + a, c * 10 + b, a, b) \
        + is_curious_solution(c * 10 + a, b * 10 + c, a, b) \
            + is_curious_solution(a * 10 + c, c * 10 + b, a, b) \
                + is_curious_solution(a * 10 + c, b * 10 + c, a, b) 

if __name__ == '__main__':
    curious_solutions = []

    for a in range(1, 10):
        for b in range(a + 1, 10):
            for c in range(10):
                n = curious_solution_count(a, b, c)
                for i in range(n):
                    curious_solutions.append(Fraction(a, b))

    product = Fraction(1, 1) 
    for solution in curious_solutions:
        product *= solution

    print(product.denominator)