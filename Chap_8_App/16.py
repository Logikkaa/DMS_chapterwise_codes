def is_safe(board, row, col):
    n = len(board)
    for i in range(row):
        if board[i][col] == 1:
            return False
        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
            return False
        if col + (row - i) < n and board[i][col + (row - i)] == 1:
            return False
    return True

def n_queens_backtracking(n, board, row=0):
    if row == n:
        return [row[:] for row in board]

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            if n_queens_backtracking(n, board, row + 1):
                return [row[:] for row in board]
            board[row][col] = 0

    return None

# Example usage
n = 4
board = [[0] * n for _ in range(n)]
solution = n_queens_backtracking(n, board)
for row in solution:
    print(row)
