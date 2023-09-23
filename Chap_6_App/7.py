def generate_equivalence_relations(n):
    relations = []
    for num in range(2 ** (n * n)):
        relation = [[(num >> (i * n + j)) & 1 for j in range(n)] for i in range(n)]
        if check_reflexive(relation) and check_symmetric(relation) and check_transitive(relation):
            relations.append(relation)
    return relations

# Example usage
n_elements = 3
equivalence_relations = generate_equivalence_relations(n_elements)
for relation in equivalence_relations:
    print(relation)
