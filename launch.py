import pyautogui
import time
import os
import sys

time.sleep(3)

button_images = [
    'ok_button.png',
    'okko_button.png',
    'macro_button.png',
    'macro1_button.png',
    'macro2_button.png'
]

max_attempts = 7

for image in button_images:
    if not os.path.isfile(image):
        print(f"Error: The image file '{image}' does not exist.")

for attempt in range(max_attempts):
    print(f"Attempt {attempt + 1} of {max_attempts}: Attempting to detect verification buttons...")
    time.sleep(2)

    for image in button_images:
        try:
            print(f"Trying to detect: {image}")
            location = pyautogui.locateOnScreen(image, confidence=0.8)
        except Exception as e:
            print(f"Error while detecting '{image}': {e}")
            location = None

        if location:
            print(f"'{image}' detected at {location}, clicking...")
            time.sleep(1)
            print(f"'{image}' clicked")
            sys.exit(0)  # Success: button found and clicked

    print("No buttons detected in this attempt. Pressing Down Arrow key to continue...")
    time.sleep(1)

print("Maximum detection attempts reached. Exiting...")
sys.exit(1)  # Failure: max attempts reached, signal to retry
