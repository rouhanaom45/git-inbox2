import pyautogui
import time
import os
import random

time.sleep(1.5)

button_images = [
    'cap-press_button.png'
]

max_attempts = 12

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
            print(f"'{image}' detected at {location}, clicking and holding at random coordinates for 25 seconds...")
            time.sleep(1)
            # Calculate random coordinates within the detected location's bounding box
            random_x = random.randint(location.left, location.left + location.width - 1)
            random_y = random.randint(location.top, location.top + location.height - 1)
            pyautogui.moveTo(random_x, random_y)
            pyautogui.click(random_x, random_y)
            time.sleep(1)
            for _ in range(random.randint(5, 7)):
                pyautogui.press('down')
                time.sleep(random.uniform(0.5, 0.8))

            exit()

    print("No buttons detected in this attempt. Pressing Down Arrow key to continue...")
    time.sleep(2)

print("Maximum detection attempts reached. Exiting...")
