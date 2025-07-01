import pyautogui
import time
import random
import string
import subprocess
time.sleep(2)

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

def generate_random_name(length=6):
    """Generate a random name with alternating consonant and vowel."""
    vowels = "aeiou"
    consonants = "".join(set(string.ascii_lowercase) - set(vowels))
    name = ""
    for _ in range(length):
        name += random.choice(consonants) + random.choice(vowels)
    return name[:length]



random_click_in_area((952, 183), (1300, 431))
time.sleep(random.uniform(1, 2))

for _ in range(random.randint(6, 7)):
        pyautogui.press('down')
        time.sleep(random.uniform(0.5, 0.8))
time.sleep(1)
# Random click in specific area
random_click_in_area((522, 208), (819, 216))
time.sleep(random.uniform(1, 2))

# Write another random name (6-8 characters)
random_name = generate_random_name(random.randint(6, 8))
human_typing(random_name)
time.sleep(random.uniform(0.5, 1))

# Random click in specific area
random_click_in_area((517, 273), (814, 284))
time.sleep(random.uniform(1, 2))

# Write another random name (6-8 characters)
random_name = generate_random_name(random.randint(6, 8))
human_typing(random_name)
time.sleep(random.uniform(0.5, 1))

random_click_in_area((517, 471), (826, 485))
time.sleep(random.uniform(4, 5))



