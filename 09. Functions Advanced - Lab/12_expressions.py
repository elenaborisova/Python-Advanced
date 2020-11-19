def get_expression(numbers, curr_result, expression=''):
    if not numbers:
        return [(expression, curr_result)]

    result_plus = get_expression(
        numbers[1:],
        curr_result + numbers[0],
        f'{expression}+{numbers[0]}'
    )

    result_minus = get_expression(
        numbers[1:],
        curr_result - numbers[0],
        f'{expression}-{numbers[0]}'
    )

    return result_plus + result_minus


numbers = list(map(int, input().split(", ")))

result = get_expression(numbers, 0)
[print(f'{expr_str}={expr_result}') for (expr_str, expr_result) in result]