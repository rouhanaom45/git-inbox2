import pyautogui
import random
import time
import subprocess

def random_wait(min_time, max_time):
    time.sleep(random.uniform(min_time, max_time))

def random_click_within_rect(top_left, bottom_right):
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.click(x, y)
    time.sleep(random.uniform(0.1, 0.3))  # Simulate human-like click

# Perform actions step by step
# Step 1: Perform a random click within the first rectangular area
random_click_within_rect((366, 381), (732, 397))
random_wait(0.5, 1)

# Step 2: Press Ctrl+V and sleep
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# Step 3: Perform a random click within the second rectangular area
random_click_within_rect((472, 469), (884, 487))
random_wait(10, 12)

# Step 4: Run the script "continue.py" using subprocess
subprocess.run(["python3", "continue11.py"])
time.sleep(2)

# Step 5: Perform a random click within the third rectangular area
random_click_within_rect((523, 561), (814, 578))
random_wait(6, 8)
random_click_within_rect((77, 206), (332, 502))
random_wait(1, 2)
for _ in range(random.randint(5, 6)):
    pyautogui.press("down")
    time.sleep(random.uniform(0.1, 0.3))
# Step 6: Perform a random click within the fourth rectangular area
random_click_within_rect((524, 491), (812, 502))
random_wait(0.5, 1)

# Step 7: Perform a random click within the fifth rectangular area
random_click_within_rect((501, 587), (843, 606))
random_wait(10, 12)

# Step 8: Run the script "welcom.py" using subprocess
subprocess.run(["python3", "welcom2.py"])
time.sleep(2)

# Step 9: Perform a sequence of random clicks with delays
random_click_within_rect((534, 584), (828, 603))
random_wait(3, 4)

random_click_within_rect((520, 586), (836, 601))
random_wait(3, 4)

random_click_within_rect((528, 585), (829, 602))
random_wait(3, 4)

random_click_within_rect((521, 601), (832, 607))
random_wait(3, 4)
pyautogui.click(96, 83)
time.sleep(2.5)
subprocess.run(["python3", "proton-adress.py"])
# Step 10: Click on specific points and sleep
time.sleep(1.5)
pyautogui.press("tab")
time.sleep(0.6)
pyautogui.press("tab")
time.sleep(0.6)

# Press Enter key
pyautogui.press("enter")
time.sleep(1.7)
pyautogui.click(96, 83)
time.sleep(2.5)

pyautogui.hotkey('ctrl', 't')
time.sleep(1)

time.sleep(0.7)
pyautogui.write('about:logins')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(3)

pyautogui.click(890, 236)
time.sleep(1.5)

pyautogui.hotkey('ctrl', 'v')
time.sleep(0.8)

pyautogui.press('enter')
time.sleep(3)
pyautogui.hotkey('ctrl', 'w')
time.sleep(1.5)

subprocess.run(["python", "email-inbox1.py"])
time.sleep(1)
