# 4.1 Go over the whole list
### using Loop to handle repeat work
```
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)
```
## 4.1.1 Getting Deepper in Loop
1. for magician in magicians: --- getting the first element
2. print(magician) --- print alice
3. then go back to for magician in magicians: --- getting the second element
4. print(magician) again - print david - repeat again - until carolina
5. if the list contain 1 million elements, it repeat 1 million times

#### Using similar variable name to name for loop
* for cat in cats:
* for dog in dogs:
* for item in list_of_items:

## 4.1.2 Adding Works In the For Loop
```
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
```
#### in for loop, you can include as many as codes you want
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
#### new line inserted everytime for clean and neat purpose

## 4.1.3 After the For Loop
```
print('Thank you, everyone. That was a great magic show!')
```
#### Only excute once
#### Using for loop - go over every game character, then after the loop add play now
***
# 4.2 Avioding Error
#### Must indent!!

## 4.2.1 Forget Indent
```
magicians = ['alice','david','carolina']
for magician in magicians:
print(magician)
```
#### Indented Block Error

## 4.2.2 Forget Indent other lines
```
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")
```
#### the last element is carolina, therefore, only her receive the last message
#### Logic error, excute only once for carolina

## 4.2.3 Unnecessary Indent
```
message = "Hello Python world!"
    print(message)
```
#### Unexpected Indent Error

## 4.2.4 Unnecessary Indent After The Loop
```
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    print('Thank you, everyone. That was a great magic show!')
```
#### Because it was indented, it will show to every magician in the list
#### Similarly, Logic Error!

## 4.2.5 Forget Colon
```
magicians = ['alice','david','carolina']
for magician in magicians
    print(magician.title() + ", that was a great trick!")
```
#### Invalid Syntax: Missing Colon
***
# 4.3 Create A Number List
#### Storing a number has many reasons
#### For example: tracking characters' positions, tracking players' score

## 4.3.1 Using Range() Function
```
for value in range(1,5):
    print(value) 
```
#### Not include 5
```
for value in range(1,6):
    print(value) 
```
#### When using range, but it didn't meet you expectation, can try adding 1 or substrating 1

## 4.3.2 Using Range to Create a Number List
#### When creating a number list, we can use list() to change range() into a list
```
number = list(range(1,6))
print(number)
```
#### even number
```
even_number = list(range(2,11,2))
print(even_number)
```
#### start with 2, and continue adding 2 until to reach or pass 11


##### squares
```
squares = []
for value in range(1,11):
    square = value ** 2 # 1
    squares.append(square) # 2
print(squares)
```
#### We can aviod using temporary square variable
```
squares = []
for value in range(1,11):
    squares.append(value**2) # Same as notation 1 and 2
print(squares)
```
#### While writing code, try to make sure code is readable, then we can combine them like the second method

## 4.3.3 Using Number List for Calculation
```
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
```
#### can apply to list that contains millions numbers

## 4.3.4 List Comprehension - Complex
#### List comprehension only allow you to write one line of code.
#### Put together - create new elements + for loop, and add new elments automatically
```
squares2 = [value**2 for value in range(1,11)]
print(squares2)
```
1. While using this logic, you have to assign a list name ex: squares
2. Then, assign a left bracket [, with expression, which create elements you want to store
3. In this case, expression is value**2
4. Next, write a for loop, provide the value, end with righr bracket]
5. for loop in this case provide values in range(1,11), which values 1-10 to the expression
6. for loop in this logic did not contain colon
***
# 4.4 Using Part of The List - Slicing
## 4.4.1 Slicing
```
players = ['charles','martina','michael','florence','eli']
print(players[0:3]) # return 0,1,2
print(players[1:4]) # getting number 2 to number 4 elements 
print(players[:4]) # without start
print(players[2:]) # start with number 3 to the end
print(players[-3:]) # getting the last three players
```

## 4.4.2 List Slicing
```
players = ['charles','martina','michael','florence','eli']
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())
```    
#### In real case, we can store players' the best score and add them into list

## 4.4.3 Copying List
#### using [:] to copy the whole list - start to end
#### for example a list include your favorite food, and a list include yours and your friend's food
```
my_foods = ['pizza','falafel','carrote cake']
friend_foods = my_foods[:]
```
```
print("My favorite food are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
```
#### to vertify we have two identical list, we will add a food in each list
```
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite food are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
```
#### Without Slicing!!!
```
my_foods = ['pizza','falafel','carrote cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite food are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
```
#### It won't work 
* We assign my_foods to friend_foods instead store a copy into friend_foods
* This logic create the new variable friend_foods associate with the list
* Therefore, when we change the list, both variables got changed at the same time
***
# 4.5 Tuple
#### Elements in List are changable, but Not in Tuple

## 4.5.1 Define Tuple
#### Tuple is parentheses () instead [], after assigning the values, we can get access to it as list
#### create a dimension that is unchangeable
```
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
```
```
dimensions[0] = 250
```
### Error - cannot change element in tuple

## 4.5.2 Go over the whole tuple
#### use for loop
```
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)
```
## 4.5.3 Changing Tuple Elements
#### Even we cannot change the elements, we can reassign the value in the tuple
```
dimensions = (200,50)
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)
```
```
dimensions = (400,100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)
```
#### store new elements in variable dimensions
#### For Life Cylce - is good to use tuple (life = fixed period)
***
# Conclusion 4.6
* Carefully using tab and spaces, sometimes it will cause trouble (indent problem)
* Therefore, only select one to use, not using them both at the same time 
* Also, there are other rules in PEP 8, such as length of your codes 
* Limit all lines to a maximum of 79 characters

## 4.6.4 Separation
* New line can seperate code without affecting it, but carefuly using it
* For example, you can seperate codes between createing lists and execute lists

## 4.6.5 PEP 8
* For more details please click this link below
* https://www.python.org/dev/peps/pep-0008/



