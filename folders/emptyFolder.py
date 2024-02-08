import os

def remove_empty_folders(directory):
    """Recursively removes empty folders in the specified directory."""
    # Counter for the number of deleted directories
    empty_folders_count = 0

    # Walk through the directory
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)

            # Check if the directory is empty
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                empty_folders_count += 1
                print(f"Removed empty folder: {dir_path}")

    print(f"Total empty folders removed: {empty_folders_count}")

def main():
    # Replace '/path/to/directory' with the path to the directory you want to clean up
    path_to_directory = '/Users/gunnarcurry/Dropbox/image/traits'
    remove_empty_folders(path_to_directory)

if __name__ == "__main__":
    main()
