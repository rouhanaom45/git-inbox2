import pyautogui
import time
import subprocess
# Sleep for 3 seconds before starting
time.sleep(3)
pyautogui.click(1219, 587)
time.sleep(2)
pyautogui.click(598, 264)
time.sleep(2)
pyautogui.click(1147, 567)
time.sleep(2)

# Click on (1338,111) then sleep 2 seconds
pyautogui.click(1338, 111)
time.sleep(2)

# Click on (294,23) then sleep 2 seconds
pyautogui.hotkey('ctrl', 't')
time.sleep(2)
# Sleep for 3 seconds before starting
time.sleep(3)
pyautogui.click(1219, 587)
time.sleep(2)
pyautogui.click(598, 264)
time.sleep(2)
pyautogui.click(1147, 567)
time.sleep(2)

# Click on (1338,111) then sleep 2 seconds
pyautogui.click(1338, 111)
time.sleep(2)

# Click on (256,20) then sleep 2 seconds
pyautogui.click(256, 20)
time.sleep(2)
pyautogui.click(241, 64)
time.sleep(1.5)
# Type "www.outlook.com", sleep 1 second, then press Enter
pyautogui.typewrite("www.outlook.com")
time.sleep(1)
pyautogui.press("enter")



# Sleep for 6 seconds to allow the page to load
time.sleep(6)
subprocess.run(["python3", "mark.py"])
time.sleep(1.5)
# Click on (294,23) again
pyautogui.hotkey('ctrl', 't')
time.sleep(2)
