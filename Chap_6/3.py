def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_fibonacci(limit):
    fib = [0, 1]
    primes = []
    i = 2
    while fib[i - 1] <= limit:
        fib_next = fib[i - 1] + fib[i - 2]
        if is_prime(fib_next):
            primes.append(fib_next)
        fib.append(fib_next)
        i += 1
    return primes

limit = 1000000  # Limit for finding prime Fibonacci numbers
prime_fib_numbers = prime_fibonacci(limit)
print("Prime Fibonacci Numbers:", prime_fib_numbers)
