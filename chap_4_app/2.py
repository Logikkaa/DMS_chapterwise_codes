import random

def generate_random_permutation(n):
    permutation = list(range(1, n + 1))
    random.shuffle(permutation)
    return permutation

n = 5
random_permutation = generate_random_permutation(n)
print(random_permutation)
