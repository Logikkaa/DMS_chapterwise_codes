def list_permutations_with_repetition(n, r, permutation=[]):
    if r == 0:
        print(permutation)
        return
    for i in range(1, n + 1):
        list_permutations_with_repetition(n, r - 1, permutation + [i])

n = 3
r = 2
list_permutations_with_repetition(n, r)
