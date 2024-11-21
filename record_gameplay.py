import subprocess
import datetime
import os
import time
from main import lcd_init, lcd_write, is_recording

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
            output_file  # Output file path
        ]

        # Run FFmpeg command
        subprocess.run(ffmpeg_command, check=True)
        print(f"Recording completed successfully. File saved as {output_file}")

    except subprocess.CalledProcessError as e:
        print(f"Recording failed: {e}")

def lcd_write(message, line):
    # Function to write a message to the LCD display
    message = message.ljust(LCD_COLUMNS, " ")
    bus.write_byte_data(LCD_ADDRESS, 0x80 | line, 0x00)
    for char in message:
        bus.write_byte_data(LCD_ADDRESS, 0x40, ord(char))

def update_lcd(message):
    # Clear the display and write the new message
    lcd_write(0x01, 0)  # Clear display
    lcd_write(message, 0)

def start_recording():
    global is_recording
    is_recording = True
    update_lcd("Recording started")
    # Add your recording logic here
    time.sleep(5)  # Simulate recording duration
    stop_recording()

def stop_recording():
    global is_recording
    is_recording = False
    update_lcd("Recording stopped")
    # Add your stop recording logic here

def main():
    update_lcd("Ready to record")
    # Wait for button press to start recording
    while True:
        if button.is_pressed:
            start_recording()
        time.sleep(0.1)

if __name__ == "__main__":
    main()
