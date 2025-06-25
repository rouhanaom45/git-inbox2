import pyautogui
import random
import time
import subprocess
import string
import sys


# Enable fail-safe to prevent runaway scripts
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.03  # Small base pause for smoother actions

# Initial delay to allow user to prepare
time.sleep(1.5)
subprocess.run(["bash", "open-profile.sh"], check=True)
time.sleep(2)

def smooth_mouse_move(target_x, target_y, duration=0.5):
    """Move mouse with human-like path using Bezier curves and micro-jitters."""
    start_x, start_y = pyautogui.position()
    steps = int(duration * 60)  # 60 FPS for smooth movement
    # Introduce slight curve in path
    control_x = start_x + (target_x - start_x) * random.uniform(0.3, 0.7) + random.randint(-20, 20)
    control_y = start_y + (target_y - start_y) * random.uniform(0.3, 0.7) + random.randint(-20, 20)
    
    for i in range(steps + 1):
        t = i / steps
        # Quadratic Bezier curve
        x = (1 - t) ** 2 * start_x + 2 * (1 - t) * t * control_x + t ** 2 * target_x
        y = (1 - t) ** 2 * start_y + 2 * (1 - t) * t * control_y + t ** 2 * target_y
        # Add micro-jitters
        x += random.uniform(-3, 3) if random.random() < 0.4 else 0
        y += random.uniform(-3, 3) if random.random() < 0.4 else 0
        pyautogui.moveTo(x, y, duration=0.016, tween=pyautogui.easeInOutQuad)
    
    # Simulate overshoot and correction
    if random.random() < 0.25:
        overshoot_x = target_x + random.randint(-15, 15)
        overshoot_y = target_y + random.randint(-15, 15)
        pyautogui.moveTo(overshoot_x, overshoot_y, duration=0.1)
        time.sleep(random.uniform(0.05, 0.2))
        pyautogui.moveTo(target_x, target_y, duration=0.15)

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

time.sleep(1)
pyautogui.click(468, 81)
time.sleep(0.5)
pyautogui.write('about:preferences')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(2.5)
pyautogui.click(1340, 127)
time.sleep(1.5)
pyautogui.click(1340, 127)
time.sleep(1.5)
pyautogui.click(1204, 393)
time.sleep(1)
pyautogui.scroll(-800)
time.sleep(2)
pyautogui.click(887, 525)
time.sleep(1.5)
pyautogui.click(335, 240)
time.sleep(1)
pyautogui.click(989, 560)
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
pyautogui.click(1340, 127)
time.sleep(1.5)
pyautogui.click(1340, 127)
time.sleep(1.5)
pyautogui.click(652, 373)
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
random_click_within_rect((540, 287), (818, 307))
random_wait(10, 12)


