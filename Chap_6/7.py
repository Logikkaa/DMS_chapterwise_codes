def fast_integer_multiplication(n):
    if n == 1:
        return 1
    return 3 * fast_integer_multiplication(n // 2) + n

n_bits = [16, 64, 256, 1024]
for n in n_bits:
    operations = fast_integer_multiplication(n)
    print(f"Number of operations for {n}-bit integer multiplication: {operations}")
