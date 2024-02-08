import os
import shutil

def move_aae_files_to_folder(directory):
    """Moves all .aae files found in directory and its subdirectories to an 'AAE' folder within the directory."""
    # Path for the AAE folder
    aae_folder = os.path.join(directory, 'AAE')

    # Create the AAE folder if it doesn't exist
    if not os.path.exists(aae_folder):
        os.makedirs(aae_folder)

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.aae'):
                file_path = os.path.join(root, file)

                # Construct the new path in the AAE folder
                new_file_path = os.path.join(aae_folder, file)

                # Check if a file with the same name already exists in the AAE folder
                if os.path.exists(new_file_path):
                    print(f"File {file} already exists in {aae_folder}, skipping.")
                    continue

                # Move the file
                shutil.move(file_path, new_file_path)
                print(f"Moved {file} to {aae_folder}")

def main():
    # Replace '/path/to/directory' with the path to the directory you want to process
    path_to_directory = '/Users/gunnarcurry/Desktop/originals'
    move_aae_files_to_folder(path_to_directory)

if __name__ == "__main__":
    main()
