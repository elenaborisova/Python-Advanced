def get_player_pos(field, size):
    for row in range(size):
        for col in range(size):
            if field[row][col] == "P":
                player_pos = [row, col]
                return player_pos


def check_outside_field_move(row, col, size):
    return 0 <= row < size and 0 <= col < size


def punish_player(text):
    if text:
        text.pop()
    return text


def consume_letter(text, field, row, col):
    if not field[row][col] == "-":
        letter = field[row][col]
        text.append(letter)
    return text


def move_player(player_pos, move_row, move_col, field):
    field[move_row][move_col] = "P"
    field[player_pos[0]][player_pos[1]] = "-"
    return field


def get_move_pos(command, player_pos):
    move_row = player_pos[0]
    move_col = player_pos[1]

    if command == "up":
        move_row -= 1
    elif command == "down":
        move_row += 1
    elif command == "right":
        move_col += 1
    elif command == "left":
        move_col -= 1

    return move_row, move_col


text = list(input())
field_size = int(input())
field = [list(input()) for _ in range(field_size)]
player_pos = get_player_pos(field, field_size)


command = input()
while not command == "end":
    move_row, move_col = get_move_pos(command, player_pos)

    if check_outside_field_move(move_row, move_col, field_size):
        text = consume_letter(text, field, move_row, move_col)
        field = move_player(player_pos, move_row, move_col, field)
        player_pos = get_player_pos(field, field_size)
    else:
        text = punish_player(text)

    command = input()


print("".join(text))
[print("".join(row)) for row in field]