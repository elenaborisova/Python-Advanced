def replace_symbols(line):
    symbols_to_replace = ("-", ",", ".", "!", "?")
    for symbol in symbols_to_replace:
        line = line.replace(symbol, "@")
    return line


def reverse_line(line):
    line = reversed(line.split())
    return " ".join(line)


def get_even_lines(file):
    for index, line in enumerate(file):
        if index % 2 == 0:
            line = replace_symbols(line)
            print(reverse_line(line))


with open("text.txt", "r") as file:
    get_even_lines(file)
