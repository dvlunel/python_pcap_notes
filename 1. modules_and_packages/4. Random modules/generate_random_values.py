""" 

In this section, we focus on getting random values. These are most likely pseudo-random (pre-defined) values. 
These are based on a seed. 

A **seed** is a value used to initialize the random number generator. In a pseudo-random number generator (PRNG), 
a seed ensures the sequence of random numbers is reproducible. If the seed is the same, the random sequence will be identical every time the code is run. 
In contrast, if no seed is specified (or `None` is used), Python will use the current system time or another system source as the seed.

### Seed hierarchy in Python:
The `random` module in Python uses a pseudo-random number generator, which means that the "random" numbers it produces are deterministic and based on a mathematical formula.
The **seed** is the starting point for this formula. If you do not set the seed explicitly with `random.seed()`, the system time or other environmental factors will be used.
Once the seed is set, the `random` module will always produce the same sequence of numbers. 

In order to prepare for the PCAP exam, we need to know what the following functions do:
`random()`, `seed()`, `choice()`, and `sample()`
"""

# The random() function of the random module (random.random) outputs random floats based on its seed.
# The seed is changed by Python every time the random() function is called (unless explicitly set).
import random
print(random.random())  # Outputs a random float between 0 and 1
print(random.random())
print(random.random())

# The seed() function of the random module (random.seed) makes it possible to hardcode the seed.
# We can manipulate the outcome of the random numbers by defining the seed.
random.seed(0)
print("random seed = 0")
# Now we will always get the same numbers (if you rerun the script with the same seed).
print(random.random())  # Always outputs the same sequence when seed is set
print(random.random())
print(random.random())

# The choice() function of the random module (random.choice()) gives the possibility to take a random 
# element (character, string, integer, float) from a list.
random.seed()  # Resets the seed to a system-based seed
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ['Gabriel', 'Michael', 'Raphael', 'Uriel', 'Selaphiel']
string = 'LetThereBeLight'
print(random.choice(numbers))  # Randomly selects a number from the list
print(random.choice(names))    # Randomly selects a name from the list
print(random.choice(string))   # Randomly selects a character from the string

# It's possible to return/print multiple random values from a list.
# Example:
for i in range(10):  # Perform 10 random selections from the numbers list
    print(random.choice(numbers))

# The sample() function of the random module (random.sample()) gives the option to return a specific number of elements 
# from a list without any duplicates. It returns a list of unique elements.
print(random.sample(names, 3))  # Returns 3 unique random names from the list (without duplicates)
