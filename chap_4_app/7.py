import random

def simulate_card_collection(m):
    collected_cards = set()
    products_purchased = 0
    while len(collected_cards) < m:
        random_card = random.randint(1, m)
        collected_cards.add(random_card)
        products_purchased += 1
    return products_purchased

m = 10
trials = 1000
total_products_purchased = 0
for _ in range(trials):
    products_purchased = simulate_card_collection(m)
    total_products_purchased += products_purchased
average_purchases = total_products_purchased / trials
print("Average Products Purchased to Obtain a Full Set:", average_purchases)
