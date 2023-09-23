def evaluate_prefix(expression):
    stack = []
    for token in reversed(expression):
        if token.isdigit():
            stack.append(int(token))
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            if token == "+":
                stack.append(operand1 + operand2)
            elif token == "-":
                stack.append(operand1 - operand2)
            elif token == "*":
                stack.append(operand1 * operand2)
            elif token == "/":
                stack.append(operand1 / operand2)
    return stack[0]

# Example usage
prefix_expression = ["+", "*", "5", "3", "4"]
result = evaluate_prefix(prefix_expression)
print(result)
