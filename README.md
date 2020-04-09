Python Crash Course
===========================
Notes for Python Beginners

## Content
* [Chapter 2 - Variables And Simple Data Types](#Chapter-2---Variables-And-Simple-Data-Types) 
* [Chapter 3 - Introducing List](#Chapter-3---Introducing-List) 
* [Chapter 4 - Working with List](#Chapter-4---Working-with-List) 
* [Chapter 5 - if Statement](#Chapter-5---if-Statement)
* [Chapter 6 - Dictionary](#Chapter-6---Dictionary)
* [Chapter 7 - User Input and while Loop](#Chapter-7---User-Input-and-while-Loop)
* [Chapter 8 - Function](#Chapter-8---Function)
* [Chapter 9 - Class](#Chapter-9---Class)
* [Chapter 10 - Files and Exception](#Chapter-10---Files-and-Exception)

### Chapter 2 - Variables And Simple Data Types
* `print()` function
* 2.1 Variable
    * Variable Naming Rule
    * Avoiding Varibale Naming Error
* 2.2 String `str()`
    * Changing String with Lower and Upper Case
    * Combining String
    * Adding Whitespace with Tab and Newline
    * Delete Whitespace
    * Aviod String (Syntax) Error
* 2.3 Number
    * Integer `int()`
    * Float `float()`
    * Using `str()` Function to Aviod Data Type Error
    * `import this` The Zen of Python

### Chapter 3 - Introducing List
* 3.1 List（What is a List? `[]`) 
    * Access List's Elements
    * Slicing Index Positions - Start with 0 not 1
    * Use Every List's Elements
* 3.2 Change, Add, Delete Elements from the List
    * Add
        * `append()` function
        * `insert()` function
    * Delete
        * `pop()` function - delete element with index position)
        * `remove()` function - delete element with value)
        * `del()` function - delete element range)
* 3.3 Organize List
    * `sort()` function (permanently)
    * `sorted()` function (temporarily)
    * `reverse()` function 
    * 'len()` function
* 3.4 Avoid Error in the List


### Chapter 4 - Working with List
* 4.1 Looping Through an Entire List
    * Getting Deeper in (Understanding) the `for loop:`
    * Adding More Works in a `for loop:`
    * Doing Something After the `for loop:`
* 4.2 Avioding Indentition Error
    * Forget Indent
    * Forget Indent for Other Lines
    * Unnecessary Indent
    * Unnecessary Indent After the `for loop:`
    * Forget Colon
* 4.3 Create a Numerical List  
    * `range()` function (ex: for value in range(1,5))
    * Using `range()` to Create a List of Numbers
    * Simple Statistics Functions with a List of Numbers
    * List Comprehension - Complex (ex: [value ** 2 for value in range(1,11)])
* 4.4 Working with Part of a List - Slicing
    * Slicing 
    * Loopingg Through a List for Slicing
    * Copying a List Using `[:]`
* 4.5 Tuple `()`
    * Defining Tuple
    * Looping Through an Entire Tuple
    * Changing Tuple Elements
* 4.6 Conclusion
    * Separation
    * PEP 8
    
### Chapter 5 - if Statement
* 5.1 A Simple `if` Statement Example
* 5.2 Conditional Tests
    * Checking if Elements (Values) are Equal
    * Checking if Elements (Values) are Equal without Considersing Upper and Lower Case
    * Checking if Elements (Values) are Inequal
    * Comparing Number
    * Checking Multiple Conditions 
        * and 
            * If one of the condition didn't pass, the whole expression is `False`
        * or 
            * If one of the condition passes, the whole expression is `True`
            * If both conditions didn't pass, then the whole expression is `False`
    * Checking Whether a Specific Element in the List
    * Checking Whether a Specific Element NOT in the List
    * Boolean Expressions
* 5.3 `if` Statement
    * Simple `if` Statement Format 
    * `if-else` Statement
    * `if-elif-else` Structure
    * Using Multiple `elif` Blocks
    * Avoid Using `else` Block 
    * Testing Multiple Conditions
* 5.4 Using `if` Statement to Handle List
    * 5.4.1 Checking for Specific Element
    * Making Sure the List is Not Empty
    * Using Mutiple Lists
    * Style of `if` Statement 
       * `<`
       * `<=`
       * `>`
       * `>=`
       * `==`
       * `!=`
### Chapter 6 - Dictionary 
* 6.1 A Simple Dictionary
* 6.2 Using Dictionary
    * Accessing Dictionary's Value
    * Adding New Key-Value Pair
    * Create an Empty Dictionary First
    * Changing a Dictionary's Values
    * Delete Key-Pair in a Dictionary
    * Dictionary that Has Similar Objects' Key-Pairs
* 6.3 Looping Through an Entire Dictionary
    * Looping Through Each Key-Pair
        * `for key, value in variable_name.items():` - returning the key-pair list
    * Looping Through Each Key
        * `for key in variable_name.key():` - retruning the key value
    * Looping Through Each Key by Order
        *  `for key in sorted(variable_name.key()):`
    * Looping Through Each Paired Value
        * `for value in variable_name.values():` - retruning the paired value
        * `set()` function - avoid repeated value (return unique value)
            * `for value in set(variable_name.values()):`
* 6.4 Nesting 
    * A List of Dictionaries
    * Storing List Inside a Dictionary
    * Storing Dictionary Inside the Dictionary
* 6.5 Conclusion
### Chapter 7 - User Input and while Loop
* 7.1 Understanding `input()` function
    * Use `int()` fucntion to Get Numerical Input Value
    * Accessing `%` (Operator) Modulo
* 7.2 `while` Loop Introduction
    * Use `while` Loop
    * Letting the User to Choose When to Quit
    * Use Sign (Flag/Mark)
    * Use `break` Statement to Exist the `while` Loop = (`break` *will not* execute the remaining code)
    * Use `continue` Statement Inside a Loop = pass = (`continue` statement allows us to go back to the beginning of the loop)
    * Avoiding Infinite Loop (press ctrl+c to quit the loop)
* 7.3 Use `while` Loop to Handle List and Dictionary
    * Moving Items Between Lists
    * Delete Specific Element in the List
    * Allowing the User to Input Values to Fill Up A Dictionary
* 7.4 Conclusion
### Chapter 8 - Function
* 8.1 Defining a Function
    * Passing Data (Element) to the Function
    * Argument (Data (Element) You Pass) and Parameter (Variable - Data (Element) Needed to Perform A Specific Task)
* 8.2 Passing Argument (Data)
    * Argument Position (Position/Order) Association 
        1. Using the Function Multiple Times
        1. The Order of Argument is Important
    * Key-Word Argument Association   
    * A Default Element/Value
    * Using the Function Other Ways (Equivalent Function Calls)
    * Avoiding Argument Error
* 8.3 Return Element/Value
    * Return Simple Element/Value
    * Making Arguments Selectable
    * Returning a Dictionary
    * Combining Function with a `while` Loop
* 8.4 Passing a List
    * Editing a List inside a Function
    * Preventing the Function From Editing the List
* 8.5 Passing Arbitrary Numbers (As Many As You Want) of Arguments
    * Combine Argument Position Association with Arbitrary Numbers of Arguments You Want
    * Use Key-Word Association With Arbitrary Numbers of Arguments You Want
* 8.6 Saving Function in the Module
    * Importing an Entire Module You Just Created 
        * `import module_name`
        * `module_name.function_name()` = using function
    * `import` Specifc Function 
        * `from module_name import function_name`
        * `from module_name import function_0, function1, function2`
    * Using `as` to Assign Different Function Name 
        * `from module_name import function_name as fn`
    * Using `as` to Assign Different Module Name 
        * `import module_name as mn`
    * `import` All the Functions from a Module 
        * `from module_name import *`
* 8.7 Function Writing Guide（Styling Function)
* 8.8 Conclusion
### Chapter 9 - Class
* Object-Oriented Programming
* 9.1 Create and Use a `class`
    * Create the `Dog` Class
        * `__init__()` method 
            * `self` must have
    * Based on Class to Create Instance
        * Accessing Attribute
        * Calling the Method
        * Create Multiple Instances
* 9.2 Working with Class and Instance
    * The `car` Class
    * Assign Default Value to Attribute
    * Edit Attribute's Value
        * Edit the Value Directly    
        * Edit The Value Through Method
        * Edit The Value Through Method Adding 
* 9.3 Inheritance
    * Son (Child) Object's Method `__init()`
        * `super.__init__()` - superclass    
    * Define Son Class's Attribute and Method
    * Rewrite Father (Parent) Class Method
    * Use Instance as Attribute
    * Simulate Creating A Real World Instance (Object)
* 9.4 Importing Class
    * Import a Single Class
        * `from module_name import class_name`
    * Saving Multiple Class in a Module
    * Import Multiple Classes from A Module
    * Import a Single Class
        * `from module_name import class_0, class_2`
    * Import the Entire Module
        * `import module_name`  
    * Import All the Classes from a Module
        * `from module_name import *`
    * In A Module Import Another Module
        * `from module_0 import class_0`
        * `from module_1 import class_1`
    * Define Your Work Flow
* 9.5 Python Package (Python Standard Library) 
* 9.6 Style of Coding A Class
* 9.7 Conclusion
### Chapter 10 - Files and Exception
* 10.1 Reading Data From File
     * Reading an Entire File
        * `with oepn('file_name.file_format') as file_object:`
        * &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`variable_name = file_object.read()`
        * &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print(variable_name)`
        * Use `r.strip())` - `variable_name.rstrip()`
     * File Paths/Directory
        * `file_path = 'C:\Users\your_name\your_folder\your_folder2\filename.txt'`
        * `with open(file_path) as file_object:`
    * Reading Line by Line
        * `filename = 'file_name.file_format'`
        * `with oepn(filename) as file_object:`
        * &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`for line in file_object:`
        * &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print(line)`
        * Use `rstrip()` - `line.rstrip()`
    * Create A List That Contain Each Line From A File 
        * Access Line Outside the `with` Block
            * `filename = 'file_name.file_format'`
            * `with oepn(filename) as file_object:`
            * &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`lines = file_object.readlines()`
            * `for line in lines:`
            * &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print(line)`
            * Use `rstrip()` - `line.rstrip()`
     * Use File's Content       
            * Use `strip()` - `line.strip()`
     * Reading A Large File: One Million Digits
            * print(variable_name[:52]) - Slicing
     * Does Pi's Value Include Your Birthday?       
* 10.2 Writing A File
     * Writing A Emtpy File
        * `filename = 'file_name.file_format'`
        * `with oepn(filename, 'w') as file_object:`
        * &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`file_object.write("sentence_0`)
        * `r` reading mode
        * `w` writing mode
        * `a` appending mode
        * `r+` reading and writing mode
     * Writing Multiple Lines
        * Use \n newline
        * `file_object.write("sentence_0\n`)
        * `file_object.write("sentence_1\n`)
     * Append to A File
        *  Use `a` Appending Mode - `with open(filename, 'a') as file_object:`    
* 10.3 Exceptions         
     * Handle `ZeroDivisonError` Exception
     * Use `try-except` Block 
     * Use Excpetion to Avoid Crashing
     * `else` block
        * Codes that rely on the `try` block should be placed on `else` block
     * Handle `FileNotFoundError` Exception
     * Analyzing Text
        * `split()` - Split a Long String 
        * `len()` - To Count Length 
     * Working with Multiple Files 
        * Put Flies in a List 
        * `filenames = ['file_0.txt', 'file_1.txt', file_2.txt`]` 
        * `for filename in filenames:` 
     * Failing Silently 
        * `pass` Statement 
     * Deciding Which Errors to Report 
* 10.4 Storing Data
     * JSON Module - `import json`
     * Using `json.dump()` And `json.load()`
        * `filename = 'numbers.json'`
        * `with open(filename, 'w') as f_obj:`
        * &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`json.dump(variable_name, f_obj)`
        * 
        * `filename = 'numbers.json'`
        * `with open(filename) as f_obj:`
        * &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`variable_name = json.load(f_obj)`
        * &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print(ariable_name)`
     * Saving and Reading User-Generated Data
     * Restrcutre/Refactor Codes
* 10.5 Conclusion
