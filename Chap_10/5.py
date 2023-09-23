def nor(a, b):
    return not (a or b)

def disjunctive_normal_form_nor(expr):
    terms = []
    for a in [False, True]:
        for b in [False, True]:
            for c in [False, True]:
                for d in [False, True]:
                    result = eval(expr)
                    if result:
                        terms.append(f"({a},{b},{c},{d})")
    return ' + '.join(terms)

expressions = ["not (x or y)", "x and not y", "x or y", "x"]
for expr in expressions:
    dnf_nor = disjunctive_normal_form_nor(expr)
    print(f"Expression: {expr}")
    print(f"Disjunctive Normal Form with NOR: {dnf_nor}")
    print(f"Number of NOR operators: {dnf_nor.count('not')}\n")
