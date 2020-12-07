def find_position(matrix, size, symbol):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == symbol:
                return row, col


def goes_outside_field(row, col, size):
    return not (0 <= row < size and 0 <= col < size)


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


size = int(input())
commands_count = int(input())
field = [list(input()) for _ in range(size)]
player_pos = find_position(field, size, "f")

DIRECTION_CHANGES = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

for _ in range(commands_count):
    command = input()
    new_row, new_col = get_new_position(player_pos, DIRECTION_CHANGES, command, size)

    if field[new_row][new_col] == "T":
        continue

    if field[new_row][new_col] == "B":
        new_row, new_col = get_new_position([new_row, new_col], DIRECTION_CHANGES, command, size)

    if field[new_row][new_col] == "F":
        field[new_row][new_col] = "f"
        field[player_pos[0]][player_pos[1]] = "-"
        print("Player won!")
        break

    field[player_pos[0]][player_pos[1]] = "-"
    field[new_row][new_col] = "f"
    player_pos = find_position(field, size, "f")

else:
    print("Player lost!")


[print("".join(row)) for row in field]
