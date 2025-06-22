import subprocess
import pyautogui
import time
import urllib.request
import os

# Step 1: Install missing dependencies first
print("Installing required dependencies (wget)...")
subprocess.run(["sudo", "apt", "install", "-y", "wget"], check=True)

# Step 2: Download the .deb package from official Google Chrome source
chrome_deb_url = "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"
chrome_deb_file = "google-chrome-stable_current_amd64.deb"

print("Downloading Google Chrome...")
subprocess.run(["wget", chrome_deb_url, "-O", chrome_deb_file], check=True)

# Step 3: Add Google's public GPG key (to fix NO_PUBKEY error)
print("Adding Google's public GPG key...")
gpg_key_url = "https://dl.google.com/linux/linux_signing_key.pub"
gpg_key_file = "/tmp/linux_signing_key.pub"

# Download the GPG key
urllib.request.urlretrieve(gpg_key_url, gpg_key_file)

# Add the GPG key
subprocess.run(["sudo", "apt-key", "add", gpg_key_file], check=True)

# Step 4: Update the package list
print("Updating package list...")
subprocess.run(["sudo", "apt", "update"], check=True)

# Step 5: Install necessary libraries
print("Installing dependencies...")
subprocess.run(["sudo", "apt", "install", "-y", "libnspr4", "libnss3"], check=True)

# Step 6: Install the .deb package
print("Installing Google Chrome...")
subprocess.run(["sudo", "dpkg", "-i", chrome_deb_file])

# Step 7: Fix any broken dependencies
print("Fixing broken dependencies...")
subprocess.run(["sudo", "apt", "--fix-broken", "install", "-y"], check=True)

# Step 8: Launch Google Chrome
print("Launching Google Chrome...")
chrome_path = "/usr/bin/google-chrome"
url = "https://google.com"  # Replace with the URL you want to visit

# Launch Chrome in the background (non-blocking)
subprocess.Popen([
    chrome_path,
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-gpu",
    "--disable-software-rasterizer",
    "--remote-debugging-port=9222",
    url
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=True)

# Allow the browser to launch and stabilize
time.sleep(4)

# Step 9: Automate key press and mouse clicks
print("Automating interactions...")
pyautogui.press("enter")  # Press the Enter key
time.sleep(6)  # Sleep for 6 seconds before the first mouse click
pyautogui.click(x=957, y=541)
time.sleep(2)
pyautogui.click(1008, 33)
time.sleep(3)
pyautogui.click(1360, 596)
time.sleep(2)
pyautogui.click(557, 482)
time.sleep(2)
pyautogui.click(290, 24)
time.sleep(2)
pyautogui.click(684, 585)
time.sleep(2)
pyautogui.click(822, 584)
time.sleep(6)
pyautogui.click(684, 583)
time.sleep(2)
pyautogui.click(941, 583)
time.sleep(2)
pyautogui.click(258, 20)
time.sleep(2)

print("Automation complete!")
