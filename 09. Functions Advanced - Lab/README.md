## **01.	Absolute Values -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/09.%20Functions%20Advanced%20-%20Lab/01_absolute_values.py)
Write a program that receives a list of numbers and prints their absolute value. Use abs()

*Example*

|       Input       |      Output       |
|-------------------|-------------------|
|1 2.5 -3 -4.5          |[1.0, 2.5, 3.0, 4.5]          |




## **02.	Rounding -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/09.%20Functions%20Advanced%20-%20Lab/02_rounding.py)
Write a program that rounds all the given numbers. Use round()

*Example*

|       Input       |      Output       |
|-------------------|-------------------|
|1.0 2.5 3.0 4.5         |[1, 2, 3, 4]          |





## **03.	Even Numbers -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/09.%20Functions%20Advanced%20-%20Lab/03_even_numbers.py)
Write a program that receives a list of numbers. Print only the even numbers from the list. Use filter()

*Example*

|       Input       |      Output       |
|-------------------|-------------------|
|1 2 3 4         |[2, 4]         |





## **04.	Sort -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/09.%20Functions%20Advanced%20-%20Lab/04_sort.py)
Write a program that prints a sorted list of numbers in ascending order. Use sorted()

*Example*

|       Input       |      Output       |
|-------------------|-------------------|
|6 2 4          |[2, 4, 6]        |




## **05.	Min Max and Sum -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/09.%20Functions%20Advanced%20-%20Lab/05_min_max_and_sum.py)
Write a program that prints the min and max values from a list and the sum of all the numbers in the list. Use min(), max() and sum()

*Example*

|       Input       |      Output       |
|-------------------|-------------------|
|2 4 6          |The minimum number is 2<br>The maximum number is 6<br>The sum number is: 12  |





## **06.	Multiplication Function -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/09.%20Functions%20Advanced%20-%20Lab/06_multiplication_function.py)
Write a function called multiply that can receive any amount of numbers as different parameters and returns the result of the multiplication of all of them. Submit only your function in judge.

*Example*

|       Input       |      Output       |
|-------------------|-------------------|
|print(multiply(1, 4, 5))<br>print(multiply(4, 5, 6, 1, 3))<br>print(multiply(2, 0, 1000, 5000)) |20<br>360<br>0          |





## **07.	Operate -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/09.%20Functions%20Advanced%20-%20Lab/07_operate.py)
Write a function called operate that receives an operator(+, -, * or /) as first argument and multiple numbers as additional arguments (*args). The function should return the result of the operator applied to all the numbers. For more clarification, see the examples below. Submit only the function in the judge system.

*Example*

|       Input       |      Output       |
|-------------------|-------------------|
|print(operate("+", 1, 2, 3))          |6          |
|print(operate("*", 3, 4))                  |12                  |



## **08.	Concatenate -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/09.%20Functions%20Advanced%20-%20Lab/08_concatenate.py)
Write a function called concatenate() that receives some strings, concatenates them and returns the result

*Example*

|       Input       |      Output       |
|-------------------|-------------------|
|print(concatenate("Soft", "Uni", "Is", "Great", "!"))          |SoftUniIsGreat!          |





## **09.	Person Info -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/09.%20Functions%20Advanced%20-%20Lab/09_person_info.py)
Write a function called get_info that receives a name, age and town, and returns a string in the format: 
"This is {name} from {town} and he is {age} years old". Use dictionary unpacking when testing your function. Submit only the function in the judge system.

*Example*

|       Input       |      Output       |
|-------------------|-------------------|
|print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))          |This is George from Sofia and he is 20 years old          |




## **10.	Character Combinations -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/09.%20Functions%20Advanced%20-%20Lab/10_character_combinations.py)
Write a program that reads a single string and prints all the possible combinations of the characters in that string. Submit your solution in the judge system.

*Example*

|       Input       |      Output       |
|-------------------|-------------------|
|abc          |abc<br>acb<br>bac<br>bca<br>cba<br>cab |




## **11.	Chairs -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/09.%20Functions%20Advanced%20-%20Lab/11_chairs.py)
Write a program that receives names on the first line (separated by comma and space ", ") and number of chairs on the second line (an integer). Find all the ways to fit those people on the chairs. Print each combination on a separate line.

*Note:* In the example below, "Peter, George" is same as "George, Peter", so we only print the first combination

*Example*

|       Input       |      Output       |
|-------------------|-------------------|
|Peter, George, Amy<br>2  |Peter, George<br>Peter, Amy<br>George, Amy |




## **12.	Expressions -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/09.%20Functions%20Advanced%20-%20Lab/12_expressions.py)
Write a program that generates all the possible expressions and their results between a given list of numbers using only the + and - operators. Print them on the console as shown in the example

*Example*

|       Input       |      Output       |
|-------------------|-------------------|
|1, 1, 1, 1          |+1+1+1+1=4<br>+1+1+1-1=2<br>+1+1-1+1=2<br>+1+1-1-1=0<br>+1-1+1+1=2<br>+1-1+1-1=0<br>+1-1-1+1=0<br>+1-1-1-1=-2<br>-1+1+1+1=2<br>-1+1+1-1=0<br>-1+1-1+1=0<br>-1+1-1-1=-2<br>-1-1+1+1=0<br>-1-1+1-1=-2<br>-1-1-1+1=-2<br>-1-1-1-1=-4 |






