from itertools import permutations

def is_derangement(perm):
    return all(perm[i] != i + 1 for i in range(len(perm)))

def list_derangements(n):
    derangements = []
    for perm in permutations(range(1, n + 1)):
        if is_derangement(perm):
            derangements.append(perm)
    return derangements

n = 3  # Number of elements in the set
derangements = list_derangements(n)
print(f"Derangements of {set(range(1, n + 1))}:")
for derangement in derangements:
    print(derangement)
