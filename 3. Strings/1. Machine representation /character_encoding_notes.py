"""
PCAP-31-03 Section 3.1 – Machine Representation of Characters

Topics:
- ASCII
- UNICODE
- UTF-8
- Code Points
- Escape Sequences
"""

# ASCII
# - 7-bit encoding (0–127)
# - Includes English letters, digits, punctuation, and control characters
# - Example: 'A' = 65
print("ASCII example:")
print("ord('A') =", ord('A'))      # 65
print("chr(65) =", chr(65))        # 'A'

# Unicode
# - Universal character encoding standard
# - Uses code points written as U+xxxx
# - Supports all characters from all languages
# - Python 3 strings are Unicode by default
print("\nUnicode example:")
print("ord('€') =", ord('€'))      # 8364
print("chr(8364) =", chr(8364))    # '€'

# UTF-8
# - Most common encoding
# - Variable-length (1 to 4 bytes)
# - ASCII-compatible (ASCII is subset of UTF-8)

# Code Points
# - Unique number for each character
# - Use ord() to get code point, chr() to convert back

# Escape Sequences
# Used for special characters in strings

print("\nEscape sequence examples:")
print("Newline character: 'Line1\\nLine2' →")
print("Line1\nLine2")

print("Tab character: 'A\\tB' →")
print("A\tB")

print("Backslash: '\\\\' →", "\\")

print("Single quote: '\\'' →", '\'')

print("Double quote: '\\\"' →", "\"")

# Hex and Unicode escape sequences
print("Hex escape: '\\x41' →", '\x41')       # 'A'
print("Unicode 16-bit: '\\u03A9' →", '\u03A9')  # 'Ω'
print("Unicode 32-bit: '\\U0001F600' →", '\U0001F600')  # 

# Summary
# ASCII: 7-bit, 128 characters
# Unicode: Universal code point system
# UTF-8: Efficient and flexible encoding
# ord(): Character to code point
# chr(): Code point to character
# Escape sequences: Represent special characters in strings
