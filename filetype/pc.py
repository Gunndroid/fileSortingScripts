import os
import shutil

def move_procreate_files_to_folder(directory):
    """Moves all .procreate files found in the directory and its subdirectories to a 'Procreate' folder within the directory."""
    # Path for the Procreate folder
    procreate_folder = os.path.join(directory, 'Procreate')

    # Create the Procreate folder if it doesn't exist
    if not os.path.exists(procreate_folder):
        os.mkdir(procreate_folder)

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.procreate'):
                file_path = os.path.join(root, file)

                # Construct the new path in the Procreate folder
                new_file_path = os.path.join(procreate_folder, file)

                # Check if a file with the same name already exists in the Procreate folder
                if os.path.exists(new_file_path):
                    print(f"File {file} already exists in {procreate_folder}, skipping.")
                    continue

                # Move the file
                shutil.move(file_path, new_file_path)
                print(f"Moved {file} to {procreate_folder}")

def main():
    # Replace '/path/to/directory' with the path to the directory you want to process
    path_to_directory = '/Users/gunnarcurry/Dropbox/artdesign/puffwizzartwork'
    move_procreate_files_to_folder(path_to_directory)

if __name__ == "__main__":
    main()
