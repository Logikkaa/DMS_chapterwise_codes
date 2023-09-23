def count_partitions(n, max_num):
    if n == 0:
        return 1
    if n < 0 or max_num == 0:
        return 0
    return count_partitions(n - max_num, max_num) + count_partitions(n, max_num - 1)

number = 5
partitions = count_partitions(number, number)
print(f"Number of partitions for {number}: {partitions}")
