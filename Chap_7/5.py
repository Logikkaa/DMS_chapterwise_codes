# Define your relation_matrix here
relation_matrix = [[0, 1, 0], [0, 0, 1], [0, 0, 0]]
transitive_closure_matrix = transitive_closure(relation_matrix)
for row in transitive_closure_matrix:
    print(row)
