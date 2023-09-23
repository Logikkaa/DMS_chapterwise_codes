def solve_recurrence_iteration(a, b, c, k):
    f = c
    for _ in range(k):
        f = a * f / b + c
    return f

a = 2
b = 3
c = 1
k = 3
f_bk = solve_recurrence_iteration(a, b, c, k)
print(f"f({b*k}) = {f_bk}")
