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

def generate_random_password(length=9):
    """Generate a random password with mixed characters."""
    chars = string.ascii_letters + string.digits + ",;!:@."
    return ''.join(random.choices(chars, k=length))

# Main function
def perform_actions():
    # Write "www.outlook.com"
    pyautogui.click(498, 82)
    time.sleep(0.5)
    human_typing("www.outlook.com")
    time.sleep(0.5)

    # Press Enter
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.click(934, 194)
    time.sleep(1)
    subprocess.run(["python3", "look1.py"])
    try:
       tab_button_location = pyautogui.locateCenterOnScreen('update_button.png', confidence=0.8)
       if tab_button_location is not None:
           print("Tab button detected, clicking at (1342, 125)...")
           pyautogui.click(891, 190)
           time.sleep(2)
           pyautogui.click(98, 84)
           time.sleep(4)
       else:
           print("Tab button not detected, proceeding to Step 1...")
    except Exception as e:
        print(f"Error detecting tab button: {e}")
        print("Proceeding to Step 1...")
    time.sleep(1)
    subprocess.run(["python3", "look1.py"])
    time.sleep(1)
    area1 = ((996, 280), (1289, 507))
    area2 = ((106, 242), (396, 435))
    chosen_area = random.choice([area1, area2])
    for _ in range(random.randint(1, 4)):
        random_click_in_area(*chosen_area)
        time.sleep(random.uniform(1, 2))

    # Random click in specific area
    random_click_in_area((227, 572), (354, 591))
    time.sleep(0.3)
    random_click_in_area((227, 572), (354, 591))
    time.sleep(random.uniform(9, 11))
    subprocess.run(["python3", "look2.py"]) 
    # Click at (251, 180)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 'shift', 'tab')
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 'shift', 'tab')
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1.5)
    subprocess.run(["python3", "repeat.py"])
    time.sleep(1)
    # Random click in specific areas
    random_click_in_area((718, 424), (840, 441))
    time.sleep(random.uniform(1, 1.5))
    random_click_in_area((724, 465), (843, 494))
    time.sleep(random.uniform(0.5, 1))
    random_click_in_area((521, 427), (661, 437))
    time.sleep(random.uniform(0.5, 1))

    # Write a random name (6-8 characters)
    random_name = generate_random_name(random.randint(6, 8)) + str(random.randint(10, 99))
    human_typing(random_name)
    time.sleep(1)

    # Random click in specific area
    random_click_in_area((522, 499), (836, 514))
    time.sleep(random.uniform(7, 9))

    # Write a random password (9-11 characters)
    random_password = generate_random_password(random.randint(9, 11))
    human_typing(random_password)
    time.sleep(random.uniform(2, 3))
    # Random click in specific area
    random_click_in_area((96, 228), (313, 447))
    time.sleep(random.uniform(1, 1.5))

    # Press Down arrow 5-7 times with short sleep
    for _ in range(random.randint(5, 7)):
        pyautogui.press('down')
        time.sleep(random.uniform(0.5, 0.8))

    # Random click in specific area
    random_click_in_area((522, 471), (825, 486))
    time.sleep(random.uniform(4, 5))
    pyautogui.click(647, 299)
    time.sleep(1)

    subprocess.run(["python3", "complete1.py"]) 

# Run the sequence
if __name__ == "__main__":
    perform_actions()
