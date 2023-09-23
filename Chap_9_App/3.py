n = int(input("Enter the number of variables: "))
values = [int(x) for x in input(f"Enter {2 ** n} function values separated by spaces: ").split()]

def int_to_bool(x):
    return bool(x)

function_values = list(map(int_to_bool, values))

def sum_of_products(values):
    sop = []
    for i, val in enumerate(values):
        if val:
            binary = format(i, f'0{n}b')
            product_terms = [f"x_{j}" if bit == '1' else f"~x_{j}" for j, bit in enumerate(binary)]
            sop.append(" ∧ ".join(product_terms))
    return " ∨ ".join(sop)

expression = sum_of_products(function_values)
print(f"Sum-of-Products Expression: {expression}")
