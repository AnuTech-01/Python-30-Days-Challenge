#CHALLENAGE 29

#Python Delete File

import os

# Specify the file path
file_path = 'example.txt'

# Check if the file exists before trying to delete it
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} has been deleted.")
else:
    print(f"The file {file_path} doesn't exist.")
