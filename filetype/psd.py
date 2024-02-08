import os
import shutil

def move_psd_files_to_folder(directory):
    """Moves all .psd files found in directory and its subdirectories to a 'PSD' folder within the directory."""
    # Path for the PSD folder
    psd_folder = os.path.join(directory, 'PSD')

    # Create the PSD folder if it doesn't exist
    if not os.path.exists(psd_folder):
        os.mkdir(psd_folder)

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.psd'):
                file_path = os.path.join(root, file)

                # Construct the new path in the PSD folder
                new_file_path = os.path.join(psd_folder, file)

                # Check if a file with the same name already exists in the PSD folder
                if os.path.exists(new_file_path):
                    print(f"File {file} already exists in {psd_folder}, skipping.")
                    continue

                # Move the file
                shutil.move(file_path, new_file_path)
                print(f"Moved {file} to {psd_folder}")

def main():
    # Replace '/path/to/directory' with the path to the directory you want to process
    path_to_directory = '/Users/gunnarcurry/Dropbox/image/artdesign/procreateExports/themes'
    move_psd_files_to_folder(path_to_directory)

if __name__ == "__main__":
    main()
