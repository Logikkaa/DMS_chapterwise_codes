def parenthesize_product(variables):
    if len(variables) == 1:
        return [variables]
    results = []
    for i in range(1, len(variables)):
        left = parenthesize_product(variables[:i])
        right = parenthesize_product(variables[i:])
        for l in left:
            for r in right:
                results.append(['('+l[0]+r[0]+')'] + l[1:] + r[1:])
    return results

n = 3  # Number of variables
variable_names = [chr(ord('A') + i) for i in range(n + 1)]
ways_to_parenthesize = parenthesize_product(variable_names[1:])
for way in ways_to_parenthesize:
    print(''.join(way))
