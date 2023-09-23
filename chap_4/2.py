def permutations_with_repetition_count(n, r):
    return n ** r

def combinations_with_repetition_count(n, r):
    return math.comb(n + r - 1, r)

n = 5
r = 3
print(f"Number of {r}-permutations with repetition:", permutations_with_repetition_count(n, r))
print(f"Number of {r}-combinations with repetition:", combinations_with_repetition_count(n, r))
