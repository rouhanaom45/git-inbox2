import pyautogui
import time
import os
import subprocess

time.sleep(1.5)

button_images = [
    'file_button.png'
]

max_attempts = 5000

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
            pyautogui.click(location)
            exit()

    print("No buttons detected in this attempt. Pressing Down Arrow key to continue...")
    time.sleep(1)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    pyautogui.write('www.github.com')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(2.5)
    pyautogui.hotkey('ctrl', 'shift', 'tab')
    time.sleep(1.3)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1.2)
    subprocess.run(["python3", "replay1.py"])
    time.sleep(1)

print("Maximum detection attempts reached. Exiting...")
