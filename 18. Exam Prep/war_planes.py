def search_matrix(matrix, search_element):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == search_element:
                return row, col


def get_new_position(direction, step, curr_pos):
    DIRECTION_CHANGES = {
        "up": (-step, 0),
        "down": (step, 0),
        "right": (0, step),
        "left": (0, -step),
    }

    change = DIRECTION_CHANGES[direction]
    new_row = curr_pos[0] + change[0]
    new_col = curr_pos[1] + change[1]
    return new_row, new_col


def count_targets(matrix):
    return len([cell for row in matrix for cell in row if cell == "t"])


def is_inside_field(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = int(input())
field = [input().split() for _ in range(size)]
commands_count = int(input())

plane_pos = search_matrix(field, "p")
targets_shot = 0

for _ in range(commands_count):
    command, direction, step = input().split()
    step = int(step)
    new_row, new_col = get_new_position(direction, step, plane_pos)

    if not is_inside_field(new_row, new_col, size):
        continue

    elif command == "move":
        if field[new_row][new_col] == ".":
            field[new_row][new_col] = "p"
            field[plane_pos[0]][plane_pos[1]] = "."
        plane_pos = search_matrix(field, "p")

    elif command == "shoot":
        if field[new_row][new_col] == "t":
            targets_shot += 1
        field[new_row][new_col] = "x"

    if not count_targets(field):
        print(f"Mission accomplished! All {targets_shot} targets destroyed.")
        break

else:
    print(f"Mission failed! {count_targets(field)} targets left.")


[print(" ".join(row)) for row in field]
