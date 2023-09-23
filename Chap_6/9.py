def sieve_of_eratosthenes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    for num in range(int(limit**0.5) + 1, limit + 1):
        if sieve[num]:
            primes.append(num)
    return primes

limit_primes = 10000
primes_up_to_10000 = sieve_of_eratosthenes(limit_primes)
print("Number of primes not exceeding 10,000:", len(primes_up_to_10000))
