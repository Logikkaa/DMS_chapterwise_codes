def is_safe(board, row, col, n):
    # Check if a queen can be placed in the given position
    # Implementation

def solve_n_queens_util(board, col, n):
    # Implementation

def solve_n_queens(n):
    # Implementation

n_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in n_values:
    count = solve_n_queens(n)
    print(f"Number of solutions for {n} queens: {count}")
