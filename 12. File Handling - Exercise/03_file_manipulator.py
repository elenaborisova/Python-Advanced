from os.path import exists
from os import remove


def create_new_file(file_name):
    with open(file_name, "w") as new_file:
        new_file.write("")


def add_content_to_file(file_name, content):
    with open(file_name, "a") as file:
        file.write(f"{content}\n")


def change_content(file_name, old_string, new_string):
    with open(file_name, "r") as file:
        content = file.read()
        new_content = content.replace(old_string, new_string)
        return new_content


def replace_old_with_new_string(file_name, old_string, new_string):
    if exists(file_name):
        new_content = change_content(file_name, old_string, new_string)
        with open(file_name, "w") as file:
            file.write(new_content)
    else:
        print("An error occurred")


def delete_file(file_name):
    if exists(file_name):
        remove(file_name)
    else:
        print("An error occurred")


line = input()
while not line == "End":
    tokens = line.split("-")
    command = tokens[0]
    file_name = tokens[1]

    if command == "Create":
        create_new_file(file_name)

    elif command == "Add":
        content = tokens[2]
        add_content_to_file(file_name, content)

    elif command == "Replace":
        old_string = tokens[2]
        new_string = tokens[3]
        replace_old_with_new_string(file_name, old_string, new_string)

    elif command == "Delete":
        delete_file(file_name)

    line = input()
