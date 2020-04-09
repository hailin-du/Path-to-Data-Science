# Introducing Lists
# 3.1 List（What is a List?)
* Can be 0-9, family names, or elements have no relationship
* use bracket [] to create a list
```python
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
```
> ['teak','canondale','redline','specialized']
## 3.1.1 Access List's Elements
```print(bicycles[0])``` 
> trek

```python
print(bicycles[0].title())
```

> Trek

## 3.1.2 Slicing Start at 0 Not 1
```print(bicycles[1])```
> cannondale

```python
print(bicycles[3])
```
> specialized


```python
print(bicycles[-1])
```
> specialized
* -1 = last position

## 3.1.3 Use Every List's Elements
```python
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
```
> My first bicycle was a Trek
***
***
# 3.2 Change, Add, Delete Elements from the List
## 3.2.1 Changing Elements
```python
motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle)
```
> ['honda', 'yamaha', 'suzuki']
```python
motorcycle[0] = 'ducati'
print(motorcycle)
```
> ['ducati', 'yamaha', 'suzuki']

## 3.2.2 Adding Elements
```python
motorcycle.append('ducati')
print(motorcycle)
```
> ['honda', 'yamaha', 'suzuki', 'ducati']

#### Provide User to Append data
So first create a empty list
```python
motorcycle2 = []
motorcycle2.append('honda')
motorcycle2.append('yamaha')
motorcycle2.append('suzuki')
print(motorcycle2)
```
> ['honda', 'yamaha', 'suzuki']

`insert() function`
```python
motorcycle = ['honda', 'yamaha', 'suzukui']
```
```
motorcycle.insert(0, 'ducati') # 0 as position that you want to add , the rest will move to right
print(motorcycle)
```
> ['ducati, 'honda', 'yamaha', 'suzuki']

## 3.2.3 Deleting Elements
```python
motorcycle = ['honda', 'yamaha', 'suzuki']
del motorcycle[0] 
print(motorcycle)
```
> ['yamaha', 'suzuki']
```python
motorcycle = ['honda', 'yamaha', 'suzuki']
del motorcycle[1]
print(motorcycle) 
```
> ['honda', 'suzuki']

`pop()` function (using pop to delete)
#### `pop()` allows you to delete the last element but still able to use it (taking it out)
```python
motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle)
```
> ['honda', 'yamaha', 'suzuki']
```python
popped_motorcycle = motorcycle.pop() 
```
#### Taking out the last element
#### For example - if `motorcycle` is being purchased based on time (oldest to latest), using pop() to take the latest one
```python
print(motorcycle)
print(popped_motorcycle)
```
>      ['honda', 'yamaha']
>      suzuki

```python
motorcycle = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycle.pop()
print('The last motocrcyle I owned was a ' + last_owned.title() + ".")
```
> The last motocrcyle I owned was a Suzuki.
#### You can use `pop()` to delete any element you want by adding position space
```python
first_owned = motorcycle.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
```
> The first motorcycle I owned was a Honda.

**Remember** <br>
* Once you used `pop()`, the element is **NOT** in the list anymore
* Del - not going to use element anymore (deleting it forever)
* Pop - after the delete you still want to use the element (stored)

### `remove()` function (don't know the element position)
```python
motorcycle = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycle)
```
> ['honda', 'yamaha', 'suzuki', 'ducati']
```python
motorcycle.remove('ducati')
print(motorcycle)
```
['honda', 'yamaha', 'suzuki']

#### Using `remove()` to delete an element, we can still keep it and continue to use it
#### pointing the reason why you delete it
```python
motorcycle = ['honda', 'yamaha','suzuki', 'ducati']
```
> ['honda', 'yamaha','suzuki', 'ducati']
```python
too_expensive = 'ducati'
motorcycle.remove(too_expensive)
print(motorcycle)
print('\nA ' + too_expensive.title() + ' is too expensive for me.')
```
> ['honda', 'yamaha','suzuki']
> 
> A Ducati is too expensive for me.

#### `remove()` can only delete **ONE** single element at a time, if the element in the list appear multiple times, you may need a LOOP to decide if you are going to delete all of them

### Position always change when you are using `pop()` or `del()` [delete function]
***
***
# 3.3 Organize A List
#### List order is unpredictable baaed on the input of a user, you can adjust the order 

## 3.3.1 Use `sort()` Function to Sort a List Permanently
```python
cars = ['bmw', 'audi', 'toyota',' subaru']
cars.sort() # sorted based on alphabet
print(cars)
```
> [audi', bmw', 'subaru', 'toyota']
```python
cars.sort(reverse=True)
print(cars)
```
> ['toyota', 'subaru', 'bmw', 'audi']

### 3.3.2 Use `sorted()` Function to Sort a List Temporarily (Sort the List Without Affecting the Original List)
```python
cars = ['bmw','audi','toyota','subaru']
print('Here is the original list:')
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print('Here is the original list again:')
print(cars)
```
>     Here is the original list:
>     ['bmw','audi','toyota','subaru']
> 
>     Here is the sorted list:
>     [audi', bmw', 'subaru', 'toyota']
>
>     Here is the original list again:
>     ['bmw','audi','toyota','subaru']
#### Sometimes lower case and upper case orders are more complicated in sorting

### 3.3.3 Use `reverse()` Function to Reverse the Order of a List
#### for example - assume car is being purchased based on time (oldest to latest)
```python
cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)
```
>     ['bmw', 'audi', 'toyota', 'subaru']
>     ['subaru', 'toyota', 'audi', 'bmw']
#### `revese()` function will forever change the order of a list

### 3.3.4 Use `len()` Function to Find the Length of a List (Count the Length of the List)
```python
cars = ['bmw','audi','toyota','subaru']
len(cars)
print(len(cars))
```
> 4
***
***
## 3.4 Avoid Error in the List
```python
motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle[3])
```
> IndexError: list index out of range

Error - out of range - always remember start from 0, in this case, only 0, 1, and 2

```python
print(motorcycle[-1])
```
> suzuki

use -1 to get access to the last element even the length of list changed

```python
motorcycle = []
print(motorcycle[-1])
```
> IndexError: list index out of range

Error - when an error happened - check the length of the list
