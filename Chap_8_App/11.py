def optimal_nim_strategy(piles):
    xor_sum = 0
    for pile in piles:
        xor_sum ^= pile
    if xor_sum == 0:
        return "Second player wins"
    return "First player wins"

# Example usage
piles = [3, 4, 5]
result = optimal_nim_strategy(piles)
print(result)
