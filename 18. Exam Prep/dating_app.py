from collections import deque

males = list(map(int, input().split()))
females = deque(list(map(int, input().split())))
matches_count = 0


while males and females:
    male = males[-1]
    female = females[0]

    if male <= 0:
        males.pop()

    elif female <= 0:
        females.popleft()

    elif female % 25 == 0:
        females.popleft()
        if females:
            females.popleft()

    elif male % 25 == 0:
        males.pop()
        if males:
            males.pop()

    elif male == female:
        males.pop()
        females.popleft()
        matches_count += 1

    else:
        females.popleft()
        males[-1] -= 2


print(f"Matches: {matches_count}")
print(f"Males left: {'none' if not males else ', '.join(map(str, males))}")
print(f"Females left: {'none' if not females else ', '.join(map(str, females))}")
