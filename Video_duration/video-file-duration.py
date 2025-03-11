import os
import subprocess
import re

# Ask for directory input
directory = input("Enter the path to the directory: ").strip()

# Function to get video duration
def get_video_duration(file_path):
    try:
        result = subprocess.run(
            ["ffprobe", "-i", file_path, "-show_entries", "format=duration", "-v", "quiet", "-of", "csv=p=0"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        seconds = float(result.stdout.strip())
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    except Exception as e:
        return "Error"

# Collect video info
video_info = []

if os.path.isdir(directory):
    for file in os.listdir(directory):
        if file.endswith(('.mp4', '.mkv')):
            file_path = os.path.join(directory, file)
            duration = get_video_duration(file_path)
            video_info.append((file, duration))

    # Save to a text file
    output_file = os.path.join(directory, "video_list.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        for name, duration in video_info:
            f.write(f"{name} - {duration}\n")

    print(f"Video information saved to: {output_file}")
else:
    print("Invalid directory. Please check the path and try again.")
