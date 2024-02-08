import os
import shutil
from datetime import datetime

def sort_files_by_birth_time(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        # Skip if it's a directory
        if os.path.isdir(item_path):
            continue
        
        try:
            # Get the birth time of the file, which is the creation date on macOS
            stat_info = os.stat(item_path)
            try:
                # Try to get the birth time (macOS)
                creation_time = stat_info.st_birthtime
            except AttributeError:
                # If the platform doesn't have st_birthtime, skip the file
                print(f"No creation date available for {item}, skipping.")
                continue

            # Format the birth time as 'Year-Month'
            folder_name = datetime.fromtimestamp(creation_time).strftime('%Y-%m')
            
            # Create a new directory for 'Year-Month' if it doesn't exist
            month_dir = os.path.join(directory, folder_name)
            if not os.path.exists(month_dir):
                os.makedirs(month_dir)
            
            # Move the file into the corresponding 'Year-Month' directory
            shutil.move(item_path, os.path.join(month_dir, item))
            print(f"Success: Moved {item} to {month_dir}/")
        except Exception as e:
            print(f"Failure: Could not move {item}. Error: {e}")

def main():
    # Replace '/path/to/directory' with the path to your target directory
    path_to_directory = '/Users/gunnarcurry/Dropbox/image/puffwizz/jpg'
    sort_files_by_birth_time(path_to_directory)

if __name__ == "__main__":
    main()
