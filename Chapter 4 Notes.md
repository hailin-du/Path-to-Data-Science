# Chapter 4 - Working with List
# 4.1 Looping Through an Entire List
### Using `for loop:` to Handle Repeat Work
```python
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)
```
>     alice
>     david
>     carolina

## 4.1.1 Getting Deeper in (Understanding) the `for loop:`
1. `for magician in magicians:` --- getting the first element
2. `print(magician)` --- print alice
3. then go back to `for magician in magicians:` --- getting the second element
4. `print(magician)` again - print david - repeat again - until carolina
5. if the list contains 1 million elements, it repeats 1 million times

#### Using Similar Variable Name to Name for loop: Function
* for cat in cats:
* for dog in dogs:
* for item in list_of_items:

## 4.1.2 Adding More Works in a `for loop:`
```python
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
```
>     Alice, that was a great trick!
>     David, that was a great trick!
>     Carolina, that was a great trick!
#### In `for loop:`, you can include as many as codes you want
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
#### Newline inserted every time for the clean and neat purpose
>     Alice, that was a great trick!
>     I can't wait to see your next trick
>
>     David, that was a great trick!
>     I can't wait to see your next trick
>
>     Carolina, that was a great trick!
>     I can't wait to see your next trick

## 4.1.3 Doing Something After the `for loop:`
```python
print('Thank you, everyone. That was a great magic show!') # outside the for loop:
```
#### Only execute once
#### Using for loop: - go over the character list (every game character), then after the loop add play now module
***
***
# 4.2 Avoiding Indentation Error
#### Must indent!!

## 4.2.1 Forget Indent
```python
magicians = ['alice','david','carolina']
for magician in magicians:
print(magician)
```
> IndentationError: expected an indented block

## 4.2.2 Forget Indent for Other Lines
```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")
```
>     Alice, that was a great trick!
>     David, that was a great trick!
>     Carolina, that was a great trick!
>     I can't wait to see your next trick, Carolina.

#### The last element is `carolina`, therefore, only she can receive the last message
#### This is a logical error, the code only executed for `carolina`

## 4.2.3 Unnecessary Indent
```python
message = "Hello Python world!"
    print(message)
```
> IndentationError: unexpected indent

## 4.2.4 Unnecessary Indent After the `for loop:`
```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    print('Thank you, everyone. That was a great magic show!')
```
>     Alice, that was a great trick!
>     I can't wait to see your next trick, Alice.
>
>     Thank you, everyone. That was a great magic show!
>     David, that was a great trick!
>     I can't wait to see your next trick, David.
>
>     Thank you, everyone. That was a great magic show!
>     Carolina, that was a great trick!
>     I can't wait to see your next trick, Caarolina.
>
>     Thank you, everyone. That was a great magic show!

#### Because `'Thank you,...` was indented within the `for loop:`, it will show to every time the loop runs
#### Similarly, this a logical error!

## 4.2.5 Forget Colon
```python
magicians = ['alice','david','carolina']
for magician in magicians
    print(magician.title() + ", that was a great trick!")
```
This type of error is not easy to discover, sometimes takes an hour to find out
#### Invalid Syntax: Missing Colon
***
***
# 4.3 Create a Numerical List
#### Storing a number has many reasons
#### For example: tracking characters' positions, tracking players' score

## 4.3.1 Using `range()` Function
```python
for value in range(1,5):
    print(value) 
```
>     1
>     2
>     3
>     4
#### Not include 5
```python
for value in range(1,6):
    print(value) 
```
>     1
>     2
>     3
>     4
>     5
#### When you are using `range()`, if it didn't meet your expectation, you can try adding 1 or substrating 1 

## 4.3.2 Using `range()` to Create a List of Numbers
#### When creating a number list, we can use `list()` to change range() into a list
```python
number = list(range(1,6))
print(number)
```
> [1, 2, 3, 4 ,5]
#### even number
```python
even_number = list(range(2,11,2))
print(even_number)
```
> [2, 4, 6, 8 ,10]
#### start with 2, and continue adding 2 until the list reach or pass 11


##### Squares
```python
squares = []
for value in range(1,11):
    square = value ** 2 # 1
    squares.append(square) # 2
print(squares)
```
> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#### We can avoid using temporary square variable
```python
squares = []
for value in range(1,11):
    squares.append(value**2) # Same as notation 1 and 2
print(squares)
```
#### While writing code, try to make sure the code is readable, then we can combine them like the one above

## 4.3.3 Simple Statistics Functions with a List of Numbers
```python
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
```
>     0
>     9
>     45
#### Can apply to list that contains millions of numbers

## 4.3.4 List Comprehension - Complex
#### List comprehension only allow you to write one line of code.
#### Put together - create new elements + for loop, and add new elments automatically
```python
squares2 = [value ** 2 for value in range(1,11)]
print(squares2)
```
1. While using this logic, you have to assign a list name ex: `squares2`
2. Then, use a left bracket `[` start with expression, which creates elements you want to store
3. In this case, the expression is value ** 2`
4. Next, write a for loop using by providing the value, `for value in range(1,11)`, end with a right bracket `]`
5. `for` loop, in this case, provide values `in range(1,11)`, which values 1 to 10 to the expression
6. for loop in this logic did not contain colon
***
***
# 4.4 Working with Part of a List - Slicing
## 4.4.1 Slicing 
```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # return 0,1,2 elements
```
> ['charles', 'martina', 'michael']
```python
print(players[1:4]) # getting number 1 to number 3 elements, without 4
```
> ['martina', 'michael', 'florence']
```python
print(players[:4]) # without start = start with 0 
```
> ['charles', 'martina', 'michael', 'florence']
```python
print(players[2:]) # start with number 3 to the end
```
> ['michael', 'florence', 'eli']
```python
print(players[-3:]) # getting the last three players
```
> ['michael', 'florence', 'eli']

## 4.4.2 Loopingg Through a List for Slicing
```python
players = ['charles','martina','michael','florence','eli']
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())
``` 
>     Here are the first three players on my team:
>     Charles
>     Martina
>     Michael

#### In the real case, we can store players' the best score and add them into a list

## 4.4.3 Copying a List Using `[:]`
#### Using `[:]` to copy the whole list - start to end
#### For example - a list include your favorite food, and a list include yours and your friend's food
```python
my_foods = ['pizza', 'falafel', 'carrote cake']
friend_foods = my_foods[:]
```
```python
print("My favorite food are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
```
>     My favorite food are:
>     ['pizza', 'falafel', 'carrote cake']
>     
>     My friend's favorite foods are:
>     ['pizza', 'falafel', 'carrote cake']

#### To verify we have two identical lists, we will add a new food in each list
```python
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite food are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
```
>     My favorite food are:
>     ['pizza', 'falafel', 'carrote cake'. 'cannoli']
>     
>     My friend's favorite foods are:
>     ['pizza', 'falafel', 'carrote cake', 'ice cream']

#### Example Without Slicing!!!
```python
my_foods = ['pizza','falafel','carrote cake']
friend_foods = my_foods # we use = instead of [:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite food are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
```
>     My favorite food are:
>     ['pizza', 'falafel', 'carrote cake'. 'cannoli', 'ice cream']
>     
>     My friend's favorite foods are:
>     ['pizza', 'falafel', 'carrote cake', 'cannoli', 'ice cream']

#### It won't work 
* We assign `my_foods` to `friend_foods` instead store a copy into `friend_foods`
* This logic creates the new variable `friend_foods` **associate** with the list
* Therefore, when we change the original list `my_foods` list, both variables (both lists) got changed at the same time
***
***
# 4.5 Tuple
#### Elements in List are changeable, but Not in Tuple

## 4.5.1 Defining Tuple
#### Tuple is parentheses `( )` instead bracket `[ ]`, after assigning the values, we can get access to tuple as list
#### Create a dimension that is unchangeable
```python
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
```
>     200
>     5
```python
dimensions[0] = 250
```
> TypeError: 'tuple' object does not support item assignment
### Error - cannot change element in the tuple

## 4.5.2 Looping Through an Entire Tuple
#### Use for loop:
```python
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)
```
>     200
>     5
## 4.5.3 Changing Tuple Elements
#### Even we cannot change the elements, we can reassign the value in the tuple
```python
dimensions = (200,50)
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400,100) # changing the value manually
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)
```

>     Original dimensions:
>     200
>     50
>     
>     Modified dimensions:
>     400
>     100
#### Store new elements in variable called dimensions
#### For Life Cylce - is good to use tuple (life = fixed period)
***
***
# 4.6 Conclusion 
* Carefully using tab and spaces, sometimes it will cause trouble (indent error)
* Therefore, only select one to use, not using them both at the same time 
* Also, there are other rules in PEP 8, such as length of your codes 
* Try to limit all your code line to a maximum of 79 characters

## 4.6.4 Separation
* Newline space can separate code without affecting it, but carefully using it
* For example, you can separate your codes using a newline space between creating lists and execute lists, so people understand the order of your codes

## 4.6.5 PEP 8
* For more details please click this link below
* https://www.python.org/dev/peps/pep-0008/



