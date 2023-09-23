def count_equivalence_relations(n):
    count = 0
    for num in range(2 ** (n * n)):
        relation = [[(num >> (i * n + j)) & 1 for j in range(n)] for i in range(n)]
        if check_reflexive(relation) and check_symmetric(relation) and check_transitive(relation):
            count += 1
    return count

# Example usage
n_elements = 3
count = count_equivalence_relations(n_elements)
print("Number of equivalence relations:", count)
