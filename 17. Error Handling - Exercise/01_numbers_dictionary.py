numbers_dictionary = {}

try:
    line = input()
    while not line == "Search":
        num_str = line
        num = int(input())
        numbers_dictionary[num_str] = num
        line = input()

    line = input()
    while not line == "Remove":
        searched_num = line
        print(numbers_dictionary[searched_num])
        line = input()

    line = input()
    while not line == "End":
        searched_num = line
        numbers_dictionary.pop(searched_num)
        line = input()

except ValueError:
    print("The variable number must be an integer")
except KeyError:
    print("Number does not exist in the dictionary")

print(numbers_dictionary)