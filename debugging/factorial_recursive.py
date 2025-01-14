#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a given non-negative integer using recursion.

    Parameters:
        n (int): The number to calculate the factorial for. Must be non-negative.

    Returns:
        int: The factorial of the input number `n`. If `n` is 0, returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the first command-line argument, convert it to an integer, and calculate its factorial.
f = factorial(int(sys.argv[1]))

# Print the result to the console.
print(f)
