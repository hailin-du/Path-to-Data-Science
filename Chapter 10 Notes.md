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
