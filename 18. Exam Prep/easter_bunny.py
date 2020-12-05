from sys import maxsize


def find_pos(matrix, symbol):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == symbol:
                return row, col


def is_inside_field(row, col, matrix):
    return 0 <= row < size and 0 <= col < size and not matrix[row][col] == "X"


def find_max_eggs(directions_stats):
    max_eggs = -maxsize
    best_dir = ""
    best_steps = []
    for dir, values in directions_stats.items():
        if values["eggs"] > max_eggs:
            max_eggs = values["eggs"]
            best_dir = dir
            best_steps = values["steps"]
    return max_eggs, best_dir, best_steps


def move(matrix, curr_pos, direction_changes, directions_stats):
    for direction, change in direction_changes.items():
        row, col = curr_pos[0] + change[0], curr_pos[1] + change[1]

        if not is_inside_field(row, col, matrix):
            directions_stats[direction]["eggs"] = -maxsize

        while is_inside_field(row, col, matrix):
            directions_stats[direction]["eggs"] += int(matrix[row][col])
            directions_stats[direction]["steps"].append([row, col])
            row += change[0]
            col += change[1]


size = int(input())
field = [input().split() for _ in range(size)]

directions_stats = {
    "up": {"eggs": 0, "steps": []},
    "down": {"eggs": 0, "steps": []},
    "right": {"eggs": 0, "steps": []},
    "left": {"eggs": 0, "steps": []}
}

DIRECTION_CHANGES = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

bunny_pos = find_pos(field, "B")
move(field, bunny_pos, DIRECTION_CHANGES, directions_stats)
max_eggs, best_direction, best_steps = find_max_eggs(directions_stats)

print(best_direction)
[print(row) for row in best_steps]
print(max_eggs)
