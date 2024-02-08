import os

def get_directory_size(directory):
    """Calculate the total size of the directory."""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def print_subdirectory_sizes(base_path):
    """Print the sizes of all subdirectories in the base path."""
    for directory in os.listdir(base_path):
        dir_path = os.path.join(base_path, directory)
        if os.path.isdir(dir_path):
            size = get_directory_size(dir_path)
            print(f"Directory: {directory}, Size: {size / 1024**3:.2f} GB")

# Replace 'your_path_here' with the path you want to check
print_subdirectory_sizes('/Users/gunnarcurry/Dropbox/image')
