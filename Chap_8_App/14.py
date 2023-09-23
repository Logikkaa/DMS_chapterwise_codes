def subset_sum_backtracking(numbers, target_sum):
    def backtrack(index, current_sum, current_subset):
        if current_sum == target_sum:
            result.append(current_subset[:])
            return
        if index == len(numbers) or current_sum > target_sum:
            return
        current_subset.append(numbers[index])
        backtrack(index + 1, current_sum + numbers[index], current_subset)
        current_subset.pop()
        backtrack(index + 1, current_sum, current_subset)

    result = []
    backtrack(0, 0, [])
    return result

# Example usage
numbers = [3, 34, 4, 12, 5, 2]
target_sum = 9
subsets = subset_sum_backtracking(numbers, target_sum)
print(subsets)
