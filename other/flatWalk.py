import os
import shutil

def flatten_directory_to_parent(directory):
    """Moves all files from subdirectories of the given directory to the parent directory."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Skip files that are already in the parent directory
            if root == directory:
                continue

            # Construct the new file path in the parent directory
            new_file_path = os.path.join(directory, file)

            # Check if a file with the same name already exists in the parent directory
            if os.path.exists(new_file_path):
                print(f"File {file} already exists in {directory}, skipping.")
                continue

            # Move the file
            shutil.move(file_path, new_file_path)
            print(f"Moved {file} to {directory}")

def main():
    # Replace '/path/to/parent/directory' with the path to the parent directory
    path_to_parent_directory = '/Users/gunnarcurry/Dropbox/image/artdesign/paintings'
    flatten_directory_to_parent(path_to_parent_directory)

if __name__ == "__main__":
    main()
