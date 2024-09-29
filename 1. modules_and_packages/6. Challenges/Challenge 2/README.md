
# Python Coding Challenge: Understanding the `__name__` Variable

## Overview

In this challenge, you'll explore the behavior and importance of the `__name__` variable in Python. This variable plays a crucial role in determining how code behaves depending on whether it's executed directly or imported as a module.


## What is `__name__`?

In Python, the `__name__` variable is a special built-in variable that helps to identify whether a Python file is being run as the main program or imported as a module into another program.

- If a Python file is executed directly, the value of `__name__` is set to `"__main__"`.
- If a Python file is imported as a module, the value of `__name__` is set to the module's name (the filename without the `.py` extension).

**Why is this important?**
- This mechanism allows you to write reusable code that can either run independently or be imported without executing the main logic unintentionally.
- It helps you design Python programs that behave differently when imported versus when run directly.

### Example:
In this challenge, when you run `module_name.py` directly, the `__name__ == "__main__"` condition will be true, and the script will print that it's running directly. However, when `module_name.py` is imported into another script (like `main_script.py`), the condition will be false, and the script will print that it has been imported.


## Requirements
- Python 3.x

## Objective
Understand how Python's `__name__` variable differentiates between running a module directly and importing it into another script.


## Challenge Steps

### Step 1: Create a Python Module
1. Create a file called **`module_name.py`** in your working directory.
2. In **`module_name.py`**, write a function called `greet()` that prints the message:

   ```python
   print("Hello from module_name!")
   ```

3. In **`module_name.py`**, add the following block of code to check the value of `__name__`:

   ```python
   if __name__ == "__main__":
       print("module_name is being run directly")
   else:
       print("module_name has been imported")
   ```

### Step 2: Create a Main Script
1. Create another file called **`main_script.py`** in the same directory.
2. In **`main_script.py`**, import the `module_name` module.
3. Call the `greet()` function from `module_name`.

### Step 3: Run the Scripts
1. Run the **`main_script.py`** script using the following command:

   ```bash
   python main_script.py
   ```

2. Observe the output to understand how the `__name__` variable behaves when the module is imported.

3. Now, run the **`module_name.py`** script directly using the following command:

   ```bash
   python module_name.py
   ```

4. Observe the output and compare it to when the script was imported.

### Step 4: Analyze the Behavior
- What is the value of `__name__` when the module is run directly?
- What is the value of `__name__` when the module is imported?
- Why does Python use the `__name__` variable in this way?

