def operate(operator, *args):
    first_num = args[0]

    def get_initial_value(operator, first_num):
        if operator == "+":
            return 0
        elif operator == "*":
            return 1
        else:
            return first_num

    result = get_initial_value(operator, first_num)

    for num in args:
        if operator == "+":
            result += num
        elif operator == "-" and not num == first_num:
            result -= num
        elif operator == "*":
            result *= num
        elif operator == "/" and not num == first_num:
            result /= num

    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))