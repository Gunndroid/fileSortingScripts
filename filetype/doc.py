import os
import shutil
import hashlib

def file_hash(filepath):
    """ Function to calculate MD5 hash of a file """
    md5_hash = hashlib.md5()
    with open(filepath, 'rb') as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
    return md5_hash.hexdigest()

def find_and_move_duplicate_documents(directory):
    """ Function to find duplicate documents and move them to a subdirectory """
    hashes = {}
    duplicates_dir = os.path.join(directory, "duplicates")

    # Create a directory for duplicates if it doesn't exist
    if not os.path.exists(duplicates_dir):
        os.makedirs(duplicates_dir)

    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith(('.txt', '.doc', '.docx', '.pdf', '.odt')):
                filepath = os.path.join(dirpath, filename)
                filehash = file_hash(filepath)

                if filehash in hashes and dirpath != duplicates_dir:
                    print(f"Duplicate found: {filepath} moved to {duplicates_dir}")
                    shutil.move(filepath, duplicates_dir)
                else:
                    hashes[filehash] = filepath

# Replace '/path/to/your/documents' with the path to the directory you want to scan
find_and_move_duplicate_documents('/Users/gunnarcurry/Dropbox/document')
