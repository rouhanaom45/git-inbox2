import pyautogui
import time
import os
import sys
import subprocess

time.sleep(1.5)

button_images = [
    'confirm0_button.png'
]

max_attempts = 20

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
            print("Performing additional tasks...")
            time.sleep(2)
            pyautogui.click(648, 294)
            time.sleep(1.5) 
            pyautogui.click(1076, 630)
            time.sleep(2)
            pyautogui.click(556, 626)
            time.sleep(1)
            pyautogui.click(92, 83)
            time.sleep(8)
            subprocess.run(["python3", "accept.py"])
            time.sleep(1)
            subprocess.run(["python3", "banner.py"])
            time.sleep(1)
            sys.exit(0)  # Success: button found and clicked

    print("No buttons detected in this attempt. Pressing Down Arrow key to continue...")
    time.sleep(5)

print("Maximum detection attempts reached. Exiting...")
time.sleep(0.7)
pyautogui.hotkey('ctrl', 'w')
time.sleep(0.7)
subprocess.run(["python3", "save.py"])
time.sleep(1)
subprocess.run(["python3", "github1.py"])
time.sleep(1)
subprocess.run(["python3", "github2.py"])
time.sleep(1)
