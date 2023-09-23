def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]

f100 = fibonacci(100)
f500 = fibonacci(500)
f1000 = fibonacci(1000)

print(f"f100 = {f100}")
print(f"f500 = {f500}")
print(f"f1000 = {f1000}")
