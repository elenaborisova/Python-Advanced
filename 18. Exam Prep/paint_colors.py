from collections import deque


def check_secondary_colors(all_colors, combinations):
    for i in range(len(all_colors) - 1, -1, -1):
        color = all_colors[i]
        if color in combinations and not all([main_color in all_colors for main_color in combinations[color]]):
            all_colors.remove(color)
    return all_colors


text = deque(input().split())

MAIN_COLORS = ("red", "yellow", "blue")
SECONDARY_COLORS = {"orange": ("red", "yellow"),
                    "purple": ("red", "blue"),
                    "green": ("yellow", "blue")
                    }

made_colors = []

while text:
    first_substring = text.popleft()
    last_substring = ""
    if text:
        last_substring = text.pop()

    first_comb = first_substring + last_substring
    second_comb = last_substring + first_substring

    if first_comb in MAIN_COLORS or first_comb in SECONDARY_COLORS:
        made_colors.append(first_comb)
    elif second_comb in MAIN_COLORS or second_comb in SECONDARY_COLORS:
        made_colors.append(second_comb)
    else:
        if len(first_substring) > 1:
            text.insert(len(text) // 2, first_substring[:-1])
        if len(last_substring) > 1:
            text.insert(len(text) // 2, last_substring[:-1])


made_colors = check_secondary_colors(made_colors, SECONDARY_COLORS)
print(made_colors)
