import pyautogui
import time
import random
import subprocess
import pyperclip
import math

# Enable fail-safe to prevent runaway scripts
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.03  # Small base pause for smoother actions

# Initial delay to allow user to prepare
time.sleep(1)

def random_sleep(min_sec, max_sec):
    """Sleep for a random time with human-like variability."""
    sleep_time = random.uniform(min_sec, max_sec)
    # Add occasional longer pauses to simulate distraction or hesitation
    if random.random() < 0.15:  # 15% chance for a longer pause
        sleep_time += random.uniform(0.7, 2.0)
    # Rarely add a brief pause to mimic quick adjustments
    elif random.random() < 0.1:
        sleep_time *= random.uniform(0.5, 0.8)
    time.sleep(sleep_time)

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

def random_click_in_rectangle(top_left, bottom_right):
    """Click within a rectangle with human-like movement and hesitation."""
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    x += random.randint(-8, 8)  # Slight offset
    y += random.randint(-8, 8)
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


# Script execution
smooth_mouse_move(1038, 630, duration=random.uniform(0.4, 0.8))
if random.random() < 0.2:
    time.sleep(random.uniform(0.15, 0.5))
pyautogui.click()
time.sleep(1)

smooth_mouse_move(696, 626, duration=random.uniform(0.4, 0.8))
if random.random() < 0.2:
    time.sleep(random.uniform(0.15, 0.5))
pyautogui.click()
time.sleep(1)

# Random click within rectangle
random_x = random.randint(803, 832)
random_y = random.randint(359, 390)
random_x += random.randint(-8, 8)
random_y += random.randint(-8, 8)
smooth_mouse_move(random_x, random_y, duration=random.uniform(0.5, 1.2))
if random.random() < 0.2:
    time.sleep(random.uniform(0.15, 0.5))
pyautogui.click()

random_sleep(1, 2)
text = pyperclip.paste()
for char in text:
    pyautogui.write(char)
    time.sleep(random.uniform(0.3, 0.45))
time.sleep(random.uniform(10, 12))
random_sleep(10, 12)

time.sleep(1)
random_click_in_rectangle((81, 203), (370, 473))
random_sleep(0.5, 1)

for _ in range(random.randint(7, 9)):
    pyautogui.press('down')
    time.sleep(random.uniform(0.5, 0.8))

random_click_in_rectangle((570, 343), (786, 356))
random_sleep(10, 14)
