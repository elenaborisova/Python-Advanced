## **01.	Count Same Values -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/03.%20Tuples%20and%20Sets%20-%20Lab/01_count_same_values.py)
You will be given a list of numbers. Write a program that prints the number of occurrences of each number.

*Examples*

|                  Input                  |      Output       |
|-----------------------------------------|-------------------|
|-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3          |-2.5 - 3 times<br>4.0 - 2 times<br>3.0 - 4 times<br>-5.5 - 1 times  |
|2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3  |2.0 - 3 times<br>4.0 - 6 times<br>5.0 - 4 times<br>3.0 - 7 times    |



## **02.	Average Student Grades -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/03.%20Tuples%20and%20Sets%20-%20Lab/02_average_student_grades.py)
Write a program, which reads a name of a student and their grades and adds them to the student record. Print the  name of the students with their grades and their average grade.   
The order in which we print the result does not matter.

*Examples*

|       Input       |                 Output                 |
|-------------------|----------------------------------------|
|7<br>Peter 5.20<br>Mark 5.50<br>Peter 3.20<br>Mark 2.50<br>Alex 2.00<br>Mark 3.46<br>Alex 3.00 |Mark -> 5.50 2.50 3.46 (avg: 3.82)<br>Peter -> 5.20 3.20 (avg: 4.20)<br>Alex -> 2.00 3.00 (avg: 2.50) |
|4<br>Scott 4.50<br>Ted 3.00<br>Scott 5.00<br>Ted 3.66                                          |Ted -> 3.00 3.66 (avg: 3.33)<br>Scott -> 4.50 5.00 (avg: 4.75)                                        |
|5<br>Lee 6.00<br>Lee 5.50<br>Lee 6.00<br>Peter 4.40<br>Kenny 3.30                              |Peter -> 4.40 (avg: 4.40)<br>Lee -> 6.00 5.50 6.00 (avg: 5.83)<br>Kenny -> 3.30 (avg: 3.30)           |



## **03.	Record Unique Names -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/03.%20Tuples%20and%20Sets%20-%20Lab/03_record_unique_names.py)
Write a program, which will take a list of names and print only the unique names in the list.  
The order in which we print the result does not matter.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|8<br>Lee<br>Joey<br>Lee<br>Joe<br>Alan<br>Alan<br>Peter<br>Joey          |Alan<br>Joey<br>Lee<br>Joe<br>Peter          |
|7<br>Lyle<br>Bruce<br>Alice<br>Easton<br>Shawn<br>Alice<br>Shawn         |Easton<br>Lyle<br>Alice<br>Bruce<br>Shawn    |
|6<br>Adam<br>Adam<br>Adam<br>Adam<br>Adam<br>Adam                        |Adam                                         |



## **04.	Parking Lot -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/03.%20Tuples%20and%20Sets%20-%20Lab/04_parking_lot.py)
Write a program that:  
•	Records a car number for every car that enters the parking lot  
•	Removes a car number when the car leaves the parking lot  

The input will be the number of commands, which you will receive, and cars in the format: direction, car_number. Print the car numbers, which are still in the parking lot.  
NOTE: The order in which we print the result does not matter.

*Examples*


|       Input       |      Output       |
|-------------------|-------------------|
|10<br>IN, CA2844AA<br>IN, CA1234TA<br>OUT, CA2844AA<br>IN, CA9999TT<br>IN, CA2866HI<br>OUT, CA1234TA<br>IN, CA2844AA<br>OUT, CA2866HI<br>IN, CA9876HH<br>IN, CA2822UU |CA2844AA<br>CA9999TT<br>CA2822UU<br>CA9876HH   |
|4<br>IN, CA2844AA<br>IN, CA1234TA<br>OUT, CA2844AA<br>OUT, CA1234TA                                                                                                   |Parking Lot is Empty                           |



## **05.	SoftUni Party -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/03.%20Tuples%20and%20Sets%20-%20Lab/05_softuni_party.py)
There is a party at SoftUni. Many guests are invited and there are two types of them: Regular and VIP. When a guest comes, check if he/she exists in any of the two reservation lists.

All reservation numbers are 8 characters long and all VIP numbers will start with a digit.

First, you will be receiving the number of guests and their reservation numbers. After that, you will be receiving guests, who came to the party, until you receive the "END" command.

In the end, print the count of the guests who didn't come to the party and their reservation numbers. The VIP guests must be first.

Both the VIP and the Regular guests must be sorted in ascending order.

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|5<br>7IK9Yo0h<br>9NoBUajQ<br>Ce8vwPmE<br>SVQXQCbc<br>tSzE5t0p<br>9NoBUajQ<br>Ce8vwPmE<br>SVQXQCbc<br>END              |2<br>7IK9Yo0h<br>tSzE5t0p                  |
|6<br>m8rfQBvl<br>fc1oZCE0<br>UgffRkOn<br>7ugX7bm0<br>9CQBGUeJ<br>2FQZT3uC<br>2FQZT3uC<br>9CQBGUeJ<br>fc1oZCE0<br>END  |3<br>7ugX7bm0<br>UgffRkOn<br>m8rfQBvl      |


