def relation_projection(relation_matrix, deleted_fields):
    projected_matrix = []
    for i in range(len(relation_matrix)):
        row = []
        for j in range(len(relation_matrix[i])):
            if j not in deleted_fields:
                row.append(relation_matrix[i][j])
        projected_matrix.append(row)
    return projected_matrix

# Example usage
relation_matrix = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
deleted_fields = [1]
projected_relation = relation_projection(relation_matrix, deleted_fields)
for row in projected_relation:
    print(row)
