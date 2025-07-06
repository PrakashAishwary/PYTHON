import os

def count_files_and_dirs(directory):
    file_count = 0
    dir_count = 0

    try:
        for entry in os.scandir(directory):
            if entry.is_file():
                file_count += 1
            elif entry.is_dir():
                dir_count += 1

        print(f"Directory: {directory}")
        print(f"Total files: {file_count}")
        print(f"Total subdirectories: {dir_count}")

    except FileNotFoundError:
        print(f"Directory not found: {directory}")
    except PermissionError:
        print(f"Permission denied: {directory}")
    except Exception as e:
        print(f"Error: {e}")

# Replace with your target directory
target_directory = input("Enter directory path: ").strip()
count_files_and_dirs(target_directory)
