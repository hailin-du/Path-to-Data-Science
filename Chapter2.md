# 2.1 print is a function
```print('Hello Python world!')```
# 2.2 Variable
```
message = 'Hello Python World!'
print(message)
message = 'Hello Python Crash Course world!'
print(message)
```
## 2.2.1 Rule
```
message_1 not 1_message
```
#### no space
#### no key word and function naming
#### short 
#### careful with 1 and small l, 0 and  captial O

## 2.2.2
```
message = 'Hello Python Crash Course world!'
print(mesage) 
```
#### Error - not defined

# 2.3 string
```
"This is a string."
'This is also a string.'
```

```
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake"
"One of Python's strengths is its diverse and supportive community."
```

## 2.3.1 Change String
```name = 'ada lovelace'
print(name.title())
name = 'Ada Lovelace'
print(name.upper())
print(name.lower())
```

## 2.3.2 Combine String
```
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")
message = "Hello, " + full_name.title() + "!"
print(message)
```

## 2.3.3 Add Space
```
print('Python')
print('\tPython') # tab
print("Languages:\nPython\nC\nJavaScript") # new line
print("Languages:\n\tPython\n\tC\n\tJavaScript") # tab + new line
```

## 2.3.4 Delete Space
```
favorite_language = 'python '
favorite_language = favorite_language.rstrip() # assign
favorite_language
favorite_language.lstrip() # leading space remove
favorite_language.strip() # leading and ending space remove
```

## 2.35 Aviod Error
```
message = 'One of Pthon's strengths is its diverse community'
print(message) # quotation
```
#### Error

# 2.4 Number
## 2.4.1 Integer
```
2+3 # 5
3-2 # 1
2*3 # 6
3/2 # 1.5
3**2 # 9
3**3 # 27
10**6 # 1000000
```

```
2+3*4 # 14
(2+3)*4 # 20
```

## 2.4.2
```
0.1 + 0.1 # 0.2
0.2 + 0.2 # 0.4 
2 * 0.1 # 0.2 
2 * 0.2 # 0.4
```

```
0.2 + 0.1 # 0.30000000000000004 included decimal different
3 * 0.1 # 0.30000000000000004
```

## 2.4.3
```
age =23
message = "Happy " + age + "rd Birthday!"
print(message)
# Error
message = "Happy " + str(age) + "rd Birthday!" # must be string
print(message)
```

# import this
## simple
## complex
## readable
## same solution
## now begin!!
