import os
import shutil

def move_specific_files_to_folders(directory):
    """Moves .zip, .celtx, and .pages files to their respective folders within the directory."""
    # Create paths for each type of folder
    zip_folder = os.path.join(directory, 'ZIP')
    celtx_folder = os.path.join(directory, 'CELTX')
    pages_folder = os.path.join(directory, 'PAGES')

    # Create the folders if they don't exist
    for folder in [zip_folder, celtx_folder, pages_folder]:
        if not os.path.exists(folder):
            os.mkdir(folder)

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            new_file_path = ''

            # Determine the destination folder based on file extension
            if file.lower().endswith('.zip'):
                new_file_path = os.path.join(zip_folder, file)
            elif file.lower().endswith('.celtx'):
                new_file_path = os.path.join(celtx_folder, file)
            elif file.lower().endswith('.pages'):
                new_file_path = os.path.join(pages_folder, file)

            # Move the file if a destination is set
            if new_file_path:
                if os.path.exists(new_file_path):
                    print(f"File {file} already exists in destination, skipping.")
                    continue

                shutil.move(file_path, new_file_path)
                print(f"Moved {file} to its respective folder")

def main():
    # Replace '/path/to/directory' with the path to the directory you want to process
    path_to_directory = '/Users/gunnarcurry/Dropbox/'
    move_specific_files_to_folders(path_to_directory)

if __name__ == "__main__":
    main()
