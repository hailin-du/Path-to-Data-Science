# 8.1 Defining Function
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


## 8.1.1 Passing Data to the Function

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

## 8.1.2 Argument (Data You Pass) and Parameter (Variable - Data Needed to Perform A Specific Task)
* `username` is a **parameter**, data you are going to pass
* Data is `jesse`, which is a **argument**
* Argument is used when using the function, it pass data to the function
* When we are using the function, we need to put data inside the parentheses ()
* In `greet-user('jesse')`, we are passing 'jesse' to `greet_user()` function, and the value will be stored in `username`
***
***
# 8.2 Passing Argument
#### function can contain multiple parameter
#### Thefore, when using function, we can contain multiple parameter
#### We can use position argument - argument's order and parameter's order are same
#### Or, keyword argument, every parameter is created by variable name and its value
#### Or, use list and dictionary

## 8.2.1 Position Argument
#### WHen using function, python must use function's every argument that is associated with the parameter
#### So the position/order can be used to associate these values

""" def describe_pet(animal_type, pet_name):
    # Display Pet info
    print("\nI have a " + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet('hamster','harry') """
#### The function defined that it needs a animal tpye and a name
#### When using the function, we need to provide a animal type and a name
#### 'hamster'(arugment) stored in animal_type(paremeter)
#### 'harry'(arugment) stored in pet_name(paremeter)
#### In the function, it used both paremeter

#### 1 Using the function mutiple time
""" describe_pet('dog','willie') """
#### We can use the fucntion mutiple time by passing the info
#### Increase effiecency

#### 2 The order of Arugment is Important
""" describe_pet('harry','hamster') """
#### Assigned wrong value to parameter

## 8.2.2 Key-Word Arugment
#### Matching - so the arugment will be matched with the correct value
#### You don't need to care about the order, because you have specify it

""" describe_pet(pet_name='harry', animal_type='hamster') """

## 8.2.3 By Deafult
#### While wrtiing function, we can give parameter a default value
#### When we use the function, unless we provide a arugment, otherwise function will use default value
#### We can skip giving a argument 
""" def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet(pet_name='willie') """
#### If no animal_type provide, python will set the default as 'dog'
#### Keep in mind, the order has been changed 
#### If we put animal_type first, the function will still take single arugment, causing erro
#### So the parameter only talking one arugment (the pet name), therefore we need to put the parameter pet_name first
""" describe_pet(pet_name='harry',animal_type='hamster') """
#### Arugment provided, ignoring the default value

## 8.2.4 Using the function other ways
# def describe_pet(pet_name, animal_type='dog')
#### Under this condition, we must provide a arugment to pet_name
#### If the animal_type is not default value, then we must provide a arugment too

#### Below are mutliple ways using function with same result
# name Willie
""" describe_pet('willie')
describe_pet(pet_name='wille') """

""" # name harry, but hamster
describe_pet('harry','hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harry') """

## 8.2.5 Avioding Arugment Error
#### For example, if function without necessary info, will cause error
""" def describe_pet(pet_name, animal_type):
    print("\nI have a " + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')
describe_pet() """
#### The trackback will tell us where is missing
#### Therefore, naming your paremater is important, because it will what info is needed

# 8.3 Return Value
#### Function can also handle data processing, and return one or a series of values
#### Use return statement to return the value back when you are using the fucntion

## 8.3.1
""" def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician) """
#### Getting info by setting arguments
#### Combine first and last name
#### Return the value (in captials)
#### Returned value stored in musician, then print out musician

#### Even though the follow code is the same
""" print('Jimi Hendrix') """
#### But when we need to store large amount of data, function like this is very useful

## 8.3.2 Making Arguments Selectable
#### For example, if we adding middle name to the function
""" def get_formatted_name(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('john','lee','hooker')
print(musician) """

#### Hoever, not everyone has a middle name
#### If no middle_name info provided, an error will pop out
#### Therefore, we can set a default value to middle_name
#### The default value will be a empty string

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)
musician = get_formatted_name('john','hooker', 'lee')
print(musician)

#### We define the first name and last name, because everyone has one
#### Since middle name is not necessary, we put that on the last

#### Inside the function, we check if middle name being provided
#### Python read any non-empty string as True
#### So if middle_name provided, will return the value

#### If no middle name provided, the if middle_name reviewed as False
#### Then else statment will be exectued

#### Hoever, make sure the middle name is in the last position when setting put arguments

## 8.3.3 Return Dictionary
#### Function can return any type of value, include list, dictionary (more complicated data strcuture)
def build_person(first_name, last_name):
    # return a dictionary, include a person's info
    person = {'first': first_name, 'last':last_name}
    return person

musician = build_person('jimi','hendrix')
print(musician)
#### We can easily expand the code to store more info
def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi','hendrix', age=27)
print(musician)
#### In default, if no age info provided, the function still save a person's first and last name

## 8.3.4 Combining Function with While Loop
""" def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
 """
# Infinite Loop
""" while True:
    print('\nPlease tell me your name:')
    f_name = input('First name: ')
    l_name = input('Last name: ')

    formatted_name = get_formatted_name(f_name, l_name)
    print('\nHello, ' + formatted_name + '!') """

#### However, always remeber set a rule to stop the loop

""" while True:
    print('\nPlease tell me your name:')
    print("(enter 'q' at any time to quit)")
    f_name = input('First name: ')
    if f_name == 'q':
        break

    l_name = input('Last name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print('\nHello, ' + formatted_name + '!') """

# 8.4 Passing List
#### We will pass the list to a function and greet everyone
def greet_user(names):
    for name in names:
        msg = "Hello, " + name.title() + '!'
        print(msg)

usernames = ['hannah','ty', 'margot']
greet_user(usernames)

## 8.4.1 Editing List Inside the Function
#### After passing the list, we can edit the list in the function
#### The change is forever, helpful to manage large data

#### A 3D Printer Company need to print the design
#### The design save in a list
#### After the design is printed, pass it to another list
""" 
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()

    print('Printing model: ' + current_design)
    completed_models.append(current_design)

print("\nThe following models have been printed")
for completed_model in completed_models:
    print(completed_model) """

#### We will resign the code by writing two functioins

def print_modesl(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print('Printing model: ' + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

print_modesl(unprinted_designs[:], completed_models) ##### create a copy #####
show_completed_models(completed_models)
#### Every function has it owns mission
#### We first defined two functions
#### Then we just need to pass the correct arugments while using the function

## 8.4.2 Stopping function to edit the list
#### We can create a copy of the list instead of the oringal one
#### For example, we want to keep the unprinted_desgisns

#function_name(list_name[:])
#### Slicing cancreate a copy

## 8.5 Passing any variable auguments
