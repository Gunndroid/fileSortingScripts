import os
import shutil

def move_audio_files_to_folders(directory):
    """Moves .mp3 and .wav files to 'MP3' and 'WAV' folders respectively."""
    mp3_folder = os.path.join(directory, 'MP3')
    wav_folder = os.path.join(directory, 'WAV')

    # Create the folders if they don't exist
    if not os.path.exists(mp3_folder):
        os.mkdir(mp3_folder)
    if not os.path.exists(wav_folder):
        os.mkdir(wav_folder)

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Move .mp3 files to the MP3 folder
            if file.lower().endswith('.mp3'):
                new_file_path = os.path.join(mp3_folder, file)
                if not os.path.exists(new_file_path):
                    shutil.move(file_path, new_file_path)
                    print(f"Moved {file} to {mp3_folder}")

            # Move .wav files to the WAV folder
            elif file.lower().endswith('.wav'):
                new_file_path = os.path.join(wav_folder, file)
                if not os.path.exists(new_file_path):
                    shutil.move(file_path, new_file_path)
                    print(f"Moved {file} to {wav_folder}")

def main():
    # Replace '/path/to/directory' with the path to the directory you want to process
    path_to_directory = '/Users/gunnarcurry/Dropbox/'
    move_audio_files_to_folders(path_to_directory)

if __name__ == "__main__":
    main()
