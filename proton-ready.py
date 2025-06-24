import pyautogui
import random
import time
import subprocess
import string
import sys

time.sleep(1.5)

def random_wait(min_time, max_time):
    """Sleep for a random time with human-like variability."""
    sleep_time = random.uniform(min_time, max_time)
    # Add occasional longer pauses to simulate distraction or hesitation
    if random.random() < 0.15:  # 15% chance for a longer pause
        sleep_time += random.uniform(0.7, 2.0)
    # Rarely add a brief pause to mimic quick adjustments
    elif random.random() < 0.1:
        sleep_time *= random.uniform(0.5, 0.8)
    time.sleep(sleep_time)

def random_click_within_rect(top_left, bottom_right):
    """Click within a rectangle with human-like movement and size-adjusted offset."""
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    # Calculate rectangle dimensions
    width = bottom_right[0] - top_left[0]
    height = bottom_right[1] - top_left[1]
    # Scale offset based on rectangle size; no offset for very small rectangles
    if width < 10 or height < 10:
        offset_x = 0
        offset_y = 0
    else:
        max_offset = min(width, height) * 0.1  # Cap offset at 10% of smaller dimension
        offset_x = random.randint(-int(max_offset), int(max_offset))
        offset_y = random.randint(-int(max_offset), int(max_offset))
    x += offset_x
    y += offset_y
    # Ensure click stays within rectangle bounds
    x = max(top_left[0], min(x, bottom_right[0]))
    y = max(top_left[1], min(y, bottom_right[1]))
    smooth_mouse_move(x, y, duration=random.uniform(0.4, 0.8))
    
    # Pre-click hesitation
    if random.random() < 0.2:
        time.sleep(random.uniform(0.15, 0.5))
        pyautogui.moveRel(random.randint(-5, 5), random.randint(-5, 5), duration=0.1)
    
    pyautogui.click()
    # Post-click drift
    if random.random() < 0.1:
        pyautogui.moveRel(random.randint(-10, 10), random.randint(-10, 10), duration=0.1)
    time.sleep(random.uniform(0.05, 0.25))

# New Step: Detect the tab button using 'tab_button.png'
try:
    tab_button_location = pyautogui.locateCenterOnScreen('tab_button.png', confidence=0.8)
    if tab_button_location is not None:
        print("Tab button detected, clicking at (1342, 125)...")
        pyautogui.click(1339, 175)
        time.sleep(2)
    else:
        print("Tab button not detected, proceeding to Step 1...")
except Exception as e:
    print(f"Error detecting tab button: {e}")
    print("Proceeding to Step 1...")

time.sleep(2)

pyautogui.click(468, 81)
time.sleep(0.5)
pyautogui.write('about:preferences')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(2.5)
pyautogui.click(1194, 257)
time.sleep(1)
pyautogui.scroll(-500)
time.sleep(2)
pyautogui.click(900, 524)
time.sleep(1.5)
pyautogui.click(334, 287)
time.sleep(1)
pyautogui.click(985, 555)
time.sleep(1.5)
pyautogui.hotkey('ctrl', 't')
time.sleep(1)  # Sleep for 1 second

# Switch back to the previous tab (Ctrl + Shift + Tab)
pyautogui.hotkey('ctrl', 'shift', 'tab')
time.sleep(1)  # Sleep for 1 second

# Close the current tab (Ctrl + W)
pyautogui.hotkey('ctrl', 'w')
time.sleep(1)  # Sleep for 1 second
pyautogui.click(468, 81)
time.sleep(0.5)
pyautogui.write('about:logins')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(2.5)
pyautogui.click(661, 417)
time.sleep(1.5)

subprocess.run(["python", "email-inbox1.py"])
time.sleep(1)

pyautogui.hotkey('ctrl', 't')
time.sleep(1)  # Sleep for 1 second

# Switch back to the previous tab (Ctrl + Shift + Tab)
pyautogui.hotkey('ctrl', 'shift', 'tab')
time.sleep(1)  # Sleep for 1 second

# Close the current tab (Ctrl + W)
pyautogui.hotkey('ctrl', 'w')
time.sleep(1)  # Sleep for 1 second
pyautogui.click(468, 81)
time.sleep(0.5)
pyautogui.write('https://mail.proton.me/u/3/inbox?welcome=true')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(12)
# Random click within one of two areas
if random.choice([True, False]):
    random_click_within_rect((84, 298), (332, 524))
else:
    random_click_within_rect((1000, 266), (1282, 494))

random_wait(1, 2)
press_count = random.randint(10, 12)

for i in range(press_count):
    pyautogui.press('down')
    time.sleep(random.uniform(0.3, 0.4))

random_wait(1, 2)
random_click_within_rect((537, 289), (817, 306))
random_wait(10, 12)


