def recursive_binary_search(arr, x, left, right):
    if left > right:
        return -1  # Element not found
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return recursive_binary_search(arr, x, mid + 1, right)
    else:
        return recursive_binary_search(arr, x, left, mid - 1)

nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11
index = recursive_binary_search(nums, target, 0, len(nums) - 1)
if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found")
