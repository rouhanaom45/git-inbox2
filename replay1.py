import pyautogui
import random
import time
import string
import math
import subprocess

# Enable fail-safe to prevent runaway scripts
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.03  # Small base pause for smoother actions

# Initial delay to allow user to prepare
time.sleep(4)

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
    print(f"Slept for {sleep_time:.2f} seconds")

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

def random_click(x1, y1, x2, y2):
    """Click within a rectangle with human-like movement and size-adjusted offset."""
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)
    # Calculate rectangle dimensions
    width = x2 - x1
    height = y2 - y1
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
    x = max(x1, min(x, x2))
    y = max(y1, min(y, y2))
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
    print(f"Clicked at ({x}, {y})")

def click_at(x, y):
    """Click at specific coordinates with human-like movement."""
    smooth_mouse_move(x, y, duration=random.uniform(0.4, 0.8))
    if random.random() < 0.2:
        time.sleep(random.uniform(0.15, 0.5))
    pyautogui.click()
    time.sleep(random.uniform(0.05, 0.25))

def type_like_human(text, is_filename=False):
    """Type text with human-like delays, pauses, and corrections."""
    for i, char in enumerate(text):
        # Context-aware pauses for filenames
        if is_filename and random.random() < 0.2 and i > 0:
            time.sleep(random.uniform(0.4, 1.0))  # Hesitation for filenames
        elif random.random() < 0.08 and i > 0:
            time.sleep(random.uniform(0.3, 0.9))
        
        # Simulate typos
        if not is_filename and random.random() < 0.015:
            wrong_char = random.choice(string.ascii_letters)
            pyautogui.write(wrong_char)
            time.sleep(random.uniform(0.1, 0.4))
            pyautogui.press('backspace')
            time.sleep(random.uniform(0.05, 0.2))
        
        # Simulate double key press
        if random.random() < 0.02:
            pyautogui.write(char)
            time.sleep(random.uniform(0.05, 0.1))
            pyautogui.press('backspace')
        
        pyautogui.write(char)
        # Variable typing speed
        if random.random() < 0.35:
            time.sleep(random.uniform(0.02, 0.08))
        else:
            time.sleep(random.uniform(0.07, 0.3))
    print(f"Typed: {text}")

def press_key_random_times(key, min_times, max_times, min_sleep, max_sleep):
    """Press a key randomly with human-like delays."""
    times = random.randint(min_times, max_times)
    for _ in range(times):
        pyautogui.press(key)
        random_sleep(min_sleep, max_sleep)
    return times

def generate_random_name(min_length, max_length):
    """Generate a random name with consonant-vowel pattern."""
    length = random.randint(min_length, max_length)
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    name = "".join(random.choice(consonants) + random.choice(vowels) for _ in range(length // 2))
    return name[:length]

def random_word(min_len, max_len):
    """Generate a random word (unchanged logic)."""
    length = random.randint(min_len, max_len)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

# Script execution
random_click(71, 180, 81, 192)
random_sleep(3, 4)
random_click(1139, 175, 1174, 190)
time.sleep(1)
random_click(1151, 223, 1301, 236)
random_sleep(4, 5)
random_click(515, 424, 659, 429)
random_sleep(1, 1.5)
subprocess.run(["python3", "click.py"])
time.sleep(1)
# Type a random name
name1 = generate_random_name(7, 9)
type_like_human(name1)

random_sleep(0.7, 1)
random_click(65, 287, 239, 480)
time.sleep(0.5)
press_key_random_times('down', 13, 15, 0.35, 0.5)
random_click(917, 425, 1013, 433)
random_sleep(4, 5)
random_click(10, 310, 62, 493)
time.sleep(2)
pyautogui.press('down')
time.sleep(2.5)
