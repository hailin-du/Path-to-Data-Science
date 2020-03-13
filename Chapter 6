# 6.1 A Simple Dictionary
Lets take a look of a game, it includes some aliens, aliens have different colors and points.
```
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
```
>      green
>      5
# 6.2 Using Dictionary
#### Dicionary = a series of keys, each key associate with values
#### assciated values can be number, string, list, or dictionary itself
#### using {} to make key and value associate
#### connect with :, to seperate key and value
#### In dictionary, you can save as many key-value as you want
alien_0 = {'color':'green'}
#### In above code, color is a key, green is a associated value

# 6.2.1 Accessing Dictionary's Value
alien_0 = {'color':'green'}
print(alien_0['color'])
#### return color's associated value, which is green

alien_0 = {'color':'green','points':5} 
#### Dictionary can included multiple key-value association

#### Case: if a player killed an alien, then you can use below code to ensure how many point the player scored
new_points = alien_0['points']
print('You just earned ' + str(new_points) + ' points!')
#### Defined the dictionary
#### Use this dictionary to get associated value, points, and save it into new_points
#### convert the number into string, then print out a message

## 6.2.1 Adding Key-Value Pair
#### Dictionary is dynamic, you can always add a key-value pair
#### To add, use dictionary name with bracket
#### Adding alien's coordinate, so we can display the alien in a specific position

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) 
#### Total 4 key-value pairs
#### Python does not care the order of pair

## 6.2.3 Create a Empty Dictionary First
#### Sometime we need to create a empty dictionary first

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

## 6.2.4 Changing Dictionary's Value
alien_0 = {'color':'green'}
print('The alien is ' + alien_0['color'] + '.')
#### Changed color to yellow
alien_0['color'] = 'yellow'
print('The alien is now ' + alien_0['color'] + '.')

#### Track Alien's position
alien_0 = {'x_position':0,'y_position': 25, 'speed':'medium'}
print('Original x-position: ' + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This Alien is very fast
    x_increment = 3
#### New position = old position plus increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('New x-position: ' + str(alien_0['x_position']))
#### We first created a dictionary
#### Then, we create if-elif-else strcuture to determine how fast the alien should move
#### 1 = moving one unit, 2 = moving two units, 3 = moving three units
#### We can change the Alien to move fast
#### alien_0['speed'] = 'fast'

## 6.2.5 Deleting Key-Pair
#### We can use del statement to delete 
alien_0 = {'color':'green','points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
#### Deleting the key - points

## 6.2.6 Many Objects' Key-Pair
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python', #### putting comma for next object key-pair
}

print("Sarah's favorite language is " + favorite_languages['sarah'].title() + '.')
#### we used favorite_languages['sarah'] to call Sarah's pair value

# 6.3 Going Over the Dictionary
#### Dictionary can have millions of keys and pairs

## 6.3.1 Going Over Each Key-Pair
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
}

for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)
#### create two variables for key and pair, k, v
#### items() return a key-pair list
#### Each loop assign the values into Key and its paired value


for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

## 6.3.2 Going Over Each Key
### Use keys()
for name in favorite_languages.keys():
    print(name.title())
#### Same Result
### for name in favorite_languages:
#### print(name.title())

#### The reason is to allow the code more reable and comprehensive

friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(' Hi ' + name.title() + ", I see your favorite language is " + 
        favorite_languages[name].title() + '!')

#### create a list to point out friends 
#### call the friends and print out a special greeting 

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')

## 6.3.3 Going Over the Key By Order
### Use sorted
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
#### sorted the key by order

## 6.3.4 Going Over Each Paired Value
### Use values()
print('The following languages have been mentioned:')
for language in favorite_languages.values():
    print(language.title())
#### values maybe repeated
### Use set()
for language in set(favorite_languages.values()):
    print(language.title())
### set only choose unique value

# 6.4 Storing 
#### Saving a series of dictionary in a list or, saving a list as paired value in dictionary
### You can:
### store a dictionray in a list
### store a list in a dictionray
### sotre a dictionary in a dictionray

## 6.4.1 Dictionray List
#### Creating a list inclue every alien, every alien is a dictionary

alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#### creating 30 alien

aliens = []
for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('...')
print('Total numberof aliens: ' + str(len(aliens)))

#### To python, each alien is unique
#### We can use for loop and if statement to change some aliens color

for alien in aliens[0:3]: # changing the first three aliens
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
print('...')
#### We can expand the code even more
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

## 6.4.2 Storing List in Dictionray
#### We can include other infomration for a pizza, not just its toppings

pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extgra cheese']
}

print('You ordered a ' + pizza['crust'] + '-crust pizza' + 'with the following toppings:')

for topping in pizza['toppings']:
    print('\t' + topping)
#### When a dictionray, a pair has multiple values, we can add a list

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
    

## Go over the dictionray first, key and pairs
## Then go over the list and recall single value

#### Adjusting the Code for Sarah - use len()

for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print('\n' + name.title() + "'s favorite languages is:")
        for language in languages:
            print('\t' + language.title())
    elif len(languages) >= 2:
        print('\n' + name.title() + "'s favorite languages are:")
        for language in languages:
            print('\t' + language.title())

## 6.4.3 Store Dictionary In A Dictionary
#### Complicated but happen
#### Username as key, and store each user info in a dictionary

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

#### defined users dictionary include two keys
#### Each key itself is a dictionary - include first, last name, and location
#### Then we store key in username, store paired-values in user_info
#### We access the value in user_info = using the key to get accesss of first, last name and location

### If the key of each user is different, the for loop will be more complicated
