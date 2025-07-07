import os

FILE = input("Enter the file path: ").strip()

if os.path.isfile(FILE):
    print(f"{FILE} is a regular file")
elif os.path.isdir(FILE):
    print(f"{FILE} is a directory")
elif os.path.exists(FILE):
    print(f"{FILE} is another type of file")
else:
    print(f"{FILE} does not exist.")

# List details like `ls -l`
try:
    print("\nFile details:")
    print(os.popen(f"ls -l '{FILE}'").read())
except Exception as e:
    print(f"Error showing details: {e}")


## Note: When you want to run a shell command and get its output directly in Python, you can use os.popen()

## method-2 if you want to take input from user and want to check if the file exists or not then you can use the following code

import os
import sys

# Get files from command-line arguments
files = sys.argv[1:]  # Skip script name

if not files:
    print("Usage: python3 script.py <file1> <file2> ...")
    sys.exit(1)

for file in files:
    if os.path.isfile(file):
        print(f"{file} is a regular file")
    elif os.path.isdir(file):
        print(f"{file} is a directory")
    elif os.path.exists(file):
        print(f"{file} is another type of file")
    else:
        print(f"{file} does not exist")
    
    # Show details like 'ls -l'
    os.system(f'ls -l "{file}"')
