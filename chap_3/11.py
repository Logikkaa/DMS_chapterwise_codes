def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    fib_prev, fib_curr = 0, 1
    for _ in range(2, n + 1):
        fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
    return fib_curr

n = 10
result = fibonacci_iterative(n)
print(result)
