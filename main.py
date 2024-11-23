import subprocess
import time
import os

is_recording = False
recording_process = None
output_file = 'output.mp4'  # Replace with your actual output file name

def start_recording():
    global is_recording, recording_process
    if not is_recording:
        is_recording = True
        print("Recording started...")
        recording_process = subprocess.Popen(['python3', 'record_gameplay.py'])

def stop_recording():
    global is_recording, recording_process
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
    print("Waiting for 3 seconds before starting recording...")
    time.sleep(3)
    start_recording()
    print("Recording for 10 seconds...")
    time.sleep(10)
    stop_recording()

if __name__ == "__main__":
    main()