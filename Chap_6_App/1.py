def check_reflexive(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] != 1:
            return False
    return True

def check_irreflexive(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] != 0:
            return False
    return True

# Example usage
relation_matrix = [[1, 0, 0], [0, 1, 1], [0, 0, 1]]
print("Reflexive:", check_reflexive(relation_matrix))
print("Irreflexive:", check_irreflexive(relation_matrix))
