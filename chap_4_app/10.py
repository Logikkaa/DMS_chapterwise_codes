import random

def monty_hall_simulation(trials):
    stay_wins = 0
    switch_wins = 0
    doors = [0, 0, 1]  # 1 represents the car, 0 represents a goat

    for _ in range(trials):
        random.shuffle(doors)
        chosen_door = random.randint(0, 2)
        
        if doors[chosen_door] == 1:
            stay_wins += 1
        else:
            switch_wins += 1
    
    stay_probability = stay_wins / trials
    switch_probability = switch_wins / trials
    return stay_probability, switch_probability

trials = 10000
stay_prob, switch_prob = monty_hall_simulation(trials)
print(f"Probability of winning by staying: {stay_prob:.4f}")
print(f"Probability of winning by switching: {switch_prob:.4f}")
