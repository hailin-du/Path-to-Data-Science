# 5.1 Simple `if` Statement
```python
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```
>     Audi
>     BMW
>     Subaru
>     Toyota
***
***
# 5.2 Condition Testing
* True & False
* True - execute the code
* Flase - ignore the code

## 5.2.1 Checking if Elements (Values) are Equal
```python
car = 'bmw'
print(car == 'bmw')
```
> True

```python
car = 'audi'
print(car == 'bmw')
```
> False

## 5.2.2 Checking if Elements (Values) are Equal without Considersing Upper and Lower Case
```python
car = 'Audi'
print(car == 'audi')
```
> False
```python
car = 'Audi'
print(car.lower() == 'audi')
```
> True
```python
print(car) 
```
> Audi
* Didn't affect the car variable
* For Website Development purpose, we save users' usernames, then we can convert them to compare if values are matching
* For example, John, covert to lower case, john == john (if john already exist), then reject user during the registration

## 5.2.3 Checking if Elements (Values) are Unequal
```python
requested_topping = 'mushrooms'
```
```python
if requested_topping != 'anchovies': # if a != b equal is True, then excute the line
    print('Hold the anchovies!')
```    
> Hold the anchovies!
## 5.2.4 Comparing Number
```python
age = 18
print(age == 18)
```
> True

```python
answer = 17
if answer != 42:
    print('That is not the correct answer. Please try again!')
```
> That is not the correct answer. Please try again!
#### Can include less than <, greather than > or others such as >= or <=
```python
age = 19
print(age<21) 
print(age<=21)
print(age>21)
print(age>=21)
```
>     True
>     True
>     False
>     False

## 5.2.5 Checking Multiple Conditions
### And
* Use and to combine two conditions
* If one of the condition didn't pass, the whole expression is False
```python
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21) # False
```
> False
```python
age_1 = 22
print(age_0 >= 21 and age_1 >= 21) # True
```
>     True
### OR
* Use or to check at least one condition meets
* If one of the condition pass, the whole epxression is True
* If both conditions didn't pass, then the whole expression is False
```python
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21) 
```
> True
```python
age_0 = 18
print(age_0 >= 21 or age_1 >= 21) 
```
> Flase

## 5.2.6 Check if a Specific Element within the List
#### In the real case, we can check to see if the username already exist in the username list
### `in`
* Use in to check if a element exist in the list
```python
requested_toppings = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings) # True 
```
> True
```python
print('pepperoni' in requested_toppings) # False
```
> False

## 5.2.7 Check if a Specific Element NOT in the List
### `not in`
* In the real case, we can check which user is not beining banned to speak in the forums
```python
banned_users = ['andrew','carolina','david']
user ='marie'
if user not in banned_users: #### if user not in the list, which is True, then excute ####
    print(user.title() + ", you can post a response if you wish.")
```
> Marie, you can post a response if you wish.

## 5.2.8 Boolean Expression
* Same as condition, either True or False
* Boolean expression usually is used for recording condition
* Such as, if the game is ruunning normally, or if the user can edit the webpage
```python
game_active = True
can_edit = False
```
#### Boolean Expression provides a effective way to track a program status
***
***
# 5.3 if Statement
```python
if conditional_test:
  do something
```
```python
age = 19
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
```
> You are old enough to vote!
## 5.3.2 if-else Statment
#### if a condition didn't pass, we use else (another) condition to excute another operation
```python
age = 17
if age >= 18: # Condition True - excute this part
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else: # Condition False - excute this park
    print('Sorry, you are too young to vote.')
    print("Please register to vote as oon as you turn 18!")
```
>     Sorry, you are too young to vote.
>     Please register to vote as oon as you turn 18!

## 5.3.3 if-elif-else Strcuture
* More than two conditions
* Test every structure within the if-elif-else and check every condition until it pass the condition

#### Case: Ticket Admissions
* Below Age 4 = Free Admission
* Age Between 4 - 17 = $5 Admission Fee
* Age 18 or Above = $10 Admission Fee
```python
age = 12
if age < 4: # False - not pass
    print('Your admission cost is $0.')
elif age < 18: #### Only excute when if condition didn't pass - True ####
    print('Your admission cost is $5.')
else: # skipped, becuase elif condition passed
    print('Your admission cost is $10.')
```
> Your admission cost is $5.
#### Cleaner Code - Setting the cost only without printing the whole sentence
```python
age = 12 
if age < 4: # assigning the price variable in the structure
    price = 0
elif age < 18: 
    price = 5
else: 
    price = 10
```
#### Easier to change the code and more efficent
```python
print('Your admission cost is $' + str(price) + '.') # Outside the if-else statement
```
## 5.3.4 Using Multiple elif Block
#### Adding elderly price
```python
age = 12
if age < 4: 
    price = 0
elif age < 18: 
    price = 5
elif age < 65:
    price = 10
else: 
    price = 5
print('Your admission cost is $' + str(price) + '.')
```

## 5.3.5 Avoid Using else 
#### We don't have to use else at the end, we can change to elif to make the code more clearly
```python
age = 12
if age < 4: 
    price = 0
elif age < 18: 
    price = 5
elif age < 65:
    price = 10
elif age >=65: # assigning the condition
    price = 5
print('Your admission cost is $' + str(price) + '.')
```
#### else can be anything!
#### If you know the end-result is, you should consider using elif instead of else

## 5.3.6 Testing Multiple Conditions
```python
requested_toppings = ['mushrooms',' extra cheese'] # customer order
```
```python
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings: # no matter the previous condition is passing or not, it still test because we used if here
    print('Adding pepperoni')
if 'extra cheese' in requested_toppings: # same here, no matter the above conditions are passing or not
    print('Adding extra cheese')
```
```python
print('\nFinished making your pizza!')
```
>     Adding mushrooms.
>     Adding extra cheese.
>
>     Finished making your pizza!

* Below code cannnot execute normally
* When Checking the first if, the list contains mushroom
* So it will skip the rest of the code (lines)
```python
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
elif 'pepperoni' in requested_toppings: # skipped - the first condition passed
    print('Adding pepperoni')
elif 'extra cheese' in requested_toppings: # skipped - the first condition passed
    print('Adding extra cheese')
```
```python
print('\nFinished making your pizza!')
```
>     Adding mushrooms.
>
>     Finished making your pizza!
***
***
# 5.4 Using if to Handle List
## 5.4.1 Checking Specific Element
#### Pizza Toppings
```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
```
```python
for requested_topping in requested_toppings:
    print('Adding ' + requested_topping + ".")
print('\nFinished making your pizza!')
```
>     Adding mushrooms.
>     Adding green peppers.
>     Adding extra cheese.
>
>     Finished making your pizza!
#### Running out Green Peppers
```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
```
```python
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers': # checking to see if the customer ordered green peppers 
        print('Sorry, we are out of green peppers right now.')
    else:
        print('Adding ' + requested_topping + ".")
print('\nFinished making your pizza!')
```
>     Adding mushrooms.
>     Sorry, we are out of green peppers right now.
>     Adding extra cheese.
>
>     Finished making your pizza!
## 5.4.2 Making Sure the List is Not Empty
* Check if the order list is empty, if it is empty ask the customer if he or she wants a plain pizza 
* If the list is not empty, then continue adding toppings
```python
requested_toppings = []
```
```python
if requested_toppings: 
    for requested_topping in requested_toppings:
        print('Adding ' + requested_topping + ".")
    print('\nFinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')
```
> Are you sure you want a plain pizza?
#### In Python, when you are using a if condition with list
* If the list contain `at least ONE element` return **True**
* If the list has nothing inside, return **False**

## 5.4.3 Using Mutiple List
```python
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushroom', 'french fries', 'extra cheese']
```
```python
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print("Sorry, we don't have " + requested_topping + '.')
print('\nFinished making your pizza!')
```
>     Adding mushrooms
>     Sorry, we don't have french fries.
>     Adding extra cheese.
>     
>     Finished making your pizza!
* If available toppings is **Fixed**, we can use **Tuple**
* Second list is the customer order list - pay attention to french fries
* We have to go over the requested_toppings list to see if the topping available in the available_toppings list
* If requested topping element is not exist in the available_topping list, then we tell the customer we don't provide that element (topping)


# 5.5 if Statement Format
* When setting if statement with condition like ==, >= and <=
* It is better to include space (acorrding to PEP 8), like if age < 4 
* Not if age<4 
