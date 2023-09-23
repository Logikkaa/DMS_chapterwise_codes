def simulate_placement_and_collision(m, n):
    keys = [0] * m
    for k in range(1, n + 1):
        location = k % m
        if keys[location] == 1:
            return True
        keys[location] = 1
    return False

m = 10
n = 20
collision = simulate_placement_and_collision(m, n)
if collision:
    print("Collision detected.")
else:
    print("No collision detected.")
