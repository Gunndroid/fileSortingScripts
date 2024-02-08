import os

def remove_hyphen_from_filenames(directory):
    """Removes hyphens from filenames in the specified directory."""
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Remove hyphens from the filename
        new_filename = filename.replace('-', '')
        new_file_path = os.path.join(directory, new_filename)
        
        # Rename the file
        if new_filename != filename:  # Check if a change is needed
            os.rename(file_path, new_file_path)
            print(f"Renamed '{filename}' to '{new_filename}'")
        else:
            print(f"No hyphens found in '{filename}', skipping.")

def main():
    # Replace '/path/to/directory' with the path to the directory containing the files you want to rename
    path_to_directory = '/Users/gunnarcurry/Dropbox/image/vanlifecowboy'
    remove_hyphen_from_filenames(path_to_directory)

if __name__ == "__main__":
    main()
