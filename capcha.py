import pyautogui
import time

time.sleep(1)
# Step-by-step actions
def perform_actions():
    # Sleep for 1 second
    time.sleep(1)
    
    # Write the first URL
    pyautogui.typewrite("https://chromewebstore.google.com/detail/captchasonic-automatic-ca/dkkdakdkffippajmebplgnpmijmnejlh")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(5)
    
    # Perform the series of clicks
    pyautogui.click(1122, 238)
    time.sleep(2.5)
    pyautogui.click(815, 256)
    time.sleep(4)
    pyautogui.click(1255, 480)
    time.sleep(2)
    pyautogui.click(1257, 64)
    time.sleep(2)
    pyautogui.click(1194, 225)
    time.sleep(1.7)
    pyautogui.click(1257, 64)
    time.sleep(1.8)
    pyautogui.click(1217, 62)
    time.sleep(1.8)
    pyautogui.click(1015, 151)
    time.sleep(1)
    # Select all and paste
    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.5)
    pyautogui.write('sonic_45edd319c381d0211a034e3b38f03af39c60')
    time.sleep(1.5)
    
    # Continue with the next set of actions
    pyautogui.click(1217, 61)
    time.sleep(2)
    pyautogui.click(294, 18)
    time.sleep(1)
    pyautogui.click(256, 21)
    time.sleep(1)
    pyautogui.click(522, 63)
    time.sleep(1)

# Run the script
perform_actions()
