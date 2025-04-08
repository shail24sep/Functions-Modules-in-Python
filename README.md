# Functions-Modules-in-Python

**Task 1: Calculate Factorial Using a Function**

x = int(input("Enter a number:"))
Prompts the user to enter a number.

input() reads it as a string, and int() converts it to an integer.

The value is stored in the variable x.

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

This defines a recursive function to calculate the factorial of a number n.

Base case:
If n is less than 2 (i.e., 0 or 1), return 1.
(Because 0! = 1 and 1! = 1)

Recursive case:
If n is 2 or more, it multiplies n by the factorial of n-1.

y = factorial(x)
Calls the factorial function with the user’s input x.

Stores the result in variable y.

print("Factorial of", x, "is:", y)

Prints the final result .

Final output as expected:

Enter a number:5
Factorial of 5 is: 120

**Task 2: Using the Math Module for Calculations**

from math import sqrt, log, sin
This line imports specific functions from Python’s built-in math module:

sqrt() – for square root

log() – for natural logarithm (base e)

sin() – for sine (in radians)

val = float(input('Enter a number:'))
Prompts the user to enter a number.

Converts the input to a floating-point number (i.e., supports decimals).

Stores the value in the variable val.

x = sqrt(val)
y = log(val)
z = sin(val)
x = sqrt(val) --> calculates the square root of the number.

y = log(val) --> calculates the natural logarithm (ln) of the number.

z = sin(val) --> calculates the sine of the number (in radians).

print("Square root:", x)
print("logarithm:", y)
print("Sine:", z)
Prints each result with a label

Final output as expected:

Enter a number:25
Square root: 5.0
logarithm: 3.2188758248682006
Sine: -0.13235175009777303


