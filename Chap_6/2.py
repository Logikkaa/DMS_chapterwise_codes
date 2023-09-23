def smallest_fibonacci_above(n):
    fib = [0, 1]
    i = 2
    while fib[i - 1] <= n:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    return fib[i - 1]

n1 = 1000000
n2 = 1000000000
n3 = 1000000000000

fib_above_n1 = smallest_fibonacci_above(n1)
fib_above_n2 = smallest_fibonacci_above(n2)
fib_above_n3 = smallest_fibonacci_above(n3)

print(f"Smallest Fibonacci above {n1}: {fib_above_n1}")
print(f"Smallest Fibonacci above {n2}: {fib_above_n2}")
print(f"Smallest Fibonacci above {n3}: {fib_above_n3}")
