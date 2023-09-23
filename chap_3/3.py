def generate_propositions(symbols, n):
    if n == 1:
        return symbols
    
    propositions = []
    for i in range(1, n):
        left_props = generate_propositions(symbols, i)
        right_props = generate_propositions(symbols, n - i)
        for left in left_props:
            for right in right_props:
                for operator in ['¬', '∨', '∧', '→', '↔']:
                    propositions.append(f"({operator} {left} {right})")
    
    return propositions

symbols = ['T', 'F', 'p', 'q']
n = 3  # Maximum number of symbols
propositions = generate_propositions(symbols, n)
for prop in propositions:
    print(prop)
