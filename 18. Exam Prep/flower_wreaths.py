from collections import deque

lilies = list(map(int, input().split(", ")))
roses = deque(list(map(int, input().split(", "))))
stored_values = 0
wreaths = 0

while lilies and roses:
    values_sum = lilies[-1] + roses[0]

    if values_sum == 15:
        wreaths += 1
        lilies.pop()
        roses.popleft()
    elif values_sum > 15:
        lilies[-1] -= 2
    else:
        stored_values += values_sum
        lilies.pop()
        roses.popleft()

wreaths += stored_values // 15

if wreaths >= 5:
    print(f"You made it, you are going to the competition with {wreaths} wreaths!")
else:
    print(f"You didn't make it, you need {5 - wreaths} wreaths more!")
