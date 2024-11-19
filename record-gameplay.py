import subprocess
import datetime
import os

def record_gameplay():
    # Create a timestamp for the file name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(".", f"gameplay_{timestamp}.mp4")  # Save to current directory
    
    try:
        # FFmpeg command to record at 720p 60fps and encode on the fly to H.264 MP4
        ffmpeg_command = [
            'ffmpeg',
            '-f', 'v4l2',  # Input format for video capture
            '-i', '/dev/video0',  # Video input device
            '-c:v', 'libx264',  # Use H.264 encoder
            '-preset', 'fast',  # Set encoder preset for speed vs quality
            '-crf', '20',  # Set CRF for video quality (lower is better quality)
            '-r', '60',  # Set output frame rate to 60fps
            '-pix_fmt', 'yuv420p',  # Ensure compatible pixel format
            '-t', '00:05:00',  # Set recording duration (5 minutes in this case)
            output_file  # Output file path
        ]

        # Run FFmpeg command
        subprocess.run(ffmpeg_command, check=True)
        print(f"Recording completed successfully. File saved as {output_file}")

    except subprocess.CalledProcessError as e:
        print(f"Recording failed: {e}")

if __name__ == "__main__":
    record_gameplay()
