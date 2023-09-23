def count_transitive_relations(n):
    count = 0
    for num in range(2 ** (n * n)):
        relation = [[(num >> (i * n + j)) & 1 for j in range(n)] for i in range(n)]
        if check_transitive(relation):
            count += 1
    return count

# Example usage
n_elements = 3
count = count_transitive_relations(n_elements)
print("Number of transitive relations:", count)
