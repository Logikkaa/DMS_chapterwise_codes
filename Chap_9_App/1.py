x = bool(int(input("Enter value for x (0 or 1): ")))
y = bool(int(input("Enter value for y (0 or 1): ")))

x_or_y = int(x or y)
x_and_y = int(x and y)
x_xor_y = int(x != y)
x_or_y = int(x or y)
x_nor_y = int(not (x or y))

print(f"x + y = {x_or_y}")
print(f"xy = {x_and_y}")
print(f"x ⊕ y = {x_xor_y}")
print(f"x | y = {x_or_y}")
print(f"x ↓ y = {x_nor_y}")
