import random

def generate_bernoulli(p):
    return 1 if random.random() < p else 0

p = 0.3
random_number = generate_bernoulli(p)
print(random_number)
