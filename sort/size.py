import os
import shutil

def move_file_to_category(file_path, category_dir):
    """Move file to the corresponding category directory."""
    if not os.path.exists(category_dir):
        os.makedirs(category_dir)
    shutil.move(file_path, os.path.join(category_dir, os.path.basename(file_path)))

def categorize_and_move_files(base_path):
    """Categorize files based on their sizes and move them to corresponding folders."""
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)

        # Skip if it's a directory
        if os.path.isdir(item_path):
            continue

        # Get file size in MB
        file_size_mb = os.path.getsize(item_path) / (1024 * 1024)

        # Determine the category based on file size
        if file_size_mb < 250:
            category = '0-250MB'
        elif 250 <= file_size_mb < 800:
            category = '250MB-800MB'
        elif 800 <= file_size_mb < 2048:
            category = '800MB-2GB'
        else:
            category = '2GB+'

        category_dir = os.path.join(base_path, category)
        move_file_to_category(item_path, category_dir)
        print(f"Moved {item} to {category_dir}/")

def main():
    # Replace '/path/to/directory' with the path to your target directory
    path_to_directory = '/Volumes/LaCie/files/family (375.28GB)/2021 (325.56GB)'
    categorize_and_move_files(path_to_directory)

if __name__ == "__main__":
    main()
