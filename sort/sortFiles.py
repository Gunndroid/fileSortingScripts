import os
import shutil

def sort_files_by_extension(directory):
    """Sort files in the given directory into subfolders by file extension."""
    # Iterate over all the files in the directory
    for filename in os.listdir(directory):
        # Get the file extension
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext:  # check if there is an extension
            # Create a directory for the extension if it doesn't exist
            ext_dir = os.path.join(directory, file_ext[1:])  # remove the dot in the extension
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir)

            # Move the file to the appropriate extension directory
            shutil.move(os.path.join(directory, filename), os.path.join(ext_dir, filename))

if __name__ == "__main__":
    # Replace '/path/to/directory' with the path of the directory you want to sort
    sort_files_by_extension('/Users/gunnarcurry/Dropbox/image/puffwizz')
