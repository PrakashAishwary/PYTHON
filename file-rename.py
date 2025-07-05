import os
directory = "your directory path where you want to rename your files"
for count, filename in enumerate(os.listdir(directory)):
    if os.path.isfile(os.path.join(directory, filename)):
        new_file = f"file-{count +1 }{os.path.splitext(filename)[1]}"
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, new_file)
        os.rename(src, dst)
        print("File {filename} renamed to {new_file}")

### Features You Can Add
"""
You can also use date and time in new filename.
date_str = datetime.now().strftime("%Y-%m-%d")
new_file = f"file-{count +1 }_{date_str}{os.path.splitext(filename)[1]}"

"""
