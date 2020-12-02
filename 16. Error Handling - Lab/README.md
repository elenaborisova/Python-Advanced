## **01. So Many Exceptions -** [Solution]()
You are provided with the following code:
    numbers_list = input().split(", ")
    result = 0
    
    for i in range(numbers_list):
        number = numbers_list[i + 1]
        if number < 5:
            result *= number
        elif number > 5 and number > 10:
            result /= number
    print(result)
    
*Input:*
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11

*Output:*
0.003968253968253968



     
