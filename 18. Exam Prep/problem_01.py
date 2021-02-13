from collections import deque

males = list(map(int, input().split()))
females = deque(list(map(int, input().split())))
matches = 0


while males and females:
    if females[0] <= 0:
        females.popleft()
        continue
    if males[-1] <= 0:
        males.pop()
        continue
    if females[0] % 25 == 0:
        females.popleft()
        females.popleft()
        continue
    if males[-1] % 25 == 0:
        males.pop()
        males.pop()
        continue

    if females[0] == males[-1]:
        matches += 1
        females.popleft()
        males.pop()
    else:
        females.popleft()
        males[-1] -= 2


print(f'Matches: {matches}')
print(f'Males left: {"none" if not males else ", ".join(map(str, reversed(males)))}')
print(f'Females left: {"none" if not females else ", ".join(map(str, females))}')

