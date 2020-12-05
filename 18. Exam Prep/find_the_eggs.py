from collections import deque


def get_sublists(sequence, count):
    sublists = [[] for _ in range(count)]

    index = 0
    while sequence:
        curr_element = sequence.popleft()
        sublists[index].append(curr_element)
        index += 1
        if index == len(sublists):
            index = 0

    return sublists


def is_stronger(sublist, middle_egg):
    middle = len(sublist) // 2
    left_eggs = sublist[:middle]
    right_eggs = deque(sublist[middle + 1:])

    if middle_egg > right_eggs.popleft() > left_eggs.pop():
        while left_eggs and right_eggs:
            if not right_eggs.popleft() > left_eggs.pop():
                return False
        return True
    return False


def find_strongest_eggs(sequence, count):
    sequence = deque(sequence)
    sublists = get_sublists(sequence, count)
    strongest_eggs = []

    for sublist in sublists:
        middle_egg = sublist[len(sublist) // 2]
        if is_stronger(sublist, middle_egg):
            strongest_eggs.append(middle_egg)

    return strongest_eggs


test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))

test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))

test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))
