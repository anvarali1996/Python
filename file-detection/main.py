# Python file detection

import os

# file_path = "file-detection/stuff/test.txt"
# file_path = '/Users/anvarjonsheraliev/Desktop/test.txt'
file_path = '/Users/anvarjonsheraliev/Desktop/PYTHON'

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That's is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else: 
    print("That location does not exist")