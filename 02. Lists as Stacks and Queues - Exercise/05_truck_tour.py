from collections import deque

n = int(input())
pumps = deque()

for _ in range(n):
    pump = list(map(int, input().split()))
    pumps.append(pump)


original_pumps = pumps.copy()
successful_pumps_sequence = []

while len(successful_pumps_sequence) < n:
    fuel = 0

    for index, pump in enumerate(pumps):
        fuel += pump[0]

        if fuel < pump[1]:
            for _ in range(index + 1):
                pumps.append(pumps.popleft())

            successful_pumps_sequence = []
            break
        else:
            fuel -= pump[1]
            successful_pumps_sequence.append(pump)


print(original_pumps.index(successful_pumps_sequence[0]))
