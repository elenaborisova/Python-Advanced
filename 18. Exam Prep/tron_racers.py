def find_position(matrix, size, symbol):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == symbol:
                return row, col


def get_new_position(curr_pos, changes, command, size):
    new_row = curr_pos[0] + changes[command][0]
    new_col = curr_pos[1] + changes[command][1]

    if new_row < 0:
        new_row = size - 1
    if new_row >= size:
        new_row = 0
    if new_col < 0:
        new_col = size - 1
    if new_col >= size:
        new_col = 0

    return new_row, new_col


def is_dead(matrix, row, col, symbol):
    if matrix[row][col] == symbol:
        matrix[row][col] = "x"
        return True
    return False


size = int(input())
field = [list(input()) for _ in range(size)]
first_pos = find_position(field, size, "f")
second_pos = find_position(field, size, "s")
DIRECTION_CHANGES = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

while True:
    first_command, second_command = input().split()
    first_row, first_col = get_new_position(first_pos, DIRECTION_CHANGES, first_command, size)
    second_row, second_col = get_new_position(second_pos, DIRECTION_CHANGES, second_command, size)

    if is_dead(field, first_row, first_col, "s"):
        break
    field[first_row][first_col] = "f"
    first_pos = first_row, first_col

    if is_dead(field, second_row, second_col, "f"):
        break
    field[second_row][second_col] = "s"
    second_pos = second_row, second_col


[print("".join(row)) for row in field]
