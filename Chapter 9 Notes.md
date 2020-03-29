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
    # First try simulating training a dog
    def __init__(self, name, age):
        # initial property of name and age
        self.name = name
        self.age = age

    def sit(self):
        # simulating ttraning a dog to sit
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        # simulating training a dog to roll over        # Return a neat descriptive info
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
    # Simulate there is a car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self):
        # Return a neat descriptive info
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
    # Simulate there is car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        # Return a neat descriptive info
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
There are three different ways to edit the property's value
1. Edit the value through instance
1. Edit the value through setting a rule inside a method
3. Edit the value through adding value inside a method

#### 1. Edit the Value Directly
```python
class Car():
    # Simulate there is a car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        # Return a neat descriptive info
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        # Print message about car mile
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name()) 
my_new_car.odometer_reading = 23 (This line)
my_new_car.read_odometer()
```
>      2016 Audi A4
>      This car has 23 miles on it.
We used `. period` to get access to the car's property `odometer_reading` 
* **This line** of code will let python to find `odometer_reading` property from instance `my_new_car` and set the value to 23
* Sometimes we can access the property directly, but sometimes we need to update the property inside the method

##### 2. Edit The Value Through Method
# having update method is much better, you don't need to access the property
# it allows you to pass the value to the method, and update it inside 
```python
class Car():
    # Simulate there is a car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        # Return a neat descriptive info
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        # Print message about car mile
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')
   
    ### Added a new method
    def update_odometer(self, mileage):
        # Assign a specific value to the mile reading
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
```
>      2016 Audi A4
>      This car has 23 miles on it.
We have added a new method `update_odometer()` to let this method to receive a mileage value, then store in `self.odometer_reading`
* Then, we call the `update_odometer()` and provide it with a value 23
* We can even expand the `update_odometer()` method to do more works
* Here, we will stop anyone to edit the mile reading downward
```python
class Car():
    # Simulate there is a car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        # Return a neat descriptive info
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        # Print message about car mile
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        # Assign a specific value to the mile reading
        # Stop anyone edits the value downward
        ### Added a new logical statement
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
```
Now, `update_odometer()` will check if the value makes sense before changing the value
* If the new value `mileage` is greater than or equal to`self.odometer_reading, we will assign that value
* If not, we give a warning

#### 3. Edit The Value Through Method Adding 
Sometimes, we will need to increase the value of the property instead assigning a new value
* For example, we purchase a second-hand car, from purchase to registration we increased 100 mileage
* The following method can help us to pass that increase and add that into mileage variable
```python
class Car():
    # Simulate there is a car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        # Return a neat descriptive info
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        # Print message about car mile
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        # Assign a specific value to the mile reading
        # Stop anyone edits the value downward
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    ### Added a new method
    def increment_odometer(self, miles):
        # Add specific value to the mile reading
        self.odometer_reading += miles

my_new_car = Car('subaru', 'outback', 2013)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23500)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()
```
>     2013 Subaru Outback
>     This car has 23500 miles on it.
>     This car has 23600 miles on it.
We have added a new method `increment_odometer()` to receive a unit of miles as a number and store that into self.odometer_reading
* Then, we created an instance, `my_used_car`
* Third, we called the method `update_odometer()` and pass the value 23500
* Lastly, we called the method `increase_odometer()` and pass the value 100

You can edit this value to make sure the increase is positive only not negative

# 9.3 Inheritance
When writing class, you don't need to start from the zero
* If you are **writing a class** that is a special version for the class that **already exists**, you can use **inheritance**
* When a class inherit from another class, that class can get all the properties and methods from another class
* The original class is called the **father** class, and the new class is called **son** class
* The son class will inherit all the properties and methods from the father class and can also define its own property and method

# 9.3.1 Son Object's Method `__init()`
When creating the son object instance, python will first need to complete the task, which passing all methods and properties to the son class
* Therefore, the son class needs the method `__init__()`  to inherit father class's methods and properties
* For example, we stimulate an electric car, but an electric car is a special car different than the traditional cars, so we will need to create a new class first based on previous class `Car()`
* Then, we just need to provide special property or behavior only for the electric car, but the electric car also has the common properties as other traditional cars cars
```python
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    # The Specialty of An Electric Car
    def __init__(self, make, model, year):
        # Inherit father class's property = Initial property for son
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
```
>     2016 Tesla Model S
Part 1 Creating
1. When creating son class, the father class must be included in the current file, and **at the front** of the son class
1. Also, when we have defined son class, the parenthesis much include the father class, **ElectricCar(Car)** and `__iniit__()` is to receive info from the instance when creating a car (inherit)
1. `super() function` is a special function to help to associate son class and father class (connect, passing)
1. This function let python to call `ElectricaCar` method `__init__()` from the father's method `__init__()`, let `ElectricCar` instance include all the properties from the father class (father class also known as superclass, there is name super coming from)

Part 2 Testing
* To test if the inherit works, we have tried to create an electric car, but providing the same info like creating a normal car
* We have created an instance, and stored in the variable name `my_tesla`
* It will call the `ElectricCar` class's method, `__init__()`, which let python to use/call father class `Car`'s method `__init()__`
* We provided arguments 'tesla`, `model s`, and `2016`.
* Except that, the electric car has not yet been provided with a special property, we just want to confirm if the electric car has the same properties as a normal car

# 9.3.3 Define Son Class's Property and Method
After the inheritance, we can add new property and method to distinguish the son and the father class
* We are adding a special property for an electric car, and a method that describes it
```python
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    # The Specialty of An Electric Car

    def __init__(self, make, model, year):
        # Inherit father class's property = Initial property for son
        # Add the initiation value for son class's special property
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        # Print a message to describe battery volume
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```
>     2016 Tesla Model S
>     This car has a 70-kWh battery.
We add the new property, `self.battery_size` and set the default value to 70
* The instance created under the `ElectricCar()` class will include that battery property, but other traditional cars won't include that
* We also added a method `describe_battery()`, to print the battery information.

There is no limitation for creating special things, you can base on the need to add property or method
1. If a property or method also have in common with all other cars, then it should be added under `Car` class, not the `ElectricCar` class       

# 9.3.4 Rewrite Father Class Method
For the father class's method, if it doesn't match with the son class's behavior, then we can always **rewrite it**
* So, we can define a method in the son class, that method has the **same name** as the one in the father class method
* Then, python will not consider father class's method, only follow the rule on son class's new defined method

For example, if a `Car` class has a method called `fill_gas_tank()`, it is pointless to the electric car, we can rewrite as below
```python
class ElectricCar(Car):
    # --snip--

    def fill_gas_tank(self):
        # electic car has no gas tank
        print("This car doesn't need a gas tank!")
```
In Inheritance, son class can keep father class's good property, and ignore the bad ones
* Now, if someone calls that method for an electric car, python will ignore the `Car` class's method, and run the above code `print` only

# 9.3.5 Use Instance as Property
When using code to stimulate an instance in real life, you may realize you have added more and more details, such as property, and method, the file getting longer and longer
* Under this circumstance, we may need to take out a part of the class as a special class, which dividing the class into small classes
* For example, when we adding details for the electric car, we may realize that there are so many special properties and methods to be added
* Then, we can take these properties and methods out, and put that into a new class name `Battery`
* And, using `Battery` instance as a property in `ElectricCar()` class

```python
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    # Simulate battery for an electric car
    
    def __init__(self, battery_size=70):
        # Initiation value for battery property
        self.battery_size = battery_size

    def describe_battery(self):
        # Print a message to describe battery volume
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

class ElectricCar(Car):
    # The Specialty of An Electric Car
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        #### Create new battery instance 
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
```
We have defined a new class name `Battery`, it didn't inherit anything from any other class
* `__init__()`, includes `self`, and another parameter name `battery_size`, this parameter is selectable
* When no argument is provided, the **default value is 70**
* Also, the `describe_batttery()` method **moved to** the `Battery` class

In `ElectricCar()` clas's we added a property called `self.battery`, this allows python to create a new `Battery` instance
* Because no value is provided, the default value is 70, and store that instance in `self.battery`
* Every time the method `__init__()` is being called, it will automatically create `Battery` instance for every `ElectricCar` instance
```python
`my_tesla.battery.describe_battery()` 
```
>     2016 Tesla Model S
>     This car has a 70-kWh battery. 
This line of code let python find battery property inside the instance `my_tesla`, and use describe_battery() to call the property from the `Battery` instance
* Even though it seems like there are more works, but now we can add as many as details we want for the electric car without messing up the `ElectricCar` class

Next we are adding one more method under `Battery` class to describe how far the electric car can go base on the volume of the batter
```python
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    def __init__(self, battery_size=70):
        # Initiation value of battery property
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')  
        
    ### Added a new method for car's range
    def get_range(self):
        # Print a message to describe how far the electric car can go
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = 'This car can go approximately ' + str(range)
        message += ' miles on full charge.'
        print(message)

class Battery():
    def __init__(self, battery_size=70):
        # Initiation value of battery property
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')  
        
    ### Added a new method for car's range
    def get_range(self):
        # Print a message to describe how far the electric car can go
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = 'This car can go approximately ' + str(range)
        message += ' miles on full charge.'
        print(message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```
* We have added a simple `if-elif statement` under the method `get_range()`, then print out the message
* We used property `battery` to call the method

>     2016 Tesla Model S
>     This car has a 70-kWh battery.
>     This car can go approximately 240 miles on a full charge.

# 9.3.6 Simulate Creating A Real World Instance
Simulate creating a real object is always difficult, like range mile is a property for `Battery` or `ElectricCar`
* For example, under the production line perspective, we should move `get_range()` under `ElectricCar` class; so `get_range` will base on battery volume to determine range mile, but report only ONE type of car with different batteries
* We can also keep `get_range` under `Battery`, but passing a reference like `car_model`, so `get_range` will base on battery volume and car's model to report range mile

When you get into this level, you have to think in a higher logical layer
* You will not only focus on python grammar but also need to think about how to use code to present the real object
* In the real world, the method of creating a model has no right or wrong answer
* Only with a model more efficient than others, so you have to practice to find the best one

# 9.4 Load the Class
As your file getting longer and longer, we can store class in the module

## 9.4.1 Load Single Class
We will create a module that only includes Class` Car` in a file name `car.py`
* From now on, any file that uses the module from the file name `car.py` has to be renamed differently to avoid having the same file name

**car.py**
```python
# A module to represent Car 

class Car():
    # Simulate there is a car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        # Return a neat descriptive info
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        # Print message about car mile
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        # Assign a specific value to the mile reading
        # Stop anyone edits the value downward
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        # Add specific value to the mile reading
        self.odometer_reading += miles
```
We should always give a brief introduction about what the class does, and with a simple description of what each function do

**my_car.py**
```python
from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23

my_new_car.read_odometer()
```
Similar, we use `import statement` to import the whole `Car` class
* By importing the class, we can keep the file short and focus on the logic of the current file
* After you have determined how the class should work, you can ignore that class file and focus on a higher logical layer

# 9.4.2 Saving Multiple Class in a Module
We can save as many as class we want
* We are adding `Battery` and `ElectricCar` in the Module

**car.py**
```python
# A module to represent Traditional Car and Electric Car 

class Car():
    # Simulate there is a car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        # Return a neat descriptive info
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        # Print message about car mile
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        # Assign a specific value to the mile reading
        # Stop anyone edits the value downward
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        # Add specific value to the mile reading
        self.odometer_reading += miles
 
 class Battery():
    # Simulate battery for an electric car
    def __init__(self, battery_size=70):
        # Initiation value of battery property
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')  
        
    def get_range(self):
        # Print a message to describe how far the electric car can go
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = 'This car can go approximately ' + str(range)
        message += ' miles on full charge.'
        print(message)

class ElectricCar(Car):
    # The Specialty of An Electric Car
    def __init__(self, make, model, year):
        # Inherit father class's property = Initial property for son
        super().__init__(make, model, year)
        # Create new battery instance 
        self.battery = Battery()
```
Now, we will create new file name `my_electric_car.py`and load the ElectricCar class to create an electric car

**my_electric_car.py**
```python
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s',  2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```
>     2016 Tesla Model S 
>     This car has a 70-kWh battery. 
>     This car can go approximately 240 miles on full charge.

## 9.4.3 Import Multiple Class from A Module
```python
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
```
We have loaded multiple `class`, and use comma to separate them. Then we can build as many as instances we want base on the need
* In the following example, we have created a Beetle Car, and a Tesla Electric Car
>     2016 Volkswagen Beetle
>     2016 Tesla Roadster

## 9.4.4 Import the Whole Module
You can import the whole module and use `.` period to get access to the class you want
* So when you use the `car` module, python won't have conflicts with any variable name in the current file
```python
import car 

my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
```
We have loaded the whole module, and use the below code to access the class. And we have created two instances as the previous block of codes
```python
module_name.class
```

## 9.4.5 Import All the Class in the Module
To import every class we can use below code
```python
from module_name import *
```
However, such an import method is **not recommended**. There are two reasons
1. One, if you are being specific on what class being imported at the beginning, other programmers can read the list immediately
      1. If you import all, there may be confusion for other programmer thinking about what class you have imported
2. Plus, if you imported a class that has the same name as other variables in the current file, there will be difficult finding a bug
      1.The reason introducing this method is because you may see someone using it

The best way is to use `module_name.class_name` to get access to the class
* So even you didn't list what class you have imported at the beginning, at least you know the location where you have used the class inside the file and avoid variable name conflicts

## 9.4.6 In A Module Import Another Module
Sometimes, we have to separate `class` into different modules to avoid the module getting too large
* Or, we will store irrelevant class in the same module
* Also, you may find out that sometimes a module depends on another module's class
* Therefore, we can import a module from one module to another

Below, we have saved the `Car` class in a module and saved the `ElectricCcar` and `Battery` in another module (file) name as `electric_car.py`
**electric_car.py**
```python
# Class that represent Electric Car

from car import Car

class Battery():
    # Simulate battery for an electric car
    def __init__(self, battery_size=70):
        # Initiation value of battery property
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')  
        
    def get_range(self):
        # Print a message to describe how far the electric car can go
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = 'This car can go approximately ' + str(range)
        message += ' miles on full charge.'
        print(message)

class ElectricCar(Car):
    # The Specialty of An Electric Car
    def __init__(self, make, model, year):
        # Inherit father class's property = Initial property for son
        super().__init__(make, model, year)
        # Create new battery instance 
        self.battery = Battery()
```
`ElectricCar` need to get access to its father class `Car`, so we will import `Car` directory into the module to `electric_car.py`
* If we forgot to import, there will be an error when we try to create `ElectricCar` instance.
* Don't forget updating the `car.py` module with a new brief introduction

**car.py**
```python
# A module to represent Car 

class Car():
    # Simulate there is a car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        # Return a neat descriptive info
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        # Print message about car mile
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        # Assign a specific value to the mile reading
        # Stop anyone edits the value downward
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        # Add specific value to the mile reading
        self.odometer_reading += miles
```
Now, we can import different class from different modules, base on the need to create any type of car
```python
from car import Car
from electric import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
```
>     2016 Volkswagen Beetle
>     2016 Tesla Roadster
We have imported the `Car` class from `car.py` module, and imported `ElectricCar` class from `electric_car.py` module

## 9.4.7 Define Your Work Flow

As you see, when organizing a big project of codes, python provides many options
* Understanding these options allow to your organize your project and also understand how other programmers develop their projects
* First, we should keep the code structure as simple as possible and complete everything in one single documents
* Then we can separate them into different modules

## 9.5 Python Package
Python Package is a series of modules. They are included when you installed python.
* These modules are completed by other programmers, we can use any function or class by using the `import` statement

Dictionary allows you to associate with value, but **not record the order** of adding your paired values
* To create a dictionary and record the order, we can use the module called `collections` and use its class `OrderedDict`
* `OrderedDict` will do the same thing as the dictionary does, except recording the order of added values

**favorite_languages.py**
```python
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + '.')
```
1. We have imported the `OrderedDict` class from module `collections`
1. Then we created an `OrderedDict` instance and stored in `favorite_languages` variable	
      1. Pay attention here, we didn't use bracket `{}`, instead we use `OrderedDict()` to create an empty ordered dictionary and stored in `favorite_languges`
1. Then we can add each paired name - language
1. When we go over the `favorite_languages` dictionary, the output is showed by order

>     Jen's favorite language is Python. 
>     Sarah's favorite language is C. 
>     Edward's favorite language is Ruby. 
>     Phil's favorite language is Python.
It is a very good class that includes the feature of dictionary and list, but also keeping the value in order

As you develop your skill, you may realize that an ordered dictionary will solve some of your coding questions

# 9.6 Style of Coding A Class
You have to be familiar with the style of coding a class, especially when you coding something very complicated
* The class name should follow **Camel-Case** rule, which 
1. Every class name first letter of a word should be capital not underline
1. Instance name and module name should use lowercase format and underline between each word

After defining a class, you should include 
1. A brief description of the class feature 
1. A brief description of what the function does
1. A brief description of the purpose of the module

We can use space to separate or organize code but do not abuse it
* Inside the class, we can use single space to separate functions
* In the module, we can use double space to separate class

When importing class, you should
1. Import the standard module's class first,
1. Then add a space, and import the class from your well-written module
* So when others reading the program, they know which module belongs to where

# 9.7 Conclusion
In this chapter, you learned:
* How to write class,
* How to use class's property to store information
* How to write method, to let the class include necessary behaviors
* How to write method `__init__()` to base on what value is needed for an instance
* How to edit instance's value
     * Directly edit the value
     * Use method to edit value
* How to use inheritance to create relevant class 
     * Use an instance from another class as a property to another class (neat and easy to read)
* How store class in a module and load them (organize)
* How to use Python Packages (`collections` module - `OrderedDict` class)
* How to follow Python's rule


