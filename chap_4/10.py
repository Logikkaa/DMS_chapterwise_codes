def list_combinations_with_repetition(n, r, combination=[]):
    if r == 0:
        print(combination)
        return
    for i in range(1, n + 1):
        list_combinations_with_repetition(n, r - 1, combination + [i])

n = 3
r = 2
list_combinations_with_repetition(n, r)
