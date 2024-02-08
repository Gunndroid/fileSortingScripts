import os

def get_directory_size(directory):
    """Calculate the total size of the directory in bytes."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def rename_folders_with_size(base_path):
    """Rename each folder to include its size."""
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if os.path.isdir(item_path):
            size = get_directory_size(item_path)
            # Convert size to a readable format (e.g., MB, GB)
            if size < 1024 ** 2:  # less than 1MB
                size_str = f"{size / 1024:.2f}KB"
            elif size < 1024 ** 3:  # less than 1GB
                size_str = f"{size / 1024**2:.2f}MB"
            else:  # GB or more
                size_str = f"{size / 1024**3:.2f}GB"

            new_name = f"{item} ({size_str})"
            new_path = os.path.join(base_path, new_name)
            os.rename(item_path, new_path)
            print(f"Renamed '{item_path}' to '{new_path}'")

def main():
    # Replace '/path/to/directory' with the path to your target directory
    path_to_directory = '/Users/gunnarcurry/Desktop/originals/2021 (35.65GB)'
    rename_folders_with_size(path_to_directory)

if __name__ == "__main__":
    main()
