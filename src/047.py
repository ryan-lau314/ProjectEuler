from sympy.ntheory import primefactors
from itertools import count

streak = 0

for n in count(647):
    prime_factor_count = len(primefactors(n))

    if prime_factor_count == 4:
        streak += 1
    else:
        streak = 0

    if streak == 4:
        print(f"Found: {n - 3} - {n}")
        break