from triangle_print import print_line


def print_triangle(n):
    [print_line(1, x + 1) for x in range(n)]
    [print_line(1, x + 1) for x in range(n - 2, -1, -1)]
