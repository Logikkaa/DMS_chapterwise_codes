import random

def correct_hat_returns_simulation(n):
    people = list(range(n))
    hats = people.copy()
    random.shuffle(hats)
    correct_count = sum([people[i] == hats[i] for i in range(n)])
    return correct_count

n = 10
trials = 10000
total_correct = 0
for _ in range(trials):
    total_correct += correct_hat_returns_simulation(n)
average_correct = total_correct / trials
print(f"Average number of correct hat returns for {n} people: {average_correct:.2f}")
