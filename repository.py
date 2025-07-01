import subprocess
import time
import pyautogui

for i in range(5):
    print(f"Running complete.py (iteration {i + 1})...")
    subprocess.run(["python", "complete.py"])
    time.sleep(2)


time.sleep(1.5)
pyautogui.hotkey('ctrl', 't')
time.sleep(1)
pyautogui.hotkey('ctrl', 'shift', 'tab')
time.sleep(1.3)
pyautogui.hotkey('ctrl', 'w')
time.sleep(1.2)
pyautogui.click(1305, 83)
time.sleep(2)
pyautogui.click(1094, 273)
time.sleep(2)
pyautogui.click(1305, 83)
time.sleep(2)

print("All runs completed.")
