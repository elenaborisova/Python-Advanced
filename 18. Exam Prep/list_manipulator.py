def list_manipulator(numbers_list, operation, position, *args):
    numbers = list(args)

    if operation == "add" and position == "beginning":
        numbers_list = numbers + numbers_list

    elif operation == "add" and position == "end":
        numbers_list.extend(numbers)

    elif operation == "remove" and position == "beginning":
        if numbers:
            nums_to_remove = args[0]
            numbers_list = numbers_list[nums_to_remove:]
        else:
            numbers_list.pop(0)

    elif operation == "remove" and position == "end":
        if numbers:
            nums_to_remove = args[0]
            numbers_list = numbers_list[:len(numbers_list) - nums_to_remove]
        else:
            numbers_list.pop()

    return numbers_list


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
