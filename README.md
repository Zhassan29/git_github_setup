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
## Github setup
Generate ssh key
```doctest
cd /c/Users/zak
cd .ssh
ssh-keygen -t rsa -b 4096 -C "(your_email")
```
Add SSH public key to Github account. read SSH key by copying the public key

Create a repository on GitHub and follow the steps to connect to Pycharm
```doctest
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin "git@github:[username]/[repository].git"
git push -u origin main
```
#### Git & Github
- add changes to our Git-hub repo -the changes that we made on localhost

-``git add filenames`` or ``git add .`` , means push everything from current location
- ``git commit -m "new markdown guide added"``
- now lets send this new data to Github
- ``git push -u origin main``
- ``git status``