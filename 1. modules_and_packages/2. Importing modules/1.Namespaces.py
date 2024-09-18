"""
In Python, namespaces are crucial for organizing code and avoiding name conflicts. They act as containers for variable names, ensuring that names defined in one context do not interfere with those in another.

Example of the hierarchy:

Namespace:
A context where names are defined (e.g., global, local).

Modules:
A module creates its own namespace. For example, if we have a module named `geometry`, it would contain all its defined names without conflicting with names in other modules.

Classes:
When we define a class, it creates a new namespace. For instance, within a class called `Circle`, any method or attribute defined will belong to that class's namespace.

Functions:
Functions also create their own namespaces. For example, a function named `calculate_area` will have its own local namespace, separate from the global namespace.

In essence:
Namespace → Module → Class → Function

"""

# Example of using namespaces:
# We can define a variable in the global namespace:
x = 10

# Defining a function that has its own local namespace:
def calculate_area(radius):
    area = 3.14 * radius ** 2  # 'area' is in the local namespace of 'calculate_area'
    return area

# Calling the function:
print(calculate_area(5))  # Output: 78.5

# The variable 'x' is accessible globally:
print(x)  # Output: 10

# If we try to access 'area' outside its function, it will raise an error:
# print(area)  # Uncommenting this will cause a NameError.

# To explore the namespaces available, we can use:
print(globals())  # Shows the global namespace
print(locals())   # Shows the local namespace (within a function or class)

# In practice, to understand the hierarchy and details of a module, it is advisable to consult the documentation.
# Example: https://docs.python.org/3/tutorial/modules.html

