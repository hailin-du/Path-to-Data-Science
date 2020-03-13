# 6.1 A Simple Dictionary
Lets take a look of a game, it includes some aliens, aliens have different colors and points.
```python
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
```
>      green
>      5
***
***
# 6.2 Using Dictionary
* Dictionary = a series of keys, each key associate with value(s)
* Assciated value(s) can be number, string, list, or dictionary itself
* Using {} (bracket not [] but {}) to make key and value associate together
* Connect with : (colon), to differentiate key and value


#### In dictionary, you can save as many key-value pairs as you want
```python
alien_0 = {'color': 'green', 'points': 5}
```
The above code, color is a key, green is a associated value

# 6.2.1 Accessing Dictionary's Value
```python
alien_0 = {'color': 'green'}
print(alien_0['color'])
```
> green
Return color's associated value, which is green
```python
alien_0 = {'color': 'green', 'points': 5} 
```
Dictionary can included multiple key-value pair 

#### Case: If a player eliminated an alien, then you can use below code to ensure how many point the player scored
```python
new_points = alien_0['points'] # calling the paired element from 'points'
print('You just earned ' + str(new_points) + ' points!')
```
> You just earned 5 points!
* Defined the dictionary
* Use this dictionary to get the associated value, points, and save it into new_points
* Convert the number into string type, then print out the message

## 6.2.1 Adding Key-Value Pair
* Dictionary is dynamic, you can always add a key-value pair
* To add a pair, use dictionary name with a key ending with bracket, then assign the element (value) to the key
* Adding alien's coordinate, so we can display the alien in a specific position
```python
print(alien_0)
```
> {'color': 'green', 'points': 5}
```python
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) 
```
> {'color': 'green', 'points': 5, 'y_position': 25, 'x_position': 0}
* Total 4 key-value pairs
* Python **does not care** the **order** of pair

## 6.2.3 Create a Empty Dictionary First
* Sometime we need to create a empty dictionary first
* Then we add key and value step by step
```python
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
```

## 6.2.4 Changing Dictionary's Values
```python
alien_0 = {'color': 'green'}
print('The alien is ' + alien_0['color'] + '.')
alien_0['color'] = 'yellow' # Changing color to yellow
print('The alien is now ' + alien_0['color'] + '.')
```
>     The alien is green.
>     The alien is now yellow.
Tracking Alien's position
```python
alien_0 = {'x_position':0,'y_position': 25, 'speed':'medium'}
print('Original x-position: ' + str(alien_0['x_position']))
```
* Moving the alien to the right
* Moving speed determine how far the alien should move
```python
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This Alien is very fast
    x_increment = 3
```
* New position = old position plus increment
```python
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New x-position: ' + str(alien_0['x_position']))
```
>     Original x-poistion: 0
>     New x-position: 2

* First, we created a dictionary, including x and y position
* Then, we are using if-elif-else strcuture to determine how fast the alien should move
* 1 = moving one unit, 2 = moving two units, 3 = moving three units
* We can change the Alien to move fast
* alien_0['speed'] = 'fast'

## 6.2.5 Delete Key-Pair in the Dictionary
We can use del statement to delete 
```python
alien_0 = {'color':'green','points': 5}
print(alien_0)
```
> {'color': 'green', 'points': 5}
```python
del alien_0['points']
print(alien_0)
```
> {'color': 'green'}
Deleted the key - points

## 6.2.6 Dictionary that Has Similar Objects' Key-Pairs
```python
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python', # utting comma for next object key-pair
}
```
```python
print("Sarah's favorite language is " + 
       favorite_languages['sarah'].title() + 
       '.')
```
We used favorite_languages['sarah'] to call Sarah's paired element (value), C
***
***
# 6.3 Going Over the Dictionary
Dictionary can have millions of keys and pairs

## 6.3.1 Going Over Each Key-Pair
```python
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
}
```
```python
for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)
```
>     Key: last
>     Value: fermi
>     
>     Key: first
>     Value: enrico
>     
>     Key: username
>     Value: efermi
* Created two variables to call key and pair, named as key or k, value or v to 
* `items() function` is calling (returning) the key-pair list
* Each loop assign the value of key into Key, and the value of paired-value into Value
```python
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python', # utting comma for next object key-pair
}
```
```python
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
```
>     Jen's favorite language is Python.
>     Sarah's favorite language is C.
>     Phill's favorite language is Python.
>     Edward's favorite language is Ruby.


## 6.3.2 Going Over Each Key
Use `keys() function`
```python
for name in favorite_languages.keys():
    print(name.title())
```
>     Jen
>     Sarah
>     Phill
>     Edward
* Same Result
```python
for name in favorite_languages:
    print(name.title())
```
The reason using keys() is to allow the code to be more reable and comprehensive
```python
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(' Hi ' + name.title() + ", I see your favorite language is " + 
        favorite_languages[name].title() + '!')
```
* Create a list to store friends' names
* Call the friend element and print out a special greeting 
* Above codes **are still using** favorite_languages dictionary
>     Edward
>     Phil
>      Hi PHil, I see your favorite language is Python!
>     Sarah
>      Hi Sarah, I see your favorite language is Python!
>     Jen
```python
if 'erin' not in favorite_languages.keys(): # checking if Erin in the dictionary list
    print('Erin, please take our poll!')
```
> Erin, please take our poll!

## 6.3.3 Going Over the Key by Order
Use `orted function`
```python
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
```
>     Edward, thank you for taking the poll.
>     Jen, thank you for taking the poll.
>     Phil, thank you for taking the poll.
>     Sarah, thank you for taking the poll.
Sorted the key **by order**

## 6.3.4 Going Over Each Paired Value
Use `values() function`
```python
print('The following languages have been mentioned:')
for language in favorite_languages.values():
    print(language.title())
```
>     The following languages have been mentioned:
>     Python
>     C
>     Python
>     Ruby
* Values maybe repeated

Use `set() function` to avoid repeated values
```python
for language in set(favorite_languages.values()):
    print(language.title())
```
>     The following languages have been mentioned:
>     Python
>     C
>     Ruby
`set() function` only return unique value
***
***
# 6.4 Storing 
#### Saving a series of dictionary in a list or, saving a list as a paired value in dictionary
You can:
* Store a dictionray in a list
* Store a list in a dictionray
* Store a dictionary in a dictionray

## 6.4.1 Dictionray List
Creating a list inclue every alien, every alien is a dictionary
```python
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
```
>     {'color':'green','points':5}
>     {'color':'yellow','points':10}
>     {'color':'red','points':15}
In the real case, we may need to create 30 aliens

```python
aliens = []
for alien_number in range(30): # creating 30 green aliens
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]: # showing the first 5 aliens
    print(alien)
print('...')
print('Total numberof aliens: ' + str(len(aliens)))
```
>      {'speed': 'slow', 'color': 'green', 'points': 5}
>      {'speed': 'slow', 'color': 'green', 'points': 5}
>      {'speed': 'slow', 'color': 'green', 'points': 5}
>      {'speed': 'slow', 'color': 'green', 'points': 5}
>      {'speed': 'slow', 'color': 'green', 'points': 5}
>      ...
>      Total number of aliens: 30

* To python, each alien is unique, even their values are same
* We can use **for loop** and **if statement** to change some aliens color
```python
for alien in aliens[0:3]: # calling the first 3 aliens and change their colors, speeds, and points
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
print('...')
```
>      {'speed': 'medium', 'color': 'yellow', 'points': 10}
>      {'speed': 'medium', 'color': 'yellow', 'points': 10}
>      {'speed': 'medium', 'color': 'yellow', 'points': 10}
>      {'speed': 'slow', 'color': 'green', 'points': 5}
>      {'speed': 'slow', 'color': 'green', 'points': 5}
>      ...

We can further expand the code even more
```python
for alien in aliens[2:5]: 
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] =='yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[:5]:
    print(alien)
```
* We may always need to crreate a list that contains a large amount of dictionary
* For example - a website need to create a dictionary for every user
* Every user will be stored in the users list
* The strcuture of the dictionary of every user are the same
* So you can go over the list with the same method
## 6.4.2 Storing List Inside the Dictionray
We can include other infomration for a pizza, not just its toppings
```python
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extgra cheese']
}

print('You ordered a ' + pizza['crust'] + '-crust pizza' + 'with the following toppings:')

for topping in pizza['toppings']:
    print('\t' + topping)
```
>     You ordered a thick-crust pizza with the following toppings:
>        mushrooms
>        extra cheese
* When we need a a dictionray that contains key with multiple values, we can can use lists
* For example, each key has multiple values
* When we go over the dictionary, each person associate with a list that contains multiple values
```python
favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}

for name, languages in favorite_languages.items():
    print('\n' + name.title() + "' favorite languages are:")
    for language in languages:
        print('\t' + language.title())   
```
>     Jen's favorite languages are:
>       Python
>       Ruby
>     
>     Sarah's favorite languages are:
>       C
>     
>     Phil's favorite languages are:
>       Python
>       Haskell
>     
>     Edward's favorite languages are:
>       Ruby
>       Go

* We notice that some people only like one language, while others like multiple languages
* We have go over the dictionray first, which going over key and pairs
* Then we go over the list and call each **single value**

We are adjusing the code for Sarah, because she only liked one language, so we use "is" instead of "are"
* Adjusting the Code for Sarah - use `len() function`

```python
for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print('\n' + name.title() + "'s favorite languages is:")
        for language in languages:
            print('\t' + language.title())
    elif len(languages) >= 2:
        print('\n' + name.title() + "'s favorite languages are:")
        for language in languages:
            print('\t' + language.title())
```

## 6.4.3 Store Dictionary Inside the Dictionary
* Complicated but happen
* Username as key, and store each user info inside the dictionary
```python
users = {
    'aeinstein': {
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },

    'mcurie': {
        'first':'marie',
        'last':'curie',
        'location':'paris',},
}

for username, user_info in users.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'] + " " + user_info['last'] # accessing internal dictionary
    location = user_info['location']

    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())
```
>     Username: aeinstein
>       Full name: Albert Einstein
>       Location: Princeton
>     
>     Username: mcurie
>       Full name: Marie Curie
>       LOcation: Paris
* Defined users dictionary, that has two keys
* Each key itself is a dictionary - include first name, last name, and location
* Then, we store key in username, store paired-values in user_info, and using `users.item() function` to call these values
* We are calling the values from user_info = using the key from the user_info to get the value of first name, last name, and location

If the structure key of each user is **different**, the for loop will be more complicated
***
***
# 6.5 Conclusion
This chapter include:
* Defining Dictionary
* Using Dictionary to store elements (values)
* Calling and editing Dictionary's elements
* Going over all the elements of a Dictionary
* Going over all key-paired values, all the keys, and all the elements of a Dictionary
* Storing dictionary inside a dictionary, a list inside a dictionary, and a dictionary inside a dictionary
