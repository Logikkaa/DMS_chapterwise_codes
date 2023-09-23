def tile_checkerboard(board, size, missing_row, missing_col):
    if size == 2:
        # Base case: place right triominoes on the remaining squares
        return place_triominoes(board, missing_row, missing_col)
    
    new_size = size // 2
    tile_checkerboard(board, new_size, missing_row, missing_col)
    tile_checkerboard(board, new_size, missing_row, missing_col + new_size)
    tile_checkerboard(board, new_size, missing_row + new_size, missing_col)
    tile_checkerboard(board, new_size, missing_row + new_size, missing_col + new_size)

def place_triominoes(board, row, col):
    triomino_number = 1
    for r in range(row, row + 2):
        for c in range(col, col + 2):
            if (r, c) != (row + 1, col + 1):
                board[r][c] = triomino_number
            triomino_number += 1

n = 4  # Board size is 2^n x 2^n
missing_row, missing_col = 2, 1  # Coordinates of the missing square
board = [[0] * (2 ** n) for _ in range(2 ** n)]
tile_checkerboard(board, 2 ** n, missing_row, missing_col)
for row in board:
    print(row)
