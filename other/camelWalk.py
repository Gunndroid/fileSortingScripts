import os
import re

def to_camel_case(name):
    # Split the name by non-alphanumeric characters
    words = re.split(r'[^a-zA-Z0-9]', name)
    # Convert to CamelCase: first word lower case, others title case
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

def rename_files(directory):
    """Renames files in the specified directory and its subdirectories to camelCase."""
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)

            # Remove file extension and convert to camelCase
            name, ext = os.path.splitext(filename)
            new_name = to_camel_case(name) + ext.lower()

            new_file_path = os.path.join(root, new_name)

            # Rename the file if the new name is different
            if new_name != filename:
                os.rename(file_path, new_file_path)
                print(f"Renamed '{filename}' to '{new_name}'")
            else:
                print(f"'{filename}' did not need changes.")

def main():
    # Replace with the path to the directory you want to process
    path_to_directory = '/Users/gunnarcurry/Dropbox/artdesign'
    rename_files(path_to_directory)

if __name__ == "__main__":
    main()
