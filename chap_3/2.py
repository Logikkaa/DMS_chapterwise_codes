def generate_expressions(operators, variables, n):
    if n == 1:
        return variables
    
    expressions = []
    for i in range(1, n):
        left_exprs = generate_expressions(operators, variables, i)
        right_exprs = generate_expressions(operators, variables, n - i)
        for left in left_exprs:
            for right in right_exprs:
                for operator in operators:
                    expressions.append(f"({left} {operator} {right})")
    
    return expressions

operators = ['+', '*', '/', '-']
variables = ['x', 'y', 'z']
n = 3  # Maximum number of symbols
expressions = generate_expressions(operators, variables, n)
for expr in expressions:
    print(expr)
