def nand(a, b):
    return not (a and b)

def disjunctive_normal_form(expr):
    terms = []
    for a in [False, True]:
        for b in [False, True]:
            for c in [False, True]:
                result = eval(expr)
                if result:
                    terms.append(f"({a},{b},{c})")
    return ' + '.join(terms)

expressions = ["not (x and y)", "x or y", "x and not y", "x"]
for expr in expressions:
    dnf = disjunctive_normal_form(expr)
    print(f"Expression: {expr}")
    print(f"Disjunctive Normal Form: {dnf}")
    print(f"Number of NAND operators: {dnf.count('not')}\n")
