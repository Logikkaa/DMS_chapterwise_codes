def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)

a = 2
n = 5
result = power(a, n)
print(result)
