def find_chair_combinations(names, count, combination=[]):
    if len(combination) == count:
        print(', '.join(combination))
        return

    for i in range(len(names)):
        name = names[i]
        combination.append(name)
        find_chair_combinations(names[i + 1:], count, combination)
        combination.pop()


names = input().split(', ')
chairs_count = int(input())
find_chair_combinations(names, chairs_count)