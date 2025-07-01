import pyautogui
import random
import time

def random_click(x1, y1, x2, y2):
    """Performs a random click within the given rectangular area."""
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)
    pyautogui.moveTo(x, y, duration=random.uniform(0.3, 0.7))  # Simulate natural movement
    pyautogui.click()
    print(f"Clicked at ({x}, {y})")

def random_sleep(min_sec, max_sec):
    """Sleeps for a random time between min_sec and max_sec seconds."""
    sleep_time = random.uniform(min_sec, max_sec)
    time.sleep(sleep_time)
    print(f"Slept for {sleep_time:.2f} seconds")

# Execute the sequence of clicks with randomization
random_click(111, 182, 168, 188)
random_sleep(3, 3)

random_click(366, 485, 967, 604)
random_sleep(0.5, 0.5)

random_click(104, 406, 864, 591)
random_sleep(2, 4)

random_click(118, 228, 193, 235)
random_sleep(2, 2)

random_click(1004, 532, 1105, 593)
random_sleep(0.5, 0.5)
