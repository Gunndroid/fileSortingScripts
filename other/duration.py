from moviepy.editor import VideoFileClip
import os
import shutil

def sort_videos_by_duration(folder_path):
    categories = {
        '0-10sec': (0, 10),
        '10-30sec': (10, 30),
        '30-1min': (30, 60),
        '1min+': (60, float('inf')),
    }

    # Ensure categories exist
    for category in categories.keys():
        cat_dir = os.path.join(folder_path, category)
        if not os.path.exists(cat_dir):
            os.makedirs(cat_dir)

    # Sort the videos
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath) and filename.lower().endswith(('.mp4', '.mov', '.avi')):
            clip = VideoFileClip(filepath)
            duration = clip.duration  # duration in seconds

            # Determine the category
            for category, (lower_bound, upper_bound) in categories.items():
                if lower_bound <= duration < upper_bound:
                    dest_dir = os.path.join(folder_path, category)
                    shutil.move(filepath, dest_dir)
                    print(f"Moved {filename} to {category}")
                    break

def main():
    folder_path = '/Volumes/LaCie/files/problemfolders/under30 (122.23GB)/2020-02 (28.66GB)'  # Replace with your folder path
    sort_videos_by_duration(folder_path)

if __name__ == "__main__":
    main()
