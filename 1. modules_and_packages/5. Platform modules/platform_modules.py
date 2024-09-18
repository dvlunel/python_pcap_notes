"""
Running Python is made possible via a few layers. For example:

1. Code
2. Python interpreter
3. Operating system
4. Hardware

For code execution or version compatibility, it is sometimes necessary to know information about the operating system and hardware. 
Preparing for the PCAP exam, you need to know the following modules and their functions:

- `platform()`
- `machine()`
- `processor()`
- `system()`
- `version()`
- `python_implementation()`
- `python_version_tuple()`

Each of these functions helps in retrieving specific details about the environment where the Python code is running.
"""

# The platform() function from the platform module returns information about the OS on which the code is executed.
import platform
print(platform.platform())  # Outputs a string with detailed information about the OS
# It's possible to filter or parse OS information by giving certain arguments
print(platform.platform(aliased=True, terse=True))  # Outputs a more compact version of the OS information

# The machine() function from the platform module returns the type of machine (hardware) the code is running on.
print(platform.machine())  # Outputs the machine type, e.g., 'x86_64'

# The processor() function from the platform module returns information about the CPU where the code is running.
print(platform.processor())  # Outputs the processor name, e.g., 'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz'

# The system() function from the platform module returns the generic OS name.
print(platform.system())  # Outputs the OS name, e.g., 'Windows', 'Linux', 'Darwin'

# The version() function from the platform module returns the version of the OS.
print(platform.version())  # Outputs the OS version, e.g., '10.0.18362'

# The python_implementation() function from the platform module returns the Python implementation.
print(platform.python_implementation())  # Outputs the implementation, e.g., 'CPython', 'PyPy'

# The python_version_tuple() function from the platform module returns the Python version as a tuple.
print(platform.python_version_tuple())  # Outputs the Python version, e.g., ('3', '8', '5')
