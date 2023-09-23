from itertools import permutations

def list_all_permutations(n):
    elements = list(range(1, n + 1))
    for perm in permutations(elements):
        print(perm)

n = 3
list_all_permutations(n)
