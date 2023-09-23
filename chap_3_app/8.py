import time

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    if n <= 1:
        return n
    fib_prev, fib_curr = 0, 1
    for _ in range(2, n + 1):
        fib_prev, fib_curr = fib_curr, fib_prev + fib_curr
    return fib_curr

n = 30  # Adjust the value as needed

start_time = time.time()
result_recursive = fibonacci_recursive(n)
end_time = time.time()
print(f"Recursive Fibonacci({n}) = {result_recursive}")
print("Time taken (recursive):", end_time - start_time, "seconds")

start_time = time.time()
result_iterative = fibonacci_iterative(n)
end_time = time.time()
print(f"Iterative Fibonacci({n}) = {result_iterative}")
print("Time taken (iterative):", end_time - start_time, "seconds")
