def solve_recurrence_unique(c1, c2, a0, a1, n):
    # Solving the Fibonacci recurrence relation
    fib = [a0, a1]
    for i in range(2, n + 1):
        fib_next = c1 * fib[i - 1] + c2 * fib[i - 2]
        fib.append(fib_next)
    return fib[n]

c1 = 1
c2 = 1
a0 = 0
a1 = 1
n = 5
result = solve_recurrence_unique(c1, c2, a0, a1, n)
print(f"The {n}-th term of the sequence is: {result}")
