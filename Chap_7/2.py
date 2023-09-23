def generate_reflexive_symmetric_relations(n):
    relations = []
    for num in range(2 ** (n * n)):
        relation = [[(num >> (i * n + j)) & 1 for j in range(n)] for i in range(n)]
        if check_reflexive(relation) and check_symmetric(relation):
            relations.append(relation)
    return relations

# Example usage for n = 6
n_elements = 6
reflexive_symmetric_relations = generate_reflexive_symmetric_relations(n_elements)
for relation in reflexive_symmetric_relations:
    print(relation)
    print("---")
