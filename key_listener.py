import keyboard

def key_pressed():
    """Function to handle key press event."""
    print("Key pressed, starting recording...")
    # Call the start_recording function from main.py
    from main import start_recording
    start_recording()

# Listen for a specific key press (e.g., 'r' key)
keyboard.add_hotkey('r', key_pressed)

# Keep the script running to listen for key presses
keyboard.wait('esc')  # Press 'esc' to exit