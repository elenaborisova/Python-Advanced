## **01.	Unique Usernames -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/04.%20Tuples%20and%20Sets%20-%20Exercise/01_unique_usernames.py)
Write a program that reads from the console a sequence of N usernames and keeps a collection only of the unique ones. On the first line, you will receive an integer N. On the next N lines, you will receive a username. Print the collection on the console (the order does not matter):

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|6<br>George<br>George<br>George<br>Peter<br>George<br>NiceGuy1234    |George<br>Peter<br>NiceGuy1234   |




## **02.	Sets of Elements -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/04.%20Tuples%20and%20Sets%20-%20Exercise/02_sets_of_elements.py)
Write a program that prints a set of elements. On the first line, you will receive two numbers - n and m, which represent the lengths of two separate sets. On the next n + m lines you will receive n numbers, which are the numbers in the first set, and m numbers, which are in the second set. Find all the unique elements that appear in both and print them on separate lines (the order does not matter).

For example:  
Set with length n = 4: {1, 3, 5, 7}  
Set with length m = 3: {3, 4, 5}  
Set that contains all the elements that repeat in both sets -> {3, 5}

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|4 3<br>1<br>3<br>5<br>7<br>3<br>4<br>5<br>2 2<br>1<br>3<br>1<br>5   |3<br>5<br>1          |



## **03.	Periodic Table -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/04.%20Tuples%20and%20Sets%20-%20Exercise/03_periodic_table.py)
Write a program that keeps all the unique chemical elements. On the first line you will be given a number n - the count of input lines that you are going to receive. On the next n lines, you will be receiving chemical compounds, separated by a single space. Your task is to print all the unique ones on separate lines (order does not matter):

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|4<br>Ce O<br>Mo O Ce<br>Ee<br>Mo      |Ce<br>Ee<br>Mo<br>O                      |
|3<br>Ge Ch O Ne<br>Nb Mo Tc<br>O Ne   |Ch<br>Ge<br>Mo<br>Nb<br>Ne<br>O<br>Tc    |




## **04.	Count Symbols -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/04.%20Tuples%20and%20Sets%20-%20Exercise/04_count_symbols.py)
Write a program that reads a text from the console and counts the occurrences of each character in it. Print the results in alphabetical (lexicographical) order. 

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|SoftUni rocks      | : 1 time/s<br>S: 1 time/s<br>U: 1 time/s<br>c: 1 time/s<br>f: 1 time/s<br>i: 1 time/s<br>k: 1 time/s<br>n: 1 time/s<br>o: 2 time/s<br>r: 1 time/s<br>s: 1 time/s<br>t: 1 time/s   |



## **05.	Phonebook -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/04.%20Tuples%20and%20Sets%20-%20Exercise/05_phonebook.py)
Write a program that receives info from the console about people and their phone numbers.

You are free to choose the way the data is entered; each entry should have a name and a number (both strings). If you receive a name that already exists in the phonebook, update its number.

After filling the phonebook, you will receive a number – N. Your program should be able to perform a search of a contact by name and print her details in format "{name} -> {number}". In case the contact isn't found, print "Contact {name} does not exist."

*Examples*

|          Input          |      Output       |
|-------------------------|-------------------|
|Adam-0888080808<br>2<br>Mery<br>Adam                                                                                       |Contact Mery does not exist.<br>Adam -> 0888080808                                                              |
|Adam-+359888001122<br>Ralf-666<br>George-5559393<br>Silvester-02/987665544<br>4<br>Silvester<br>silvester<br>Rolf<br>Ralf  |Silvester -> 02/987665544<br>Contact silvester does not exist.<br>Contact Rolf does not exist.<br>Ralf -> 666   |




## **06.	Longest Intersection -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/04.%20Tuples%20and%20Sets%20-%20Exercise/06_longest_intersection.py)
Write a program that finds the longest intersection. You will be given a number N. On the next N lines you will be given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}". Find the intersection of these two ranges and save the longest one of all N intersections. At the end print the numbers that are included in the longest intersection and its length in the format: "Longest intersection is {longest_intersection} with length {length_longest_intersection}"

*Note:* in each range, there will always be intersection. If there are two equal intersections, print the first one.

*Examples*

|       Input       |                Output                  |
|-------------------|----------------------------------------|
|3<br>0,3-1,2<br>2,10-3,5<br>6,15-3,10                         |Longest intersection is [6, 7, 8, 9, 10] with length 5             |
|5<br>0,10-2,5<br>3,8-1,7<br>1,8-2,4<br>4,7-2,5<br>1,10-2,11   |Longest intersection is [2, 3, 4, 5, 6, 7, 8, 9, 10] with length 9 |




## **07.	Battle of Names -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/04.%20Tuples%20and%20Sets%20-%20Exercise/07_battle_of_names.py)
You will receive a number N. On the next N lines, you will be receiving names. You must sum the ascii values of each letter in the name and integer divide it by the value of the current line. Save the devised number to a set of either odd or even numbers, depending if it's an odd or even number. After that, sum the values of the odd and even numbers.

•	If the summed numbers are equal, print the union values, separated by ", ".   
•	If the odd sum is bigger than the even, print the different values, separated by ", ".  
•	If the even sum is bigger than the odd, print the symmetric different values, separated by ", ".

*NOTE:* On every operation, the starting set should be the odd set

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|4<br>Pesho<br>Stefan<br>Stamat<br>Gosho                        |304, 128, 206, 511          |
|6<br>Preslav<br>Gosho<br>Ivan<br>Stamat<br>Pesho<br>Stefan     |733, 101                    |


