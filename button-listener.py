from gpiozero import Button
from signal import pause
import subprocess
import os

# Define GPIO pin connected to the button
BUTTON_PIN = 17  # GPIO 17
button = Button(BUTTON_PIN)

# Record flag to track the state of recording
is_recording = False

def start_recording():
    """Start the recording process."""
    global is_recording
    if not is_recording:
        # Start the recording command
        is_recording = True
        print("Recording started...")
        
        # Command to start recording, adjust the command as needed
        # Replace with the correct path for your script and options
        subprocess.Popen(['python3', 'record-gameplay.py'])
    else:
        print("Recording is already in progress.")

def stop_recording():
    """Stop the recording process."""
    global is_recording
    if is_recording:
        # Stop the recording, adjust the command as needed
        is_recording = False
        print("Recording stopped.")
        
        # You can kill the subprocess or handle stopping logic here
        # Example: subprocess.Popen(['killall', 'ffmpeg']) or your specific stop logic
        # subprocess.Popen(['killall', 'python3'])  # Adjust to stop the specific script

def button_pressed():
    """Handler for button press."""
    global is_recording
    if is_recording:
        stop_recording()  # Stop the recording if it's already recording
    else:
        start_recording()  # Start the recording if not recording

# Set the function to call when the button is pressed
button.when_pressed = button_pressed

print("Waiting for button press...")
pause()  # Keep the script running to detect button presses
