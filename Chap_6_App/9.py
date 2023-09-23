def relation_join(relation_a, relation_b, common_fields):
    joined_relation = []
    for row_a in relation_a:
        for row_b in relation_b:
            matched = True
            for field in common_fields:
                if row_a[field] != row_b[field]:
                    matched = False
                    break
            if matched:
                joined_relation.append(row_a + row_b)
    return joined_relation

# Example usage
relation_a = [[1, 0], [0, 1]]
relation_b = [[1, 0], [0, 1]]
common_fields = [0]
join_result = relation_join(relation_a, relation_b, common_fields)
for row in join_result:
    print(row)
