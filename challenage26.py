#CHALLENAGE 26

# Simple Python File Handling Program

# Step 1: Create and write to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a simple file handling example.\n")
    file.write("Python makes file handling easy!\n")

# Step 2: Read from the file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# Step 3: Append new text to the file
with open("example.txt", "a") as file:
    file.write("This line was added using the append mode.\n")

# Step 4: Read and display the updated content
with open("example.txt", "r") as file:
    updated_content = file.read()
    print("Updated File Content:\n", updated_content)
