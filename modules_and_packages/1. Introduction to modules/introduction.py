"""
The code of python expands, and the codes gets bigger. Something that happens a lot to day to day code in python
So a way to make the code more readable is to decomposition of the code (make the code down into smaller pierces)
stored in seperate files.

A solution is this is by using modules. A module is a file that is a piece of code that can be imported from another python file.

"""

# For instance, wrinting all this code
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# We can make a seperate file, and import thoese functions
import calc_functions

# And use them by using the statements as
subtract_foruma = subtract(20,10)
print(subtract_foruma)

