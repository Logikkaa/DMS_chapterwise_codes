def symmetric_closure(matrix):
    closure_matrix = [row[:] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            closure_matrix[i][j] = max(matrix[i][j], matrix[j][i])
    return closure_matrix

# Example usage
relation_matrix = [[1, 0, 1], [0, 1, 0], [0, 0, 1]]
symmetric_closure_matrix = symmetric_closure(relation_matrix)
for row in symmetric_closure_matrix:
    print(row)
