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



## **03. Supermarket -** [Solution]()
Write a program that reads an input consisting of a name and adds it to a queue until "End" is received. If you receive "Paid", print every customer name and empty the queue, otherwise we receive a client and we must add him to the queue. When we receive "End", we must print the count of the remaining people in the queue in the format: "{count} people remaining."

*Examples*

|   Input   |         Output             |
|-----------|----------------------------|
|George<br>Peter<br>William<br>Paid<br>Michael<br>Oscar<br>Olivia<br>Linda<br>End |George<br>Peter<br>William<br>4 people remaining.  |
|Anna<br>Emma<br>Alexander<br>End                                                 |3 people remaining.                                |

