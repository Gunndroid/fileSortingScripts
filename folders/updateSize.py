
import os
import re

def get_directory_size(directory):
    """Calculate the total size of the directory in bytes."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def format_size(size):
    """Convert size to a readable format (e.g., KB, MB, GB)."""
    if size < 1024 ** 2:  # less than 1MB
        return f"{size / 1024:.2f}KB"
    elif size < 1024 ** 3:  # less than 1GB
        return f"{size / 1024**2:.2f}MB"
    else:  # GB or more
        return f"{size / 1024**3:.2f}GB"

def update_folder_names_with_size(base_path):
    """Update each folder name with its current size."""
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if os.path.isdir(item_path):
            # Remove existing size info from folder name
            cleaned_name = re.sub(r'\s*\(\d+\.\d+[KMG]B\)$', '', item)
            new_size = format_size(get_directory_size(item_path))
            new_name = f"{cleaned_name} ({new_size})"
            new_path = os.path.join(base_path, new_name)
            os.rename(item_path, new_path)
            print(f"Renamed '{item_path}' to '{new_path}'")

def main():
    # Replace '/path/to/directory' with the path to your target directory
    path_to_directory = '/Volumes/LaCie/files'
    update_folder_names_with_size(path_to_directory)

if __name__ == "__main__":
    main()
