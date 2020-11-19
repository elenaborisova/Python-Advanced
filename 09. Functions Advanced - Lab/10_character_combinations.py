def get_combinations(chars, index):
    if index >= len(chars):
        print(''.join(chars))
        return

    get_combinations(chars, index + 1)

    for i in range(index + 1, len(chars)):
        chars[index], chars[i] = chars[i], chars[index]
        get_combinations(chars, index + 1)
        chars[index], chars[i] = chars[i], chars[index]


chars = list(input())
get_combinations(chars, 0)