import pyautogui
import time
import subprocess

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
            pyautogui.hotkey('ctrl', 't')
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'shift', 'tab')
            time.sleep(1.3)
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(1.2)
            pyautogui.click(418, 83)
            time.sleep(0.7)
            pyautogui.write('www.github.com')
            time.sleep(0.5)
            pyautogui.press("enter")
            time.sleep(12)


def perform_additional_tasks():
    """Define tasks to perform after the web button is detected."""
    print("Performing additional tasks...")
    time.sleep(1)
    print("All tasks completed.")

if __name__ == "__main__":
    # Step 1: Detect the web button via the detection script
    detect_web_button('trak3.py')

    # Step 2: Perform additional tasks after the web button is detected
    perform_additional_tasks()
