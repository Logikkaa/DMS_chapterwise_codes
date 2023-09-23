def is_divisible(num, divisor):
    return num % divisor == 0

def check_divisibility(divisor):
    for n in range(1, 100):
        fib_num = fibonacci_recursive(n)  # You need to implement the Fibonacci function
        if is_divisible(fib_num, divisor):
            print(f"F({n}) = {fib_num} is divisible by {divisor}")

divisor_5 = 5
divisor_7 = 7
divisor_11 = 11

check_divisibility(divisor_5)
check_divisibility(divisor_7)
check_divisibility(divisor_11)
