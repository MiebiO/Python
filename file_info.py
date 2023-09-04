# Import the os module for operating system-related functions.
import os

# Initialize an empty dictionary to store file information.
file_info = {}

# Get the current working directory.
current_directory = os.getcwd()
print(current_directory)
print(type(current_directory))

# List all files and directories in the current directory.
files = os.listdir(current_directory)

# Iterate through each item (file or directory) in the current directory.
for file in files:
    # Construct the full file path by combining the directory path and the item name.
    file_path = current_directory + '/' + file
    print(file_path)

    # Check if the item is a file (not a directory).
    if os.path.isfile(file_path) == True:
        # Get the size of the file in bytes.
        file_size = os.path.getsize(file_path)
        print(file_size)

        # Add the file name and its size to the 'file_info' dictionary.
        file_info[file] = str(file_size) + ' Bytes'
    else:
        # If it's not a file (e.g., a directory), skip it.
        pass

# Print the list of all items (files and directories) in the current directory.
print(files)

# Print the 'file_info' dictionary containing file names and their sizes.
print(file_info)
