def search_matrix(matrix, size, search):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == search:
                return row, col


def get_new_pos(command, curr_pos):
    new_row, new_col = curr_pos[0], curr_pos[1]
    if command == "up":
        new_row -= 1
    elif command == "down":
        new_row += 1
    elif command == "right":
        new_col += 1
    elif command == "left":
        new_col -= 1
    return new_row, new_col


def is_inside_territory(row, col, size):
    return 0 <= row < size and 0 <= col < size


def print_result(food_quantity, matrix):
    print(f"Food eaten: {food_quantity}")
    [print("".join(row)) for row in matrix]


size = int(input())
territory = [list(input()) for _ in range(size)]
snake_pos = search_matrix(territory, size, "S")
food_quantity = 0


while food_quantity < 10:
    command = input()
    new_row, new_col = get_new_pos(command, snake_pos)

    if not is_inside_territory(new_row, new_col, size):
        territory[snake_pos[0]][snake_pos[1]] = "."
        print("Game over!")
        break

    elif territory[new_row][new_col] == "*":
        food_quantity += 1

    elif territory[new_row][new_col] == "B":
        territory[new_row][new_col] = "."
        new_row, new_col = search_matrix(territory, size, "B")

    territory[new_row][new_col] = "S"
    territory[snake_pos[0]][snake_pos[1]] = "."
    snake_pos = search_matrix(territory, size, "S")

else:
    print("You won! You fed the snake.")

print_result(food_quantity, territory)
