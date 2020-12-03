from collections import deque


def craft_toy(toy_magic_value, crafted_toys):
    if toy_magic_value == 150:
        crafted_toys["Doll"] += 1
    elif toy_magic_value == 250:
        crafted_toys["Wooden train"] += 1
    elif toy_magic_value == 300:
        crafted_toys["Teddy bear"] += 1
    elif toy_magic_value == 400:
        crafted_toys["Bicycle"] += 1
    return crafted_toys


def check_pairs(crafted_toys):
    if crafted_toys["Doll"] and crafted_toys["Wooden train"]:
        return True
    elif crafted_toys["Teddy bear"] and crafted_toys["Bicycle"]:
        return True
    return False


def print_message(crafted_toys):
    if check_pairs(crafted_toys):
        print("The presents are crafted! Merry Christmas!")
    else:
        print("No presents this Christmas!")


def print_materials(materials, materials_magic_levels):
    if materials:
        print(f"Materials left: {', '.join(list(map(str, materials)))}")
    if materials_magic_levels:
        print(f"Magic left: {', '.join(list(map(str, materials_magic_levels)))}")


def print_toys(crafted_toys):
    for toy, count in sorted(crafted_toys.items()):
        if count:
            print(f"{toy}: {count}")


materials = list(map(int, input().split()))
materials_magic_levels = deque(list(map(int, input().split())))
magic_needed = (150, 250, 300, 400)
crafted_toys = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}

while materials and materials_magic_levels:
    toy_magic_value = materials[-1] * materials_magic_levels[0]

    if toy_magic_value in magic_needed:
        crafted_toys = craft_toy(toy_magic_value, crafted_toys)
        materials.pop()
        materials_magic_levels.popleft()

    elif toy_magic_value < 0:
        result = materials[-1] + materials_magic_levels[0]
        materials.pop()
        materials_magic_levels.popleft()
        materials.append(result)

    elif toy_magic_value > 0:
        materials_magic_levels.popleft()
        materials[-1] += 15

    else:
        if materials[-1] == 0:
            materials.pop()
        if materials_magic_levels[0] == 0:
            materials_magic_levels.popleft()


print_message(crafted_toys)
print_materials(materials, materials_magic_levels)
print_toys(crafted_toys)
