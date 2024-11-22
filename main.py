import subprocess
import time

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

def main():
    print("Waiting for 3 seconds before starting recording...")
    time.sleep(3)
    start_recording()

if __name__ == "__main__":
    main()