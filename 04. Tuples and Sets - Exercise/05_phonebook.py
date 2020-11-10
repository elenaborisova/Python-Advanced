def get_phonebook_info():
    phonebook = {}

    entry = input()
    while not entry.isdigit():
        name, number = entry.split("-")
        phonebook[name] = number

        entry = input()

    n = int(entry)

    return phonebook, n


def search_phonebook_contacts(phonebook, n):
    for _ in range(n):
        name = input()
        if name in phonebook:
            print(f"{name} -> {phonebook[name]}")
        else:
            print(f"Contact {name} does not exist.")


phonebook, n = get_phonebook_info()
search_phonebook_contacts(phonebook, n)
