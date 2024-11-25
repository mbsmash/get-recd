import subprocess
import os
import time

is_recording = False
recording_process = None
output_file = None

def start_recording():
    global is_recording, recording_process, output_file
    if not is_recording:
        is_recording = True
        print("Recording started...")
        recording_process = subprocess.Popen(['python3', 'record_gameplay.py'])
        output_file = f"./gameplay_{int(time.time())}.mp4"  # Update with the expected output file name

def stop_recording():
    global is_recording, recording_process, output_file
    if is_recording:
        is_recording = False
        print("Recording stopped...")
        if recording_process:
            recording_process.terminate()
            try:
                recording_process.wait(timeout=5)
                print("Recording process terminated successfully.")
            except subprocess.TimeoutExpired:
                print("Recording process did not terminate in time, killing it.")
                recording_process.kill()
            recording_process = None
        # Check if the output file exists
        if os.path.exists(output_file):
            print(f"Recording file '{output_file}' has been saved successfully.")
        else:
            print(f"Recording file '{output_file}' was not found.")

def main():
    start_recording()
    input("Press Enter to stop recording...\n")
    stop_recording()

if __name__ == "__main__":
    main()