# Python Review Session Class Notes

## Summary

- Introduction
- Data Types
  - String
  - Integer, Float
  - Boolean
- Logical Operators
- Collection Data Types
  - List
  - Tuples
  - Dictionary
  - Set
- Conditional - If
- Loops
  - While
  - For
  - While vs For
- Functions
  - Arguments
  - Arbitrary Arguments, *args
  - Keyword Arguments
  - Arbitrary Keyword Arguments, **kwargs
  - Default Parameter Value
  - The pass Statement
- Decorators
- Exception Handling
  - Exceptions
  - Raise an exception
- pip
- Built-in Functions in Python
- Modules

## Introduction to Python

- Comments in Python start with the hash character, #
- The equal sign (=) is used to assign a value to a variable
- \ can be used to escape
- Indentation 4 spaces.
- Overall code syntax rules are stated at PEP8. There are online tools. [PEP8 online check](http://pep8online.com/)

### Using Python as a Calculator

The operators +, -, * and / work just like in most other languages:

```py
2 + 2
# 4
```

## Data Types

### String

Assign string to a variable a = "Hello"
Expressing string with quotes, '', "", ''' ''', """ """

Multiline Strings with ''' ''' or """ """:

```py
a = """python ders tekrarı yapmak önemli"""
```

Last one is called docstring. A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the __doc__ special attribute of that object.Strings are immutable, which means a string value cannot be updated. We can verify this by trying to update a part of the string which will led us to an error.

- String Length:

```py
a = "Hello, World!"
print(len(a))
```

Indexes (positive and negative)

  - Individual characters in a string may be chosen. If the string has length L, then the indices start from 0 for the initial character and go to L-1 for the rightmost character. 
  - Negative indices may also be used to count from the right end, -1 for the rightmost character through -L for the leftmost character.

- Call char by index:

```py
a = "Hello World!"
print(a[1])
```
- Slicing
    - stringReference [ start : pastEnd ]
    - stringReference [ : pastEnd ]
    - stringReference [ start : ]
    - stringReference [ : ]
    - Change the order: s[::-1]


- Methods

```py
upper() # Returns an uppercase version of the string
lower() # Returns a lowercase version of the string
title()
capitalize()
count(item)  # Returns the number of repetitions of the substring sub inside s.
split() # Splits at any sequence of whitespace (blanks, newlines, tabs) and returns the remaining parts of s as a list
split(sep)  # Separator that gets removed from between the parts of the list.
startswith() # True/False
endswith() # True/False
strip([chars]) # Returns a copy of the string with both leading and trailing characters removed
```