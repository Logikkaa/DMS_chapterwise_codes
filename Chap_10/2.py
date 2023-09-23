def generate_boolean_functions(degree):
    functions = []
    for i in range(2**(2**degree)):
        binary_repr = bin(i)[2:].zfill(2**degree)
        functions.append(binary_repr)
    return functions

degree = 3
boolean_functions = generate_boolean_functions(degree)
for idx, function in enumerate(boolean_functions):
    print(f"Function {idx}: {function}")
