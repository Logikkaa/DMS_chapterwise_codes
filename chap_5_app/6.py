def matrix_chain_multiplication(matrices):
    n = len(matrices)
    dp = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for chain_length in range(2, n + 1):
        for i in range(n - chain_length + 1):
            j = i + chain_length - 1
            for k in range(i, j):
                cost = matrices[i][0] * matrices[k][1] * matrices[j][1]
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + cost)

    return dp[0][n - 1]

matrices = [(10, 100), (100, 5), (5, 50)]
min_multiplications = matrix_chain_multiplication(matrices)
print(f"Minimum Number of Multiplications: {min_multiplications}")
