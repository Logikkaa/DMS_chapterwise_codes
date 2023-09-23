def fast_matrix_multiplication(n):
    if n == 1:
        return 1
    return 2 * fast_matrix_multiplication(n // 2) + n ** 2

n_matrices = [4, 16, 64, 128]
for n in n_matrices:
    operations = fast_matrix_multiplication(n)
    print(f"Number of operations for {n}x{n} matrix multiplication: {operations}")
