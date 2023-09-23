def spanning_tree_count(n):
    return n ** (n - 2)

n_values = [1, 2, 3, 4, 5, 6]
for n in n_values:
    count = spanning_tree_count(n)
    print(f"Number of spanning trees in K{n}: {count}")
