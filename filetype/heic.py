import os
import shutil

def move_heic_files_to_folder(directory):
    """Moves all .HEIC files found in the directory and its subdirectories to a 'HEIC' folder within the directory."""
    # Path for the HEIC folder
    heic_folder = os.path.join(directory, 'HEIC')

    # Create the HEIC folder if it doesn't exist
    if not os.path.exists(heic_folder):
        os.mkdir(heic_folder)

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.heic'):
                file_path = os.path.join(root, file)

                # Construct the new path in the HEIC folder
                new_file_path = os.path.join(heic_folder, file)

                # Check if a file with the same name already exists in the HEIC folder
                if os.path.exists(new_file_path):
                    print(f"File {file} already exists in {heic_folder}, skipping.")
                    continue

                # Move the file
                shutil.move(file_path, new_file_path)
                print(f"Moved {file} to {heic_folder}")

def main():
    # Replace '/path/to/directory' with the path to the directory you want to process
    path_to_directory = '/Users/gunnarcurry/Dropbox/'
    move_heic_files_to_folder(path_to_directory)

if __name__ == "__main__":
    main()
