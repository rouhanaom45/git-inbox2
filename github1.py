import pyautogui
import random
import time
import string
import sys
import subprocess
import math

# Enable fail-safe to prevent runaway scripts
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.03  # Small base pause for smoother actions

# Initial delay to allow user to prepare
time.sleep(2)

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

def random_human_typing(text, is_password=False):
    """Type text with human-like delays, pauses, and corrections."""
    for i, char in enumerate(text):
        # Context-aware pauses for passwords or URLs
        if is_password and random.random() < 0.2 and i > 0:
            time.sleep(random.uniform(0.4, 1.0))  # Hesitation for sensitive input
        elif random.random() < 0.08 and i > 0:
            time.sleep(random.uniform(0.3, 0.9))
        
        # Simulate typos
        if not is_password and random.random() < 0.015:
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

def generate_password():
    """Generate a random password (unchanged logic)."""
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice("@.,;!:")
    all_chars = string.ascii_letters + string.digits + "@.,;!:"
    remaining_chars = random.choices(all_chars, k=random.randint(5, 8))
    password = list(lower + upper + digit + special + ''.join(remaining_chars))
    random.shuffle(password)
    return ''.join(password)

def random_string(length, chars):
    """Generate a random string (unchanged logic)."""
    return ''.join(random.choice(chars) for _ in range(length))

# Step 1: Type website and press Enter
time.sleep(3)
subprocess.run(["python3", "omocaptcha.py"])
time.sleep(1)
subprocess.run(["python3", "get-city.py"])
time.sleep(1)
subprocess.run(["python3", "vpn.py"])
time.sleep(1)
subprocess.run(["python3", "fingerprint.py"])
time.sleep(1)
smooth_mouse_move(411, 85, duration=random.uniform(0.4, 0.8))
if random.random() < 0.2:
    time.sleep(random.uniform(0.15, 0.5))
pyautogui.click()
time.sleep(0.5)
random_human_typing("www.github.com")
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(15)
subprocess.run(["python3", "git1.py"])
time.sleep(1)

# Step 2: Detect the tab button using 'copilot_button.png'
try:
    tab_button_location = pyautogui.locateCenterOnScreen('copilot_button.png', confidence=0.8)
    if tab_button_location is not None:
        print("Copilot button detected, clicking at (1309, 264)...")
        smooth_mouse_move(1311, 174, duration=random.uniform(0.4, 0.8))
        if random.random() < 0.2:
            time.sleep(random.uniform(0.15, 0.5))
        pyautogui.click()
        time.sleep(2)
    else:
        print("Tab button not detected, proceeding to Step 1...")
except Exception as e:
    print(f"Error detecting tab button: {e}")
    print("Proceeding to Step 1...")

time.sleep(1)

# Step 3: Random clicks in one of two rectangles
rect1 = [(69, 320), (219, 536)]
rect2 = [(1132, 313), (1320, 501)]
chosen_rect = random.choice([rect1, rect2])
clicks = random.randint(1, 4)
for _ in range(clicks):
    random_click_in_rectangle(chosen_rect[0], chosen_rect[1])
    random_sleep(1, 2)

# Step 4: Click in specific rectangle
random_click_in_rectangle((1272, 184), (1321, 198))
random_sleep(12, 14)
subprocess.run(["python3", "get-email.py"])
time.sleep(1)
subprocess.run(["python3", "git2.py"])
time.sleep(1)

# Step 5: Detect the cookie button
try:
    cooki_button_location = pyautogui.locateCenterOnScreen('cooki_button.png', confidence=0.8)
    if cooki_button_location is not None:
        print("Cooki button detected, clicking at (1309, 264)...")
        time.sleep(0.7)
        smooth_mouse_move(cooki_button_location[0], cooki_button_location[1], duration=random.uniform(0.4, 0.8))
        if random.random() < 0.2:
            time.sleep(random.uniform(0.15, 0.5))
        pyautogui.click()
        time.sleep(2)
    else:
        print("cooki button not detected, proceeding to Step 1...")
except Exception as e:
    print(f"Error detecting cooki button: {e}")
    print("Proceeding to Step 1...")

time.sleep(1)

# Step 6: Click in another rectangle
random_click_in_rectangle((693, 260), (777, 357))
random_sleep(1, 2)

# Step 7: Press down arrow 3 times with delay
for _ in range(3):
    pyautogui.press('down')
    time.sleep(random.uniform(0.1, 0.3))

# Step 8: Click and write clipboard content
random_click_in_rectangle((817, 163), (1214, 171))
random_sleep(0.5, 1)
pyautogui.hotkey('ctrl', 'v')
random_sleep(0.5, 1)

# Step 9: Click and write random password
random_click_in_rectangle((813, 244), (1199, 254))
random_sleep(0.5, 1)
random_password = generate_password()
random_human_typing(random_password, is_password=True)
random_sleep(1, 2)

# Step 10: Click and write random name
random_click_in_rectangle((813, 359), (1219, 370))
random_sleep(0.5, 1)
name = ''.join(
    random.choice(string.ascii_lowercase) + random.choice('aeiou') for _ in range(random.randint(3, 4))
) + str(random.randint(10, 99))
random_human_typing(name)
random_sleep(2, 3)

random_click_in_rectangle((1272, 235), (1335, 341))
time.sleep(0.6)
for _ in range(4):
    pyautogui.press('down')
    time.sleep(random.uniform(0.1, 0.3))

time.sleep(0.7)

# Step 11: Final click and wait
random_click_in_rectangle((818, 456), (1228, 477))
random_sleep(3.5, 4.5)
random_click_in_rectangle((1273, 203), (1342, 408))
time.sleep(1)

# Step 12: Button detection loop
failed_attempts = 0
max_attempts = 10  # Exit after 10 consecutive failures

while True:
    time.sleep(1)
    try:
        button_location = pyautogui.locateCenterOnScreen('pass_button.png', confidence=0.8, grayscale=True)
        if button_location:
            random_click_in_rectangle((818, 456), (1228, 477))
            time.sleep(2)
            failed_attempts = 0  # Reset failure count when button is found
        else:
            failed_attempts += 1  # Increment failure count
    except pyautogui.ImageNotFoundException:
        failed_attempts += 1  # Increment failure count if image is not found

    if failed_attempts >= max_attempts:
        print("Button not found for 10 consecutive attempts. Exiting.")
        sys.exit()  # Fully exit after 10 consecutive failures
