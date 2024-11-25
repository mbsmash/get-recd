import subprocess
import sys
import os
import signal
import time

def handle_sigterm(signum, frame):
    print("Received SIGTERM signal, stopping recording...")
    sys.exit(0)

signal.signal(signal.SIGTERM, handle_sigterm)

timestamp = int(time.time())
output_file = os.path.join(".", f"gameplay_{timestamp}.mp4")  # Save to current directory



def record_gameplay():
    # Create a timestamp for the file name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    try:
        # FFmpeg command to record at 720p 60fps and encode on the fly to H.264 MP4
        ffmpeg_command = [
            'ffmpeg',
            '-f', 'v4l2',  # Input format for video capture
            '-thread_queue_size', '4096',  # Set input queue size
            '-input_format', 'mjpeg',  # Input format for video capture
            '-framerate', '60',  # Set input frame rate to 60fps
            '-video_size', '1280x720',  # Set input video resolution to 720p
            '-i', '/dev/video0',  # Video input device
            '-f', 'alsa',  # Input format for audio capture
            '-thread_queue_size', '4096',  # Set input queue size
            '-i', 'hw:2,0',  # Audio input device
            '-c:v', 'mjpeg', # Set video codec to MJPEG
            '-c:a', 'aac',  # Set audio codec to AAC
            '-preset', 'fast',  # Set encoder preset for speed vs quality
            '-crf', '20',  # Set CRF for video quality (lower is better quality)
            '-r', '60',  # Set output frame rate to 60fps
            '-pix_fmt', 'yuv420p',  # Ensure compatible pixel format
            output_file  # Output file path
        ]

        # Run FFmpeg command
        process = subprocess.Popen(ffmpeg_command)
        process.wait()
        print(f"Recording completed successfully. File saved as {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    record_gameplay()
