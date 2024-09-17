"""
In Python, we aim to split the code as much as possible into modules.
This helps to keep the code smaller and less complex.

Example of the hierarchy:

Package:
__init__.py (This file signals that a directory is a package)

Module:
math (A built-in module in Python)

Functions or Methods:
math.sqrt() (A function in the math module)

Classes:
math.Vector (If it existed, it would be a class in the math module)

In essence:
Package → Module → Attributes/Objects → Functions/Methods (and Classes, if applicable)
"""

# Example of importing a module:
# We can import modules and use their functions or attributes.
# For instance:
import math

# We can also import specific attributes or functions from a module, such as pi:
from math import pi

# This allows us to use an attribute directly without referencing the full module.
# Example:
print(pi)  # instead of using print(math.pi)

# There's also a way to give an imported attribute an alias, like this:
from math import pi as pi_value
print(pi_value)

# If we want to know all the available functions and attributes in a module, we can use:
print(dir(math))

# Based in the above result, you can find easly which package is relevant.
# More practical would be the read the documentation of the module
# https://docs.python.org/3/library/math.html