#CHALLENAGE 28

#Python Write/Create file

# Open a file in write mode (it will create the file if it doesn't exist)
with open('example.txt', 'w') as file:
    # Write some text to the file
    file.write("Hello, this is a test file.\n")
    file.write("Python makes file handling easy!")

# Confirm that the file has been created and written to
print("File has been created and written successfully.")


 
