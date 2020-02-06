# 3.1 List
#### Can be 0-9, family names, or elements no relationship
#### use [] to create list
```
bicycles = ['teak','canondale','redline','specialized']
print(bicycles)
```
## 3.1.1 Access List
```print(bicycles[0])``` 

##### teak

```print(bicycles[0].title())```

## 3.1.2 Start with 0 not 1
```print(bicycles[1])```
##### canondale
```print(bicycles[3])```
##### specialized

```print(bicycles[-1])```
##### -1 last position
##### specialized

## 3.1.3 use list elemnt
```
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
```

# 3.2 Change, add, delete elements from List
## 3.2.1 Change
```
motorcycle = ['honda','yamaha','suzuku']
print(motorcycle)
motorcycle[0] = 'ducati'
print(motorcycle)
```

## 3.2.2 Add
```
motorcycle.append('ducati')
print(motorcycle)
```

#### provide user to append, so create a empty list
```
motorcycle2 = []
motorcycle2.append('honda')
motorcycle2.append('yamaha')
motorcycle2.append('suzuku')
print(motorcycle2)
```

### insert function
```
motorcycle = ['honda','yamaha','suzuku']
```
```
motorcycle.insert(0, 'ducati') # 0 as add space to , rest move to right
print(motorcycle)
```

## 3.2.3 Delete
```
motorcycle = ['honda','yamaha','suzuku']
del motorcycle[0] 
```
###### honda gone
```
print(motorcycle)
```
```
motorcycle = ['honda','yamaha','suzuku']
del motorcycle[1]
print(motorcycle) 
```
##### yamaha gone

### pop function to delete
#### pop allow to delete the last element but continue using it
```
motorcycle = ['honda','yamaha','suzuku']
print(motorcycle)
```
```
popped_motorcycle = motorcycle.pop() 
```
#### take the last element 
#### for example - if motorcycle is purchased based on time, using pop to take the latest one
```
print(motorcycle)
print(popped_motorcycle)
```
```
motorcycle = ['honda','yamaha','suzuku']
last_owned = motorcycle.pop()
print('The last motocrcyle I owned was a ' + last_owned.title() + ".")
```

#### You can use pop() to delete any element by adding position
```
first_owned = motorcycle.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
```

#### remember once you used pop, the element is NOT in the list anymore
#### Del - not going to use element anymore
#### Pop - after delete you want to use the element

### remove function - not knowing element position
```
motorcycle = ['honda','yamaha','suzuku','ducati']
print(motorcycle)
```
```
motorcycle.remove('ducati')
print(motorcycle)
```
#### using remove to delete can still keep using the element
#### pointing the reason why you delete it
```
motorcycle = ['honda','yamaha','suzuku','ducati']
```
```
too_expensive = 'ducati'
motorcycle.remove(too_expensive)
print(motorcycle)
print('\nA ' + too_expensive.title() + ' is too expensive for me.')
```
#### remove only delete one single element, if the element in the list appear mutliple times, you may need a loop to decide if you are going to delete all of them.

### position always change when you pop or delete

## 3.3 Organize List
#### List order is unpredicatble baase on the input of user, you can adjust the order

## 3.3.1 Sort() function
```
cars = ['bmw','audi','toyota','subaru']
cars.sort() # sorted based on alphabet
print(cars)
```
```
cars.sort(reverse=True)
print(cars)
```
### 3.3.1 Sorted() function - sort list without affecting the orginal
```
cars = ['bmw','audi','toyota','subaru']
print('Here is the original list:')
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print('Here is the original list again:')
print(cars)
```
#### sometimes lower case and upper case order are more complicated

### 3.3.3 reverse() 
#### for example - car is purchased based on time
```
cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)
```
#### revese() forever changing the order of a list

### 3.3.4 len() - count the length of the list
```
cars = ['bmw','audi','toyota','subaru']
len(cars)
print(len(cars))
```

## 3.4 Avoid Error in List
```
motorcycle = ['honda','yamaha','suzuku']
print(motorcycle[3])
```
### Error - out of range - always remeber start from 0

```
print(motorcycle[-1])
```
### use -1 to get access to the last element even the length of list changed

```
motorcycle = []
print(motorcycle[-1])
```
### Error - when error happened - check the length of a list
