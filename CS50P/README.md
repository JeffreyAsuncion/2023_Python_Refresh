
https://cs50.harvard.edu/python/2022/

## 2023.07.02 10:58:00 - CS50P - Intro


CLI - command line interface

functions are actions or verbs

arguments are inputs to a functions that influence its behavior

side effects are the products of a function

bugs are a mistake in a program

SyntaxError an error in the coding side


importance of 
- readability
- simiplicity


reasonable people can disagree, but justify


Scope
- variable scope

## 2023.07.02 20:00:00 CS50P - Lecture 01 - Conditionals

>
>=
<
<=
==
!=

if, elif, else, or, and

if, elif, elif, elif, else
can be substituted for 
match - which is like switch

# match is in Python 3.10 and higher


## 2023.07.03 05:51:23 CS50P - Loops

while, for, range, list
dicts
list of dicts
None

dictionary are highly preformant, hashmap

What's good about functions is that you can change
- the underline implementation details 
- as long as you don't change
    - the name of the function
    - its parameter
    - what it returns 

so you can change want happens underneath the hood,
as long as functionality is the same

## 2023.07.03 07:26:00 Lecture 03 - Exception 

Syntax Error - errors in code before run-time

Defensive Programming
need to test Edge Cases or Corner Cases
for integer input
- positive
- zero
- negative
- char or string

return is stronger than break
- they both get you out of a loop 
- but return also returns a value

try, except, else, break, return, pass

## 2023.07.03 11:55:00 Lecture 04 - Debugging

set breakpoint

play debug icon

continue, step over, step into, step out

## 2023.07.03 12:15:00 Lecture 04 - Libraries

modules is a library with one or more functions or other features built-in
- reusability of code, factor out code and create a library/module

example libraries that come with python
- random

docs.python.org/3/library/random.html

import keyword
from keyword

command-line arguments

python hello.py ...

- sys

docs.python.org/3/library/sys.html

sys.argv


3rd party modules - packages

pypi
pypi.org

pypi.org/project/cowsay


package manager pip

pip install cowsay

- requests

pypi.org/project/requests

json - language agnostic format for exchanging data, text file in a json format

Libraries


## 2023.07.03 15:15:00 CS50P - Style

up until now, we have been writing code that is hopefully at least correct. 
- (does want it is intended to do)

and hopefully it is well designed. 
- relatively a few lines of code to achieve some goal while still readable 
- using functions, prevent re-invent the wheel
- probably not the best style? or form of quality for some code

Style is subjective
- programmer
- company
- course
- language

PEP8 - Python Enhancement Proposal
- set of proposals of standards rules?

style is for
- readability
- maintanability 

peps.python.org/pep-0008/

"Readability counts"
- "A style guide is about consistency. Consistency with this style guide is important.  Consistency within a project is more important. Consistency within one module or function is the most important."


What is Style?
- Indentation: yes
- Tabs or Spaces?: spaces 4
- Maximum Line Length: 
- Blank Lines
- Imports: top in order
- ...

style tools

pylint
pip install pylint
pycodestyle.pycqa.org

pycodestyle
pycodestyle.pycqa.org

black
pip install black
black.readthedocs.io

# to format > black students.py

## 2023.07.03 15:38:00 CS50P - Lecture 05 - Unit Test

1. write code
2. test with sample inputs

good to get into the habit of testing your code with code of your own
- unit tests

unit tests
- confidence 
- validation

pytest
- will automate the test
- as long as you write the tests

pip install pytest
docs.pytest.org

pytest test_calculator

test for 
- user input
- functionality? math?

breakdown the tests for different categories
- positive numbers
- negative numbers
- zero

pytest 
F -->> fail
. -->> pass


# important Note
- pytest tests return values
- pytest does not test side effects (like prints)

Make your test 
- simple
- small

Create test folder
- __init__.py
- test_hello.py

the init is to treat the folder as a package

pytest test



## 2023.07.03 18:44:00 CS50P - Lecture06 - File I/O

File I/O is about saving files persistently

open
docs.python.org/3/library/functions.html#open


file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

vs the more pythonic way

with open("names.txt", "a") as file:
    file.write(f"{name}\n")

csv.reader VS csv.DictReader

csv. Reader() allows you to access CSV data using indexes and is ideal for simple CSV files. csv. DictReader() on the other hand is friendlier and easy to use, especially when working with large CSV files.

-PIL
pillow.readthedocs.io



## 2023.07.03 17:46:00 - CS50P - Lecture07 - Regular Expressions

Regular Expressions - regexes - a pattern

use patterns to match to certain type of data input
- email address 
- website
- app on phone
to validate the correct data / validate your input

Regex is to help define patterns in our code. and compare it form the data from someone else. 
or
to clean up data that is too messy. 

- re library
docs.python.org/3/library/re.html

re.search(pattern, string, flags=0)

'.' -->> any character except a new line
'*' -->> 0 or more repetitions
'+' -->> 1 or more repetitions
'?' -->> 0 or 1 repetitions
{m} -->> m repetition
{m,n} -->> m-n repetitions
'^' -->> matches the start of the string
'$' -->> matches the end of the string or just before the newline at the end of the string


r'\.' -->> literal .
'[ ]' -->> set of chars
'[^@]' -->> any char except @

\d -->> decimal digit
\D -->> not a decimal digit
\s -->> whitespace character
\S -->> not a whitespace character
\w -->> word character ... as well as numbers and the underscore
\W -->> not a word character

A|B -->> either A or B
(...) -->> a group
(?:...) -->> non-capturing version


FLAGS
re.IGNORECASE
re.MULTILINE
re.DOTALL


# Reasonable people might agree to disagree

# 1:12:31 

re.match(pattern, string, flags=0)

:= walrus operator
- assignment in a conditional 


re.sub

re.split(pattern, string, maxsplit=0, flags=0)

re.findall(pattern, string, flags=0)
- search for multiple copy of string


## Reges helps Express these patterns in order to 
* Validate Data
* Clean up Data 
* Extract Data


## 2023.07.05 09:57:00 - CS50P - Lecture08 - Object-Oriented Programming


data types

tuple -->> immutable
list -->> mutable

you can index into both using #'s [ ]

dict --> mutable 
as for access you access each part of dictionary by name instead of by number 
which is more clear and expressive by name of variable


docs.python.org/3/tutorial/classes.html

class
- a blueprint for pieces of data
- object
- a mold that you can define and give a name
- when you use that mold or blueprint, you get types of data, just like what you want
- classes allow you to invent your own data types in Python and given them a name

class
- attributes
- instance variables
- methods
- class variables
- properties : an attribute with more defense mechanisms
- decorators @property

def __init__

encapsulate all functionality related to that class
- validate that name exists
- validate if a house is correct

__str__ -->> for User
__repr__ -->> for Developer



Integer - int
docs.python.org/3/library/functions.html#int
class int(x, base=10)

String - str
class str(object='')

Lists - list
class list([iterable])
docs.python.org/3/library/stdtypes.html#list

Dictionary - dict
class dict
docs.python.org/3/library/stdtypes.html#dict




class methods
@classmethod
@staticmethod

# CODE SMELL


Inheritance


docs.python.org/3/library/exceptions.html

Operator Overloading