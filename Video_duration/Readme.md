# Video Metadata Extractor

This script allows you to dynamically input a directory path and extract the names and durations of all video files within that directory. The output is saved to a `video_list.txt` file.

## Features
- Dynamically input the directory path.
- Extract video filenames and their durations.
- Supports multiple video formats (e.g., `.mp4`, `.mkv`, `.avi`, `.mov`, etc.).
- Outputs the results to a `video_list.txt` file.

## Prerequisites
Ensure `ffmpeg` is installed on your system. If not, download and install it from [ffmpeg.org](https://ffmpeg.org/).

### Check if `ffmpeg` is installed:
```bash
ffmpeg -version
```

## Usage Instructions

1. **Set up your environment:**
   Ensure Python is installed on your system. You can check by running:
   ```bash
   python --version
   ```

2. **Install required libraries:**
   Ensure you have the `subprocess` and `os` modules (these are part of the Python standard library).

3. **Run the script:**
   ```bash
   python your_script_name.py
   ```

4. **Provide the directory path:**
   When prompted, enter the full path of the directory containing your video files.

5. **View the output:**
   After execution, check the `video_list.txt` file in the same directory where the script is located. It will list the video filenames and their durations.

## Example Output
```
video1.mp4 - 00:05:34
video2.mkv - 01:12:45
video3.avi - 00:42:19
```

## Customization
- Modify the script to filter specific video formats.
- Change the output filename by updating the script's output path.

## Troubleshooting
- Ensure `ffmpeg` is in your system's PATH.
- Verify the directory path is correct and accessible.
- Check for typos in video filenames.

## License
This project is open-source and available for personal and commercial use.

