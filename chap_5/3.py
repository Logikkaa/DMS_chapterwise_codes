    import random
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def estimate_relative_prime_probability(num_trials):
    relative_prime_count = 0
    for _ in range(num_trials):
        a = random.randint(1, 100000)
        b = random.randint(1, 100000)
        if gcd(a, b) == 1:
            relative_prime_count += 1
    estimated_probability = relative_prime_count / num_trials
    return estimated_probability

num_trials = 100000
estimated_probability = estimate_relative_prime_probability(num_trials)
correct_probability = 6 / math.pi**2  # Probability from the theorem

print(f"Estimated probability of being relatively prime: {estimated_probability:.6f}")
print(f"Correct probability from the theorem: {correct_probability:.6f}")
