"""
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list


"""


numbers = list(range(1, 11))
extracted_elements = numbers[:5]
reversed_elements = extracted_elements[::-1]
print("Extracted elements:", extracted_elements)
print("Reversed elements:", reversed_elements)

