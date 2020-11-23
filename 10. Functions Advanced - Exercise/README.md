## **01.	Negative vs Positive -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/10.%20Functions%20Advanced%20-%20Exercise/01_negative_vs_positive.py)
You will receive a list of numbers. Separate the negative numbers from the positive. Find the total sum of the negatives and positives, replace the negative number with its absolute value and print the following:

If the absolute negative number is bigger than the positive number:  
	"The negatives are stronger than the positives"  
If the positive number is bigger than the absolute negative number:  
	"The positives are stronger than the negatives"  

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|1 2 -3 -4 65 -98 12 57 -84          |-189<br>137<br>The negatives are stronger than the positives  |





## **02.	Odd or Even -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/10.%20Functions%20Advanced%20-%20Exercise/02_odd_or_even.py)
You will receive a command and a list of numbers:  
If the command is "Odd": Print the sum of the Odd numbers multiplied by the length of the initial list.  
If the command is "Even": Print the sum of the Even numbers multiplied by the length of the initial list.  

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|Odd<br>1 3 5 34 7 9 12 11 13 10 |490          |






## **03.	Arguments Length -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/10.%20Functions%20Advanced%20-%20Exercise/03_arguments_length.py)
Create a function called args_length that returns the number of arguments. Submit only the function in the judge system.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|print(args_length(1, 32, 5))          |3          |
|print(args_length("john", "peter"))                  |2                  |
|print(args_length([1, 2, 3]))   |1 |



## **04.	Even or Odd -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/10.%20Functions%20Advanced%20-%20Exercise/04_even_or_odd.py)
Create a function called even_odd that can receive different amount of numbers and a command at the end. The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list. Submit only the function in the judge system.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|print(even_odd(1, 2, 3, 4, 5, 6, "even"))          |[2, 4, 6]          |
|print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))  |[1, 3, 5, 7, 9]                  |



## **05.	Function Executor -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/10.%20Functions%20Advanced%20-%20Exercise/05_function_executor.py)
Create a function called func_executor that can receive different number of tuples, each of which will have exactly 2 elements: first will be a function and the second will be a tuple of the arguments that need to be passed to that function. Create a list which will contain all the results of the executed functions with its corresponding arguments. For more clarification, see the examples below. Submit only your function in the judge system.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|def sum_numbers(num1, num2):<br>    return num1 + num2<br><br>def multiply_numbers(num1, num2):<br>    return num1 * num2<br><br>print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))  |[3, 8]         |





## **06.	Keyword Arguments Length -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/10.%20Functions%20Advanced%20-%20Exercise/06_keyword_arguments_length.py)
Create a function called kwargs_length which can receive different amount of keyword arguments and returns their length. Submit only the function in the judge system.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|dictionary = {'name': 'Peter', 'age': 25}<br>print(kwargs_length(**dictionary))  |2          |




## **07.	Age Assignment -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/10.%20Functions%20Advanced%20-%20Exercise/07_age_assignment.py)
Create a function called age_assignment that receives different number of names and then different amount of key-value pairs. The key will be a single letter (first letter of a name), and the value a number (age). For each name, find its first letter in the key-value pairs and assign the age to the persons name. At the end return a dictionary with all the names and ages as shown in the example. Submit only the function in the judge system.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|print(age_assignment("Peter", "George", G=26, P=19))          |{'Peter': 19, 'George': 26}      |
|print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))                  |{'Amy': 22, 'Bill': 61, 'Willy': 36}                  |



## **08.	Recursion Palindrome -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/10.%20Functions%20Advanced%20-%20Exercise/08_recursive_palindrome.py)
Write a recursive function called palindrome which will receive a word and an index (always 0). Implement the function, so it returns "{word} is a palindrome" if the word is a palindrome and "{word} is not a palindrome" if the word is not a palindrome using recursion. Submit only the function in the judge system.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|print(palindrome("abcba", 0))          |abcba is a palindrome          |
|print(palindrome("peter", 0))                  |peter is not a palindrome                  |



## **09.	Recursive Power -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/10.%20Functions%20Advanced%20-%20Exercise/09_recursive_power.py)
Create a recursive function called recursive_power which should receive a number and a power. Using recursion return the result of number ** power. Submit only the function in the judge system.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|print(recursive_power(2, 10))          |1024          |
|print(recursive_power(10, 100))                 |10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000                  |
