from collections import deque


def perform_calculation(nums, operator):
    result = nums[0]
    nums = nums[1:]

    for num in nums:
        if operator == "+":
            result += num
        elif operator == "-":
            result -= num
        elif operator == "*":
            result *= num
        elif operator == "/":
            result //= num

    return result


expression = deque(input().split())
OPERATIONS = ("*", "/", "+", "-")
waiting_list = []
result = 0

while expression:
    char = expression.popleft()
    if char in OPERATIONS:
        result = perform_calculation(waiting_list, char)
        expression.appendleft(result)
        waiting_list.clear()
    else:
        waiting_list.append(int(char))

print(result)
