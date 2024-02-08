import os
import shutil
from datetime import datetime

def sort_files_by_day(directory):
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
                # If the platform doesn't have st_birthtime, use the last modified time
                creation_time = stat_info.st_mtime
                print(f"Using last modified date for {item}")

            # Format the birth time as 'Year-Month-Day'
            day_folder = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d')
            
            # Create a new directory for 'Year-Month-Day' if it doesn't exist
            day_dir = os.path.join(directory, day_folder)
            if not os.path.exists(day_dir):
                os.makedirs(day_dir)
            
            # Move the file into the corresponding 'Year-Month-Day' directory
            shutil.move(item_path, os.path.join(day_dir, item))
            print(f"Success: Moved {item} to {day_dir}/")
        except Exception as e:
            print(f"Failure: Could not move {item}. Error: {e}")

def main():
    # Replace '/path/to/directory' with the path to your target directory
    path_to_directory = '/Volumes/LaCie/files/travel (702.88GB)/europe'
    sort_files_by_day(path_to_directory)

if __name__ == "__main__":
    main()
