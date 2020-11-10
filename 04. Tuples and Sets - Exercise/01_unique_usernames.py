def get_unique_usernames(n):
    unique_usernames = {input() for _ in range(n)}
    return unique_usernames


def print_result(unique_usernames):
    [print(username) for username in unique_usernames]


print_result(get_unique_usernames(int(input())))