def smallest_equivalence_relation(matrix):
    closure_matrix = transitive_closure(matrix)
    smallest_equivalence_matrix = symmetric_closure(closure_matrix)
    return smallest_equivalence_matrix

# Example usage
relation_matrix = [[1, 0, 1], [0, 1, 0], [0, 0, 1]]
smallest_equivalence_matrix = smallest_equivalence_relation(relation_matrix)
for row in smallest_equivalence_matrix:
    print(row)
