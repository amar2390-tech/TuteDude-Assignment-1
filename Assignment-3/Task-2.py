"""
Task
2: Using the Math Module for Calculations
Problem Statement: Write a Python program that:
1. Asks the user for a number as input.
2. Uses the math module to calculate the:
o Square root of the number
o Natural logarithm(log base e) of the number
o Sine of the number( in radians)
3. Displays the calculated results.
"""
import math
# Step 1: Ask the user for a number as input
number = float(input("Enter a number: "))
# Step 2: Use the math module to calculate the required values
square_root = math.sqrt(number)
natural_log = math.log(number)
sine_value = math.sin(number)
# Step 3: Display the calculated results
print(f"Square root of {number} is: {square_root}")
print(f"Natural logarithm (log base e) of {number} is: {natural_log}")
print(f"Sine of {number} (in radians) is: {sine_value}")

