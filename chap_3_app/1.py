import math

n_less_than_100 = None
n_less_than_1000 = None

for n in range(1, 1000):
    factorial = math.factorial(n)
    num_digits = len(str(factorial))
    
    if num_digits < 100:
        n_less_than_100 = n
    if num_digits < 1000:
        n_less_than_1000 = n
    else:
        break

print("Largest n for fewer than 100 decimal digits:", n_less_than_100)
print("Largest n for fewer than 1000 decimal digits:", n_less_than_1000)
