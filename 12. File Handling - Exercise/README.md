## **01.	Even Lines -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/12.%20File%20Handling%20-%20Exercise/01_even_lines/01_even_lines.py)
Write a program that reads a text file and prints on the console its even lines. Line numbers start from 0. Before you print the result replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.

*Examples*

|      text.txt     |      Output       |
|-------------------|-------------------|
|-I was quick to judge him, but is wasn't his fault.<br>-Is this some kind of joke?! Is is?<br>-Quick, hide here. It is safer. |fault@ his wasn't it but him@ judge to quick was @I<br>safer@ is It here@ hide @Quick@    |



## **02.	Line Numbers -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/12.%20File%20Handling%20-%20Exercise/02_line_numbers/02_line_numbers.py)
Write a program that reads a text file and inserts line numbers in front of each of its lines and counts all the letters and punctuation marks. The result should be written to another text file. 

*Examples*

|      text.txt     |    output.txt     |
|-------------------|-------------------|
|-I was quick to judge him, but is wasn't his fault.<br>-Is this some kind of joke?! Is is?<br>-Quick, hide here. It is safer.          |Line 1: -I was quick to judge him, but it wasn't his fault. (37)(4)<br>Line 2: -Is this some kind of joke?! Is it? (24)(4)<br>Line 3: -Quick, hide here. It is safer. (22)(4)          |





## **03.	File Manipulator -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/12.%20File%20Handling%20-%20Exercise/03_file_manipulator.py)
Create a program that will receive commands until the command "End". The commands can be:  
•	"Create-{file_name}" - Creates the given file with an empty content. If the file already exists, remove the existing text in it (as if the file is created again)  
•	"Add-{file_name}-{content}" - Append the content and a new line after it. If the file does not exist, create it and add the content  
•	"Replace-{file_name}-{old_string}-{new_string}" - Open the file and replace all the occurrences of the old string with the new string. If the file does not exist, print: "An error occurred"  
•	"Delete-{file_name}" - Delete the file. If the file does not exist, print: "An error occurred"  

*Examples*

|       Input       |      Comment      |
|-------------------|-------------------|
|Create-file.txt<br>Add-file.txt-First Line<br>Add-file.txt-Second Line<br>Replace-random.txt-Some-some<br>Replace-file.txt-First-1st<br>Replace-file.txt-Second-2nd<br>Delete-random.txt<br>Delete-file.txt<br>End          |The first command creates the empty file<br>After the first and second Add command, the content is:<br>First Line<br>Second Line<br>On the first Replace command, an error must occur<br>After the next two Replace commands, the content is:<br>1st Line<br>2nd line<br>After the first Delete command, an error occurs<br>Finally, the 'file.txt' file is deleted          |





## **04.	Directory Traversal -** [Solution](https://github.com/elenaborisova/Python-Advanced/blob/main/12.%20File%20Handling%20-%20Exercise/04_directory_traversal/04_directory_traversal.py)
Write a program that traverses a given directory for all files. Search through the first level of the directory only and write information about each found file in report.txt. The files should be grouped by their extension. Extensions should be ordered by name alphabetically. The files with extensions should also be sorted by name. report.txt should be saved on the Desktop. Ensure the desktop path is always valid, regardless of the user.

*Examples*

|       Input       |     Directory Content     |     report.txt    | 
|-------------------|---------------------------|-------------------| 
|.                  |Folder Example:<br>index.html<br>index.js<br>python.py<br><br>demo.pptx<br>log.txt<br>notes.txt<br>program.py |.html<br>- - - index.html<br>.js<br>- - - index.js<br>.pptx<br>- - - demo.pptx<br>.py<br>- - - program.py<br>- - - python.py<br>.txt<br>- - - log.txt<br>- - - notes.txt |


