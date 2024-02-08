from moviepy.editor import VideoFileClip

def cut_video_into_parts(filename, clip_duration_minutes=30):
    with VideoFileClip(filename) as video:
        duration = video.duration  # Video duration in seconds
        part_duration = clip_duration_minutes * 60  # Convert minutes to seconds

        for part_number in range(int(duration / part_duration)):
            start_time = part_number * part_duration
            end_time = start_time + part_duration
            new_clip = video.subclip(start_time, end_time)

            output_filename = f"{filename.rsplit('.', 1)[0]}_part{part_number + 1}.mp4"
            new_clip.write_videofile(output_filename, codec="libx264", audio_codec="aac")
            print(f"Created {output_filename}")

def main():
    video_filename = '/Volumes/LaCie/files/problemfolders/100+/archive/babytapes.mp4'
    cut_video_into_parts(video_filename)

if __name__ == "__main__":
    main()
