# Object-Oriented Programming
An object can represent a thing or a scenario from the real world

1. You will define a `class`, and objects will belong to this `class`

1. Each object share similarities, and based on that, we assign each object with a unique personality

1. Based on the `class` to create an object,  this process is also known as instantiation, it allows you to use `class`'s instance.

# 9.1 Create and Use `class`
 `class` can simulate to be anything
* For example, a `class` = `dog`, it means it can be any type of dog but not a specific dog
* For most dogs, they will have a name and age
* Dogs will also know how to sit down and roll
* Our class, `dog` will include all these data
* The class `dog` will let python knows how to create the dog's objects

# 9.1.1 Create `Dog` Class
Based on `Dog` Class, each instance will store name and age, and assign the ability of `sit()`` and `rollover()`
```python
class Dog():
    # First try pretending training a dog
    def __init__(self, name, age):
        # initial property of name and age
        self.name = name
        self.age = age

    def sit(self):
        # pretentding ttraning a dog to sit
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        # pretending training a dog to roll over
        print(self.name.title() + ' rolled over!')
```
There are things we need to pay attention here!
* First, we defined a class named `Dog` (In python, **the upper case usually refer to class**)
* `__init__()` function inside the class called method. All you learn about the function is also known as the method (it is just the way you called the function is different, **function = method**)
* `__init__()` is a special method, every time the class `Dog` create a new instance, python will run it automatically
* Both the beginning and the end of `__init__()` have two underlines, which a way to avoid having name conflict with the normal method

#### `__init__()` includes three parameters
* `self` - **you must have, and must at the front**
* name
* age

1. While python calls the `__init__()` method (function) to create `Dog` instance, it will pass the arguments to `self`
1. Any method (function) related to this class will also pass the arguments to `self`, which `self` is a way that leads to the instance, let the instance to get access to the class's inside property and method  
1. While we create a dog instance, python calls the `Dog` class method `__init__()`
1. We will pass arguments `name` and `age` to `Dog()`, and let `self` to pass these arguments (you can think arguments are temporarily stored in `self` and pass them), so we don't need to pass them by ourselves
1. When we based on class `Dog` to create an instance, all we need is provide arguments to parameters `name` and `age` 

#### Understanding the Concept
* Both variables `self.name` and `self.age` have `self`， any variable with `self` at the front can be used inside the `class` or get access these variables by instance (data stored in `name` and `age`)
* `self.name = name` get element from the parameter `name` and stored in the variable called `name`
* So `name` variable will be associated with the current instance. 
* `self.age` is doing the same thing, anything using this method to store data, the data will also be called as property

#### Understanding the Method
* Class `Dog` also defined other two methods (functions), `sit()` and `roll_over`
* Because it does not need any extra elements like name or age, it only has one parameter, `self`
* Right now, both functions only printing out a message 
* But for game design purpose, we can add the effect under these functions
* Or the way to control the dog to do certain actions

# 9.1.2 Based on Class to Create Instance
Class `Dog`, is a series of instruction, letting the python know how to create dog instance

```python
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print('My dog is ' + str(my_dog.age) + ' years old.')
```

We create a dog, name `willie` and age `6`
* Python will use these arguments and call the Class `Dog`'s method `__init__()` to create a specific instance
* Then it will base on the arguments to create `name` and `age` 's property
* `__init__()` does not include `return statement`, but it will return this dog instance automatically
* We then save this instance in the variable name `my_dog`
* We can use upper case for class, like `Dog`, and lower case for instance like `my_dog` to store the instance 

#### 1. Accessing Property (We Use Period - Grammar)
```python
'my_dog.name'
```

* This grammar shows how python access the value from the property
* Python will first find the instance `my_dog`, and find the property `name` that matches with this instance
* In class `Dog`, the way to refer to this property is `self.name`
* Then, in the `print statement`, we changed the `name` to be uppercase `title()`, and the `age` to be a string `str()`

#### 2. Calling the Method
We can also use `.` period to use any other methods inside the class `Dog`

```python
my_dog.sit()
my_dog.roll_over()
```
Even though we don't know what the property or method do, by giving the descriptive name, like `name`， 'age', 'sit()', 'roll_over',  we can predict what does the function do

#### 3. Create Multiple Instances
```python
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print('My dog is ' + str(my_dog.age) + ' years old.')
my_dog.sit()
print("Your dog's name is " + your_dog.name.title() + ".")
print('Your dog is ' + str(your_dog.age) + ' years old.')
your_dog.sit()
```

>     My dog's name is Willie.
>     My dog is 6 years old.
>     Willie is now sitting.
>     Your dog's name is Lucy.
>     Your dog is 3 years old.
>     Lucy is now sitting.


* Even though we give the same name and age for the second dog, python will still base on class `Dog` to create another instance
* You can base on clas to create as many as instances you want, but each instance must be stored in a **different variable (different variable name)**
* Or **take a space** of a `list` or `dictionary`

# 9.2 Use Class and Instance
1. You can use `class` to simulate any scenario in the real world
1. After you have finished defining your class, most of the time will be using `class` to create an instance
1. One important thing is that you need to edit your instance property
1. Either edit the property directly
1. Or write a way inside the method to edit it
```python
class Car():
    # Pretend there is a car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        # Return a neat descritpive info
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
```

>     2016 Audi A4

We used the similar method `__init__()` to receive three parameters `make`, `model`, `year` and stored them inside the instance `my_new_car` created by this class
* When we create `Car` instance, we have to provide company, model, and production year
* We created a get_descriptive_name() method, and use the property `year`, `make` and `model` with `self` to get the access
* Based on class `Car`, we store the instance in `my_new_car`
* Then we call the method `get_descriptive_name()` to see which kind of car we are having

# 9.2.2 Assign Default Value to Property
Every property inside a class must have an initial value, no matter it is a 0 or empty string
1. Under some circumstances, we can set a default value inside `__init__()`, so we don't need to provide an initial value to that property
     * We will add `odometer_reading` property, given a default value `0`
     * We also added a `read_odometer()` method, to read the mile of a car
     
```python
class Car():
    # Pretend there is car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        # Return a neat descritpive info
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        # Print message about car mile
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```
* The method `__init__()` will store the properties for `make`, 'model`, 'year` but also create a property called `odometer_reading`
* However, not all the car have a 0 mile when the car arrives at the distributor
* So, we will add a way to edit the value

# 9.2.3 Edit Property's Value
