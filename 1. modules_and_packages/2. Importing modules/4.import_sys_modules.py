"""
For the PCAP exam we have to understand how we can import the sys modules

In Python, we often use the `sys` module to interact with the Python interpreter.
The `sys` module provides access to variables and functions related to the Python runtime environment.

Example of the hierarchy:

Package:
__init__.py (This file signals that a directory is a package)

Module:
sys (A built-in module in Python)

Functions or Methods:
sys.exit() (A function that exits the program)

Attributes:
sys.argv (An attribute that stores command-line arguments passed to the script)

In essence:
Package → Module → Attributes/Objects → Functions/Methods (and Classes, if applicable)
"""

# Example of importing the sys module:
import sys

# `sys.argv` is an attribute that stores command-line arguments passed to the script.
# The first element of sys.argv is always the name of the script itself.
# Example:
print("Script name:", sys.argv[0])

# `sys.exit()` is a method that can be used to terminate the program.
# Example (commented to avoid terminating this script):
# sys.exit()

# You can also set an alias for the module or specific attributes/functions:
import sys as system
print("Alias example:", system.argv[0])

# If we want to know all the available functions and attributes in the sys module:
print(dir(sys))

# Commonly used functions and attributes in the sys module:
# sys.version -> Returns the Python version being used.
print("Python version:", sys.version)

# sys.platform -> Returns the platform (e.g., 'linux', 'win32').
print("Platform:", sys.platform)
