import os
import shutil
from datetime import datetime

def sort_files_by_year(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        # Skip if it's a directory
        if os.path.isdir(item_path):
            continue
        
        try:
            # Get the birth time of the file
            stat_info = os.stat(item_path)
            try:
                # Try to get the birth time (creation date on macOS)
                creation_time = stat_info.st_birthtime
            except AttributeError:
                # If the platform doesn't have st_birthtime, skip the file
                print(f"No creation date available for {item}, skipping.")
                continue

            # Format the birth time as 'Year'
            year_folder = datetime.fromtimestamp(creation_time).strftime('%Y')
            
            # Create a new directory for 'Year' if it doesn't exist
            year_dir = os.path.join(directory, year_folder)
            if not os.path.exists(year_dir):
                os.makedirs(year_dir)
            
            # Move the file into the corresponding 'Year' directory
            shutil.move(item_path, os.path.join(year_dir, item))
            print(f"Success: Moved {item} to {year_dir}/")
        except Exception as e:
            print(f"Failure: Could not move {item}. Error: {e}")

def main():
    # Replace '/path/to/directory' with the path to your target directory
    path_to_directory = '/Users/gunnarcurry/Desktop/originals/originals'
    sort_files_by_year(path_to_directory)

if __name__ == "__main__":
    main()
