def get_santa_pos(neighborhood, size):
    for row in range(size):
        for col in range(size):
            if neighborhood[row][col] == "S":
                santa_pos = [row, col]
                return santa_pos


def get_move_pos(command, santa_pos):
    move_row = santa_pos[0]
    move_col = santa_pos[1]

    if command == "up":
        move_row -= 1
    elif command == "down":
        move_row += 1
    elif command == "right":
        move_col += 1
    elif command == "left":
        move_col -= 1

    return move_row, move_col


def receive_cookies(neighborhood, row, col, presents_count):
    neighborhood[row + 1][col] = "-"
    neighborhood[row - 1][col] = "-"
    neighborhood[row][col + 1] = "-"
    neighborhood[row][col - 1] = "-"
    presents_count -= 4
    return neighborhood, presents_count


def move_santa(neighborhood, row, col, presents_count, happy_kids, santa_pos):
    if neighborhood[row][col] == "V":
        presents_count -= 1
        happy_kids += 1
    elif neighborhood[row][col] == "C":
        neighborhood, presents_count = receive_cookies(neighborhood, row, col, presents_count)

    neighborhood[row][col] = "S"
    neighborhood[santa_pos[0]][santa_pos[1]] = "-"
    return presents_count, neighborhood, happy_kids


def check_presents_count(neighborhood):
    return len([cell for row in neighborhood for cell in row if cell == "V"])


presents = int(input())
size = int(input())
hood = [input().split() for _ in range(size)]
santa_pos = get_santa_pos(hood, size)
happy_kids = 0


command = input()
while not command == "Christmas morning":
    move_row, move_col = get_move_pos(command, santa_pos)
    presents, hood, happy_kids = move_santa(hood, move_row, move_col, presents, happy_kids, santa_pos)
    santa_pos = get_santa_pos(hood, size)

    if presents <= 0:
        print("Santa ran out of presents!")
        break

    command = input()


[print(" ".join(row)) for row in hood]
no_presents_kids = check_presents_count(hood)

if happy_kids and not no_presents_kids:
    print(f"Good job, Santa! {happy_kids} happy nice kid/s.")
elif no_presents_kids:
    print(f"No presents for {no_presents_kids} nice kid/s.")
