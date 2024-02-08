# import os
# import re

# def to_camel_case(name):
#     # Split the name by non-alphanumeric characters
#     words = re.split(r'[^a-zA-Z0-9]', name)
#     # Convert to CamelCase: first word lower case, others title case
#     camel_case_name = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
#     # Return the camelCase name limited to 40 characters
#     return camel_case_name[:40]

# def rename_files(directory):
#     """Renames files in the specified directory to camelCase and limits the name to 40 characters."""
#     for filename in os.listdir(directory):
#         file_path = os.path.join(directory, filename)

#         # Skip directories
#         if os.path.isdir(file_path):
#             continue

#         # Remove file extension and convert to camelCase
#         name, ext = os.path.splitext(filename)
#         new_name = to_camel_case(name) + ext.lower()

#         # Ensure the entire file name, including the extension, is only 40 characters
#         if len(new_name) > 40:
#             # Reserve space for the extension and trim the basename accordingly
#             basename_length = 40 - len(ext)
#             new_name = new_name[:basename_length] + ext.lower()

#         new_file_path = os.path.join(directory, new_name)

#         # Rename the file if the new name is different
#         if new_name != filename:
#             os.rename(file_path, new_file_path)
#             print(f"Renamed '{filename}' to '{new_name}'")
#         else:
#             print(f"'{filename}' did not need changes.")

# def main():
#     # Replace '/path/to/directory' with the path to the directory you want to process
#     path_to_directory = '/Users/gunnarcurry/Dropbox/video/rawfootage/mp4'
#     rename_files(path_to_directory)

# if __name__ == "__main__":
#     main()
