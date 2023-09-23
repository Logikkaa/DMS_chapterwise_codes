def solve_recurrence_iteration(c1, c2, a0, a1, k):
    if k == 0:
        return a0
    if k == 1:
        return a1
    a_k_minus_1 = a1
    a_k_minus_2 = a0
    for i in range(2, k + 1):
        a_k = c1 * a_k_minus_1 + c2 * a_k_minus_2
        a_k_minus_2, a_k_minus_1 = a_k_minus_1, a_k
    return a_k

c1 = 2
c2 = 3
a0 = 1
a1 = 2
k = 5
ak = solve_recurrence_iteration(c1, c2, a0, a1, k)
print(f"a_{k} = {ak}")
