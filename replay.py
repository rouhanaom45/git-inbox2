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
    # Add rare distraction pause
    elif random.random() < 0.05:  # 5% chance for a longer distraction
        base_time += random.uniform(3.0, 5.0)
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
    
    # Calculate distance for pause logic
    distance = math.sqrt((target_x - start_x) ** 2 + (target_y - start_y) ** 2)
    
    for i in range(steps + 1):
        t = i / steps
        # Quadratic Bezier curve for natural movement
        x = (1 - t) ** 2 * start_x + 2 * (1 - t) * t * control_x + t ** 2 * target_x
        y = (1 - t) ** 2 * start_y + 2 * (1 - t) * t * control_y + t ** 2 * target_y
        # Add micro-jitters to simulate hand tremors
        x += random.uniform(-3, 3) if random.random() < 0.4 else 0
        y += random.uniform(-3, 3) if random.random() < 0.4 else 0
        pyautogui.moveTo(x, y, duration=0.016, tween=pyautogui.easeInOutQuad)
        # Add rare mid-movement pause for long movements
        if distance > 200 and random.random() < 0.05 and i == steps // 2:
            time.sleep(random.uniform(0.1, 0.3))
    
    # Simulate overshoot and correction for human imprecision
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
        # Double-check cursor position for small rectangles
        if random.random() < 0.1:
            smooth_mouse_move(x + random.randint(-5, 5), y + random.randint(-5, 5), duration=0.1)
            time.sleep(random.uniform(0.05, 0.15))
            smooth_mouse_move(x, y, duration=0.15)
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
    
    # Simulate pre-click hesitation or cursor adjustment
    if random.random() < 0.2:
        time.sleep(random.uniform(0.15, 0.5))
        # Small cursor adjustment to mimic human precision
        pyautogui.moveRel(random.randint(-5, 5), random.randint(-5, 5), duration=0.1)
    
    # Rare accidental double-click
    if random.random() < 0.03:
        pyautogui.click()
        time.sleep(random.uniform(0.05, 0.1))
        pyautogui.moveRel(random.randint(-5, 5), random.randint(-5, 5), duration=0.1)
    
    pyautogui.click()
    # Post-click drift or pause to mimic human behavior
    if random.random() < 0.1:
        pyautogui.moveRel(random.randint(-10, 10), random.randint(-10, 10), duration=0.1)
    time.sleep(random.uniform(0.05, 0.25))

def random_human_typing(text, is_password=False):
    """Simulate human typing with realistic delays, pauses, and corrections."""
    # Simulate thinking before typing sensitive input
    if is_password and random.random() < 0.1:
        time.sleep(random.uniform(0.5, 1.5))
    
    for i, char in enumerate(text):
        # Context-aware pauses (longer for passwords or after punctuation)
        if (is_password or char in ",.!;@") and random.random() < 0.2 and i > 0:
            time.sleep(random.uniform(0.4, 1.0))  # Hesitation for sensitive input or punctuation
        elif random.random() < 0.08 and i > 0:  # Normal hesitation
            time.sleep(random.uniform(0.3, 0.9))
        
        # Simulate occasional typos (more likely for non-passwords)
        if not is_password and random.random() < 0.015:
            wrong_char = random.choice(string.ascii_letters)
            pyautogui.write(wrong_char)
            time.sleep(random.uniform(0.1, 0.4))
            pyautogui.press('backspace')
            time.sleep(random.uniform(0.05, 0.2))
            # Rare double typo
            if random.random() < 0.05:
                wrong_char2 = random.choice(string.ascii_letters)
                pyautogui.write(wrong_char2)
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
    random_click_within_rect((30, 322), (163, 558))
else:
    random_click_within_rect((1173, 279), (1296, 556))

random_wait(1, 2)
press_count = random.randint(10, 12)

for i in range(press_count):
    # Occasionally skip a press to mimic human inconsistency
    if random.random() < 0.05:
        time.sleep(random.uniform(0.1, 0.2))
        continue
    pyautogui.press('down')
    time.sleep(random.uniform(0.3, 0.4) * random.uniform(0.8, 1.2))  # Slight speed variation

random_wait(1, 2)
random_click_within_rect((255, 160), (587, 166))
random_wait(0.5, 1.2)

# Write a random name
random_human_typing(generate_random_name())
random_wait(0.8, 1.4)

random_click_within_rect((615, 159), (689, 169))
random_wait(1, 1.5)
random_click_within_rect((625, 199), (724, 238))
random_wait(0.8, 1.4)
random_click_within_rect((252, 244), (574, 255))
random_wait(0.5, 1)

# Write a random password
password = generate_random_password()
random_human_typing(password, is_password=True)
random_wait(1, 2)

random_click_within_rect((35, 286), (140, 461))
random_wait(1, 2)
for _ in range(random.randint(5, 6)):
    # Occasionally accelerate scrolling
    if random.random() < 0.1:
        time.sleep(random.uniform(0.05, 0.15))
    else:
        time.sleep(random.uniform(0.1, 0.3))
    pyautogui.press("down")

random_click_within_rect((247, 271), (589, 280))
random_wait(1, 2)
# Rewrite the same password
random_human_typing(password, is_password=True)
time.sleep(1)

random_click_within_rect((395, 327), (586, 339))
random_wait(5, 6.5)
smooth_mouse_move(648, 293, duration=random.uniform(0.4, 0.8))
if random.random() < 0.2:
    time.sleep(random.uniform(0.15, 0.5))
pyautogui.click()
time.sleep(1)
random_click_within_rect((862, 211), (868, 219))
random_wait(5, 5.6)
