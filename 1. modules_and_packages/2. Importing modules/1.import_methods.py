"""
There are various ways to import modules in Python, each with its own use case. 
The key methods include:

1. `import module`: Imports the entire module.
2. `from module import item`: Imports specific items (functions, classes, etc.) from a module.
3. `import module as alias`: Imports a module and gives it a shorter or more convenient alias.
4. `from module import *`: Imports all items from the module, though it's generally not recommended because it can clutter the namespace.
"""

# 1. Importing the entire module:
# You have access to all functions and attributes within the module, but you must prefix them with the module name.
import math
print(math.sqrt(16))  # Access sqrt from math using the module name

# 2. Importing specific items from a module:
# You only import the specific function or object you need, making the code more concise.
from math import sqrt, pi
print(sqrt(16))  # No need to use the module name here, as sqrt is directly imported
print(pi)        # Directly accessing the constant pi

# 3. Importing a module with an alias:
# This method is useful when working with long module names or frequently using the module, allowing for more readable code.
import math as m
print(m.sqrt(16))  # Using the alias 'm' instead of 'math'

# 4. Importing everything from a module:
# This brings all functions and attributes into the current namespace. It is less common and can cause conflicts.
from math import *
print(sqrt(16))  # Direct access to all math functions without needing the 'math.' prefix

# Note: Importing everything (`import *`) can cause namespace pollution, making it harder to track where functions come from.
# It's generally better to import only what you need or use an alias.
