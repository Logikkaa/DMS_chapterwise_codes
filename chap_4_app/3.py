import random

def count_inversions(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count

def generate_random_permutations(m, n):
    permutations = []
    total_inversions = 0
    for _ in range(m):
        permutation = generate_random_permutation(n)
        inversions = count_inversions(permutation)
        total_inversions += inversions
        permutations.append(permutation)
    average_inversions = total_inversions / m
    return permutations, average_inversions

m = 10
n = 5
permutations, avg_inversions = generate_random_permutations(m, n)
print("Generated Permutations:")
for perm in permutations:
    print(perm)
print("Average Number of Inversions:", avg_inversions)
