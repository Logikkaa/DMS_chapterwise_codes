from itertools import permutations

def is_derangement(perm):
    return all(perm[i] != i + 1 for i in range(len(perm)))

n_elements_derangement = 8
derangements = []
for perm in permutations(range(1, n_elements_derangement + 1)):
    if is_derangement(perm):
        derangements.append(perm)

print(f"Derangements of {set(range(1, n_elements_derangement + 1))}:")
for derangement in derangements:
    print(derangement)
