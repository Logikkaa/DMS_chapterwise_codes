def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half_pow = power(a, n // 2)
        return half_pow * half_pow
    else:
        half_pow = power(a, (n - 1) // 2)
        return a * half_pow * half_pow

a = 2.5
n = 6
result = power(a, n)
print(result)
