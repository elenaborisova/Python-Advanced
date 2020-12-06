def find_position(matrix, size, symbol):
    positions = []
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == symbol:
                positions.append([row, col])
    return positions


def is_position_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def check_for_checkmate(queen_pos, size, matrix):
    for direction in CHANGES:
        q_row, q_col = queen_pos[0], queen_pos[1]
        change_row, change_col = CHANGES[direction][0], CHANGES[direction][1]
        while is_position_valid(q_row + change_row, q_col + change_col, size):
            q_row += change_row
            q_col += change_col
            if matrix[q_row][q_col] == "Q":
                break
            elif matrix[q_row][q_col] == "K":
                return True
    return False


SIZE = 8
board = [input().split() for _ in range(SIZE)]
king_pos = find_position(board, SIZE, "K")[0]
queens_positions = find_position(board, SIZE, "Q")
queens_winners = []

CHANGES = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
    "up-left": (-1, -1),
    "down-left": (1, -1),
    "up-right": (-1, 1),
    "down-right": (1, 1),
}

for queen in queens_positions:
    if check_for_checkmate(queen, SIZE, board):
        queens_winners.append(queen)


if queens_winners:
    [print(queen) for queen in queens_winners]
else:
    print("The king is safe!")
