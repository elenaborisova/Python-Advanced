def find_position(matrix, size, symbol):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == symbol:
                return row, col


def is_position_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_new_position(curr_pos, changes, command):
    move_row = curr_pos[0] + changes[command][0]
    move_col = curr_pos[1] + changes[command][1]
    return move_row, move_col


def get_command_input():
    tokens = input().split()
    command = tokens[0]
    row = int(tokens[1])
    col = int(tokens[2])
    return command, row, col


def is_dead(energy, matrix, curr_pos, move_row, move_col):
    if energy <= 0:
        matrix[move_row][move_col] = "X"
        matrix[curr_pos[0]][curr_pos[1]] = "-"
        print(f"Paris died at {move_row};{move_col}")
        return True
    return False


paris_energy = int(input())
size = int(input())
field = [list(input()) for _ in range(size)]

paris_pos = find_position(field, size, "P")
DIRECTION_CHANGES = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}


while True:
    move_command, spawn_row, spawn_col = get_command_input()
    field[spawn_row][spawn_col] = "S"
    move_row, move_col = get_new_position(paris_pos, DIRECTION_CHANGES, move_command)
    paris_energy -= 1

    if not is_position_valid(move_row, move_col, size):
        continue

    if is_dead(paris_energy, field, paris_pos, move_row, move_col):
        break

    if field[move_row][move_col] == "S":
        paris_energy -= 2
        if is_dead(paris_energy, field, paris_pos, move_row, move_col):
            break

    elif field[move_row][move_col] == "H":
        field[move_row][move_col] = "-"
        field[paris_pos[0]][paris_pos[1]] = "-"
        print(f"Paris has successfully abducted Helen! Energy left: {paris_energy}")
        break

    field[move_row][move_col] = "P"
    field[paris_pos[0]][paris_pos[1]] = "-"
    paris_pos = find_position(field, size, "P")


[print("".join(row)) for row in field]
