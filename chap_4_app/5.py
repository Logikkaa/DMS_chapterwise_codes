import random

def insertion_sort(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            comparisons += 1
        arr[j + 1] = key
    return comparisons

def generate_and_sort_permutations(m, n):
    total_comparisons = 0
    for _ in range(m):
        permutation = generate_random_permutation(n)
        comparisons = insertion_sort(permutation)
        total_comparisons += comparisons
    average_comparisons = total_comparisons / m
    return average_comparisons

m = 10
n = 5
avg_comparisons = generate_and_sort_permutations(m, n)
print("Average Number of Comparisons using Insertion Sort:", avg_comparisons)
