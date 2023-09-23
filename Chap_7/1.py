def generate_relations(n):
    relations = []
    for num in range(2 ** (n * n)):
        relation = [[(num >> (i * n + j)) & 1 for j in range(n)] for i in range(n)]
        relations.append(relation)
    return relations

# Example usage for n = 4
n_elements = 4
all_relations = generate_relations(n_elements)
for relation in all_relations:
    print(relation)
    print("---")
