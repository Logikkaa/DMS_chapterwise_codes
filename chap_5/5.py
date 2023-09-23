import random

def generate_random_permutation(n):
    permutation = list(range(1, n + 1))
    random.shuffle(permutation)
    return permutation

num_permutations = 100
n = 100
random_permutations = [generate_random_permutation(n) for _ in range(num_permutations)]

for idx, perm in enumerate(random_permutations):
    print(f"Permutation {idx + 1}:", perm)
