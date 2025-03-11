To get the names and lengths (duration) of all video files in your directory, you can use a Python script that reads the directory and extracts video metadata.The script allow you to enter the directory dynamically. Here's a script that does exactly that:

### Instructions to Run the Script:
1. Ensure `ffmpeg` is installed on your system. You can download it from [ffmpeg.org](https://ffmpeg.org/).
2. Open Command Prompt and run the script:
   ```bash
   python your_script_name.py
   ```
3. The script will create a `video_list.txt` file in the same directory, listing each video with its duration.
