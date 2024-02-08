import os
import shutil
from datetime import datetime

def sort_files_by_week_number(directory):
    for root, _, files in os.walk(directory):
        # Skip if fewer than or equal to 50 files
        if len(files) <= 50:
            continue
        
        for item in files:
            item_path = os.path.join(root, item)
            
            # Skip if it's a directory
            if os.path.isdir(item_path):
                continue
            
            try:
                # Get the birth time of the file (creation date on macOS)
                stat_info = os.stat(item_path)
                try:
                    # Try to get the birth time (macOS)
                    creation_time = stat_info.st_birthtime
                except AttributeError:
                    # If the platform doesn't have st_birthtime, skip the file
                    print(f"No creation date available for {item}, skipping.")
                    continue

                # Get the ISO calendar week number
                date = datetime.fromtimestamp(creation_time)
                year, week_num, day_of_week = date.isocalendar()
                folder_name = f"{year}-W{week_num:02d}"
                
                # Create a new directory for 'Year-Week' if it doesn't exist
                week_dir = os.path.join(root, folder_name)
                if not os.path.exists(week_dir):
                    os.makedirs(week_dir)
                
                # Move the file into the corresponding 'Year-Week' directory
                shutil.move(item_path, os.path.join(week_dir, item))
                print(f"Success: Moved {item} to {week_dir}/")
            except Exception as e:
                print(f"Failure: Could not move {item}. Error: {e}")

def main():
    # Replace '/path/to/directory' with the path to your target directory
    path_to_directory = '/Users/gunnarcurry/Dropbox/image/photos/jpg'
    sort_files_by_week_number(path_to_directory)

if __name__ == "__main__":
    main()
