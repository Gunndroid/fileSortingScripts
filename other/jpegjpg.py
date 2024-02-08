import os

def convert_extension_to_lowercase_jpg(directory):
    """Changes file extensions .JPEG and .JPG to lowercase .jpg in the specified directory and its subdirectories."""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.jpeg', '.jpg')):
                old_file_path = os.path.join(root, file)
                # Construct the file's new name with a lowercase .jpg extension
                new_file_name = os.path.splitext(file)[0] + '.jpg'
                new_file_path = os.path.join(root, new_file_name)

                # Rename the file if the new name is different
                if new_file_path != old_file_path:
                    os.rename(old_file_path, new_file_path)
                    print(f"Renamed '{old_file_path}' to '{new_file_path}'")
                else:
                    print(f"No change needed for '{file}'")

def main():
    # Replace '/path/to/directory' with the path to the directory you want to process
    path_to_directory = '/Users/gunnarcurry/Dropbox/image/artdesign/procreateExports/jpeg'
    convert_extension_to_lowercase_jpg(path_to_directory)

if __name__ == "__main__":
    main()
