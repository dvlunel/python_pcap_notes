""" 

In this section we focus on getting random values. These are most likly psuedo (pre-defined) values. These are 
based on a seed. (GTP explain what a seed is)

(GTP also explain how the hiearcy of a seed works in a python situation (also where it's based on))

In order to prepare for the PCAP exam, we need to know what the following three modules do
random(), seed(), choice(), sample()

"""

# The random() function of the random module (random.random) outputs random floats based on it's seed.
# The seed is changed by python everytime the random() function is called
import random
print(random.random())
print(random.random())
print(random.random())

# The seed() function of the random module (random.random) makes it possible to hardcode the seed
# We can maniplute the outcome of the random numbers be defining the seed
random.seed(0)
print("random seed = 0")
# Now we should get the same numbers (if you rerun the script)
print(random.random())
print(random.random())
print(random.random())

# If we want to use the 

