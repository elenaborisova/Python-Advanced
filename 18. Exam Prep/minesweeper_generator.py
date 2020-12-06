from ast import literal_eval as make_tuple


def is_position_valid(size, r, c):
    return 0 <= r < size and 0 <= c < size


def count_bombs_around(size, row, cell, matrix):
    curr_count = 0
    for r in range(row - 1, row + 2):
        for c in range(cell - 1, cell + 2):
            if is_position_valid(size, r, c) and matrix[r][c] == "*":
                curr_count += 1
    return str(curr_count)


def calculate_number_cells(matrix):
    for row in range(len(matrix)):
        for cell in range(len(matrix)):
            if matrix[row][cell] is None:
                matrix[row][cell] = count_bombs_around(size, row, cell, matrix)
    return matrix


size = int(input())
bombs_count = int(input())
mine_field = [[None for _ in range(size)] for _ in range(size)]

for _ in range(bombs_count):
    bomb_pos = make_tuple(input())
    row, col = bomb_pos[0], bomb_pos[1]
    mine_field[row][col] = "*"


mine_field = calculate_number_cells(mine_field)
[print(" ".join(row)) for row in mine_field]
