import os

def rename_folders_to_lowercase(directory):
    """Renames all subdirectories within the given directory to lowercase names."""
    for name in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, name)):
            new_name = name.lower()
            if new_name != name:
                os.rename(os.path.join(directory, name), os.path.join(directory, new_name))
                print(f"Renamed folder {name} to {new_name}")

def main():
    # Replace '/path/to/directory' with the path to your target directory.
    path_to_directory = '/Users/gunnarcurry/Dropbox'
    rename_folders_to_lowercase(path_to_directory)

if __name__ == "__main__":
    main()
