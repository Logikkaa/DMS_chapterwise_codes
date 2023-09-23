def transitive_closure(matrix):
    closure_matrix = [row[:] for row in matrix]
    n = len(matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure_matrix[i][j] = closure_matrix[i][j] or (closure_matrix[i][k] and closure_matrix[k][j])
    return closure_matrix

# Example usage
relation_matrix = [[1, 0, 1], [0, 1, 0], [0, 0, 1]]
transitive_closure_matrix = transitive_closure(relation_matrix)
for row in transitive_closure_matrix:
    print(row)
