
# Python Coding Challenge: Public and Private Variables

## Overview

In this challenge, you'll explore how Python handles public and private variables in classes. This challenge will help you understand variable access control in Python and how it differs from other programming languages.


## Public and Private Variables in Python

### Public Variables
In Python, all variables are **public** by default. Public variables can be accessed from anywhere, both inside and outside the class.

### Private Variables
Private variables in Python are not strictly private but are a convention. Python uses a naming convention to indicate private variables:
- A single leading underscore (`_`) is used to indicate that a variable is **protected** and should not be accessed directly. However, this is just a convention, and you can still access such variables from outside the class.
- A double leading underscore (`__`) triggers name mangling. The interpreter changes the name of the variable in a way that makes it harder to access from outside the class. This is Python's way of implementing a form of "private" variable.

### Example:
In this challenge, you'll see that:
- You can access the `name` attribute directly because it is public.
- You can still access `_age` directly, though it's considered bad practice.
- Accessing `__salary` will require a special syntax because of name mangling.



## Challenge Steps

### Step 1: Create a Python Class
1. Create a file called **`person.py`** in your working directory.
2. In **`person.py`**, define a class `Person` with the following attributes:
   - A public attribute `name` that stores the person's name.
   - A private attribute `_age` (note the underscore), which stores the person's age.
   - A private attribute `__salary` (note the double underscore), which stores the person's salary.

3. Add the following methods to the `Person` class:
   - A method `greet()` that prints a message: `"Hello, my name is {name}."`
   - A method `show_age()` that prints the age (accessing `_age`).
   - A method `show_salary()` that prints the salary (accessing `__salary`).

### Step 2: Create a Main Script
1. Create another file called **`main.py`** in the same directory.
2. In **`main.py`**, create an instance of the `Person` class and pass a name, age, and salary.
3. Call the `greet()`, `show_age()`, and `show_salary()` methods.

4. After calling these methods, try accessing the public attribute `name`, the private attribute `_age`, and the private attribute `__salary` directly from the `Person` object.

### Step 3: Run the Script
1. Run the **`main.py`** script using the following command:

   ```bash
   python main.py
   ```

2. Observe how Python handles access to public and private attributes.

### Step 4: Analyze the Behavior
- Can you directly access the public attribute `name`?
- Can you access the private attribute `_age` directly? If yes, why?
- What happens when you try to access the `__salary` attribute directly? Why is it different from `_age`?


## Requirements
- Python 3.x

## Objective
Understand how Python handles public and private variables, experiment with accessing variables directly, and observe how Python implements name mangling for private attributes.
