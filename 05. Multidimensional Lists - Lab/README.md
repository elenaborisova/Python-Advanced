## **01.	Sum Matrix Elements -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/05.%20Multidimensional%20Lists%20-%20Lab/01_sum_matrix_elements.py)
Write a program that reads a matrix from the console and prints:  
•	The sum of all matrix elements  
•	The matrix itself  
On the first line, you will get matrix sizes in format "{rows}, {columns}"  

*Examples* 

|       Input       |      Output       |
|-------------------|-------------------|
|3, 6<br>7, 1, 3, 3, 2, 1<br>1, 3, 9, 8, 5, 6<br>4, 6, 7, 9, 1,    |76<br>[[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]   |



## **02.	Sum Matrix Columns -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/05.%20Multidimensional%20Lists%20-%20Lab/02_sum_matrix_columns.py)
Write a program that reads a matrix from the console and prints the sum for each column. On the first line, you will get the matrix's rows. On the next rows, you will get elements for each column separated with a space. 

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|3, 6<br>7 1 3 3 2 1<br>1 3 9 8 5 6<br>4 6 7 9 1 0 |12<br>10<br>19<br>20<br>8<br>7   |
|3, 3<br>1 2 3<br>4 5 6<br>7 8 9   |12<br>15<br>18   |



## **03.	Primary Diagonal -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/05.%20Multidimensional%20Lists%20-%20Lab/03_primary_diagonal.py)
Write a program that finds the sum of matrix primary diagonal.

*Input*  
•	On the first line, you are given the integer N – the size of the square matrix  
•	The next N lines holds the values for every row – N numbers separated by a space  

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|3<br>11 2 4<br>4 5 6<br>10 8 -12  |4                   |
|3<br>1 2 3<br>4 5 6<br>7 8 9      |15                  |





## **04.	Symbol in Matrix -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/05.%20Multidimensional%20Lists%20-%20Lab/04_symbol_in_matrix.py)
Write a program that reads N, a number representing the rows and cols of a matrix. On the next N lines, you will receive rows of the matrix. Each row consists of ASCII characters. After that, you will receive a symbol. Find the first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})". If there is no such symbol print an error message "{symbol} does not occur in the matrix"

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|3<br>ABC<br>DEF<br>X!@<br>! |(2, 1)          |
|4<br>asdd<br>xczc<br>qwee<br>qefw<br>4   |4 does not occur in the matrix                 |




## **05.	Square with Maximum Sum -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/05.%20Multidimensional%20Lists%20-%20Lab/05_square_with_maximum_sum.py)
Write a program that read a matrix from console. Find biggest sum of 2x2 submatrix and print it to console.

*Input*
On first line you will get matrix sizes in format rows, columns.   
One next rows lines you will get elements for each column separated with coma.  

*Output*
Print biggest top-left square, which you find and sum of its elements.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|3, 6<br>7, 1, 3, 3, 2, 1<br>1, 3, 9, 8, 5, 6<br>4, 6, 7, 9, 1, 0     |9 8<br>7 9<br>33    |
|2, 4<br>10, 11, 12, 13<br>14, 15, 16, 17   |12 13<br>16 17<br>58  |



