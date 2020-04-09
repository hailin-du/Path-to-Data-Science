# Files and Exceptions
In this chapter, you will learn how to handle a large amount of data, handle mistake (exceptions) to avoid the program crashing
1. You will also learn how to use exceptions as special objects to manage mistakes while running the program (the code)
2. You will also learn the module `json`, which allows you to store user data, avoid losing the data after the program stop running
  
***
* Learning how to handle file and store data allow you to use your program easier, user can choose what kind of the data they want to input, and when to input
* After using your program, the user is allowed to close the program or continue using it
* Knowing how to handle exceptions help you to manage scenarios when a file does not exist, or other problems that cause the program crashing
* You program can run much better while handling wrong data, no matter the mistakes are unintentionally or intentionally to try to destroy the program
* These skills will increase a program's adaptability, reliability, and stability

# 10.1 Reading Data From File
Text files can store as many amounts of data you want, such as data of weather, transportation, social-economic, literature and etc.
1. You want to write a program to read the content of text file, reset these data format, and write into the write so the browser can review the content
1. To use text file data, first, you need to read the file into memory,
1. Yuu can read the entire file content at once, or read the content by one line at a time

## 10.1.1 Reading an Entire File
In order to read a file, a file must exist first and include a few lines (data)
* The file we created contains pi's value to 30 decimal places, 10 decimal places per line
* We can either create the file by ourselves by naming it `pi_digits`, or download it directly from this repository

The below code will open and read the file
```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
```

In this program, the first line of code done many works
* No matter what method you planned to use the file, an `open()` function must be placed first in order to access the file
* `open()` function will receive an argument, to find a file based on the name you have given, then Python will try to look for  the file in the current directory (the same path with your current script)
* Python will base on the current python script's file location to locate the `pi_digits.txt` file
* Then `open()` function, in this case `open('pi_digits.txt`) will return object that represent file `pi_digits.txt` and store it in the variable name `file_object`
***
The keyword `with` means that after we have decided no longer need to access the file, we can either `open()` or `close()` the file
* However, if we choose to close the file too early, then we are no longer going to access the file and may cause bugs when the problem runs
* Also, if we never execute the `close()` function, then the file will never close
* When there is a bug, we may damage the original file and cause loss of data
* Sometimes it is difficult for us to choose when to close a file, but if we use the above coding structure, Python will close the file when it thinks it is the right timing

1. After we have a file object representing  `pi_digits.txt` file, we can use `read()` function to read the entire content

1. We have stored a long string into the variable name `contents` and print out the value of it

Output:
>     3.1415926535
>       8979323846
>       2643383279
>     
>     (There maybe an empty spaceline after the last line 2643383279 in your terminal)
***
But why there is an empty line?
* When the `read()` function reaches to **the end of the file**, it will **return an empty spaceline**, so when we print, there will be an empty line
* To delete, we can use the function `rstrip()`

```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
```
>     3.1415926535
>       8979323846
>       2643383279
**Remeber:**

`rstrip()` will delete any empty space from a string

## 10.1.2 File Paths/Directory
When we passing simple file like `pi_digits.txt`, Python look the file based on your current python script's path
* However, we may have saved the text file in a different path, like a different folder location
* For example, your Python script is created under the folder name `python_work`, inside the folder there is a folder name called `text_files`, and one of the file you want to access is stored inside
* In this case, even the file stored inside `python_work` folder, Python can't look for the file by going into the `text_files` folder
* To open a file, we need to provide a path, to let python to find the file in a specific location
* Since `text_files` folder is located inside the `python_work` folder, we can use the **relative file path** to let python to open the file

For Linux and OS X system we can use the code below
```python
with open('text_files/filename.txt') as file_object:
```

This line of code will let Python look for the file under `python_work` folder, and search for the `.txt` file you want inside the `text_files` folder

Below is a line of codes for Windows System, Windows use backslash `\` not forward slash `/`
```python
with open('text_files\filename.txt') as file_object:
```
You can tell Python the exact location of the file you want to open regardless where your python script is located
* We can use the **absolute file path**, when the relative file path is not working
* If the `text_files` folder is not stored in the `python_work` folder and it's stored in `other_files` folder, then the relative file path is not going to work

1.Absolute paths are usually longer than relative paths, so it’s helpful to store them in a variable and then pass that variable to `open()` function`

For Linux and OS X
```python
file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
with open(file_path) as file_object:
```
For Windows
```python
file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
with open(file_path) as file_object:
```

We can access any file in the system using the absolute file path
1. The most simple way to do this is, we will store the data file under the same location of the Python script file (same path)
1. Or store the file under the same directory, like a folder inside of a folder, like `text_files` folder example

**Warning**
For Windows System, sometimes the system can read `(/)` forward slashes (it may not work) 
1. If not, try to use `(\)` backslashes
1. However, since `(\)` has different functionality, to make sure the code is working, we should use original string method to call the file location, which adding `r` at the beginning of single quotation ```

## 10.1.3 Reading Line by Line
When reading a file, we may need to check every single line
* You may want to look for specific information or use some method to edit the content
For example, you may read the entire file, and use weather to find any line that contains the keyword `sunny`
* For newsletter, you may check for the hashtag <headline> line, and use a specific format to handle it
* We can use `for loop` to help us to read line by line
```python
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
```
>     3.1415926535
>     
>       8979323846
>     
>       2643383279

We first store the file, `pi_digits.txt`, that we are about to read in a variable name `filename`, that is must common way to handle a file
* The variable `filename` is not the exact file, it just to let Python know which file you are looking for 
* So we can always easily replace `pi_digits.txt` file to any other file you want to use

***
After we use `open()` function, we store the represented object in the variable name `file_object`; we also used the keyword `with` here to better open and close the file 
* To review the content, we use a `for loop` to check every line (the content) of the represented object

Then we realize, there are **more empty spacelines** between the content

**Why it is happening?** 
* Because inside the file, at the end of every line has an invisible newline character to move the data to the newline
* And `print()` function will also add a newline character, so now at the end of every line has two newline characters: one from the file and one from `print()` function
* To delete, we can use `rstrip()` function

```python
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
```
>     3.1415926535
>       8979323846
>       2643383279

Now the output has the same content has the file

## 10.1.4 Create A List That Contain Each Line From A File
When using keywords `with`, `open()`, return the file object only can be used **inside `with` block**
* To access the file object content outside the `with` block, we need to store the content of every line into a list and use the list outside `with` block
* We can process parts of the file immediately, or process then later
* Below is an example of saving `pi_digits.text` each line into a list inside the 'with` block
* Then we print out the list outside `with` block 

```python
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines() #1

for line in lines: #2
    print(line.rstrip())
```
* `readlines()` function will reach each line from the file and stored in a list, then the list store in a variable name `lines` inside the `with` block 
* Outside the `with` block, we can still use the variable `line`
* Then we create a simple `for loop` to read each line, since each line is an element of a list, so the content will be print it exactly as the file

## 10.1.5 Use File's Content
After reading the file into the memory, we can access the data in any method
* Below is an example to use pi's value
* We will create a string, it contains every digit from the file and without spaces
```python
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))
```
>     3.1415926535  8979323846  2643383279
>     36
Like previous example, we first open the file, and store everyline in a list
Like the previous example, we first open the file and store every line in a list
* We create a variable name `pi_string` to store pi's value
* Then we use `for loop` to add each line (data) into `pi_string` and delete the newline character
* However, the variable `pi_string` include the left whitespace of each line, to delete, we can use `strip()` function instead of `rstrip()`
```python
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip() # Change to strip()
print(pi_string)
print(len(pi_string))
```
>     3.141592653589793238462643383279
>     32
So we got 30 digits of the pi's value, and the length of this string, 32 (include the number 3 and the period)
* When reading a file, Python will read every file as a string data type structure
* We can convert the value (the data type) into a number by using `int()` or `float()`

## 10.1.6 Reading A Large File: One Million Digits
The previous code can handle file size much larger than that
* If we have a file that includes 1,000,000 digits of the pi's value, we do not need to edit the code
* We just need to pass a new file, a file that contains one million pi digits
* In here, we only printing the pi's value up to 50 digits, to avoid the terminal printing entire 1 million digits
```python
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:52] + '...')
print(len(pi_string))
```
The output shows that we do have a string containing pi to 1,000,000 decimal places:
>     3.14159265358979323846264338327950288419716939937510...
>     1000002
As long as your computer ram/memory is enough capacity, you can handle as much as data you want 
* (file is provided in this repository)

## 10.1.7 Does Pi's Value Include Your Birthday?
We can check if the pi's first 1 million digits value include your birthday by expanding the code
* We can first covert the number of a birthday as a string and look that up in `pi_string`
```python
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
```
>     Enter your birthday, in the form mmddyy: 051395
>     Your birthday does not appear in the first million digits of pi

We asked the user to input the birthday, then we check if the value exists in `pi_string`
* My birthday does not appear in the first million digits of pi :(
* After reading the file, you can do any analysis you want

# 10.2 Writing A File

The simplest way to store data is by writing the data into a file
1. By manually adding the data, even you close the entire program in the terminal, the data you input still exist
1. You can review the data after the program is closed, and even share the data or edit the data afterward

## 10.2.1 Writing A Emtpy File
In order to write text into a file, we need to provide another argument to the `open()` function, which telling python you are writing the text in the current opened file
* We will store a simple message into a file but not printing it
```python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
```

In this example, we provided two arguments to `open()` function, one is the name of the file, and another argument is `w`, which telling python we are using the `write mode` to open the file
* When opening the file, we can set the mode, which are:
     * `r` reading
     * `w` writing
     * `a` appending` 
     * `r+`  reading and writing 
* If you skipped the mode, by default, Python will only use the reading mode to open the file
* If the file you are writing in does not exist, `open()` function will create the file itself, then use `w` write mode to open the file
* However, if the file already exists, and you used the `w` write mode when python return to file object it will clean original file
1. We used `write()` function adding the string into the file
1. We didn't print the output in the terminal, but if you open the file` programming.txt`, you will see the line
1. Compare to a different text file in your computer, it has no difference; you can open the file, type in new value, copy the value, or paste other values into the file
***
I love programming.
***
**Remember:**
Python can only write string data type into the text file, to write number data type, you must convert the value from number to string type using `str()` function

## 10.2.2 Writing Multiple Lines
`write()` function will not add newline character at the end of your string, so the file may look different as you expected
```python
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")
```
If you open the `programming.txt` file, it will look like this
***
I love programming.I love creating new games.
***
To let every string become a unique line, you can add newline character in each line
```python
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
```
***
I love programming.<br/>
I love creating new games.
***
Now the output is different
* As always, we can use whitespace, tab, or empty line to control the output format

## 10.2.3 Append to A File
If you want to add new content instead of replacing the original content, we can use `a` append mode to open the file
* When you open the file with `a` append mode, Python will not clean the original file when returning the file object
* The new content you write into a file will be added **at the end of the file**.<br/>

Also, as always, if the file you want to open does not exist, Python will create the file your
* Lets add new content to the `programming.txt` file
```python
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
```
**programming.txt**
***
I love programming.<br/>
I love creating new games.<br/>
I also love finding meaning in large datasets.<br/>
I love creating apps that can run in a browser.<br/>
***
We provide the argument `a` to add the new content at the end of the file, **NOT** replace the original content
* We added new two lines and they will be added into `programming.txt` file
* The final output will include original content and newly added content

# 10.3 Exceptions 
Python will use exceptions to handle the program's mistakes as special objects
* When Python unable to handle the mistake, it will create exception objects
* If you write how to handle these exception codes, the program will continue to run
* If you didn't do anything, the program will stop and display a traceback, which includes a report of the exception that was raised<br>

Exceptions are handled with `try-except` blocks. A `try-except` block asks Python to do something, but it also tells Python what to do if an exception is raised
* When using `try-except` blocks, even an exception is raised, the program will still run
* It will show a friendly helpful error message, instead of a confused report from the traceback

## 10.3.1 Handle `ZeroDivisonError` Exception
You probably know that a number cannot be divided by 0, but we still let python do it
* You will see a traceback
```python
print(5/0)
```
>     Traceback (most recent call last):
>       File "yourfile.py", line 1, in <module>
>         print(5/0)
>     ZeroDivisionError: division by zero
Above traceback, it shows that `ZeroDivisionError` is an exception object
* When Python cannot follow your command, it will create this type of object
* Under this circumstance, Python will stop running the program, and point out where the exception is raised, and we can base on that to edit the code
* Next, we will tell Python what to do when this kind of exception is raised
* So, when this kind of exception happens again, we can be prepared

## 10.3.2 Use `try-except` Block 
When you think there is a mistake raised, you can write `try-except` blocks to handle the exception
* You will let Python try to run some codes first, and tell that if these codes cause exception what to do <br?

To handle `ZeroDivisionError` exception we use `try-except` blocks
```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero")
```
>     You can't divide by zero

* We write code `print(5/0)` under the `try` block, if the code inside the `try` block didn't raise an exception, Python will skip `except` block
* If there is an exception from the `try` block, then Python will go to the `except` block and execute the code inside
* In this case, `try` block has raised a `ZeroDivisionError` exception, so Python will execute the code inside the `except` block, which prints a friendly error message instead of a traceback
* If behind the `try-except` blocks there are more codes, Python will continue to run, because you already told Python how to handle an exception

## 10.3.3 Use Excpetion to Avoid Crashing
When error happened and the program still has work to complete, handling error becomes important
* For example, if the program requires the user to input a value, but the user input invalid value, the program will crash
* Then it is important to remind the user and prevent the program from getting crash
* We will create a simple calculator to handle division
```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
```
>     Give me two numbers, and I'll divide them.
>     Enter 'q' to quit.
>     
>     First number: 5
>     Second number: 0
>     Traceback (most recent call last):
>       File "yourfile.py", line 1, in <module>
>         answer = int(first_number) / int(second_number)
>     ZeroDivisionError: division by zero
* First, we asked the user to input a value and store in a variable `first_number`
* If the user didn't input `q` as quit, we continue to ask for the second number and stored in a variable 'second_number`
* Then, we will calculate the answer and store the value in a variable name `answer`
* The program didn't take control to handle any exceptions, so if it divides 0, the program will crash <br>

We should prevent letting the user seeing the traceback
* User can know the information that you didn't want to share in the traceback
* For example, the user will know the program file name, and see part of the code that didn't run through
* Sometimes, hackers can base on this information to make judgments on your code to see where is the weakest point to attack

## 10.3.4 `else` block
By adding `try-except` block for possible errors, we can increase the error resistant
* We will create `try-except` block to handle `ZeroDivisionError`, and expand our codes by adding `else` block that base on the `try` block
* Any codes that rely on the `try` block should be placed on `else` block
```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
```
>     Give me two numbers, and I'll divide them.
>     Enter 'q' to quit.
>     
>     First number: 5
>     Second number: 0
>     You can't divide by 0!
>     
>     First number: 5
>     Second number: 2
>     2.5
>     
>     First number: q
* We will let Python try to calculate the division in the `try` block
* `try` block only includes codes that may raise an exception
* Codes rely on the` try` block will be placed inside the `else` block
* If the calculation works, we use `else` block to print out the result
* `except` block tells Python what to do if `ZeroDivisionError` is raised
* If `try` block fails to execute, we will print out a friendly error message telling the user how to avoid this kind of mistake, to prevent  user seeing a traceback <br>

`try-except-else` blocks principles:
1. Python will first execute codes inside the `try` block; only codes that may raise an exception should place inside the `try` block
1. Sometimes you’ll have additional codes that need to run only when the codes in `try` block were successful; those additional codes should go to the `else` block
1. The `except` block tells Python what to do in case a certain exception arises <br>

By predicting possible errors, we can write a healthy program.
* Even the program has encountered invalid data or lacking certain value resources, the program can still run, prevent innocent user mistakes and malicious attacks

## 10.3.5 Handle `FileNotFOundError` Exception
The most common exception when handling a file is cannot find the file
* The file you  want to get access to probably store in other places or named differently, or maybe the file just don't exist
* We can always use `try-except` block to handle those situations <br>
Lets try to read a file that does not exist, `alice.txt`
```python
filename = 'alice.txt'
with open(filename) as f_obj:
    contents = f_obj.read()
```
>     Traceback (most recent call last):
>       File "alice.py", line 3, in <module>
>         with open(filename) as f_obj:
>     FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'

Python cannot read a file that does not exist, so an exception araised
* The last line of traceback tells the Python cannot find a file that it is trying to open
* In this example, an error is created by `open()` function
* To handle this, we will put `open()` inside the `try` block

```python
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
```

In this example, `try` block will cause the `FileNotFoundError` exception, so Python will then go to the `except` block that matches this error and execute the code stored inside
* A friendly message will be printed out instead of a traceback
* The program has nothing more to do if the file doesn’t exist, so the error handling code doesn’t help the program
* Lets expand the code to see how it works when handling multiple files


## 10.3.6 Analyzing Text
You can analyze an entire text file of a book
* Many classical works of literature are provided by a simple text file because there is no copyright
* In this chapter, we will Gutenberg （http:/http://gutenberg.org/), which provide a collection of literature that are available in the public domain
* It is a great resource if you interested in analyzing literature works
* Next, let's take *Alice in Wonderland* text, and analyze it how many vocabulary words it contains
* We will use`split()` function, it is base on a collection of strings to create a list of word, we will test it with a collection of strings that only contains `Alice in Wonderland`
```python
title = "Alice in Wonderland"
print(title.split())
```
>    ['Alice', 'in', 'Wonderland']
* `split()` function will split the string into many parts and store them in a list
* The output will be a list of words, however, some words will probably be punctuation
* To analyze the text file of *Alice in Wonderland*, we will use `split()` function, and calculate how many elements it contains, then tries to get an approximate number of how many words it contains
```python
filename = 'alice.txt'
try: # File contains UTF-8 file format, so we will need to analyze the file ignore illegal string
    with open(filename, encoding='gb18030', errors='ignore') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
 # Count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
```
**We are passing three arguments here**:<br>
1. Filename
1. encoding='gb18030' because the textfile contains UTF-8 file format
1. We will ignore those illegal string datatype 
1. You can try to ignore those two arguments if your codes work

>     The file alice.txt has about 29465 words.

* If `alice.txt` file is moved to the correct path, the `try` block will execute
* We then covert the variable content from a long string into a list of strings using `split()` function
* When we use `len()` we now can see how the list is
* Then we print out a message about how many words the file contains
* All these codes are placed inside the `else` block, only when `try` block is executed
* The number is pretty big because it also includes extra info about publication, but it’s a good approximation of the length of *Alice in Wonderland*

 ## 10.3.7 Working with Multiple Files
 Lets analyze more books
 * By doing that, we will first move the majority of codes into `count_words()` function (we will define this function), which easier for us to analyze multiple books
```python
def count_words(filename):
    # Count the approximate number of words in a file
    try:
        with open(filename, encoding='gb18030', errors='ignore') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
    # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = 'alice.txt'
count_words(filename)
```
Same Output:
>     The file alice.txt has about 29465 words.
We didn't change the codes much from the previous example, only putting the codes inside `count_words()` function and adding new notation <br>

Now, we can write a simple `for loop` to analyze multiple books and see how many words each book contains
* We will first store the file names we want to analyze in a list
* Then, we will call the `count_words()` function for each file in the list
* We’ll try to count the words for *Alice in Wonderland*, *Siddhartha*, *Moby Dick*, and *Little Women*
* We didn't include `siddhartha.txt` in the current Python script's path, so you will see how well our program handles a missing file
```python
def count_words(filename):
    # Count the approximate number of words in a file
    try:
        with open(filename, encoding='gb18030', errors='ignore') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
    # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
```
>     The file alice.txt has about 29465 words.
>     Sorry, the file siddhartha.txt does not exist.
>     The file moby_dick.txt has about 215830 words.
>     The file little_women.txt has about 189079 words.
In this example, using `try-except` blocks provided two significant advantages
1. Avoid the user seeing a traceback
1. The program will continue to find and analyze other files <br>

* If we didn't add that when the program can't find `siddhartha.txt` file, there will be `FileNotFoundError` exception and the user will see the traceback
* The program will also stop running and no longer analyze *Moby Dick* and *Little Women*

## 10.3.8 Failing Silently
In the previous example, we are telling the user there is a file we couldn't find
* However, we don't need to tell the user, sometimes we just want the program failing silently, as nothing has happened, continue running
* To fail silently, we can add `pass` statement inside the except block, which meaning don't do anything when it fails
```python
def count_words(filename):
    # Count the approximate number of words in a file
    try:
        with open(filename, encoding='gb18030', errors='ignore') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
    # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
```
>     The file alice.txt has about 29465 words.
>     The file moby_dick.txt has about 215830 words.
>     The file little_women.txt has about 189079 words.
Compare to the previous program, the only difference in this program is the `pass` statement
* Now, if there is a `FileNotFoundError` exception raised, the `except` block will execute the `pass` statement, which nothing will happen
* There will be no trackback nor output; the user only seeing each file contains how many words, but no signal telling the user there is a file not found <br>

The `pass` statement also acts as a **placeholder**
* It reminds you where your code you choose to do nothing
* For example, for this program, we may want to write the file name that we didn't find into a new file call `missing_file.txt`
* User won't see this file, but we can read this file and handle the problem of all missing files

## 10.3.9 Deciding Which Errors to Report
Under what circumstance we should report the error to the user<br>
<br>
Or, where we should fail silently?<br>

* If the user knows which file they want to analyze, then they may want to know which file didn't get analyzed, and tell the reason to them
* If the user wants to see the output only, and not interested in knowing which file they need to analyze, then we don't need to tell them which file is not found
* Showing the message that a user didn't want to see will lower a program's credibility
* Python's error handle structure allows you to control and share the level of error information with the user <br>

A well-written, tested program won't raise internal error easily, like logical or grammar errors
* However, programs that rely on external factors, such as user input, specific file path, network connection, then there may be  exceptions arise
* Based on programming experience, we can decide where the program should handle the `exception` block 
* And control the level of the error information you want to share with the user

# 10.4 Storing Data
Many programs require the user to input certain information
* Like, you want to let the user store preferences in a game or provide data for a visualization
* No matter where your focus is, the program will store user's information into a **list or a dictionary structure**
* When the user closes the program, you always want to store the information they entered
* A simple way to do this is using module `json` to store data <br>

`json` module allows you to cover simple Python data structure into a file, and when the program run next time it can load back the data of that file
* You can even use `json` between Python programs to share data
* More importantly, **JSON** data format structure is not only for Python
* This allows you to use **JSON**  formatted data to share any data you want with people using other programming languages <br>

The JSON (JavaScript Object Notation) format was originally developed for JavaScript. However, it has since become a common format used by many languages, including Python

## 10.4.1 Using `json.dump()` And `json.load()`
We first write a short program to store a list of numbers and then write another program that reads these numbers back into memory
* We will use `json.dump()` to store this list of numbers in the first program
* Then, use `json.load()` for the second program <br>

Function `json.dump()` will receive two arguments:
1. the data that needs to be stored
1. the file object that store the data
```python
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
```
* We imported the module `json`, and created a list of numbers
* Then, we choose a file name in where to store the list of numbers and use file extension `.json` to indicate that the data stored as `JSON` format
* Lastly, we use the function `json.dump()` to store a list of numbers into the file name`numbers.json`
* Since there is no output in our terminal, we can open the file `numbers.json` to see the result <br>
***
> [2, 3, 5, 7, 11, 13]
***
Now, we ill write another program using `json.load()` to load the list of numbers back into the memory
```python
import json

filename = 'numbers.json'

with open(filename) as f_obj:
    numbers = json.load(f_obj)
    print(numbers)
```
> [2, 3, 5, 7, 11, 13]
First, we have to make sure we are loading the correct file we just wrote
* This time, we just load the data, so no `w` writing mode is needed
* We then used function `json.load()` to load the data that is stored in `numbers.json` and save data into the variable name `numbers`
* Lastly, we print out the content of that file
## 10.4.2 Saving and Reading User-Generated Data
For user-generated data, it is good to use `json` to store them
* If we didn't save the data in some way,s when the program stop running we will lose all the user data
* Lets look at an example, the user will input their name and able to load the data back when the program starts next time
```python
import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
```
>     What is your name? Eric
>     We'll remember you when you come back, Eric!
* We asked the user to input a name and stored in a variable name `username`
* Next, we used `json.dump()` function, passing the data `username` and the file object and saved the data in that file
* Lastly, we print out a message letting the username know that we saved the data <br>

Next, we will write a program and greet the user who saved the name
```python
import json

filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")
```
> Welcome back, Eric!
* We used `json.load()` function to read the data that is stored in the `username.json` file
* Then, store the data we just read in a variable name `username`
* After the data, the username (the value inputted by the user), is loaded back to the memory, we can print out a message to greet the user <br>

Now, we will combine these two programs into one
* When this program is running, we will try to  get the data from the `username.json` file
* So, we will first write a `try` block to retrieve the username from memory if possible
* If the file does not exist, we will use `except` block to ask the user to input a username
* And store it into the `username.json` file (It will create one)
* When the program runs again, the data can be retrieved
```python
import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
```
We didn't add any new code here, just combining the previous two programs into one
* First, we will try to open the `username.json` file (if the file exists), then we will load the data of username back to the memory 
* And execute codes inside the `else` block  to print out a welcome back message
* If the file does not exist, there will be `FileNotFoundError` exception, so then Python will execute the code inside `except` block
* Which, is asking the user to input a username, then use `json.dump()` function to store that username and print out a message letting the username know that we saved the data <br>

No matter we execute the `except` block or the `else` block, both will show the output of the username and an appropriate message statement <br>
<br>
If the program is running for the first time, it will shows
>     What is your name? Eric
>     We'll remember you when you come back, Eric!
If not, then
> Welcome back, Eric!

## 10.4.3 Restrcutre/Refactor Codes
You will always encounter a situation that the code can run normally, but you can improve the code<br>
Which, splitting a series of functions to let each function perform a specific task
* Such a process is known as refactoring, making the code more understandable, clear, and easier to expand
* To refactor the code we just wrote, we can put the majority of logic into one or multiple functions
* The key point of the code is to greet the user, so we will put all the code inside a function `greet_user()`
```python
import json

def greet_user():
    # Greet the user by name
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")

greet_user()
```
We have given a new notation to tell the task of this function is carrying; This program is a little be clearer
* The `greet_user()` function is not only greeting the user, but also retrieving a stored username and ask the user to input one if the file doesn't exist <br>
Next, we will refactor the `greet_user()` function to not perform so many tasks
* We will be moving the part getting the user's input into another function
```python
import json
def get_stored_username():
    # Get stored username if available
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    # Greet the user by name
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")

greet_user()
```
The newly added function `get_stored_username` perform a clearer task
* Which, get stored username if the file available (if the file exist)
* If the file `username.json` does not exist, then function return `None`
* This will help us either return a value you are expecting, or return nothing
* Allow us to do a simple test with the return value of the function <br>

If we able to retrieve the data of the username, then we print out a welcome back message
* Otherwise, we ask the user to input a username value
* We can even split the `greet_user()` into another block of codes
* If the username does not exist, we ask the user to input one

```python
import json
def get_stored_username():
    # Get stored username if available
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    # Ask for a new username
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username
        
def greet_user():
    # Greet the user by name
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
        
greet_user()
```
In the above code, each function perform a specific task
* We called the function, `greet_user()` to print out an appropriate message either greeting the old user or welcoming the new user
* Therefore, we will use the `get_stored_username()`, this function only responsible for retrieving a stored username if one exists
* Then we will use `get_new_username()`, this function only responsible for getting a new username and storing it
* Such refactoring is an important process for us to write clearer codes, and help us better maintain and expand the codes

# 10.5 Conclusion
In this chapter, you learned
* How to use file
* How to read an entire file
* How to read file content line by line
* How to write data into a file
* How to append data at the end of a file
* What is an exception?
* How to handle program when possible exception it arises
* How to store Python data structure when there is user-generated data
* How to avoid user inputting data again when the program stop

