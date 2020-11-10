def get_set_elements(n):
    elements = set()
    for _ in range(n):
        element = input()
        elements.add(element)

    return elements


def find_intersection_elements(first_set, second_set):
    return first_set.intersection(second_set)


def print_result(intersection_elements):
    print('\n'.join(intersection_elements))


first_set_length, second_set_length = list(map(int, input().split()))

first_set = get_set_elements(first_set_length)
second_set = get_set_elements(second_set_length)

print_result(find_intersection_elements(first_set, second_set))