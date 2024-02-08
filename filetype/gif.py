import os
import shutil

def move_gif_files_to_folder(directory):
    """Moves all .gif files found in the directory and its subdirectories to a 'GIF' folder within the directory."""
    # Path for the GIF folder
    gif_folder = os.path.join(directory, 'GIF')

    # Create the GIF folder if it doesn't exist
    if not os.path.exists(gif_folder):
        os.mkdir(gif_folder)

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.gif'):
                file_path = os.path.join(root, file)

                # Construct the new path in the GIF folder
                new_file_path = os.path.join(gif_folder, file)

                # Check if a file with the same name already exists in the GIF folder
                if os.path.exists(new_file_path):
                    print(f"File {file} already exists in {gif_folder}, skipping.")
                    continue

                # Move the file
                shutil.move(file_path, new_file_path)
                print(f"Moved {file} to {gif_folder}")

def main():
    # Replace '/path/to/directory' with the path to the directory you want to process
    path_to_directory = '/Users/gunnarcurry/Dropbox/image/artdesign/puffwizzartwork'
    move_gif_files_to_folder(path_to_directory)

if __name__ == "__main__":
    main()
