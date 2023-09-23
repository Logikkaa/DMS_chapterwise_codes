def check_symmetric(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def check_antisymmetric(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if matrix[i][j] == 1 and matrix[j][i] == 1:
                return False
    return True

# Example usage
relation_matrix = [[1, 0, 1], [0, 1, 0], [1, 0, 0]]
print("Symmetric:", check_symmetric(relation_matrix))
print("Antisymmetric:", check_antisymmetric(relation_matrix))
