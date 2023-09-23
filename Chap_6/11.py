import math

def derangement_probability(n):
    return math.factorial(n) / math.exp(1)

for n in range(1, 21):
    probability = derangement_probability(n)
    print(f"n = {n}: Probability = {probability:.10f}")
