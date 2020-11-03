## **01. Reverse Strings -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/01.%20Lists%20as%20Stacks%20and%20Queues%20-%20Lab/01_reverse_string.py)
Write program that:  
•	Reads an input string  
•	Reverses it using a stack  
•	Prints the result back on the console  

*Examples*

|       Input       |      Output       |
|-------------------|-------------------|
|I Love Python      |nohtyP evoL I      |
|Stacks and Queues  |seueuQ dna skcatS  |


## **02. Matching Brackets -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/01.%20Lists%20as%20Stacks%20and%20Queues%20-%20Lab/02_matching_brackets.py)
We are given an arithmetic expression with brackets. Scan through the string and extract each sub-expression.  
Print the result back on the console.  

*Examples*

|                Input                |                      Output                        |
|-------------------------------------|----------------------------------------------------|
|1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5  |(2 + 3)<br>(3 + 1)<br>(2 - (2 + 3) * 4 / (3 + 1))   |
|(2 + 3) - (2 + 3)                    |(2 + 3)<br>(2 + 3)                                  |



## **03. Supermarket -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/01.%20Lists%20as%20Stacks%20and%20Queues%20-%20Lab/03_supermarket.py)
Write a program that reads an input consisting of a name and adds it to a queue until "End" is received. If you receive "Paid", print every customer name and empty the queue, otherwise we receive a client and we must add him to the queue. When we receive "End", we must print the count of the remaining people in the queue in the format: "{count} people remaining."

*Examples*

|   Input   |         Output             |
|-----------|----------------------------|
|George<br>Peter<br>William<br>Paid<br>Michael<br>Oscar<br>Olivia<br>Linda<br>End |George<br>Peter<br>William<br>4 people remaining.  |
|Anna<br>Emma<br>Alexander<br>End                                                 |3 people remaining.                                |


## **04. Water Dispenser -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/01.%20Lists%20as%20Stacks%20and%20Queues%20-%20Lab/04_water_dispenser.py)
Write a program that reads on the first line the starting quantity of water in a dispenser. Then on the next few lines you will be given the names of some people that want to get water (each on separate line) until you receive the command "Start". Add those people in a queue. Finally, you will receive some commands until the command "End":  
-	{liters} - Litters that the current person in the queue wants to get. Check if there is enough water in the dispenser for that person.  
  o	If there is enough water, print "{person_name} got water" and remove him/her from the queue.  
  o	Otherwise, print "{person} must wait" and remove the person from the queue without reducing the water in the dispenser  
-	refill {liters} - add the given litters in the dispenser.  

At the end print how many litters of water are left in the format: "{left_liters} liters left"  

*Examples*

|   Input   |         Output             |
|-----------|----------------------------|
|2<br>Peter<br>Amy<br>Start<br>2<br>refill 1<br>1<br>End                           |Peter got water<br>Amy got water<br>0 liters left                                         |
|10<br>Peter<br>George<br>Amy<br>Alice<br>Start<br>2<br>3<br>3<br>3<br>End         |Peter got water<br>George got water<br>Amy got water<br>Alice must wait<br>2 liters left  |


## **05. Hot Potato -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/01.%20Lists%20as%20Stacks%20and%20Queues%20-%20Lab/05_hot_potato.py)
Hot potato is a game in which children form a circle and start passing a hot potato. The counting starts with the first kid. Every nth toss the child left with the potato leaves the game. When a kid leaves the game, it passes the potato along. This continues until there is only one kid left.  

Create a program that simulates the game of Hot Potato. Print every kid that is removed from the circle. In the end, print the kid that is left last.  

*Examples*

|                 Input               |             Output            |
|-------------------------------------|-------------------------------|
|Tracy Emily Daniel<br>2                    |Removed Emily<br>Removed Tracy<br>Last is Daniel                                         |
|George Peter Michael William Thomas<br>10  |Removed Thomas<br>Removed Peter<br>Removed Michael<br>Removed George<br>Last is William  |
|George Peter Michael William Thomas<br>1   |Removed George<br>Removed Peter<br>Removed Michael<br>Removed William<br>Last is Thomas  |
