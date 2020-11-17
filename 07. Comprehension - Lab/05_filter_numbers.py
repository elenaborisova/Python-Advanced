def is_number_valid(number):
    return any([number % div == 0 for div in range(2, 11)])


start = int(input())
end = int(input())

print(
    [num for num in range(start, end + 1)
     if is_number_valid(num)
     ]
)
