from collections import deque


def rotate_list(numbers):
    numbers.appendleft(numbers.pop())
    return list(numbers)


def find_pureness(numbers):
    curr_pureness = 0
    for index, digit in enumerate(numbers):
        curr_pureness += index * digit
    return curr_pureness


def best_list_pureness(numbers, k):
    stats = {}
    for rotation in range(k + 1):
        if not rotation == 0:
            numbers = rotate_list(deque(numbers))
        curr_pureness = find_pureness(numbers)
        stats[rotation] = curr_pureness

    best_pureness = max(stats.values())
    for rotation, pureness in stats.items():
        if pureness == best_pureness:
            return f"Best pureness {best_pureness} after {rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
