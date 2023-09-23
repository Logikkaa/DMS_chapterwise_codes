def reflexive_closure(matrix):
    closure_matrix = [row[:] for row in matrix]
    for i in range(len(matrix)):
        closure_matrix[i][i] = 1
    return closure_matrix

# Example usage
relation_matrix = [[1, 0, 1], [0, 1, 0], [0, 0, 1]]
reflexive_closure_matrix = reflexive_closure(relation_matrix)
for row in reflexive_closure_matrix:
    print(row)
