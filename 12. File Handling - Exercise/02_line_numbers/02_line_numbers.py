def count_letters_and_punct_marks(line):
    letters_count = len([char for char in line if char.isalpha()])
    punct_marks_count = len([char for char in line if not char.isalnum() and not char == " "])
    return letters_count, punct_marks_count


def insert_line_numbers(number):
    return f"Line {number}:"


def change_lines(file):
    changed_lines = []

    for number, line in enumerate(file, start=1):
        line = line.strip()
        letters_count, punct_marks_count = count_letters_and_punct_marks(line)
        line = f"{insert_line_numbers(number)} {line} ({letters_count})({punct_marks_count})"
        changed_lines.append(line)

    return changed_lines


def write_result_to_another_file(changed_lines):
    with open("output.txt", "w") as new_file:
        new_file.write("\n".join(changed_lines))


with open("text.txt", "r") as file:
    changed_lines = change_lines(file)
    write_result_to_another_file(changed_lines)
