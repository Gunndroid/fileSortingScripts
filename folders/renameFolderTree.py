
import os

def rename_folders_to_lowercase_and_remove_spaces(directory):
    """Renames all subdirectories within the given directory to lowercase names and removes spaces recursively."""
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in dirs:
            new_name = name.lower().replace(' ', '')
            if new_name != name:
                original_path = os.path.join(root, name)
                new_path = os.path.join(root, new_name)
                os.rename(original_path, new_path)
                print(f"Renamed folder '{original_path}' to '{new_path}'")

def main():
    # Replace '/path/to/directory' with the path to your target directory.
    path_to_directory = '/Volumes/LaCie/finished'
    rename_folders_to_lowercase_and_remove_spaces(path_to_directory)

if __name__ == "__main__":
    main()
