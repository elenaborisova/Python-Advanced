def fix_calendar(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

    # min_num = 10000
    # sorted_count = 0
    #
    # while sorted_count < len(numbers):
    #     for num in numbers[:len(numbers) - sorted_count]:
    #         if num < min_num:
    #             min_num = num
    #     numbers.remove(min_num)
    #     numbers.append(min_num)
    #     min_num = 10000
    #     sorted_count += 1
    #
    # return numbers

numbers = [3, 2, 1, 7, 5, 9]
fixed = fix_calendar(numbers)
print(fixed)