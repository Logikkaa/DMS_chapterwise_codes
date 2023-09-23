import math

def lottery_probability(n):
    total_outcomes = math.comb(n, 6)
    favorable_outcomes = 1  # Since there's only one way to select the six numbers
    probability = favorable_outcomes / total_outcomes
    return probability

n = 49  # Assuming you're selecting from a set of 1 to 49
probability = lottery_probability(n)
print(f"Probability of selecting the six numbers: {probability:.10f}")
