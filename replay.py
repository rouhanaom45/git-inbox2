import pyautogui
import random
import time
import string
import math
import subprocess

# Enable fail-safe to prevent runaway scripts
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.03  # Slightly reduced base pause for smoother actions

# Initial delay to allow user to prepare
time.sleep(3)

def random_wait(min_time, max_time):
    """Generate a random wait time with natural human variability."""
    base_time = random.uniform(min_time, max_time)
    # Add occasional longer pauses to simulate distraction or hesitation
    if random.random() < 0.15:  # 15% chance for a longer pause
        base_time += random.uniform(0.7, 2.0)
    # Rarely add a very brief pause to mimic quick human adjustments
    elif random.random() < 0.1:
        base_time *= random.uniform(0.5, 0.8)
    time.sleep(base_time)

def smooth_mouse_move(target_x, target_y, duration=0.5):
    """Move mouse with human-like path using Bezier curves and micro-jitters."""
    start_x, start_y = pyautogui.position()
    steps = int(duration * 60)  # 60 FPS for smooth movement
    # Introduce slight curve in path to mimic natural hand movement
    control_x = start_x + (target_x - start_x) * random.uniform(0.3, 0.7) + random.randint(-20, 20)
    control_y = start_y + (target_y - start_y) * random.uniform(0.3, 0.7) + random.randint(-20, 20)
    
    for i in range(steps + 1):
        t = i / steps
        # Quadratic Bezier curve for natural movement
        x = (1 - t) ** 2 * start_x + 2 * (1 - t) * t * control_x + t ** 2 * target_x
        y = (1 - t) ** 2 * start_y + 2 * (1 - t) * t * control_y + t ** 2 * target_y
        # Add micro-jitters to simulate hand tremors
        x += random.uniform(-3, 3) if random.random() < 0.4 else 0
        y += random.uniform(-3, 3) if random.random() < 0.4 else 0
        pyautogui.moveTo(x, y, duration=0.016, tween=pyautogui.easeInOutQuad)
    
    # Simulate overshoot and correction for human imprecision
    if random.random() < 0.25:
        overshoot_x = target_x + random.randint(-15, 15)
        overshoot_y = target_y + random.randint(-15, 15)
        pyautogui.moveTo(overshoot_x, overshoot_y, duration=0.1)
        time.sleep(random.uniform(0.05, 0.2))
        pyautogui.moveTo(target_x, target_y, duration=0.15)

def random_human_typing(text, is_password=False):
    """Simulate human typing with realistic delays, pauses, and corrections."""
    for i, char in enumerate(text):
        # Context-aware pauses (longer for passwords to mimic caution)
        if is_password and random.random() < 0.2 and i > 0:
            time.sleep(random.uniform(0.4, 1.0))  # Hesitation for sensitive input
        elif random.random() < 0.08 and i > 0:  # Normal hesitation
            time.sleep(random.uniform(0.3, 0.9))
        
        # Simulate occasional typos (more likely for non-passwords)
        if not is_password and random.random() < 0.015:
            wrong_char = random.choice(string.ascii_letters)
            pyautogui.write(wrong_char)
            time.sleep(random.uniform(0.1, 0.4))
            pyautogui.press('backspace')
            time.sleep(random.uniform(0.05, 0.2))
        
        # Simulate occasional double key press
        if random.random() < 0.02:
            pyautogui.write(char)
            time.sleep(random.uniform(0.05, 0.1))
            pyautogui.press('backspace')
        
        pyautogui.write(char)
        # Variable typing speed with bursts and slowdowns
        if random.random() < 0.35:  # 35% chance for faster typing
            time.sleep(random.uniform(0.02, 0.08))
        else:
            time.sleep(random.uniform(0.07, 0.3))

def random_click_within_rect(top_left, bottom_right):
    """Click within a rectangle with human-like movement and hesitation."""
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    # Add slight offset to avoid perfect clicks
    x += random.randint(-8, 8)
    y += random.randint(-8, 8)
    smooth_mouse_move(x, y, duration=random.uniform(0.4, 0.8))
    
    # Simulate pre-click hesitation or cursor adjustment
    if random.random() < 0.2:
        time.sleep(random.uniform(0.15, 0.5))
        # Small cursor adjustment to mimic human precision
        pyautogui.moveRel(random.randint(-5, 5), random.randint(-5, 5), duration=0.1)
    
    pyautogui.click()
    # Post-click drift or pause to mimic human behavior
    if random.random() < 0.1:
        pyautogui.moveRel(random.randint(-10, 10), random.randint(-10, 10), duration=0.1)
    time.sleep(random.uniform(0.05, 0.25))

def generate_random_name():
    """Generate a random name (unchanged from original logic)."""
    name = ''.join(random.choice(string.ascii_lowercase) + random.choice("aeiou") for _ in range(random.randint(4, 5)))
    return name + str(random.randint(10, 99))

def generate_random_password():
    """Generate a random password (unchanged from original logic)."""
    length = random.randint(9, 11)
    characters = string.ascii_letters + string.digits + ",;!:@."
    return ''.join(random.choice(characters) for _ in range(length))

# Random click within one of two areas
if random.choice([True, False]):
    random_click_within_rect((37, 306), (112, 416))
else:
    random_click_within_rect((1211, 393), (1312, 521))

random_wait(1, 2)
press_count = random.randint(14, 15)

for i in range(press_count):
    pyautogui.press('down')
    time.sleep(random.uniform(0.15, 0.35))  # Varied scrolling speed

random_wait(1, 2)
random_click_within_rect((238, 151), (569, 161))
random_wait(0.7, 1.2)

# Write a random name
random_human_typing(generate_random_name())
random_wait(1.2, 1.6)

random_click_within_rect((641, 156), (720, 162))
random_wait(1, 1.5)
random_click_within_rect((615, 193), (720, 234))
random_wait(0.8, 1.4)
random_click_within_rect((237, 241), (654, 250))
random_wait(0.5, 1)

# Write a random password
password = generate_random_password()
random_human_typing(password, is_password=True)
random_wait(1, 2)

random_click_within_rect((57, 178), (149, 460))
random_wait(1, 2)
for _ in range(random.randint(2, 3)):
    pyautogui.press("down")
    time.sleep(random.uniform(0.1, 0.35))  # Varied scrolling speed

random_click_within_rect((243, 271), (662, 278))
random_wait(1, 2)
# Rewrite the same password
random_human_typing(password, is_password=True)
time.sleep(1)

random_click_within_rect((383, 326), (568, 340))
random_wait(6, 7)
random_click_within_rect((859, 147), (868, 154))
random_wait(5, 5.6)
