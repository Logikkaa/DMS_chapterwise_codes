import random

def simulate_coin_flips(n, p):
    heads_count = 0
    results = []
    for _ in range(n):
        result = generate_bernoulli(p)
        results.append(result)
        heads_count += result
    return results, heads_count

n = 10
p = 0.6
results, heads_count = simulate_coin_flips(n, p)
print("Coin Flip Results:", results)
print("Number of Heads:", heads_count)
