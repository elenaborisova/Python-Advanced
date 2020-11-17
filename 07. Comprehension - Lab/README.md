## **01.	ASCII Values -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/07.%20Comprehension%20-%20Lab/01_ascii_values.py)
Write program that receives a list of characters and creates a dictionary with each character as a key and its ASCII value as a value. Try solving that problem using comprehensions.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|a, b, c, a          |{'a': 97, 'b': 98, 'c': 99}          |
|d, c, m, h          |{'d': 100, 'c': 99, 'm': 109, 'h': 104}                  |



## **02.	No Vowels -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/07.%20Comprehension%20-%20Lab/02_no_vowels.py)
Using a comprehension write a program that receives a text and removes all the vowels from it. Print the new text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|Python          |Pythn         |
|ILovePython          |LvPythn                  |


## **03.	Even Matrix -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/07.%20Comprehension%20-%20Lab/03_even_matrix.py)
Write a program that receives a matrix of numbers and prints a new one only with the numbers that are even. Use nested comprehension for that problem.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|2<br>1, 2, 3<br>4, 5, 6  |[[2], [4, 6]]          |
|4<br>10, 33, 24, 5, 1<br>67, 34, 11, 110, 3<br>4, 12, 33, 63, 21<br>557, 45, 23, 55, 67 |[[10, 24], [34, 110], [4, 12], []]                  |



## **04.	Flattening Matrix -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/07.%20Comprehension%20-%20Lab/04_flattening_matrix.py)
Write a program that receives a matrix and prints the flattened version of it (a list with all the values). For example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|2<br>1, 2, 3<br>4, 5, 6  |[1, 2, 3, 4, 5, 6]          |
|3<br>10, 2, 21, 4<br>5, 20, 41, 9<br>6, 2, 4, 99  |[10, 2, 21, 4, 5, 20, 41, 9, 6, 2, 4, 99]                  |



## **05.	Filter Numbers -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/07.%20Comprehension%20-%20Lab/05_filter_numbers.py)
You will be given a start and an end. Print all the numbers in the given range (inclusive) that are divisible by any of the numbers from 2 to 10. Use comprehensions for this problem.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|1<br>20          |[2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20]          |
|45<br>50                  |[45, 46, 48, 49, 50]                 |


