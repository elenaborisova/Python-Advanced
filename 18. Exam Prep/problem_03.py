def get_magic_triangle(n):
    triangle = [[1], [1, 1]]

    for row in range(3, n + 1):
        triangle.append([1 for _ in range(row)])

    for row in range(n):
        for col in range(row + 1):
            if 0 < col < row:
                triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col]

    return triangle


print(get_magic_triangle(5))
