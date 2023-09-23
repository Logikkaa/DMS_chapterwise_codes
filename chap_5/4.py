def birthday_collision_probability(desired_probability):
    probability = 1.0
    people = 0
    while probability > (1 - desired_probability):
        probability *= (365 - people) / 365
        people += 1
    return people

desired_probabilities = [0.7, 0.8, 0.9, 0.95, 0.98, 0.99]

for prob in desired_probabilities:
    people_needed = birthday_collision_probability(prob)
    print(f"Number of people needed for {prob:.2%} probability: {people_needed}")
