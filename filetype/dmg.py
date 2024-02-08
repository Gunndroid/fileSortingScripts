import os
import shutil

def move_dmg_files_to_folder(directory):
    """Moves all .dmg files found in the directory and its subdirectories to a 'DMG' folder within the directory."""
    # Path for the DMG folder
    dmg_folder = os.path.join(directory, 'DMG')

    # Create the DMG folder if it doesn't exist
    if not os.path.exists(dmg_folder):
        os.mkdir(dmg_folder)

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.dmg'):
                file_path = os.path.join(root, file)

                # Construct the new path in the DMG folder
                new_file_path = os.path.join(dmg_folder, file)

                # Check if a file with the same name already exists in the DMG folder
                if os.path.exists(new_file_path):
                    print(f"File {file} already exists in {dmg_folder}, skipping.")
                    continue

                # Move the file
                shutil.move(file_path, new_file_path)
                print(f"Moved {file} to {dmg_folder}")

def main():
    # Replace '/path/to/directory' with the path to the directory you want to process
    path_to_directory = '/Users/gunnarcurry/Dropbox/'
    move_dmg_files_to_folder(path_to_directory)

if __name__ == "__main__":
    main()
