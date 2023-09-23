n = int(input("Enter the number of variables: "))
values = [int(x) for x in input(f"Enter {2 ** n} function values separated by spaces: ").split()]

def int_to_bool(x):
    return bool(x)

function_values = list(map(int_to_bool, values))

def expression(values):
    expression = []
    for i, val in enumerate(values):
        if val:
            binary = format(i, f'0{n}b')
            sum_terms = [f"x_{j}" if bit == '1' else f"~x_{j}" for j, bit in enumerate(binary)]
            expression.append(" + ".join(sum_terms))
    return " + ".join(expression)

expression = expression(function_values)
print(f"Boolean Expression: {expression}")
