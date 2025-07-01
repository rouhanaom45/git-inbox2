import pyautogui
import subprocess
import time


while True:
    
    time.sleep(1.5)
    pyautogui.click(428, 83)
    time.sleep(0.5)
    pyautogui.press('delete')
    time.sleep(0.5)
    pyautogui.write('https://outlook.live.com/mail/0/')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(12)

    result = subprocess.run(["python", "verif1.py"])
    if result.returncode == 0:
        print("verif1.py succeeded. Continuing with remaining steps...")
        break  # Exit loop and continue with final step
    else:
        print("verif1 failed. Restarting confirm.py...")
        continue  # Restart the loop

# Final step after create.py succeeds
time.sleep(1.5)
subprocess.run(["python", "verif2.py"])

# Step 7: Sleep for 1.5 seconds
time.sleep(1.5)

# Step 8: Run verif3.py
subprocess.run(["python", "verif3.py"])

# Step 9: Sleep for 1 second
time.sleep(1)
time.sleep(1)
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

subprocess.run(["python", "continue.py"])
print("confirm.py finished successfully.")
time.sleep(1)
