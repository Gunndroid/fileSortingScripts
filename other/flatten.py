

import os
import shutil

def flatten_directory(source_directory, target_directory):
    """Move all files from source_directory and its subdirectories into target_directory."""
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            # Construct the path to the file in the source directory
            file_path = os.path.join(root, file)
            # Construct the path to where the file will be moved in the target directory
            target_path = os.path.join(target_directory, file)
            
            # Check if a file with the same name already exists in the target directory
            if not os.path.exists(target_path):
                shutil.move(file_path, target_path)
                print(f"Moved file {file} to {target_directory}")
            else:
                print(f"File {file} already exists in {target_directory}, skipping.")

def main():
    source = '/Users/gunnarcurry/Dropbox/image/traits'
    target = '/Users/gunnarcurry/Dropbox/image/traits'
    
    # Make sure the target directory exists
    if not os.path.exists(target):
        os.makedirs(target)
    
    flatten_directory(source, target)

if __name__ == "__main__":
    main()
