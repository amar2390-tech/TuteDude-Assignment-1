
# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.

def factorial(n):    # Check if the input is a negative number
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    else:
        result = 1
        for i in range(2, n + 1):  # Loop from 2 to n
            result *= i  # Multiply result by i
        return result  # Return the calculated factorial
n=input("Enter a number: ")
print(f"The factorial of {n} is {factorial(int(n))}")  # Call the function and print the output

