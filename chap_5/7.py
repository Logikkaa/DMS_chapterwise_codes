import random

def odd_person_out_simulation(n, p=0.5):
    flips_needed = 0
    while True:
        flips_needed += 1
        heads_count = 0
        for _ in range(n):
            if random.random() < p:
                heads_count += 1
        if heads_count % 2 != 0:
            return flips_needed

for n in range(3, 11):
    total_flips = 0
    trials = 10000
    for _ in range(trials):
        total_flips += odd_person_out_simulation(n)
    avg_flips = total_flips / trials
    print(f"Average flips needed for n = {n}: {avg_flips:.2f}")
