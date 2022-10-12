# Python introduction
## why python
###  Easy to Read, Learn and Write
- Python is a high-level programming language that has English-like syntax. This makes it easier to read and understand the code.
###  Improved Productivity
- Python is a very productive language. Due to the simplicity of Python, developers can focus on solving the problem. They don’t need to spend too much time in understanding the syntax or behavior of the programming language.
###  Vast Libraries Support
- The standard library of Python is huge, you can find almost all the functions needed for your task. So, you don’t have to depend on external libraries.
###  Python is a Simple Language
- Python is an easily readable and simple to understand language for developers who have never written a code in it. As a result, the community of Python users are continuously evolving and growing.
###  Python is Free
- Python is a programming language which is free of charge and open.
---
### What is a variable
- It is used to store data
- A reserved memory location to store values

An example
```doctest
first_name = "zakarie"
last_name = "hassan"
salary = 50
travel = 3.5
```

 ### what is a string

- A string in Python is a sequence of characters.

An example:
``first_name = "zakarie" #string``
 ### what is an integer
 - An integer is a whole number, positive or negative, without decimals, of unlimited length.

 - An example
``salary = 50 #integer``

### What is a float
- Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

An example
``travel = 3.5 #float``

### What is a boolean
- Boolean values are the values True or False in Python.

---

### Intro to Data types & operators
- `+ - *`

###### Comparison operators
- `>` greater than
- `<` less than
- `==` true or false
- `>=` greater than or equal
- `<=` less than or equal

```doctest
a = 24
b = 16

print(a + b) # outcome added value of a & b
print(a - b) # outcome -a from b
# comparison
print(a > b) # true
print(a < b) # false
```
```doctest
# Boolean Builtin methods in Python - Boolean Methods
# - DRY do not repeat yourself print("")

greeting = "Hello World!"
print(greeting)
print(greeting.isalpha())
print(greeting.islower())
print(greeting.startswith("H"))
print(greeting.endswith("!")) # checks if it ends with specific letter
print(greeting.isdigit())

```
```doctest
# String Slicing
# string indexing - starts from 0
# H e l l o   W o r l  d  !
# 0 1 2 3 4 5 6 7 8 9 10 11
#                   -3 -2-1

greeting = "Hello World!"
#print(greeting)
# we have builtin method that checks the len of string
#print(len(greeting)) #
print(greeting[-2])
print(greeting[0:5]) # prints 0-5
print(greeting[-6:]) #
# String Slicing
# string indexing - starts from 0
# H e l l o   W o r l  d  !
# 0 1 2 3 4 5 6 7 8 9 10 11
#                   -3 -2-1

greeting = "Hello World!"
#print(greeting)
# we have builtin method that checks the len of string
#print(len(greeting)) #
print(greeting[-2])
print(greeting[0:5]) # prints 0-5
print(greeting[-6:]) #

```

```doctest
# String Methods are available

# use var = string "asfdsfaasdfsadfsadf                                 "
white_space = "lot's of spaces at the end                                "
print(len(white_space))
# strip() removes the white spaces at the end of the string
print(len(white_space.strip())) # this will remove all the white spaces at the end
print(print(len(white_space)))

Example_text = "zakarie here's sOme text with lOt's of text"
# print(Example_text.count("text"))
print(Example_text)
print(Example_text.lower())
print(Example_text.upper())
print(Example_text.capitalize())
print(Example_text.replace("with", ","))

```

```doctest
# data collections
# lists
# tuples
# dict

# lists
# syntax list = ["gcjhgcgh", "fyfy", "jfhfh"]


# apply dry
shopping_list = ["ketchup", "fanta", "eggs", "bread"]
print(shopping_list)
print(type(shopping_list))
shopping_list.append("chicken") # add item to the list
print(shopping_list)
print(shopping_list[2])
shopping_list[2] = "icecream" # relplace eggs with icecream
print(shopping_list)
shopping_list.remove("fanta") # how to remove an item from list
print(shopping_list)




#can list have multiple data types
multiple_type = [1, 2, 3, "one", "five", "ten"]
#print(multiple_type)
#print(multiple_type[2])


# tuples
# immutable - cant be changed - edited -added
# user_details = DOB - country name - city name -
# Syntax ("")
essentials = ("milk", "paracetamol", "drinks")
print(essentials)
print(type(essentials))
# what is the diff between Lists & tuples
essentials [0] = "coffee"
print(essentials)

```

```doctest
# what is a Dictionary
# how to manage dictionaries - how to manage the data using dict
# it works as key value pair key = value
# syntax { "key": "value"     }

# store students data - name, course name, progress, completed lessons

student_1 = {
    "keys": "values",
    "name": "zakarie",
    "stream": "devops",
    "completed_lessons": 4,
    "completed_lessons_names": ["lists", "tuples", "strings"]
}
print(student_1)
print(type(student_1))
print(student_1["stream"]) # this will display the value saved inside stream

# print/ display completed_lessons_names
# print/ display completed_lessons_names_index 0 means lists

print(student_1["completed_lessons_names"])
print(student_1["completed_lessons_names"][0])

```

```doctest
student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

# delete an item from the list of completed_lesson_names
student_1["completed_lessons_names"].remove("strings")
print(student_1["completed_lessons_names"])

# dict builtin methods
# display keys only or values
# keys() values()

# displays keys only from student_1
print(student_1.keys())

# display values only from student_1
print(student_1.values())
```