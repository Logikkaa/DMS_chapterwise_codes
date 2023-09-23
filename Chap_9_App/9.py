def boolean_function(table):
    result = False
    for input_values, output_value in table.items():
        if output_value:
            result |= all(input_values)
    return result

# Example usage
table = {(False, False): False, (False, True): False, (True, False): True, (True, True): False}
result = boolean_function(table)
print(result)
