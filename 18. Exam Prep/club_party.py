def find_free_hall(halls, char, capacity, overflown_halls):
    for hall, people in halls.items():
        if sum(people) + char <= capacity:
            return hall, overflown_halls
        else:
            overflown_halls.append(hall)
    return None, overflown_halls


def check_hall_overflow(overflown_halls, halls):
    for hall in overflown_halls:
        print(f"{hall} -> {', '.join(map(str, halls[hall]))}")
        halls.pop(hall)
    return []


hall_capacity = int(input())
letters_and_numbers = list(reversed(input().split()))
halls = {}
overflown_halls = []


for char in letters_and_numbers:
    if char.isalpha():
        halls[char] = []
    elif char.isdigit():
        people = int(char)
        hall, overflown_halls = find_free_hall(halls, people, hall_capacity, overflown_halls)
        if hall is not None:
            halls[hall].append(people)

    overflown_halls = check_hall_overflow(overflown_halls, halls)
