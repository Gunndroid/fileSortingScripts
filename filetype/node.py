import os
import shutil

def move_node_modules_to_parent(directory):
    """Moves 'node_modules' directories to their respective parent directories."""
    for root, dirs, files in os.walk(directory):
        if 'node_modules' in dirs:
            node_modules_path = os.path.join(root, 'node_modules')
            parent_dir = os.path.dirname(root)

            # New path for node_modules in the parent directory
            new_path = os.path.join(parent_dir, 'node_modules')

            # Check if a node_modules directory already exists in the parent directory
            if os.path.exists(new_path):
                print(f"A 'node_modules' directory already exists in {parent_dir}, skipping.")
                continue

            # Move the node_modules folder
            shutil.move(node_modules_path, new_path)
            print(f"Moved 'node_modules' from {root} to {parent_dir}")

def main():
    # Replace '/path/to/directory' with the path to the directory you want to start the search
    path_to_directory = '/Users/gunnarcurry/Dropbox/'
    move_node_modules_to_parent(path_to_directory)

if __name__ == "__main__":
    main()
