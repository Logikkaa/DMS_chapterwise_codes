def longest_increasing_subsequence(sequence):
    lis = [1] * len(sequence)
    for i in range(1, len(sequence)):
        for j in range(0, i):
            if sequence[i] > sequence[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    return max(lis)

def longest_decreasing_subsequence(sequence):
    lds = [1] * len(sequence)
    for i in range(1, len(sequence)):
        for j in range(0, i):
            if sequence[i] < sequence[j] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1
    return max(lds)

sequence = [3, 4, 8, 1, 5, 6, 2]
print("Longest Increasing Subsequence:", longest_increasing_subsequence(sequence))
print("Longest Decreasing Subsequence:", longest_decreasing_subsequence(sequence))
