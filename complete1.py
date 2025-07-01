import pyautogui
import time
import random
import string

time.sleep(2)
# Helper functions
def human_typing(text):
    """Simulate human-like typing."""
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(random.uniform(0.05, 0.15))

def random_click_in_area(top_left, bottom_right):
    """Perform a random click within a rectangular area."""
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.click(x, y)

def generate_random_year(start=1990, end=2002):
    """Generate a random year."""
    return str(random.randint(start, end))

# Continue actions
def continue_actions():
    # Random click in specific area
    random_click_in_area((515, 279), (616, 294))
    time.sleep(random.uniform(0.5, 1))

    for _ in range(random.randint(1, 10)):
        pyautogui.press('down')
        time.sleep(random.uniform(0.2, 0.28))
    time.sleep(random.uniform(0.5, 1))
    pyautogui.press('enter')
    time.sleep(random.uniform(0.5, 1))

    # Random click in specific area
    random_click_in_area((665, 276), (727, 294))
    time.sleep(random.uniform(0.5, 1))

    for _ in range(random.randint(1, 27)):
        pyautogui.press('down')
        time.sleep(random.uniform(0.2, 0.28))
    time.sleep(random.uniform(0.5, 1))
    pyautogui.press('enter')
    time.sleep(random.uniform(0.5, 1))


    # Random click in specific area
    random_click_in_area((777, 281), (844, 291))
    time.sleep(random.uniform(0.5, 1))

    # Write random year
    random_year = generate_random_year()
    human_typing(random_year)
    time.sleep(1)
    # Random click in specific area
    random_click_in_area((525, 473), (832, 486))
    time.sleep(random.uniform(5, 6.5))

# Run both parts
if __name__ == "__main__":
    area1 = ((86, 230), (322, 421))
    area2 = ((1005, 258), (1282, 492))
    chosen_area = random.choice([area1, area2])
    for _ in range(random.randint(1, 4)):
        random_click_in_area(*chosen_area)
        time.sleep(random.uniform(0.5, 1))

    time.sleep(random.uniform(1, 2))

    # Randomly press down arrow 4-6 times with short delay
    for _ in range(random.randint(5, 7)):
        pyautogui.press('down')
        time.sleep(random.uniform(0.5, 0.8))

    continue_actions()  # Call the second part
