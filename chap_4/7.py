def list_permutations_recursive(n, r, permutation=[]):
    if r == 0:
        print(permutation)
        return
    for i in range(1, n + 1):
        if i not in permutation:
            list_permutations_recursive(n, r - 1, permutation + [i])

n = 5
r = 3
list_permutations_recursive(n, r)
