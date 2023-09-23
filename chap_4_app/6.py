import random

def bubble_sort(arr):
    comparisons = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                comparisons += 1
        if not swapped:
            break
    return comparisons

m = 10
n = 5
total_comparisons = 0
for _ in range(m):
    permutation = generate_random_permutation(n)
    comparisons = bubble_sort(permutation.copy())
    total_comparisons += comparisons
average_comparisons = total_comparisons / m
print("Average Number of Comparisons using Modified Bubble Sort:", average_comparisons)
