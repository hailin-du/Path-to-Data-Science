# 7.1 Understanding `input () Function`
* `input() function` stop the program and wait for the user to input (enter) text 
* Then python will save the value in a variable
```python
message = input("Tell me something, and I will epeat it back to you:")
print(message)
```
Hello everyone!
>     Tell me something, and I will epeat it back to you: Hello everyone!
* `input() function` should give hint or instruction, letting the user know what to do

* First, the user will see "Tell me something, and I will repeat it back to you:"
* Second, the program will wait the user until the user input something and press enter
* Third, the value will be saved in message and print the message out

#### Sublime Text cannot run in the program, it has to be run in the terminal for the user to input the value

## 7.1.1 Write Clear Program
When you use `input() function`, always use a clear instruction, letting the user know what info you want the user to provide
```python
name = input('Please enter your name: ')
print('Hello, ' + name + '!')
```
Eric
>     Please enter your name: Eric
>     Hello, Eric!
* Sometime your instruction is more than one line
* You can save the message first, then passed to the `input() function`
```python
prompt = 'If you tell us who you are, we can personalize the messages you see.'
prompt += '\nwhat is your first name? ' # Adding one more string into the variable name prompt

name = input(prompt)
print('\nHello, ' + name + '!')
```
Eric
>     If you tell us who you are, we can personalize the messages you see.
>     What is your first name? Eric
>
>     Hello, Eric!

## 7.1.2 Use `int() fucntion` to Get Number Balue
When you use `input() function`, python reads value as string
```python
age = input('How old are you? ')
age
```
21
>     How old are you? 21
>     '21' # String not number
```python
print(age)
age >= 18 # Error will occur
```
Cannot compare string to a number
>     TypeError: unorderable types: str() >= int()

use `int() function` to conver the string into a number type
```python
age = input('How old are you? ')
age = int(age)
age >= 18 # No Error after convert
```
21
>     How old are you? 21
>     True

#### Case: We will test a person to see if he or she is tall enough to ride on the coller roaster
```python
height = input('How tall are you, in inches? ')
height = int(height) #convert string into integer

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'will be able to ride when you're a little older.")
```
71
>     How tall are you, in ches? 71
>     You're tall enough to ride!

## 7.1.3 Acessing % Modulus
* `%`  shows the remainder of division
* If one number can be perfectly divided, then the reminder is 0
* You can use `%` to predict and see if a number is odd or even
```python
print(4 % 3)
print(5 % 3)
print(6 % 3)
print(7 % 3)
```
>     1
>     2
>     0
>     1

#### Case; Tesing a number is even or odd
```python
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + ' is even.')
else:
    print("\nThe number " + str(number) + ' is odd.')
```
Even number cannbe perfectly divided by 2, so when a number divided by 2 using %, the remainder is 0, that means it is a even number
42
>     Enter a number, and I'll tell you if it's even or odd: 42
>
>     The number 42 is even.
***
***

# 7.2 `while` Loop Introduction
Different than `for` loop, '`while` loop is running forever until specific condition is not meet

## 7.2.1 Use `while` Loop
We can use `while` loop to count 1 to 5
```python
current_number = 1 
while current_number <= 5:
    print(current_number)
    current_number += 1
```
* First, the set a variable and start counting from 1
* Then, we **set a condition** if the number is smaller or equal to 5, the loop continue
* Each time of the loop, we add one value (1+1, 2+1, 3+1...) to current_number variable
* As long as the condition is met, current_number <= 5, the loop continue
* Once the condition greater than 5, the loop stop

#### Game is always using `while` loop, to ensure that when a player wants to play a game, the player can continue playing it
#### If player wants to stop, the program stop 

## 7.2.2 Letting the User to Choose When to Quit
We can use `while` loop to set a condition for the program

We will define a quit value, if the user didn't input the quit value, the program will continue to run
```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit` to end the program. "

message = "" # set the message as as a empty string, allow the python to compare
while message != 'quit': # When running the first time, message "" (empty string) will be used to compare with quit
    message = input(prompt)
    print(message)
```
Hello everyone! (first time input)

Hello again. (second time input)

quit (third time input)

>     Tell me something, and I will repeat it back to you:
>     Enter 'quit' to end the program. Hello everyone!
>     Hello everyone!
>     
>     Tell me something, and I will repeat it back to you:
>     Enter 'quit' to end the program. Hello again.
>     Hello again. 
>     
>     Tell me something, and I will repeat it back to you:
>     Enter 'quit' to end the program. quit
>     quit

* If message is not set at the beginning, python has nothing to compare, which cannot run the program
* Until the user enter quit, the program will continue to run


1. First, the we define a instruction, letting the user to know that he or she has two choices
      1. Enter a message or enter 'quit'
2. Then, we created a varaible (message) to store user's input (value)
3. If nothing was enter for the first time, the program cannot run, so we set the value as "" (empty string)
4. We have activated the `while` loop, then print out the message and wait for user to enter something for the first time
5. No matter what value the user has entered, value will be stored in the variable name `message`
6. Then, python will check the value to see if it equals to 'quit', if it does the program stop
7. But, the program also print out the message 'quit' to let the user know that quit is being entered

We can avoid the word 'quit' to print using `if statement`

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit to end the program. "
message = "" 
while message != 'quit': 
    message = input(prompt)
    
    if message != 'quit': # add if statement to avoid printing the word 'quit'
        print(message)
```

## 7.2.3 Use Sign (Mark)
In gaming, there are many conditions causing the stop of a program.
* For example, a player has finished eliminating all the enemies or the city is he is protecting is being destroyed
* We cannot include all these conditions within the `while` loop
* In this case, we create a sign (a mark), which a varaible to see if the program still being activated (continuing)

Sign, here, is treated as a **traffic (signal) light**
* We will assign the condition `True` to the program for the program to run, and `False` to stop the program
* Then, while loop only checking one condition

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit to end the program. "

active = True #always being activated (continue running)
while active: # while active True
    message = input(prompt)

    if message == 'quit': 
        active = False # change the variable name active False if 'quit' is being entered 
    else: # we can use elif to define other condtions to stop the program when the condition is being met
        print(message)
```

## 7.2.4 Use `break` Statement to Exist the `while` Loop
```
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit when you are finished.) "

while True:
    city = input(prompt)

if city == 'quit':
    break
else:
    print("I'd love to go to " + city.title() + '!')
```
* We will start the `while` loop with True, until it meets the condition 'quit' and execute `break` statement

>     Please enter the name of a city you have visited: New York
>     (Enter 'quit when you are finished.)
>     I'd love to go to New York!
>
>     Please enter the name of a city you have visited:
>     (Enter 'quit when you are finished.) San Francisco
>     I'd love to go to San Francisco!
>
>     Please enter the name of a city you have visited:
>     (Enter 'quit when you are finished.) quit

## 7.2.5 Use `continue` Statement Inside the Loop
* `continue` statement allows us to go back to the beginning of the loop
* It based on the result from the condition test to determine the loop continue or go back to the beginning of the loop
* `continue` statement doesn't like `break`, `break` *will not* execute the remaining code

Lets see how `continue statement` works by counting 1 to 10, we will only print out the odd number
```
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
```
>     1
>     3
>     5
>     7
>     9
* If the variable current_number has no remainder, then the loop goes back to the beginning of the loop 
* The code `print(current_number)` will be skipped, because `continue` means skip the remaining codes
* If the current_number cannot be perfectly divided and the remainder is not equal 0
* Then the following code will be excuted (print out the current number)

## 7.2.6 Avoiding Infinite Loop
Every `while` loop must has a way (condition) to stop the program
```python
x = 1
while x <= 5:
    print(x)
    x += 1
``
#### But if you forgot the code x += 1, the loop will be running forever!
```python
x = 1
while x <= 5:
    print(x)
```
>     1
>     1
>     1
>     1
>     1
>     1
>     ...

#### You can press **ctrl+c** in the terminal to quit the loop
* If you wish to set a specific value to stop the program, make sure double checking it first
* Add a loop condition, set it as `False` or `break`
***
***
# 7.3 Use `while` Loop to Handle List and Dictionary
* In order to store a large amount of users data, we need `while` loop
* `for` loop is a effiecent way, but for loop is not suppose to be used to edit the list
* Otherwise, it will cause python ha a difficult time to track each element
* To go over the list and edit it, we can use `while` loop
* Using `while` loop with list and dictionary, we can collect, store and organize a large amount of data input for future reference

# 7.3.1
* For example, a list contains newly registered users but the users haven't been verified yet
* After verifying these users, move these users to the verified list
* We can use while loop to extra users from unverified and add them into the verified list

```python
unconfirmed_users = ['alice',' brian', 'candace'] # created a list for users that are waiting to be verified
confirmed_users = [] # a list that after verification

while unconfirmed_users: # verify all the users until no user in the unconfirmed_users list
    current_user = unconfirmed_users.pop() 
    
    print('Verifying user: ' + current_user.title())
    confirmed_users.append(current_user) # move the user into confirmed_users list

# showing all verified users
print('\nThe following users have been confirmed:')
for confirmed_users in confirmed_users:
    print(confirmed_users) 
```
>     Verifying user: Candace
>     Verifying user: Brian
>     Verifying user: Alice
>
>     The following users have been confirmed:
>     Candace
>     Brian
>     Alice

Understanding the Process
* There are two lists:
    * A list that contains unverified users 
    * Another list to store verified users
* `while` loop going forever until the unconfimred_users list becomes empty
* `pop() function` is used to delete a single element at a time, which is the last position of element in the unconfirmed_users list
* Candace will be deleted first
* We will add the verified user into confirmed_users list
* The list of unconfimred_users will be shorter and shorter, until it is empty

## 7.3.2 Delete Specific Element in the List
* Use `remove() function` to delete a specific element
* What if your list has a **repeatable** element?
* We can use `while` loop until the list no longer contains that element (value)
```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```
* `while` loop will continue to check the list to see if it contains the word 'cat'
* Each time of the loop will remove the element named 'cat'

## 7.3.3 Allowing the User to input Value to Fill Dictionary
* We can use `while` loop to guide the user to enter any amount of data
* Each loop will store the user's name and answer, 
* And we save data into the dictionary to associate the user and the answer

```python
responses = {}
polling_active = True # set a sign, to see the poll continues

while polling_active:
    name = input('\What is your name? ') # given instruction
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response # store the answer into dictionary
    
    repeat = input('Would you like to let another person respond? (yes/ no) ') # check to see if more people want to join the poll
    if repeat == 'no':
        polling_active = False

# Showing the result
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + ' would like to climb ' + response + '.')
```
>     What is your name? Eric
>     Which mountain would you like to climb someday? Denali
>     Would you like to let another person respond? (yes/ no) yes
>
>     What is your name? Lynn
>     Which mountain would you like to climb someday? Devil's Thumb
>     Would you like to let another person respond? (yes/ no) no

>     --- Poll Results ---
>     Lynn would like to climb Devil's Thumb.
>     Eric would like to climb Denali.
Understand the Process
* We first created a empty dictionary
* Then, we set a sign (mark) for the variable name `polling_active`, if it stays `True`, `while loop` continue to run
* We ask the user's names and the moutains that he or she wants to climb (name as key, moutain value as paried values)
* Store the information into dictionary, name `reponses`
* Ask the user if another person wants to participate, if no, polling-active changes to ·False· - stop the program
* Lastly, we print out the result
***
***
# 7.4 Conclusion
* In this chapter, we have used `input() function`
* Used `while` loop
* Multiple ways to control `while` Loop - Set sign, use `break` statement, and `continue` statement
* Used `while` loop to move elements between lists
* Delete a specific elements in a list
* Combine `while` loop with list and dictionary
