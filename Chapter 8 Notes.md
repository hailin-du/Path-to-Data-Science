# Chapter 8 - Functions
# 8.1 Defining a Function
* When you have defined a function, you can use that function
* By doing that, you don't need to write the code repeatedly
* You can call the function to run a specific task

Example - Define an Easy Function

```python
def greet_users():
    # Display simple greeting
    print('Hello!')

greet_users()
```
> Hello!

Above code is an example of how we just defined a function
* The name of the function is `greet_users()`, at this point, it doesn't need any info to be filled inside the parentheses
(However, you must include parentheses ( ) after the name `greet_users`, and end with a colon :)
* Following, the indent of the code is the structure of the function
* We commented the code by using #
* The only code inside the function is `print('Hello!')`, so this function only does one specific work, which prints out Hello!
* To use the function, we can **call** the function by calling the **function name** and **use parentheses with necessary information**


## 8.1.1 Passing Data (Element) to the Function

We will add `username` inside the parentheses of the function `greet_users()`
* By adding `username`, the function will accept any element you give to the username
* Now, the function requires you to give aa element to the username

```python
def greet_users(username):
    print('Hello, ' + username.title() + '!')

greet_users('jesse')
```
> Hello, Jesse!

* `greet_users('jesse')` use the function `greet_user()`
* Passing the infomration that is needed for the `print()` statement

## 8.1.2 Argument (Data (Element) You Pass) and Parameter (Variable - Data (Element) Needed to Perform A Specific Task)
* `username` is a **parameter**, data you are going to pass
* Data is `jesse`, which is an **argument**
* Argument is used when using the function, it passes data to the function
* When we are using the function, we need to put data inside the parentheses ()
* In `greet-user('jesse')`, we are passing 'jesse' to `greet_user()` function, and the value will be stored in `username`
***
***
# 8.2 Passing Argument (Data)
Function can contain multiple parameters
* Therefore, when using a function, we can pass **multiple elements** to it 
* We can **order** the **argument** - the argument's order and the parameter's order are the same
* Or, uses **keyword argument**, every parameter is created by the variable name, so we can just **assign the element** to the parameter when calling the function
* We can even use list or dictionary

## 8.2.1 Argument Position (Position/Order) Association 
When we use the function, python must associate every argument with the correct parameter

So the position/order is the key that can be used to create the association

```python
def describe_pet(animal_type, pet_name):
    # Display pet info
    print("\nI have a " + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet('hamster','harry')
```
>     I have a hamster.
>     My hamster's name is Harry.

* The function is being defined that requires `animal_type` and `pet_name` 
* When using the function, we need to provide elements for `animal_type` and `pet_name`
* `'hamster'` as a argument, stored in `animal_type` in a parameter
* `'harry'` as a argument, stored in `pet_nam` in a parameter
* In the function, it used both paremeter

#### 1 Using the Function Multiple Times
```python
describe_pet('dog','willie')
```
>     I have a dog.
>     My dog's name is Wille.
We can use the function multiple time by passing elements again, which has increased our efficiency

#### 2 The Order of Argument is Important
```python
describe_pet('harry','hamster')
```
>     I have a harry.
>     My harry's name is Hamster.
we have assigned wrong elements to parameters

## 8.2.2 Key-Word Argument Association 
* We are matching the elements with the parameters, so arguments can be passed to the correct parameter
* In this case, you DON'T need to care about the order of arguments, because we just pointed the parameters out

```python
describe_pet(pet_name='harry', animal_type='hamster') 
```
```python
describe_pet(animal_type='hamster', pet_name='harry',) 
```
Both function calls will return the same outputs, the order does not matter

## 8.2.3 A Default Element/Value
We can give the parameter a default value
* When we use the function, unless we provide an argument, the function will use the default element
* We can skip the part giving an argument to `animal_type`

```python
def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet(pet_name='willie')
```
>     I have a god.
>     My dog's name is Willie.

```python
describe_pet('willie`)
````

Above code will have the same output

```python
describe_pet(pet_name='harry', animal_type='hamster') 
```

We have provided an argument, so the function will **ignore** the default element `dog`

* If no `animal_type` is being provided, python will set the default as `dog`
* Keep in mind that, the **order is IMPORTANT here
* We have to put parameter that is WITHOUT a default element at the beginning, then we put the one with default element at the end
* This allows python to read the argument correctly and associate with the correct parameter
* In this case, we put `pet_name` first, `animal_type='dog'` at the end



## 8.2.4 Using the Function Other Ways (Equivalent Function Calls)
We can use Argument Position Association, Key-Word Argument Association, and set the Default Element/Value at the same time
```python
def describe_pet(pet_name, animal_type='dog')
```
* Under this condition, we must provide an argument to `pet_name`
* If you don't want the default value from the `animal_type`, then we must provide an argument too

Below are multiple ways using the function with the same output
```python
# A dog name Willie
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster name Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
```

## 8.2.5 Avoiding Argument Error
For example, if the function cannot identify the argument, or you pass too much or too little argument to the function, it will have an association error

```python
def describe_pet(pet_name, animal_type):
    print("\nI have a " + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')
describe_pet()
```
>     TypeError: describe_pet() missing 2 required positional arguments: `animal_type` and `pet_name`
* The trackback which parameter is a missing argument
* Therefore, naming your parameter correctly is important, because it will tell us what element is needed

***
***

# 8.3 Return Element/Value
Function can also handle data processing, and return one or a series of values
* We can move those difficult tasks inside the function, and let function to handle for us
We can use `return statement` to return the value back to you

## 8.3.1 Return Simple Element/Value
```python
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)
```
> Jimi Hendrix
* Function defined to receive parameters, `first_name` and `last_name`
* Then, the function combine first and last name, and add a space between it
* Return the value (in capitals) using `return statement`
* Returned value stored in `musician`, then print out `musician`

Even though the follow code has the same output
```python
print('Jimi Hendrix')
```
But when we need to store a large amount of data, function like this is very useful
* When you have stored the first and the last name separately, we can call this function can combine them for us

## 8.3.2 Making Arguments Selectable
For example, if we are adding the middle name to the function
```python
def get_formatted_name(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
```
> John Lee Hooker
Hoever, not everyone has a middle name
* If no `middle_name` argument is not provided, an error will occur
* Therefore, we can set a default value to middle_name
* The default value will be an **empty string**
* Plus, we will move the `middle_name` **to the end** 

```python
def get_formatted_name(first_name, last_name, middle_name=''): # empty string = False
    # return nice full name
    if middle_name: # if string provided = True
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
    
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
```
>     Jimi Hendrix
>     John Lee Hooker

In this case, `full_name` is created based on three possible arguments
* We have defined the `first_name` and `last_name`, because everyone has one
* Since `middle_name` is selectable, we put that at the end
* Inside the function, we are using `if statement` to check if the argument of `middle_name` is being provided

Python read any **non-empty string as True**
* So if the argument of `middle_name` is provided, will return the value **True** and execute the code
* If no argument is provided, the `middle_name` will be reviewed as **False**
* Then `else statement` will be executed

However, make sure the `middle_name` is at the **END** (the last position) when defining your function

## 8.3.3 Returning a Dictionary
Function can return any type of element/value, including list, dictionary or even a more complicated data structure
```python
def build_person(first_name, last_name):
    # return a dictionary that includes a person's info
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)
```
> {'first': ' jimi', 'last': 'hendrix'}

We can easily expand the code to store more data, such as middle name, age, career, or any other data you want
```python
def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix', age=27)
print(musician)
```
We have used `if statement`, if no argument is provided to `age`, the function will still save a person's first name and last name

## 8.3.4 Combining Function with a `while` Loop
```python
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

# This is an infinite loop
while True:
    print('\nPlease tell me your name:')
    f_name = input('First name: ')
    l_name = input('Last name: ')

    formatted_name = get_formatted_name(f_name, l_name)
    print('\nHello, ' + formatted_name + '!')
```
The loop is missing a method to quit/stop the program

Always remember **set a rule to stop the loop**

```python
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print('\nPlease tell me your name:')
    print("(enter 'q' at any time to quit)")
    
    f_name = input('First name: ')
    if f_name == 'q':
        break

    l_name = input('Last name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print('\nHello, ' + formatted_name + '!')
```
>     Please tell me your name:
>     (enter 'q' at any time to quit)
>     First name: eric
>     Last name: matthes
>
>     Hello, Eric Matthes!
>
>     Please tell me your name:
>     (enter 'q' at any time to quit)
>     First name: q

We have added a message to tell the user when to quit. Every time the user input something, the program will check if the user has entered a quit value. 
* If it does, we quit the program
* If the input is not 'q', we continue the program 

***
***

# 8.4 Passing a List
Sometimes, passing the list to a function is very efficient. The list can include any possible data, such as name, number, or even a complicated object like the dictionary
* After passing the list, the function can access the element directly

The below code will pass the list to a function and greet everyone
```python
def greet_user(names):
    # Greet everyone in the list
    for name in names:
        msg = "Hello, " + name.title() + '!'
        print(msg)

usernames = ['hannah', 'ty', 'margot'] # username list
greet_user(usernames)
```
>      Hello, Hannah!
>      Hello, Ty!
>      Hello, Margot!
* We created a `greet_user(names)` function, the function will receive a list of names and stored in `names`
* The function will go over the list and print a greeting message for each user

## 8.4.1 Editing a List inside a Function
We can edit list inside a function

The edit/change is **forever**, it is helpful to manage a large amount of data

For example - A 3D Printer Company need to print design model
* The design model will be saved in a list
* After the design model is printed, pass that model to another list
```python
# First, create a list that includes the design model that needed to print
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# imitate we are printing the model
# After we printed the model, move it to the completed_models list
while unprinted_designs:
    current_design = unprinted_designs.pop()
    
    # pretend there is a printing process the model
    print('Printing model: ' + current_design)
    completed_models.append(current_design)

# showing the models that is being printed
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
```
>     Printing model: dodecahedron
>     Printing model: robot pendant
>     Printing model: iphone case
>
>     The following models have been printed
>     dodecahedron
>     robot pendant
>     iphone case
* We first created a `unprinted_designs` list, and a **empty** `completed_model` list to store future element
* As long as the `unprinted_designs` still has an element, the `while` will continue
* Each loop will delete a design model using `pop function`, and stored a variable called `current_design`
* Then it shows a message of printing the model and move that element into `completed_model`

We can organize the code by separating the tasks into two functions

```python
def print_modesl(unprinted_designs, completed_models):

    # imitate we are printing the model
    # after we printed the model, move it to the completed_models list
    
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        
        # pretend there is a printing process the model
        print('Printing model: ' + current_design)
        completed_models.append(current_design)

# Second Function
def show_completed_models(completed_models):

    # showing the models that is being printed
    
    print("\nThe following models have been printed")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_modesl(unprinted_designs, completed_models) 
show_completed_models(completed_models)
```
First Function
* The first function needs two arguments, which a `unprinted_designs` list and a `completed_models` list
* This function will pretend the printing process, and remove the element one by one from the `unprint_designs`
* Each element will be added into `completed_models` list

Second Function
* The second function only need one argument, which the `completed_models` lust
* The function will print the name of each model

The above functions will have the same output as the previous one, but more is organized and easy to read

```python
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_modesl(unprinted_designs, completed_models) 
show_completed_models(completed_models)
```
* We have created a `unprinted_designs` list, and an **empty** `completed_models` list to store model that is being printed
* Because we have defined two functions, we just need to pass the correct arguments to the correct parameters
* We called the `print_models()` function, and pass the correct arguments to it - to show the printing process
* Then, we called the `show_completed_models()`, and pass the `completed_models` list to it - to print out the model names

This allows us to understand the code easily, and easy to expand or maintain the program
* If need to print other design models, we can just call the `print_models()` function again
* Each function will handle one specific task

## 8.4.2 Preventing the Function From Editing the List
Sometimes, we need to stop the function to edit the list

For example, we may want to keep the `unprinted_designs` list for future references
* To solve that, we can create a copy of the list, not the original list

```python
function_name(list_name[:])
```

**Slicing** allows us to create a copy of a list

To keep the `unprinted_designs` list, we can do the same

```python
print_models(unprinted_designs[:], completed_models)
```
***
***

# 8.5 Passing Arbitrary Numbers (As Many As You Want) of Arguments
Sometimes, you don't know the function will receive how many arguments
* Python function allows you to collect as many as arguments you want
* For example, a function to make a pizza, it needs to take many toppings
* But you don't know how many toppings the customer is going to order

The below function only has one parameter, which `*toppings`
* No matter how many arguments are being provided, the parameters will collect them

```python
def make_pizza(*toppings):
    # printing all the toppings that the customer has ordered
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

>     ('pepperoni',)
>     ('mushrooms', 'green peppers', 'extra cheese')

The Parameter `*toppings`, the `*` star created a topping empty tuple, and put all the topping elements inside the tuple
* The `print statement` proves that python can handle one, three, or even more arguments
* The function used a similar way to handle different calling
* Remember, the python has put the arguments into a tuple, even it is receiving one argument

Now, we will replace the `print statement` with a loop, to go over the topping list and describe the customer pizza
```python
def make_pizza(*toppings):
    # describe the pizza
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

>     Making a pizza with the following toppings:
>     - pepperoni
>     
>     Making a pizza with the following toppings:
>     - mushrooms
>     - green peppers
>     - extra cheese

No matter how many arguments the function is receiving, this grammar will always work!

## 8.5.1 Combine Argument Position Association with Arbitrary Numbers of Arguments You Want
* For function to receive different types of arguments, we must put the parameters that receive arbitrary numbers of arguments **at the end**
* Python will first match the position argument or key-word argument
* Then, put the rest of the arguments into the last parameters

```python
def make_pizza(size, *toppings):
        # describe the pizza
        print('\nMaking a ' + str(size) +
              '-inch pizza with the following toppings:')
        for topping in toppings:
            print('- ' + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')   
```

>     Making a 16-inch pizza with the following toppings:
>     - pepperoni

>     Making a 12-inch pizza with the following toppings:
>     - mushrooms
>     - green peppers
>     - extra cheese

Python will first receive the argument and store that into `size`, and put the rest into a tuple named `toppings`
* First is `size`, then is `toppings`

## 8.5.2 Use Key-Word Association With Arbitrary Numbers of Arguments You Want
Sometimes, a function needs to receive arbitrary numbers of arguments without knowing what kind of elements will be passed
* Under this condition, we can define the function to receive arbitrary numbers of key-value paired elements (no matter how many of them being passed)
* For example, creating a user profile - you know that you will receive user's info, but not knowing what kind of info you will be receiving

Below is the code show the `build_profile()` function to receive first and last name, and arbitrary numbers of key-word arguments

```python
def build_profile(first, last, **user_info):

    # create a dictionary, that includes the info we know about the user
    
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert','einstein',
                             location='princeton',
                             field='physics')

print(user_profile)
```

> {'first_name': 'albert', 'last_name': 'einstein', 'location': 'princeton', 'field': 'physics'}


* `build_profile()` function will require us to provide first and last name arguments
* It allows the users to provide as many as key-word paired elements
* `**` double stars created an empty dictionary, and put any key-word paired elements inside
* Inside the function, it can access the element in the `user_info` like any other dictionaries

**Understanding the Process**
1. Inside the `build_profile()` function, we created an empty profile dictionary to store basic user info
1. We put first and last name inside that dictionary, because the function will definitely receive those two elements
1.  `for key, value in user_info.items():` allows us to go over each key-word paired element and add them into `profile` dictionary
1. Lastly, we return those elements back to the `profile` dictionary
1. We called the function by providing:
   1. first name `albert`
   1. last name `einstein`
   1. key-word paired element, location = `princeton`
   1. key-word paired element, field = 'physics')
1. It will return to the `user_profile` through the function and print out the output

No matter how many key-word paired elements are provided, the function can handle them correctly

# 8.6 Saving Function in the Module
Function can separate a block of codes from the main program

By giving a descriptive name to the function, the main program can understand the task of that function easily
* We can save that function as a module in a separate file, and load that module into the main program
* `import statement` allows you to use the code of a module at your current program file

## 8.6.1 Importing a Saved Module You Just Created
By saving the function in a separate file, we can **hide the detail** of the code, and focus on **a higher logical layer**
* It also allows you to use the function repeatedly
* Plus, you can share the module with different programmers instead of sharing the whole program file

```python
def make_pizza(size, *toppings):
        # describe the pizza
        print('\nMaking a ' + str(size) +
              '-inch pizza with the following toppings:')
        for topping in toppings:
            print('- ' + topping)
```       
We created a function saved in the `pizza.py` file

```python
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') 
```
Then, we create second file, name `making_pizzas.py` 

When reading the file, `import pizza` open the file named `pizza.py` 
* It will copy the function into the current program file (you don't see the copied code)
* Python will run these codes behind the screen
* All you need to know is, in `making_pizza`, you can use the function from `pizza.py file`


To call the function of a module, you can call the module name you want to import and the function name, using `.` period to connect them
* module `piiza`, function name `make_pizza()`
* To use `module_name.function_name()`, which `pizza.make_pizza()`

# 8.6.2 `import` Specifc Function
You can `import` specifc function from a module
```python
from module_name import function_name
```
You can import as many as functions you want using , comma
```python
from module_name import function_0, function1, function_2
```

For the previous example, if we want to import specific function

```python
from pizza import make_pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') 
```

If you use this method, you don't need the period when you call the function

Because we have `import` the function by calling the function name, so we can just use the function directly 

# 8.6.3 Using `as` to Assign Different Function Name
If the name of the function you imported has conflicts with variables or functions  in the current program file, we can give a different name to a function
* If the function name is too long, we can consider given a different name as well

```python
from pizza import make_pizza as mp


mp(16, 'pepperoni')
m[(12, 'mushrooms', 'green peppers', 'extra cheese') 
```

We have renamed the function `make_pizza()` as `mp()`
## When we use the function, we can just call `mp()`
## It will avoid the conflict, if the current program file contain variable or function name named `make_pizza()`

```python
from module_name import function_name as fn
```

## 8.6.4 Using `as` to Assign Different Module Name
Similar, if the module name is too long, we can assign a shorter name
```python
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') 
```

We assigned a different name for the module
* When we call the function, we can use `p.make_pizza`, not `pizza.make_pizza()`
* By doing this, we can pay more attention to function name (it is always more important than the module)

```python
import module_name as mn
```

## 8.5.5 `import` All the Functions from a Module
### Using `*` star to allow python to import all the functions
```python
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') 
```

1. The star '*'  in `import statement` will copy all the functions into the current program file
1. Because we have imported every function, we can just use the function by calling the function name
1. However, when importing a large module, we should avoid this method because:
    1. Because the function name may have conflict with you current program file
    1. Python encounter simialr function names and variables, and replace them, not import them

The best way is only to import the function you need or import the module with a `.` period 
* This allows you to read the code more clearer and more understandable
```python
from module_name import *
```

## 8.7 Function Writing Guide（Styling Function)
There are a few things you should remember when writing a function
* Give a descriptive name to the function, and only using lower case and `_` underline - this will help you and others to understand what does the function do
* Every function should include notation/comments to describe its task -
* A well-written documented notation allows others to use the function by reading along
* Others should only know the function name, the arguments, and the return elements type when using the function

When writing parameters, equal sides should not contain empty space
```python
def function_name(parameter_0, parameter_1='default value`)
```
When calling the function, we should also follow this rule
```python
function_name(value_0, parameter_1='value`)
```

[PEP 8](https://www.python.org/dev/peps/pep-0008/) recommends that each line of code should not exceed 79 characters

If there are many parameters, causing the function exceeding 79 characters, we can press `Enter` key at the left parenthesis ( and press `Tab` key twice to indent the parameters

```python
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    function body...
```
Usually, your python editor allows you to line the code up

If a program or a module includes many functions, we can use double space lines to separate these functions, so we know when a function starts and ends

Every `import statement` should be put at the beginning of the file, except the beginning of the file is used to describe what the program does

***
***

# 8.8 Conclusion
* You learned how to write a function
* Passing arguments, and let the function access the arguments
* Understand the Arguments Positions and Key-Word Arguments Associations
* Receive Arbitrary Numbers of Arguments
* Function that handles input and function shows the output
* Combine function with list, dictionary, if statement, and while loop
* Store function in a separate file known as module
* Keeping the program file simple and easy to read
