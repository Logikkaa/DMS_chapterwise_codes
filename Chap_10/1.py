def count_boolean_functions(degree):
    return 2**(2**degree)

degrees = [7, 8, 9, 10]
for degree in degrees:
    num_functions = count_boolean_functions(degree)
    print(f"Number of Boolean functions of degree {degree}: {num_functions}")
