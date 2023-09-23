def generate_reflexive_transitive_relations(n):
    relations = []
    for num in range(2 ** (n * n)):
        relation = [[(num >> (i * n + j)) & 1 for j in range(n)] for i in range(n)]
        if check_reflexive(relation) and check_transitive(relation):
            relations.append(relation)
    return relations

# Example usage for n = 5
n_elements = 5
reflexive_transitive_relations = generate_reflexive_transitive_relations(n_elements)
for relation in reflexive_transitive_relations:
    print(relation)
    print("---")
