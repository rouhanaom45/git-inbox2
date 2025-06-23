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
time.sleep(1)

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

def generate_random_name():
    """Generate a random name (unchanged logic)."""
    name = ''.join(random.choice(string.ascii_lowercase) + random.choice("aeiou") for _ in range(random.randint(4, 5)))
    return name + str(random.randint(10, 99))

def generate_random_password():
    """Generate a random password (unchanged logic)."""
    length = random.randint(9, 11)
    characters = string.ascii_letters + string.digits + ",;!:@."
    return ''.join(random.choice(characters) for _ in range(length))

# Step-by-step script
time.sleep(1.5)
subprocess.run(["bash", "profile1.sh"])
time.sleep(4.5)
smooth_mouse_move(478, 44, duration=random.uniform(0.4, 0.8))
if random.random() < 0.2:
    time.sleep(random.uniform(0.15, 0.5))
pyautogui.click()
time.sleep(1)
smooth_mouse_move(502, 83, duration=random.uniform(0.4, 0.8))
if random.random() < 0.2:
    time.sleep(random.uniform(0.15, 0.5))
pyautogui.click()
time.sleep(1)
pyautogui.write('https://account.proton.me/mail/signup?mode=sps&ref=mailhero')
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(8)
pyautogui.click(96, 83)
time.sleep(7)

# Random click within one of two areas
if random.choice([True, False]):
    random_click_within_rect((44, 266), (180, 450))
else:
    random_click_within_rect((1142, 255), (1323, 471))

random_wait(1, 2)
press_count = random.randint(5, 6)

for i in range(press_count):
    pyautogui.press('down')
    time.sleep(random.uniform(0.3, 0.4))

random_wait(1, 2)
random_click_within_rect((124, 512), (347, 600))
random_wait(0.5, 1.2)
press_count = random.randint(16, 17)

for i in range(press_count):
    pyautogui.press('down')
    time.sleep(random.uniform(0.3, 0.4))

random_wait(1, 2)
random_click_within_rect((124, 159), (596, 164))
random_wait(0.5, 1.2)
# Write a random name
random_human_typing(generate_random_name())
random_wait(0.8, 1.4)

random_click_within_rect((661, 159), (756, 167))
random_wait(1, 1.5)
random_click_within_rect((670, 200), (770, 238))
random_wait(0.8, 1.4)
random_click_within_rect((118, 244), (650, 251))
random_wait(0.5, 1)

# Write a random password
password = generate_random_password()
random_human_typing(password, is_password=True)
random_wait(1, 2)

random_click_within_rect((114, 288), (528, 295))
random_wait(1, 2)
# Rewrite the same password
random_human_typing(password, is_password=True)
time.sleep(1)

random_click_within_rect((356, 346), (526, 361))
random_wait(5, 6.5)
smooth_mouse_move(648, 293, duration=random.uniform(0.4, 0.8))
if random.random() < 0.2:
    time.sleep(random.uniform(0.15, 0.5))
pyautogui.click()
time.sleep(1)
random_click_within_rect((862, 211), (868, 219))
random_wait(5, 5.6)

subprocess.run(["python3", "bad-traffic.py"])
time.sleep(1)

random_click_within_rect((722, 224), (960, 237))
random_wait(1.5, 2.4)
random_click_within_rect((368, 394), (767, 407))
random_wait(1.5, 2.0)

subprocess.run(["python3", "get-email-adress.py"])
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(random.uniform(0.5, 1))
random_click_within_rect((435, 483), (808, 502))
random_wait(6.5, 7.5)
smooth_mouse_move(1079, 628, duration=random.uniform(0.4, 0.8))
if random.random() < 0.2:
    time.sleep(random.uniform(0.15, 0.5))
pyautogui.click()
time.sleep(1)
smooth_mouse_move(537, 629, duration=random.uniform(0.4, 0.8))
if random.random() < 0.2:
    time.sleep(random.uniform(0.15, 0.5))
pyautogui.click()
time.sleep(1)
smooth_mouse_move(96, 62, duration=random.uniform(0.4, 0.8))
if random.random() < 0.2:
    time.sleep(random.uniform(0.15, 0.5))
pyautogui.click()
time.sleep(2)
