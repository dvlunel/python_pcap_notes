"""
PCAP-31-03 Section 3.2 – Operate on Strings

This script demonstrates:
- Using ord() and chr()
- Indexing and slicing strings
- String immutability
- Iterating through strings
- Concatenating and multiplying strings
- Comparing strings
- Using membership operators: in, not in
"""
# A overloaded operater returns a string without any odering
overloaded_operator = 'aaa' + 'bbb'
# A communitive operator returns a string with ordering
for car in 'hello from the world of python':
    print(car, end='-')


# ord() and chr()
# ord(char) returns the Unicode code point of a character
# chr(code) returns the character for a Unicode code point
print("ord() and chr() examples:")
print("ord('A') =", ord('A'))      # Output: 65
print("chr(66) =", chr(66))        # Output: 'B'

# Indexing
# Strings are sequences, and each character has an index
text = "Python"
print("\nIndexing:")
print("text[0] =", text[0])        # First character: 'P'
print("text[-1] =", text[-1])      # Last character: 'n'

# Slicing
# You can extract substrings using [start:stop]
print("\nSlicing:")
print("text[0:3] =", text[0:3])    # Characters 0 to 2: 'Pyt'
print("text[:4] =", text[:4])      # Start to index 3: 'Pyth'
print("text[2:] =", text[2:])      # Index 2 to end: 'thon'

# Immutability
# Strings in Python are immutable, meaning they cannot be changed after creation
print("\nImmutability:")
# Attempting to change a character in a string will raise an error
# text[0] = 'J'  ← This will cause a TypeError
print("Strings cannot be modified directly. You must create a new string.")

# Iterating through strings
# You can loop over each character in a string using a for loop
print("\nIterating:")
for char in text:
    print(char, end=" ")           # Output: P y t h o n

# Concatenation
# Use the '+' operator to join strings
print("\n\nConcatenation:")
greeting = "Hello, "
name = "David"
message = greeting + name
print("message =", message)        # Output: Hello, David

# Multiplication
# Use the '*' operator to repeat a string
print("\nMultiplication:")
print("'ha' * 3 =", "ha" * 3)      # Output: 'hahaha'

# Comparison
# Strings are compared lexicographically (like dictionary order)
print("\nComparison:")
print("'abc' == 'abc':", 'abc' == 'abc')        # True
print("'abc' < 'abd':", 'abc' < 'abd')          # True
print("'5' > '2':", '5' > '2')                  # True (string comparison)

# Note: You can't directly compare a string with a number (e.g. '5' > 2 would raise TypeError)

# Membership operators: in, not in
# Use 'in' to check if a substring exists within another string
print("\nMembership operators:")
sentence = "The quick brown fox"
print("'quick' in sentence:", 'quick' in sentence)            # True
print("'slow' not in sentence:", 'slow' not in sentence)      # True

# Summary:
# - Strings are sequences of characters
# - They are immutable (cannot be changed in-place)
# - Use slicing and indexing to access parts of a string
# - Use ord()/chr() to work with character code points
# - Use loops to iterate over strings
# - Use + and * for joining and repeating strings
# - Use in/not in to check for presence of substrings