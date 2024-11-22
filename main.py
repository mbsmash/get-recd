import subprocess
import os
import signal
from pynput import keyboard

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
            os.kill(recording_process.pid, signal.SIGINT)
            recording_process = None

def toggle_recording():
    if is_recording:
        stop_recording()
    else:
        start_recording()

def on_press(key):
    try:
        if key.char == 'r':
            toggle_recording()
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def main():
    print("Waiting for input...")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()