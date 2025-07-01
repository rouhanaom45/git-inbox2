import pyautogui
import subprocess
import time


while True:
    
    time.sleep(1.5)
    pyautogui.click(438, 61)
    time.sleep(0.5)
    pyautogui.press('delete')
    time.sleep(0.5)
    pyautogui.write('https://email.inbox.eu/mailbox')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(7)

    result = subprocess.run(["python", "verif11.py"])
    if result.returncode == 0:
        print("verif11.py succeeded. Continuing with remaining steps...")
        break  # Exit loop and continue with final step
    else:
        print("verif11 failed. Restarting confirm.py...")
        continue  # Restart the loop

# Final step after create.py succeeds
time.sleep(1.5)
subprocess.run(["python", "verif22.py"])

# Step 7: Sleep for 1.5 seconds
time.sleep(1.5)

# Step 8: Run verif3.py
subprocess.run(["python", "clipboard0.py"])

# Step 9: Sleep for 1 second
time.sleep(1)
pyautogui.hotkey('ctrl', 'w')
time.sleep(1)
