import os
import shutil

def sort_files_into_folders(directory, max_files_per_folder):
    """Sorts files into folders with a maximum of max_files_per_folder files in each."""
    # Gather all file names and sort them numerically
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

    # Create and distribute files into folders
    folder_count = 0
    for i, file in enumerate(files):
        if i % max_files_per_folder == 0:
            folder_count += 1
            folder_name = f"Folder_{folder_count}"
            folder_path = os.path.join(directory, folder_name)
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

        shutil.move(os.path.join(directory, file), os.path.join(folder_path, file))

def main():
    # Replace with the path to the directory containing the files
    path_to_directory = '/Users/gunnarcurry/Dropbox/artdesign/puffwizzartwork/puffwizzgeneratorbuilds/buildfinal6:28:22/puffwizz_metadata'
    max_files_per_folder = 50
    sort_files_into_folders(path_to_directory, max_files_per_folder)

if __name__ == "__main__":
    main()
