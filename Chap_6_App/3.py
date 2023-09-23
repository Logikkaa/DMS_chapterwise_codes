def check_transitive(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                for k in range(len(matrix)):
                    if matrix[j][k] == 1 and matrix[i][k] != 1:
                        return False
    return True

# Example usage
relation_matrix = [[1, 0, 1], [0, 1, 1], [0, 0, 1]]
print("Transitive:", check_transitive(relation_matrix))
