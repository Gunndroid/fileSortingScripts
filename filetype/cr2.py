import os
import shutil

def move_cr2_files_to_folder(directory):
    """Moves all .CR2 files found in the directory and its subdirectories to a 'CR2' folder within the directory."""
    # Path for the CR2 folder
    cr2_folder = os.path.join(directory, 'CR2')

    # Create the CR2 folder if it doesn't exist
    if not os.path.exists(cr2_folder):
        os.mkdir(cr2_folder)

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.cr2'):
                file_path = os.path.join(root, file)

                # Construct the new path in the CR2 folder
                new_file_path = os.path.join(cr2_folder, file)

                # Check if a file with the same name already exists in the CR2 folder
                if os.path.exists(new_file_path):
                    print(f"File {file} already exists in {cr2_folder}, skipping.")
                    continue

                # Move the file
                shutil.move(file_path, new_file_path)
                print(f"Moved {file} to {cr2_folder}")

def main():
    # Replace '/path/to/directory' with the path to the directory you want to process
    path_to_directory = '/Users/gunnarcurry/Dropbox/image'
    move_cr2_files_to_folder(path_to_directory)

if __name__ == "__main__":
    main()
