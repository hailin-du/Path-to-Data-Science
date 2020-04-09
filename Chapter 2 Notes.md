# 2.1 `print()` is a function
```print('Hello Python World!')```

>     Hello Python World!
***
***
# 2.2 Variable
```python
message = 'Hello Python World!'
print(message)
message = 'Hello Python Crash Course World!'
print(message)
```
>     Hello Python World!
>     Hello Python Crash Course World!

## 2.2.1 Variable Naming Rule
```python
message_1 NOT 1_message
```
* No space between wording
* Not using key word or function name 
* Not too short
* Be careful with 1 and small "l", 0 and  captial "O"

## 2.2.2 Aviod Varibale Naming Error
```python
message = 'Hello Python Crash Course World!'
print(mesage) 
```
>     NameError: name 'mesage' is not defined
#### Error - not defined
***
***
# 2.3 String
```
"This is a string."
'This is also a string.'
```

```
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake"
"One of Python's strengths is its diverse and supportive community."
```

## 2.3.1 Changing String with Lower and Upper Case
```python
name = 'ada lovelace'
print(name.title())
```
>     Ada Lovelace
```python
name = 'Ada Lovelace'
print(name.upper())
print(name.lower())
```
>     ADA LOVELACE
>     ada lovelace
## 2.3.2 Combining String
```python
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + " " + last_name
print(full_name)
```
>     ada lovelace
```python
print("Hello, " + full_name.title() + "!")
message = "Hello, " + full_name.title() + "!"
print(message)
```
    Hello, Ada Lovelace!
## 2.3.3 Add Whitespace with Tab and Newline
```python
print('Python')
print('\tPython') # tab
```
>     Python
>         Python
```python
print("Languages:\nPython\nC\nJavaScript") # new line
print("Languages:\n\tPython\n\tC\n\tJavaScript") # tab + new line
```
>     Languages:
>     Python
>     C
>     JavaScript
    
>     Languages:
>         Python
>         C
>         JavaScript
## 2.3.4 Delete Whitespace
```python
favorite_language = 'python '
favorite_language = favorite_language.rstrip() # assign - end space remove
favorite_language
favorite_language.lstrip() # begin space remove
favorite_language.strip() # begin and end space remove
```
>     'python ' 
>     'python'
## 2.3.5 Aviod String (Symtax) Error
```python
message = 'One of Pthon's strengths is its diverse community'
print(message) # quotation
```
>     Error
Using "   ''   " 
Or
Using '   ""   ' within the space

***
***
# 2.4 Number
## 2.4.1 Integer
```python
2+3 # 5
3-2 # 1
2*3 # 6
3/2 # 1.5
3**2 # 9
3**3 # 27
10**6 # 1000000
```
>     5
>     1
>     6
>     1.5
>     9
>     27
>     1000000
```python
2+3*4 # 14
(2+3)*4 # 20
```
>     14
>     20

## 2.4.2 Float
```python
0.1 + 0.1 # 0.2
0.2 + 0.2 # 0.4 
2 * 0.1 # 0.2 
2 * 0.2 # 0.4
```
>     0.2
>     0.4
>     0.2
>     0.4
```python
0.2 + 0.1 # 0.30000000000000004 # included decimal will cause the number become float tpye
3 * 0.1 # 0.30000000000000004
```

## 2.4.3 Using `str()` Function to Aviod Data Type Error
```python
age = 23
message = "Happy " + age + "rd Birthday!"
print(message)
```
>     TypeError: Can't convert 'int' object to str implicitly
```python
message = "Happy " + str(age) + "rd Birthday!" # must be string
print(message)
```
>     Happy 23rd Birthday!
***
***
# `import this` The Zen of Python
## Simple > Complex
## Complex > Complicated
## Readability Count!
## Same Solution (Choose Simple One)
## Now Begin!! (Now is better than never)
```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
