# main_script.py
import pyautogui
import time
import subprocess
import random


def random_click_in_area(top_left, bottom_right):
    """Perform a random click within a rectangular area."""
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.click(x, y)



def detect_web_button(script_name):
    """Run an external script to detect the web button and keep trying until successful."""
    while True:
        # Start the external detection script
        process = subprocess.Popen(['python3', script_name])
        process.wait()  # Wait for it to finish

        if process.returncode == 0:  # Success code indicates the button was found
            print(f"Web button detected and clicked by {script_name}. Proceeding with tasks...")
            return  # Exit the loop and proceed to next tasks
        else:
            print(f"Web button not detected by {script_name}. Retrying...")
            time.sleep(2)

def perform_additional_tasks():
    """Define tasks to perform after the web button is detected."""
    print("Performing additional tasks...")
    time.sleep(1) 
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.7)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.7)
    random_click_in_area((818, 293), (878, 351))
    time.sleep(0.7)
    subprocess.run(['python', 'clipboard1.py'])
    time.sleep(1)
    pyautogui.click(1339, 86)
    time.sleep(1)
    pyautogui.click(1127, 364)
    time.sleep(1.5)
    pyautogui.click(884, 237)
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(480, 41)
    time.sleep(1)
    subprocess.run(['python', 'email-inbox.py'])
    print("All tasks completed.")

if __name__ == "__main__":
    # Step 1: Detect the web button via the detection script
    random_click_in_area((62, 197), (264, 527))
    time.sleep(random.uniform(1, 1.5))
    for _ in range(random.randint(5, 7)):
        pyautogui.press('up')
        time.sleep(random.uniform(0.5, 0.8))

    detect_web_button('macro-found.py')

    # Step 2: Perform additional tasks after the web button is detected
    perform_additional_tasks()
