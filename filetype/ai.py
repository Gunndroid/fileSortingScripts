import os
import shutil

def move_ai_files_to_folder(directory):
    """Moves all .ai files found in the directory and its subdirectories to an 'AI' folder within the directory."""
    # Path for the AI folder
    ai_folder = os.path.join(directory, 'AI')

    # Create the AI folder if it doesn't exist
    if not os.path.exists(ai_folder):
        os.mkdir(ai_folder)

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.ai'):
                file_path = os.path.join(root, file)

                # Construct the new path in the AI folder
                new_file_path = os.path.join(ai_folder, file)

                # Check if a file with the same name already exists in the AI folder
                if os.path.exists(new_file_path):
                    print(f"File {file} already exists in {ai_folder}, skipping.")
                    continue

                # Move the file
                shutil.move(file_path, new_file_path)
                print(f"Moved {file} to {ai_folder}")

def main():
    # Replace '/path/to/directory' with the path to the directory you want to process
    path_to_directory = '/Users/gunnarcurry/Dropbox/'
    move_ai_files_to_folder(path_to_directory)

if __name__ == "__main__":
    main()
