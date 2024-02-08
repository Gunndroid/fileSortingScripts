import os
import shutil

def move_tiff_files_to_folder(directory):
    """Moves all .tiff and .tif files found in the directory and its subdirectories to a 'TIFF' folder within the directory."""
    # Path for the TIFF folder
    tiff_folder = os.path.join(directory, 'TIFF')

    # Create the TIFF folder if it doesn't exist
    if not os.path.exists(tiff_folder):
        os.mkdir(tiff_folder)

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.tiff', '.tif')):
                file_path = os.path.join(root, file)

                # Construct the new path in the TIFF folder
                new_file_path = os.path.join(tiff_folder, file)

                # Check if a file with the same name already exists in the TIFF folder
                if os.path.exists(new_file_path):
                    print(f"File {file} already exists in {tiff_folder}, skipping.")
                    continue

                # Move the file
                shutil.move(file_path, new_file_path)
                print(f"Moved {file} to {tiff_folder}")

def main():
    # Replace '/path/to/directory' with the path to the directory you want to process
    path_to_directory = '/Users/gunnarcurry/Dropbox/'
    move_tiff_files_to_folder(path_to_directory)

if __name__ == "__main__":
    main()
