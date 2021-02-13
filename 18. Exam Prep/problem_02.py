def search_matrix(matrix, size, search):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == search:
                return row, col


def move(command, curr_pos):
    row, col = curr_pos[0], curr_pos[1]

    if command == 'up':
        row -= 1
    elif command == 'down':
        row += 1
    elif command == 'right':
        col += 1
    elif command == 'left':
        col -= 1

    return row, col


def is_inside_field(size, row, col):
    return 0 <= row < size and 0 <= col < size


string = input()
size = int(input())
field = [list(input()) for _ in range(size)]
player_pos = search_matrix(field, size, 'P')


commands_count = int(input())
for _ in range(commands_count):
    command = input()
    new_row, new_col = move(command, player_pos)

    if not is_inside_field(size, new_row, new_col):
        string = string[:-1]
        continue

    if field[new_row][new_col].isalpha():
        string += field[new_row][new_col]

    field[player_pos[0]][player_pos[1]] = '-'
    field[new_row][new_col] = 'P'
    player_pos = search_matrix(field, size, 'P')


print(string)
[print(''.join(row)) for row in field]
