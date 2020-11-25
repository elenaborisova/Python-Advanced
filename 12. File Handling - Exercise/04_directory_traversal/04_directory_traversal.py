from os import walk, environ
from os.path import splitext, sep, join
from collections import defaultdict


def get_all_files(directory_path):
    all_files = []
    all_separators_count = directory_path.count(sep)

    for root, dirs, files in walk(directory_path):
        if all_separators_count - root.count(sep) > 1:
            continue
        all_files.extend(files)

    return all_files


def get_file_extension(file):
    file_extension = splitext(file)[-1]
    return file_extension


def group_files(all_files):
    extensions_and_files = defaultdict(list)

    for file in all_files:
        file_extension = get_file_extension(file)
        extensions_and_files[file_extension] += [file]

    return extensions_and_files


def format_content(extensions_and_files):
    new_content = ""

    for ext, file_names in sorted(extensions_and_files.items()):
        new_content += f"{ext}\n"
        for file in sorted(file_names):
            new_content += f"- - - {file}\n"

    return new_content


def save_new_file(new_content):
    desktop_path = join(join(environ["USERPROFILE"]), "Desktop") + sep + "report.txt"
    with open(desktop_path, "w") as new_file:
        new_file.write(new_content)


directory_path = input()
all_files = get_all_files(directory_path)
extensions_and_files = group_files(all_files)
new_content = format_content(extensions_and_files)
save_new_file(new_content)
