import pyautogui
import time
import pyperclip  # For clipboard handling
import subprocess


time.sleep(2)
# Function to write clipboard content
def write_clipboard_content():
    clipboard_content = pyperclip.paste()  # Retrieve the clipboard content
    if clipboard_content:  # Check if clipboard is not empty
        for char in clipboard_content:
            pyautogui.typewrite(char)  # Simulate typing each character
            time.sleep(0.05)  # Small delay to mimic human typing
    else:
        print("Clipboard is empty. Please copy something before running the script.")



time.sleep(1.5)
subprocess.run(["bash", "profile1.sh"])
time.sleep(11)
pyautogui.click(478, 44)
time.sleep(1)

# Function to perform the sequence of actions
def perform_actions():
    pyautogui.click(585, 82)
    time.sleep(0.5)
    pyautogui.write('https://addons.mozilla.org/nl/firefox/addon/omocaptcha-auto-solve-captcha/')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.click(758, 464)
    time.sleep(1)

    # Press down arrow twice with short sleep in between
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)

    # Click at (749, 600)
    pyautogui.click(720, 539)
    time.sleep(6)

    # Click at (1277, 484)
    pyautogui.click(1280, 326)
    time.sleep(4)

    # Click at (1314, 372)
    pyautogui.click(1316, 229)
    time.sleep(4)

    # Click at (1312, 218)
    pyautogui.click(1307, 86)
    time.sleep(1)

    # Click at (1297, 315)
    pyautogui.click(1301, 173)
    time.sleep(1)

    # Click at (1010, 382)
    pyautogui.click(1013, 243)
    time.sleep(2.5)

    # Click at (1305, 218)
    pyautogui.click(1306, 83)
    time.sleep(3)

    # Click at (1132, 396)
    pyautogui.click(1124, 304)
    time.sleep(1)

    # Press Ctrl + A
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(2)

    # Write clipboard content
    write_clipboard_content()
    time.sleep(3)

    # Click at (1308, 221)
    pyautogui.click(1303, 83)
    time.sleep(2)

    # Click at (291, 179)
    pyautogui.click(933, 41)
    time.sleep(1)
    pyautogui.click(539, 40)
    time.sleep(1)

    # Click at (252, 178)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    pyautogui.click(252, 42)
    time.sleep(1.5)


# Run the sequence
if __name__ == "__main__":
    perform_actions()
