import random
import time

def selection_sort(arr):
    # Implementation

def insertion_sort(arr):
    # Implementation

def merge_sort(arr):
    # Implementation

def quick_sort(arr):
    # Implementation

n_values = [100, 1000, 10000]
for n in n_values:
    random_list = [random.randint(1, 999999) for _ in range(n)]

    start_time = time.time()
    selection_sort(random_list.copy())
    selection_time = time.time() - start_time

    start_time = time.time()
    insertion_sort(random_list.copy())
    insertion_time = time.time() - start_time

    start_time = time.time()
    merge_sort(random_list.copy())
    merge_time = time.time() - start_time

    start_time = time.time()
    quick_sort(random_list.copy())
    quick_time = time.time() - start_time

    print(f"n = {n}:")
    print(f"Selection Sort: {selection_time:.6f} seconds")
    print(f"Insertion Sort: {insertion_time:.6f} seconds")
    print(f"Merge Sort: {merge_time:.6f} seconds")
    print(f"Quick Sort: {quick_time:.6f} seconds")
