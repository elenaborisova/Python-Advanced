from math import floor


def search_matrix(matrix, size, search):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == search:
                return row, col


def find_new_pos(curr_pos, command, DIRECTIONS):
    curr_row, curr_col = curr_pos[0], curr_pos[1]

    if command == 'up':
        curr_row += DIRECTIONS['up'][0]
        curr_col += DIRECTIONS['up'][1]

    elif command == 'down':
        curr_row += DIRECTIONS['down'][0]
        curr_col += DIRECTIONS['down'][1]

    elif command == 'right':
        curr_row += DIRECTIONS['right'][0]
        curr_col += DIRECTIONS['right'][1]

    elif command == 'left':
        curr_row += DIRECTIONS['left'][0]
        curr_col += DIRECTIONS['left'][1]

    return curr_row, curr_col


def is_new_pos_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = int(input())
field = [input().split() for _ in range(size)]
player_pos = search_matrix(field, size, 'P')
player_path = []
coins = 0


DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}


while True:
    command = input()

    if command not in DIRECTIONS:
        continue

    new_row, new_col = find_new_pos(player_pos, command, DIRECTIONS)
    if not is_new_pos_valid(new_row, new_col, size) or field[new_row][new_col] == 'X':
        coins = floor(coins * 0.5)
        print(f'Game over! You\'ve collected {coins} coins.')
        break

    coins += int(field[new_row][new_col])
    player_path.append([new_row, new_col])
    player_pos = [new_row, new_col]

    if coins >= 100:
        print(f'You won! You\'ve collected {coins} coins.')
        break


print('Your path:')
[print(row) for row in player_path]
