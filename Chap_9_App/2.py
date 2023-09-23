def bool_func_values(n):
    values = []
    for i in range(2 ** n):
        values.append(format(i, f'0{n}b'))
    return values

boolean_functions = bool_func_values(8)

for i, func in enumerate(boolean_functions):
    print(f"Function {i}: {func}")
