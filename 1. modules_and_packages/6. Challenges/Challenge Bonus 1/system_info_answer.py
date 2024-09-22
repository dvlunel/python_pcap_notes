# First, we need to import the platform module
import platform

# Second, we create a function within the Python file
def collect_system_info():
    # Third, we define a dictionary to store system information
    system_info = {
        'Platform': platform.platform(),
        'Machine': platform.machine(),
        'Processor': platform.processor(),
        'OS': platform.system(),
        'OS Version': platform.version(),
        'Python Implementation': platform.python_implementation(),
        'Python Version': '.'.join(platform.python_version_tuple()) # We join the tuple to form a string
    }

    # Fourth, print some introductory information
    print('System Information:')
    print('-------------------')
    
    # Fifth, loop through each key-value pair in system_info using the .items() method
    for key, value in system_info.items():
        # Print the key and value from the dictionary
        print(f"{key}: {value}")

# Sixth, ensure the function runs when the script is executed directly
if __name__ == "__main__":
    collect_system_info()
