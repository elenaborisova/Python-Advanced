from collections import deque


def have_enough_firework_punches(fireworks):
    return all([value >= 3 for value in fireworks.values()])


firework_effects = deque(list(map(int, input().split(', '))))
explosive_power = list(map(int, input().split(', ')))

fireworks = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0,
}

while firework_effects and explosive_power:
    if firework_effects[0] <= 0:
        firework_effects.popleft()
        continue

    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue

    values_sum = firework_effects[0] + explosive_power[-1]

    if values_sum % 3 == 0 and not values_sum % 5 == 0:
        fireworks['Palm Fireworks'] += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif values_sum % 5 == 0 and not values_sum % 3 == 0:
        fireworks['Willow Fireworks'] += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif values_sum % 3 == 0 and values_sum % 5 == 0:
        fireworks['Crossette Fireworks'] += 1
        firework_effects.popleft()
        explosive_power.pop()
    else:
        firework_effects[0] -= 1
        firework_effects.append(firework_effects.popleft())

    if have_enough_firework_punches(fireworks):
        print('Congrats! You made the perfect firework show!')
        break

else:
    print('Sorry. You can’t make the perfect firework show.')


if firework_effects:
    print(f'Firework Effects left: {", ".join(map(str, firework_effects))}')
if explosive_power:
    print(f'Explosive Power left: {", ".join(map(str, explosive_power))}')


for firework, count in fireworks.items():
    print(f'{firework}: {count}')
