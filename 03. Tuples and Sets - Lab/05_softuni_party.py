def input_to_list(guests_count):
    return [input() for _ in range(guests_count)]


def input_to_list_until_command(command):
    result = []

    line = input()
    while not line == command:
        result.append(line)
        line = input()

    return result


def get_not_arrived_guests(guests, guests_arrived):
    return set(guests) - set(guests_arrived)


def print_result(result):
    result = sorted(result)
    print(len(result))
    [print(guest) for guest in result if guest[0].isdigit()]
    [print(guest) for guest in result if not guest[0].isdigit()]


guests = input_to_list(int(input()))
guests_arrived = input_to_list_until_command("END")

print_result(
    get_not_arrived_guests(guests, guests_arrived)
)
