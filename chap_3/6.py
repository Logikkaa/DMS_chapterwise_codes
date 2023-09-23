def square_power(a, n):
    if n == 0:
        return 1
    return power(a, 2) * square_power(a, n - 1)

a = 3
n = 4
result = square_power(a, n)
print(result)
