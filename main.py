from gpiozero import Button
from signal import pause
import subprocess
import os
import smbus2
import time
from button_listener import button_pressed as button_listener_pressed
from check_usb_storage import check_usb_storage

# Define GPIO pin connected to the button
BUTTON_PIN = 17  # GPIO 17
button = Button(BUTTON_PIN)

# Record flag to track the state of recording
is_recording = False

# I2C LCD display settings
LCD_ADDRESS = 0x27  # Adjust based on your LCD's I2C address
LCD_COLUMNS = 16
LCD_ROWS = 2

# Create an SMBus instance for I2C communication
bus = smbus2.SMBus(1)

# LCD initialization
def lcd_init():
    # Sending initialization commands to the LCD
    lcd_write(0x33, 0)  # Initialize
    lcd_write(0x32, 0)  # Set to 4-bit mode
    lcd_write(0x28, 0)  # Function set: 2 lines, 5x8 font
    lcd_write(0x0C, 0)  # Display ON, Cursor OFF
    lcd_write(0x06, 0)  # Entry mode: Increment cursor
    lcd_write(0x01, 0)  # Clear display
    time.sleep(0.05)

def lcd_write(value, mode):
    """Write a byte to the LCD."""
    ...

def lcd_toggle_enable(bits):
    """Toggle the enable pin on the LCD."""
    ...

def lcd_message(message):
    """Display a message on the LCD."""
    ...

def start_recording():
    """Start the recording process."""
    global is_recording
    if not is_recording:
        # Start the recording command
        is_recording = True
        print("Recording started...")

        # Update the LCD with status
        lcd_message("Recording Started")

        # Command to start recording, adjust this based on your setup
        subprocess.Popen(['python3', 'record-gameplay.py'])
    else:
        print("Recording is already in progress.")

def stop_recording():
    """Stop the recording process."""
    global is_recording
    if is_recording:
        # Stop the recording command
        is_recording = False
        print("Recording stopped.")

        # Update the LCD with status
        lcd_message("Recording Stopped")
    else:
        print("No recording in progress.")

def button_pressed():
    """Handler for button press."""
    global is_recording
    if is_recording:
        stop_recording()  # Stop the recording if it's already recording
    else:
        start_recording()  # Start the recording if not recording

# Set the function to call when the button is pressed
button.when_pressed = button_pressed

# Initialize the LCD
lcd_init()

# Check USB storage
check_usb_storage()

print("Waiting for button press...")
lcd_message("Waiting for input...")
pause()  # Keep the script running to detect button presses