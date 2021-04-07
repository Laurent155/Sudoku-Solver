from client import *


def solve_sudoku(board):
    solve_partial_sudoku(0, 0, board)
    return board


def solve_partial_sudoku(row, col, board):
    current_row = row
    current_col = col
    if current_col == 9:
        current_row += 1
        current_col = 0
        if current_row == 9:
            return board

    if board[current_row][current_col] == 0:
        return try_digits_at_position(current_row, current_col, board)

    return solve_partial_sudoku(current_row, current_col + 1, board)


def try_digits_at_position(row, col, board):
    for i in range(1, 10):
        if is_valid_at_position(i, row, col, board):
            board[row][col] = i
            update_window(win, board, row, col)
            pygame.time.wait(200)
            if solve_partial_sudoku(row, col + 1, board):
                return True
        else:
            pass
            update_window_false(win, board, row, col, i)
            pygame.time.wait(150)
    board[row][col] = 0
    return False


def is_valid_at_position(value, row, col, board):
    row_is_valid = value not in board[row]
    column_is_valid = value not in map(lambda r: r[col], board)

    if not row_is_valid or not column_is_valid:
        return False

    subgrid_row_start = (row // 3) * 3
    subgrid_col_start = (col // 3) * 3
    for row_idx in range(3):
        for col_idx in range(3):
            row_to_check = subgrid_row_start + row_idx
            col_to_check = subgrid_col_start + col_idx
            existing_value = board[row_to_check][col_to_check]

            if existing_value == value:
                return False
    return True


actual_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]]


def main():
    run = True

    # solve_sudoku(actual_board)
    # update_window(win, actual_board, -1, -1)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                complete_window(win)
        solve_sudoku(actual_board)
        update_window(win, actual_board, -1, -1)

main()
