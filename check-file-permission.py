import os

# Get file path from user
FILE = input("Enter the full path of the file: ").strip()

# Check if the file exists
if os.path.exists(FILE):
    print(f"{FILE} exists.")
    
    # Check read permission
    if os.access(FILE, os.R_OK):
        print(f"You have READ permission on {FILE}")
    else:
        print(f"You do NOT have READ permission on {FILE}")
    
    # Check write permission
    if os.access(FILE, os.W_OK):
        print(f"You have WRITE permission on {FILE}")
    else:
        print(f"You do NOT have WRITE permission on {FILE}")
    
    # Check execute permission
    if os.access(FILE, os.X_OK):
        print(f"You have EXECUTE permission on {FILE}")
    else:
        print(f"You do NOT have EXECUTE permission on {FILE}")
else:
    print(f"{FILE} does NOT exist.")
