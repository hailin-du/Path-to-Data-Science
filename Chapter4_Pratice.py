## 4.1 For Loop
food = ['cake','pizza','ice cream']
for item in food:
    print('I like ' + item + ', it tastes good')

## 4.2 
animals = ['cat','dog','rabbit','bird']
for animal in animals:
    print('A ' + animal + ' would make a great pet.')
print('Any of these animals would make a great pet!')

## 4.3 Number List
for value in range(1,21):
    print(value)

## 4.4 One Million
million = list(range(1,1000001))
# for number in million:
#    print(million)
#### output too long, press control-c to quit

## 4.5 Sum of One MIllion
print(min(million))
print(max(million))
print(sum(million))

## 4.6 Odd Number
for value in range(1,21,2):
    print(value)

## 4.7 Exponent of 3
three = []
for value in range(3,31,3):
    three.append(value)
print(three)

## 4.8 **
number2 = list(range(1,11))
for number in number2:
    number = number ** 3
    print(number)

## 4.9 ** List Comprehension
number3 = [number ** 3 for number in range(1,11)]
print(number3)

## 4.10 Slicing
foods = ['pizza', 'falafel', 'carrote cake', 'cannoli', 'ice cream']
print('The first three items in the list are: ' + str(foods[:3]))
print('Three items from the middle of the list are: '  + str(foods[2:5]))
print('The last three items in the list are: ' + str(foods[-3:]))

## 4.11 Your Food List and My Food List
food = ['cake','pizza','ice cream']
friend_food = food[:]
food.append('sushi')
friend_food.append('burger')
print('My favorite food are: ' + str(food))
print("My friend's favorite food are: " + str(friend_food))
for item in friend_food:
    print(item.title())

## 4.12 Mutiple Loop
print('Below are my favorite food:')
for item in food:
    print(item.title())

print("\nBelow are my friend's favorite food:")
for item in friend_food:
    print(item.title())

## 4.13 Buffet
buffets = ('bread','ice cream','cake','candy','juice')
for buffet in buffets:
    print(buffet.title())
# buffets[4] = 'water' ## Error

buffets = ('bread','ice cream','cake','chocolate','water')
for buffet in buffets:
    print(buffet.title())
## reassign new elements in tuple

