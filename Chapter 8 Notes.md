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
* Data is `jesse`, which is a **argument**
* Argument is used when using the function, it pass data to the function
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

#### 1 Using the Function Multiple Time
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
* When we use the function, unless we provide an arugment, the function will use the default element
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


## 8.2.4 Using the Function Other Ways
We can use Argument Position Association, Key-Word Argument Association, and set Default Element/Value at the same time
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
