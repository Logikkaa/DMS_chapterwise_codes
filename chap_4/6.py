def list_combinations_recursive(n, r, combination=[]):
    if r == 0:
        print(combination)
        return
    for i in range(1, n + 1):
        if not combination or i > combination[-1]:
            list_combinations_recursive(n, r - 1, combination + [i])

n = 5
r = 3
list_combinations_recursive(n, r)
