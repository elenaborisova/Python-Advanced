def reverse_nums(nums):
    reversed_nums = []

    while nums:
        reversed_nums.append(nums.pop())

    return reversed_nums


numbers = input().split()
print(' '.join(reverse_nums(numbers)))
