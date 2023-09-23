import math

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

n = 5
r = 3
print(f"Number of {r}-permutations:", permutations_count(n, r))
print(f"Number of {r}-combinations:", combinations_count(n, r))
