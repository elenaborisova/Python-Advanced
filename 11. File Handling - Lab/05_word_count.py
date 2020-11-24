import re


def get_words_from_file(file_path):
    with open(file_path, "r") as file:
        return file.read().split()


def get_words_from_line(line):
    return re.split(r"[^A-Za-z0-9]", line.lower())


def count_words(words, line, words_counts):
    for word in words:
        if word in line:
            words_counts[word] += line.count(word)


def get_words_counts(file_path, words):
    words_counts = {word: 0 for word in words}

    with open(file_path, "r") as file:
        for line in file:
            words_in_line = get_words_from_line(line)
            count_words(words, words_in_line, words_counts)

    return words_counts


def create_and_write_new_file(file_path, words_counts):
    sorted_words_counts = dict(sorted(words_counts.items(), key=lambda x: -x[1]))

    with open(file_path, "w") as file:
        for word, count in sorted_words_counts.items():
            file.write(f"{word} - {count}\n")


words_file_path = "words.txt"
text_file_path = "text.txt"
output_file_path = "output.txt"

words_counts = get_words_counts(text_file_path, get_words_from_file(words_file_path))
create_and_write_new_file(output_file_path, words_counts)
