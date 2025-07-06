# Find the Newest File in a Directory

import os
def find_newest_file(directory): 
    files  = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))] 
    if not files:
        print("no files found")
        return None
    new_files = max(files, key = os.path.getmtime)
    return new_files

target_dir = "your target directory path here"

find_newest_file(target_dir)