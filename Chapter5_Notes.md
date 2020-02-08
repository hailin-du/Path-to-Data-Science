# 5.1 Simple If Statement
```
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```
# 5.2 Condition Testing
* True & False
* True - excute
* Flase - ignore the codes

## 5.2.1 Checking if it Equals
```
car = 'bmw'
print(car == 'bmw')
```
#### True

```
car = 'audi'
print(car == 'bmw')
```
#### False

## 5.2.2 Checking if it Equals Without considersing Upper and Lower Case
```
car = 'Audi'
print(car == 'audi')
```
#### False

```
car = 'Audi'
print(car.lower() == 'audi')
```
#### True
```
print(car) 
```
#### Audi
* Didn't affect the car variable
* For Website Development purpose, we save users' usernames, then we can convert them to compare
* For example, John, covert to lower case, john == john (if john already exist), then reject user during registration

## 5.2.3 Checking if it Unequal
```
requested_topping = 'mushrooms'
```
```
if requested_topping != 'anchovies': #### if a != b equal to True, then excute the line #####
    print('Hold the anchovies!')
```    
## 5.2.4 Compare Number
```
age = 18
print(age==18)
```
#### True

```
answer = 17
if answer != 42:
    print('That is not the correct answer. Please try again!')
```
#### can include less than, greather than or others.
```
age = 19
print(age<21) 
print(age<=21)
print(age>21)
print(age>=21)
```

## 5.2.5 Checking Multiple Conditions
### And
* Use and to combine two conditions
* If one of the condition didn't pass, the whole expression is False
```
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21) #### False
age_1 = 22
print(age_0 >= 21 and age_1 >= 21) #### True
```
### OR
* Use or to check at least one condition meets
* If one of the condition pass, the whole epxression is True
* If both conditions didn't pass, then the whole expression is False
```
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21) 
```
#### True
```
age_0 = 18
print(age_0 >= 21 or age_1 >= 21) 
```
#### True

## 5.2.6 Check if a specific element within the List
#### In real case, we can check if the username already exist in the username list
### In
* Use in to check if a element exist in the list
```
requested_toppings = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings) #### True ####
print('pepperoni' in requested_toppings) #### False ####
```

## 5.2.7 Check if a specific element NOT in the List
### Not In
* In real case, we can check which user is not banned to speak in forums
```
banned_users = ['andrew','carolina','david']
user ='marie'
if user not in banned_users: #### if user not in the list, which is True, then excute ####
    print(user.title() + ", you can post a response if you wish.")
```
## 5.2.8 Boolean Expression
* Same as condition, either True or False
* Boolean expression usually is used for recording condition
* Such as, if the game is ruunning normally, or if user can edit the webpage
```
game_active = True
can_edit = False
```
#### Boolean Expression provides a effective way to track a program status

# 5.3 if Statement
```
if conditional_test:
  do something
```
```
age = 19
if age >= 18:
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
```
## 5.3.2 if-else Statment
#### if condition didn't pass, we use else to excute another operation
```
age = 17
if age >= 18: # Condition True - excute this part
    print('You are old enough to vote!')
    print('Have you registered to vote yet?')
else: # Condition False - excute this park
    print('Sorry, you are too young to vote.')
    print("Please register to vote as oon as you turn 18!")
```
## 5.3.3 if-elif-else Strcuture
* More than two conditions
* Test every structure within the if-elif-else and check every condition until it pass the condition

#### Case:
* Below Age 4 = Free Admission
* Age Between 4 - 17 = $5 Admission Fee
* Age 18 or Above = $10 Admission Fee
```
age = 12
if age < 4: # False - not pass
    print('Your admission cost is $0.')
elif age < 18: #### Only excute when if condition didn't pass - True ####
    print('Your admission cost is $5.')
else: # skipped, becuase elif condition passed
    print('Your admission cost is $10.')
```
#### Cleaner Code - setting price only without printing the whole sentence
```
age = 12 
if age < 4: #### setting price variable in the strcuture
    price = 0
elif age < 18: 
    price = 5
else: 
    price = 10
```
#### Easier to change the code and more efficent
```
print('Your admission cost is $' + str(price) + '.')
```

## 5.3.4 Using Multiple elif Block
#### Adding elderly price
```
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

## 5.3.5 Ignore else 
#### We don't have to use else at the end, we can change to elif to make code more clearly
```
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
#### if you know the end-result is, you should consider using elif instead of else

## 5.3.6 Testing Multiple Conditions
```
requested_toppings =['mushrooms','extra cheese'] # customer order
```
```
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings: # no matter the previous condition is passing or not, it still test because we used if here
    print('Adding pepperoni')
if 'extra cheese' in requested_toppings: # same here, no matter the above conditions are passing or not
    print('Adding extra cheese')
```
```
print('\nFinished making your pizza!')
```
```
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
elif 'pepperoni' in requested_toppings: # skipped - the first condition passed
    print('Adding pepperoni')
elif 'extra cheese' in requested_toppings: # skipped - the first condition passed
    print('Adding extra cheese')
```
```
print('\nFinished making your pizza!')
```
# 5.4 Using if to Handle List
## 5.4.1 Checking Specific Element
#### Pizza Toppings
```
requested_toppings = ['mushrooms','green peppers','extra cheese']
```
```
for requested_topping in requested_toppings:
    print('Adding ' + requested_topping + ".")
print('\nFinished making your pizza!')
```
#### Running out Green Peppers
```
requested_toppings = ['mushrooms','green peppers','extra cheese']
```
```
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers': #### checking if customer ordered green peppers ####
        print('Sorry, we are out of green peppers right now.')
    else:
        print('Adding ' + requested_topping + ".")
print('\nFinished making your pizza!')
```

## 5.4.2 Ensure the list is not empty
* Check if the order list is empty, if it is empty ask customer wants a plain pizza
* If not empty, then continue adding toppings
```
requested_toppings = []
```
```
if requested_toppings: 
    for requested_topping in requested_toppings:
        print('Adding ' + requested_topping + ".")
    print('\nFinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')
```
#### In Python, when using if condition with list
* if the list contain at least one element return True
* if the list has nothing, return false

## 5.4.3 Using Mutiple List
```
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushroom','french fries','extra cheese']
```
```
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print("Sorry, we don't have " + requested_topping + '.')
print('\nFinished making your pizza!')
```
* If available toppings is fixed, we can use tuple
* Second list is customer order - pay attention to french fries
* We have go over the requested_toppings list to see if the topping available in available_toppings list
* If requested topping not exist, then we tell the customer we don't provide


# 5.5 if Statement Format
* When setting if statement with condition like ==, >= and <=
* It is better to include space (acorrding to PEP 8), like if age < 4 
* Not if age<4 
