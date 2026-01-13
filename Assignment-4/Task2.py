user_input = input("Enter some text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")
print("Data successfully written to output.txt")

# Step 2: Append additional data to the same file
additional_data = input("Enter additional text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(additional_data + "\n")
print("Data successfully appended")

# Step 3: Read and display the final content of the file
with open("output.txt", "r") as file:
    content = file.read()
print("Final content of output.txt:")
print(content)

