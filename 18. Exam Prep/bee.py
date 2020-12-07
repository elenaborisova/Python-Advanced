def find_position(matrix, size, symbol):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == symbol:
                return row, col


def is_position_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def check_for_flowers(matrix, row, col, flowers):
    if matrix[row][col] == "f":
        flowers += 1
    return flowers


def get_new_position(curr_pos, changes, command):
    new_row = curr_pos[0] + changes[command][0]
    new_col = curr_pos[1] + changes[command][1]
    return new_row, new_col


size = int(input())
territory = [list(input()) for _ in range(size)]
bee_pos = find_position(territory, size, "B")
flowers = 0
DIRECTION_CHANGES = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}


command = input()
while not command == "End":
    new_row, new_col = get_new_position(bee_pos, DIRECTION_CHANGES, command)

    if is_position_valid(new_row, new_col, size):
        flowers = check_for_flowers(territory, new_row, new_col, flowers)

        if territory[new_row][new_col] == "O":
            territory[new_row][new_col] = "."
            new_row, new_col = get_new_position([new_row, new_col], DIRECTION_CHANGES, command)
            flowers = check_for_flowers(territory, new_row, new_col, flowers)

        territory[new_row][new_col] = "B"
        territory[bee_pos[0]][bee_pos[1]] = "."
        bee_pos = find_position(territory, size, "B")

    else:
        territory[bee_pos[0]][bee_pos[1]] = "."
        print("The bee got lost!")
        break

    command = input()


if flowers < 5:
    print(f"The bee couldn't pollinate the flowers, she needs {5 - flowers} flowers more")
else:
    print(f"Great job, the bee managed to pollinate {flowers} flowers!")

[print("".join(row)) for row in territory]
