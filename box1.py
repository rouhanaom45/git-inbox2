import pyautogui
import time
import random
import subprocess
import string

def human_type(text, interval_range=(0.05, 0.15)):
    for char in text:
        pyautogui.write(char)
        time.sleep(random.uniform(*interval_range))

def random_click(top_left, bottom_right):
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.moveTo(x + random.uniform(-2, 2), y + random.uniform(-2, 2), duration=random.uniform(0.1, 0.4))
    pyautogui.click()

def generate_patterned_name(length=6, with_digits=False):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    name = ''
    for _ in range(length // 2):
        name += random.choice(consonants) + random.choice(vowels)
    if len(name) < length:
        name += random.choice(vowels)
    if with_digits:
        name += f"{random.randint(10, 99)}"
    return name[:length] + (name[length:] if with_digits else '')

def generate_password(length=10):
    chars = string.ascii_letters + string.digits + ",;!:@."
    return ''.join(random.choice(chars) for _ in range(length))

# Start the automation
pyautogui.write("https://www.inbox.eu/en/signup/personal")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(7)

# Run oki.py
subprocess.run(["python", "oki.py"])
time.sleep(1)
random_click((79, 147), (315, 427))
time.sleep(random.uniform(0.5, 1.0))
pyautogui.click(1040, 564)
time.sleep(2.5)
subprocess.run(["python", "oki.py"])
time.sleep(1)
random_click((79, 147), (315, 427))
time.sleep(random.uniform(0.5, 1.0))

for _ in range(random.randint(6, 8)):
    pyautogui.press("up")
    time.sleep(0.35)

time.sleep(1)
# 1st Click
random_click((461, 331), (710, 334))
time.sleep(random.uniform(0.5, 1.0))

# Random name + 2 digits
name_with_digits = generate_patterned_name(random.randint(6, 8), with_digits=True)
human_type(name_with_digits)
time.sleep(random.uniform(1.0, 2.0))

email = name_with_digits + "@inbox.eu"

with open("email1.txt", "w", encoding="utf-8") as f:
    f.write(email)

time.sleep(1)
# 4th Click
random_click((502, 427), (853, 448))
time.sleep(random.uniform(4.7, 5.1))
random_click((564, 415), (842, 434))
time.sleep(random.uniform(3.7, 4.0))
random_click((456, 245), (795, 256))
time.sleep(random.uniform(0.7, 1.0))
# Random password
password = generate_password(random.randint(9, 11))
human_type(password)
time.sleep(random.uniform(1.0, 2.0))
random_click((460, 341), (838, 346))
time.sleep(random.uniform(0.7, 1.0))
human_type(password)
time.sleep(random.uniform(1.0, 2.0))
random_click((448, 432), (635, 438))
time.sleep(random.uniform(0.7, 1.0))
# Random name
name1 = generate_patterned_name(random.randint(6, 8))
human_type(name1)
time.sleep(random.uniform(1.2, 2.3))

# 5th Click
random_click((706, 432), (866, 441))
time.sleep(random.uniform(0.7, 1.0))

# Random name
name2 = generate_patterned_name(random.randint(6, 8))
human_type(name2)
time.sleep(random.uniform(1.2, 2.3))
random_click((434, 483), (439, 486))
time.sleep(random.uniform(1.0, 1.5))
random_click((434, 508), (440, 515))
time.sleep(random.uniform(1.0, 1.5))
random_click((468, 583), (826, 603))
time.sleep(random.uniform(3.7, 4.0))
random_click((63, 184), (294, 452))
time.sleep(random.uniform(0.7, 1.0))
# Press down arrow 68 times
for _ in range(random.randint(6, 8)):
    pyautogui.press("down")
    time.sleep(0.35)

time.sleep(1)

random_click((519, 447), (841, 459))
time.sleep(random.uniform(3.0, 3.6))

# 9th Click
random_click((525, 541), (825, 560))
time.sleep(random.uniform(5.0, 6.0))

pyautogui.click(1134, 364)
time.sleep(1.3)

random_click((43, 305), (149, 537))
time.sleep(random.uniform(0.7, 1.0))

random_click((699, 381), (1038, 399))
time.sleep(random.uniform(1.7, 2.2))

pyautogui.press('down')
time.sleep(random.uniform(0.7, 0.9))
pyautogui.press('enter')
time.sleep(random.uniform(1.5, 1.9))


random_click((1033, 525), (1097, 542))
time.sleep(random.uniform(2.7, 3.6))

random_click((992, 505), (1089, 521))
time.sleep(random.uniform(2.5, 3.3))

subprocess.run(["python", "finisho.py"])
time.sleep(1)
pyautogui.click(95, 61)
time.sleep(4)
