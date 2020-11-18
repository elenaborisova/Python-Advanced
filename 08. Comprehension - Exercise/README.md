## **01.	Word Filter -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/08.%20Comprehension%20-%20Exercise/01_word_filter.py)
Using comprehension, write a program that receives some strings separated by space and take only those words, whose length is even. Print each word on a new line.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|kiwi orange banana apple          |kiwi<br>orange<br>banana          |
|pizza cake pasta chips                  |cake                  |


## **02.	Words Lengths -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/08.%20Comprehension%20-%20Exercise/02_words_lengths.py)
Using list comprehension, write a program that receives some strings separated by comma and space ", " and prints on the console each string with its length in the format: "{first_str} -> {first_str_len}, {second_str} -> {second_str_len},…"

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|Peter, George, Bill, Lilly, Katy          |Peter -> 5, George -> 6, Bill -> 4, Lilly -> 5, Katy -> 4          |
|Some, Random, Text                  |Some -> 4, Random -> 6, Text -> 4                  |


## **03.	Capitals -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/08.%20Comprehension%20-%20Exercise/03_capitals.py)
Using dictionary comprehension write a program that receives countries on the first line separated by comma and space ", " and their corresponding capital cities on the second line (again separated by comma and space ", ") and prints each country with their capital on a separate line in the format: "{country} -> {capital}"

*Hints*  
  •	You can use the zip() method to zip the two lists into tuple pairs.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|Bulgaria, Romania, Germany, England<br>Sofia, Bucharest, Berlin, London          |Bulgaria -> Sofia<br>Romania -> Bucharest<br>Germany -> Berlin<br>England -> London |



## **04.	Number Classification -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/08.%20Comprehension%20-%20Exercise/04_number_clasification.py)
Using list comprehension write a program that receives numbers separated by comma and space ", " and prints all the positive, negative, even and odd numbers on separate lines as shown below.

*Note:* Zero is counted for a positive number

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33          |Positive: 1, 0, 5, 3, 4, 12, 19<br>Negative: -2, -100, -20, -33<br>Even: -2, 0, 4, -100, -20, 12<br>Odd: 1, 5, 3, 19, -33  |



## **05.	Diagonals -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/08.%20Comprehension%20-%20Exercise/05_diagonals.py)
Using nested list comprehension write a program that reads NxN matrix, finds its diagonals, prints them and their sum as shown below.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|3<br>1, 2, 3<br>4, 5, 6<br>7, 8, 9 |First diagonal: 1, 5, 9. Sum: 15<br>Second diagonal: 3, 5, 7. Sum: 15 |



## **06.	Matrix of Palindromes -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/08.%20Comprehension%20-%20Exercise/06_matrix_of_palindromes.py)
Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns like the one in the examples below.  
•	Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …  
•	Columns + rows define the middle letter:   
  o	column 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …  
  o	column 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …  
  
*Input*  
•	The numbers r and c stay at the first line at the input.  
•	r and c are integers.  

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|4 6          |aaa aba aca ada aea afa<br>bbb bcb bdb beb bfb bgb<br>ccc cdc cec cfc cgc chc<br>ddd ded dfd dgd dhd did  |
|3 2                  |aaa aba<br>bbb bcb<br>ccc cdc   |



## **07.	Flatten lists -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/08.%20Comprehension%20-%20Exercise/07_flatten_lists.py)
Write a program to flatten several lists of numbers, received in the following format:  
•	String with numbers separated by '|'.  
•	Values are separated by spaces (' ', one or several)  
•	Order the output list from the last to the first received, and their values from left to right as shown below.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|1 2 3 \|4 5 6 \|  7  8          |7 8 4 5 6 1 2 3          |
|7 \| 4  5\|1 0\| 2 5 \|3                  |3 2 5 1 0 4 5 7                  |
|1\| 4 5 6 7  \|  8 9               |8 9 4 5 6 7 1   |



## **08.	Heroes Inventory -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/08.%20Comprehension%20-%20Exercise/08_heroes_inventory.py)
Using comprehension write a program that receives some hero names and items that need to be added in their inventory (item name and item cost). Print the total amount of items with their total cost for each hero.

*Input*  
•	On the first line you will receive the names of the heroes separated by comma and space ", "  
•	On the next lines until the command "End", you will be given items with their cost in the following format: "{name}-{item}-{cost}". If an item already exists in a hero inventory - ignore it.

*Output*  
•	For each hero print his name, the total items and the total cost of the items in the format: "{name} -> Items: {items_count}, Cost: {items_cost}"

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|Peter, George<br>Peter-Sword-20<br>Peter-Shield-10<br>George-Gem-100<br>Peter-Sword-15<br>George-Sword-20<br>End |Peter -> Items: 2, Cost: 30<br>George -> Items: 2, Cost: 120   |


## **09.	Bunker -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/08.%20Comprehension%20-%20Exercise/09_bunker.py)
Using comprehension write a program that finds the number of given items in a bunker and their average quality. 

On the first line you will be given all item categories present in the bunker, then you will be given a number (n). On the next "n" lines you will be given different items in the following format: "{category} - {item_name} - quantity:{item_quantity};quality:{item_quality}". Store that information, you will need it later. 

After you receive all the inputs, print the total amount of items (sum the quantities) in the format: "Count of items: {count}". After that print the average quality of all items in the format: "Average quality: {quality sum/categories count}" - formatted to the second digit. Finally, print all categories with the items on separate lines in the format: "{category} -> {item1}, {item2}, …".

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|food, water, materials, metal<br>5<br>food - pizza - quantity:10;quality:5<br>water - mineral - quantity:5;quality:10<br>materials - wood - quantity:2;quality:5<br>metal - copper - quantity:3;quality:10<br>food - burgers - quantity:5;quality:2  |Count of items: 25<br>Average quality: 8.00<br>food -> pizza, burgers<br>water -> mineral<br>materials -> wood<br>metal -> copper   |



## **10.	Matrix Modification -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/08.%20Comprehension%20-%20Exercise/10_matrix_modification.py)
Write a program that reads a matrix from the console. On the first line you will get matrix rows. On next rows lines you will get elements for each column separated with space. You will be receiving commands in the following format:  
•	Add {row} {col} {value} – Increase the number at the given coordinates with the value.  
•	Subtract {row} {col} {value} – Decrease the number at the given coordinates by the value.  

Coordinates might be invalid. In this case you should print "Invalid coordinates". When you receive "END" you should print the matrix and stop the program.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|3<br>1 2 3<br>4 5 6<br>7 8 9<br>Add 0 0 5<br>Subtract 1 1 2<br>END |6 2 3<br>4 3 6<br>7 8 9  |
|4<br>1 2 3 4<br>5 6 7 8<br>8 7 6 5<br>4 3 2 1<br>Add 4 4 100<br>Add 3 3 100<br>Subtract -1 -1 42<br>Subtract 0 0 42<br>END  |Invalid coordinates<br>Invalid coordinates<br>-41 2 3 4<br>5 6 7 8<br>8 7 6 5<br>4 3 2 101  |






