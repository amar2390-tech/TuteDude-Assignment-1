"""
Task 2: Create a Personalized Greeting
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.

"""
# Step 1: Take user's first name and last name as input
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
# Step 2: Concatenate the first name and last name into a full name
full_name = first_name + " " + last_name
# Step 3: Print a personalized greeting message using the full name
print("Hello, " + full_name + "! Welcome to the python program!")
