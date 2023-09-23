def find_solutions(C, n, current_solution=[]):
    if n == 0:
        if C == 0:
            print(current_solution)
        return
    for x in range(C + 1):
        find_solutions(C - x, n - 1, current_solution + [x])

C = 5
n = 3
find_solutions(C, n)
