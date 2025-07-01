import pyautogui
import time
import pyperclip  # For clipboard handling
import subprocess


time.sleep(2)

def perform_actions():
    pyautogui.click(585, 82)
    time.sleep(0.5)
    pyautogui.write('https://addons.mozilla.org/nl/firefox/addon/omocaptcha-auto-solve-captcha/')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(7.5)
    pyautogui.click(758, 464)
    time.sleep(1)

    # Press down arrow twice with short sleep in between
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)

    # Click at (749, 600)
    pyautogui.click(720, 539)
    time.sleep(4)

    # Click at (1277, 484)
    pyautogui.click(1280, 326)
    time.sleep(2)

    # Click at (1314, 372)
    pyautogui.click(1316, 229)
    time.sleep(2)

    # Click at (1312, 218)
    pyautogui.click(1307, 86)
    time.sleep(1)

    # Click at (1297, 315)
    pyautogui.click(1301, 173)
    time.sleep(1)
    pyautogui.click(1013, 243)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    pyautogui.click(252, 42)
    time.sleep(1.5)

if __name__ == "__main__":
    perform_actions()
