"""
With the `dir()` of the `math` module, we discovered the following functions and attributes:

['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 
'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 
'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 
'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh',
'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

However, we need to prepare for the following functions for the PCAP exams:

`ceil()`, `floor()`, `trunc()`, `factorial()`, `hypot()`, `sqrt()`
"""

# Let's look at the first three functions:
# First, import them:
from math import ceil, floor, trunc

# Now, let's run them using a float:
print(ceil(7.7))  # Output: 8
print(floor(7.7))  # Output: 7
print(trunc(7.7))  # Output: 7

# So what do these functions do?
# ceil() rounds the number upwards to the nearest integer:
print("ceil")
print(ceil(7.7))  # 8
print(ceil(7.8))  # 8
print(ceil(7.4))  # 8
print(ceil(-7.4))  # -7
print(ceil(-7.8))  # -7

# floor() rounds the number downwards to the nearest integer:
print("floor")
print(floor(7.7))  # 7
print(floor(7.8))  # 7
print(floor(7.4))  # 7
# Note: for negative numbers, it rounds downwards as well:
print(floor(-7.4))  # -8
print(floor(-7.8))  # -8

# trunc() removes the decimal part, truncating the number towards 0:
print("trunc")
print(trunc(7.7))  # 7
print(trunc(7.8))  # 7
print(trunc(7.4))  # 7
print(trunc(-7.4))  # -7
print(trunc(-7.8))  # -7

# Now let's look at factorial():
# The factorial of a number n is the product of all integers from 1 to n.
from math import factorial
print("factorial")
print(factorial(3))  # 3! = 3 * 2 * 1 = 6
print(factorial(4))  # 4! = 4 * 3 * 2 * 1 = 24

# Now let's look at sqrt():
# sqrt() calculates the square root of a number.
from math import sqrt
print("sqrt")
print(sqrt(16))  # The square root of 16 is 4.0
print(sqrt(100))  # The square root of 100 is 10.0

# Finally, let's examine hypot():
# hypot() calculates the length of the hypotenuse of a right-angled triangle given two sides.
# It follows the formula: sqrt(x**2 + y**2)
from math import hypot
print("hypot")
print(hypot(3, 4))  # Output: 5.0 (since 3**2 + 4**2 = 9 + 16 = 25, and sqrt(25) = 5)
