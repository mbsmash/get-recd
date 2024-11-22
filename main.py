import subprocess
import keyboard

is_recording = False
recording_process = None

def start_recording():
    global is_recording, recording_process
    if not is_recording:
        is_recording = True
        print("Recording started...")
        recording_process = subprocess.Popen(['python3', 'start_recording.py'])

def stop_recording():
    global is_recording, recording_process
    if is_recording:
        is_recording = False
        print("Recording stopped...")
        if recording_process:
            recording_process.terminate()
            recording_process = None

def toggle_recording():
    if is_recording:
        stop_recording()
    else:
        start_recording()

def main():
    print("Waiting for input...")

    # Set the function to call when the key is pressed
    keyboard.add_hotkey('space', toggle_recording)  # Replace 'space' with the desired key

    keyboard.wait('esc')  # Keep the script running, replace 'esc' with the key to stop the script

if __name__ == "__main__":
    main()