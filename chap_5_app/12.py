def number_of_onto_functions(m, n):
    return n ** m - (n - 1) ** m

m = 3  # Number of elements in the domain
n = 2  # Number of elements in the codomain
onto_functions = number_of_onto_functions(m, n)
print(f"Number of onto functions: {onto_functions}")
