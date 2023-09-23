import random

def minimize_using_qm(expression):
    # Implement the Quine–McCluskey algorithm here
    # Return the minimized expression and the number of steps

def generate_random_expression(variables):
    num_terms = random.randint(1, len(variables) * 2)  # Generate 1 to 2n terms
    terms = []
    for _ in range(num_terms):
        term = random.choice(variables)
        if random.random() < 0.5:
            term = f"not {term}"
        terms.append(term)
    return " and ".join(terms)

num_expressions = 10
variables = ["x", "y", "z", "w", "u"]
total_steps = 0

for _ in range(num_expressions):
    random_expr = generate_random_expression(variables)
    minimized_expr, steps = minimize_using_qm(random_expr)
    total_steps += steps
    print(f"Random Expression: {random_expr}")
    print(f"Minimized Expression: {minimized_expr}")
    print(f"Steps required: {steps}\n")

average_steps = total_steps / num_expressions
print(f"Average steps required: {average_steps}")
