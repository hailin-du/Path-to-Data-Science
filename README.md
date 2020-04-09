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
        * <
        * <=
        * >
        * >=
        * ==
        * !=
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
### Chapter 8 - Function
### Chapter 9 - Class
### Chapter 10 - Files and Exception
