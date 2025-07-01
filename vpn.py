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

def perform_actions():
    pyautogui.click(585, 82)
    time.sleep(0.5)
    pyautogui.write('https://addons.mozilla.org/nl/firefox/addon/nordvpn-proxy-extension/')
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
    pyautogui.click(716, 583)
    time.sleep(4)

    # Click at (1277, 484)
    pyautogui.click(1234, 412)
    time.sleep(2)
    pyautogui.click(1318, 246)
    time.sleep(2)
    pyautogui.click(214, 264)
    time.sleep(1)
    pyautogui.scroll(-300)
    time.sleep(1)
    pyautogui.click(662, 571)
    time.sleep(2)
    pyautogui.click(1268, 84)
    time.sleep(1.5)
    pyautogui.click(1259, 180)
    time.sleep(1.5)
    pyautogui.click(981, 253)
    time.sleep(1.5)
    pyautogui.click(1303, 83)
    time.sleep(1.5)
    pyautogui.click(1105, 577)
    time.sleep(10)
    pyautogui.write('drogo3585@gmail.com')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(8.5)
    pyautogui.write('78455216bB')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(8.5)
    pyautogui.click(1172, 66)
    time.sleep(2)
    pyautogui.click(1306, 84)
    time.sleep(1.5)
    pyautogui.click(1276, 331)
    time.sleep(1.5)
    write_clipboard_content()
    time.sleep(1.5)
    pyautogui.press('tab')  # Press the Tab key
    time.sleep(1.3)         # Sleep for 1.3 seconds
    pyautogui.press('enter')  # Press the Enter key
    time.sleep(10)
    pyautogui.click(942, 116)
    time.sleep(1.3)
    pyautogui.click(1306, 84)
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    pyautogui.click(252, 42)
    time.sleep(1.5)    
# Run the sequence
if __name__ == "__main__":
    perform_actions()
