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
- add ``gitignore`` then ``add all dependencies in this file to ensure not pushed``

```bash
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
```
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