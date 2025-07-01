import pyautogui
import time
import random
import string
import subprocess
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

def generate_random_password(length=9):
    """Generate a random password with mixed characters."""
    chars = string.ascii_letters + string.digits + ",;!:@."
    return ''.join(random.choices(chars, k=length))

# Main function
def perform_actions():
    # Write "www.outlook.com"
    human_typing("www.outlook.com")
    time.sleep(0.5)

    # Press Enter
    pyautogui.press('enter')
    time.sleep(15)
    subprocess.run(["python3", "look1.py"])
    # Random clicks in one of two rectangular areas
    area1 = ((996, 280), (1289, 507))
    area2 = ((106, 242), (396, 435))
    chosen_area = random.choice([area1, area2])
    for _ in range(random.randint(1, 4)):
        random_click_in_area(*chosen_area)
        time.sleep(random.uniform(1, 2))


    # Random click in specific area
    random_click_in_area((227, 572), (354, 591))
    time.sleep(random.uniform(9, 11))
    subprocess.run(["python3", "look2.py"]) 
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'shift', 'tab')
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1.5)

# Run the sequence
if __name__ == "__main__":
    perform_actions()

