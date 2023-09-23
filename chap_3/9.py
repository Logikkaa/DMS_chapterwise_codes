def recursive_linear_search(arr, x, index=0):
    if index == len(arr):
        return -1  # Element not found
    if arr[index] == x:
        return index
    return recursive_linear_search(arr, x, index + 1)

nums = [4, 2, 8, 1, 6, 3]
target = 6
index = recursive_linear_search(nums, target)
if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found")
