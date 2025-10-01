#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

 n = int(input("How many terms of Fibonacci sequence do you want? "))

# Check for invalid number
if n <= 0:
    print("0 is an invalid number plaese select a number greater then 0.")
else:
    a, b = 0, 1
    print("Fibonacci sequence:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
