from itertools import combinations

def list_all_combinations(n):
    elements = list(range(1, n + 1))
    for r in range(1, n + 1):
        for comb in combinations(elements, r):
            print(comb)

n = 3
list_all_combinations(n)
