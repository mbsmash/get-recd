from gpiozero import Button
from signal import pause

button = Button(17)  # GPIO 17

def button_pressed():
    print("Button was pressed!")

button.when_pressed = button_pressed

print("Waiting for button press...")
pause()  # Keep the script running to detect button presses
