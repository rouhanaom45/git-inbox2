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
            pyautogui.click(541, 82)
            time.sleep(0.5)
            pyautogui.press('delete')
            time.sleep(0.6)
            pyautogui.write("https://signup.live.com/signup?sru=https%3a%2f%2flogin.live.com%2foauth20_authorize.srf%3flc%3d1033%26client_id%3d9199bf20-a13f-4107-85dc-02114787ef48%26cobrandid%3dab0455a0-8d03-46b9-b18b-df2f57b9e44c%26mkt%3dEN-US%26opid%3dCAA35A05EF16B727%26opidt%3d1745589342%26uaid%3dd883df32e74de719ffb4be9bd13fe7c4%26contextid%3d2FE2EF1BDCE6CF0D%26opignore%3d1&mkt=EN-US&uiflavor=web&fl=dob%2cflname%2cwld&cobrandid=ab0455a0-8d03-46b9-b18b-df2f57b9e44c&client_id=9199bf20-a13f-4107-85dc-02114787ef48&uaid=d883df32e74de719ffb4be9bd13fe7c4&suc=9199bf20-a13f-4107-85dc-02114787ef48&fluent=2&lic=1")
            time.sleep(0.6)
            pyautogui.press('enter')
            time.sleep(13)

def perform_additional_tasks():
    """Define tasks to perform after the web button is detected."""
    print("Performing additional tasks...")
    time.sleep(1)

if __name__ == "__main__":
    # Step 1: Detect the web button via the detection script
    detect_web_button('trak2.py')

    # Step 2: Perform additional tasks after the web button is detected
    perform_additional_tasks()
