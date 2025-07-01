#!/bin/bash

# Install megacmd if not already installed
apt install -y wget
wget https://mega.nz/linux/repo/xUbuntu_20.04/amd64/megacmd-xUbuntu_20.04_amd64.deb
apt install -y ./megacmd-xUbuntu_20.04_amd64.deb
rm megacmd-xUbuntu_20.04_amd64.deb

# Install unzip if not already installed
apt install -y unzip

# Log out if already logged in
mega-logout 2>/dev/null

# Log in to MEGA account
mega-login volcnao62@gmail.com 21504174lL@

# File to track downloaded files
DOWNLOADED_LOG="downloaded_files.txt"

# Create downloaded log file if it doesn't exist
touch "$DOWNLOADED_LOG"

# Check if profile.txt exists
if [ ! -f "profile.txt" ]; then
    echo "Error: profile.txt not found in the current directory."
    exit 1
fi

# Read the filename from profile.txt
selected_file=$(cat profile.txt | tr -d '\n' | tr -d '\r')

# Check if selected_file is empty
if [ -z "$selected_file" ]; then
    echo "Error: profile.txt is empty."
    exit 1
fi

# Check if the file has a .zip extension
if [[ ! "$selected_file" =~ \.zip$ ]]; then
    echo "Error: File specified in profile.txt must be a .zip file."
    exit 1
fi

# Check if file is already downloaded
if grep -Fx "$selected_file" "$DOWNLOADED_LOG" > /dev/null; then
    echo "File $selected_file has already been downloaded."
    exit 0
fi

# List files in /github-firefox to verify the file exists
files=$(mega-ls /proton-firefox 2>/dev/null)

# Check if the selected file exists in the MEGA directory
if ! echo "$files" | grep -Fx "$selected_file" > /dev/null; then
    echo "Error: File $selected_file not found in /github-firefox."
    exit 1
fi

# Download the specified file
echo "Downloading file: $selected_file"
mega-get "/proton-firefox/$selected_file" .

# Verify download
if [ -f "$selected_file" ]; then
    echo "Successfully downloaded $selected_file"
    # Add to downloaded log
    echo "$selected_file" >> "$DOWNLOADED_LOG"
else
    echo "Failed to download $selected_file"
    exit 1
fi

# Unzip to a temp directory
UNZIPPED_TOP="${selected_file%.zip}"
mkdir -p "$UNZIPPED_TOP"
unzip -o "$selected_file" -d "$UNZIPPED_TOP" | grep -Eiv 'inflating|extracting'

if [ $? -ne 0 ]; then
    echo "Error unzipping $selected_file!"
    exit 1
fi

echo "Unzipping completed successfully."

# Detect actual Firefox profile folder (must contain prefs.js)
REAL_PROFILE=$(find "$UNZIPPED_TOP" -type f -name "prefs.js" | head -n1 | xargs dirname)

if [ -z "$REAL_PROFILE" ]; then
    echo "Error: Could not find valid Firefox profile folder (missing prefs.js)."
    exit 1
fi

echo "Detected Firefox profile folder: $REAL_PROFILE"

# Add Firefox preferences and clean up session restore files
cat <<EOF > "$REAL_PROFILE/user.js"
user_pref("browser.sessionstore.resume_from_crash", false);
user_pref("browser.startup.page", 0);
user_pref("browser.startup.homepage_override.mstone", "ignore");
user_pref("browser.tabs.warnOnClose", false);
user_pref("browser.warnOnQuit", false);
user_pref("browser.sessionstore.max_tabs_undo", 0);
EOF

rm -f "$REAL_PROFILE/sessionstore.js" \
      "$REAL_PROFILE/sessionCheckpoints.json" \
      "$REAL_PROFILE/recovery.jsonlz4" \
      "$REAL_PROFILE/recovery.baklz4"

# Set DISPLAY if running in headless or VNC session
export DISPLAY=:1

# Start Firefox with the profile if not already running
if ! pgrep firefox > /dev/null; then
    nohup firefox --no-remote --new-instance --profile "$REAL_PROFILE" --purgecaches &> /dev/null &
    echo "Firefox launched successfully with the new profile."
else
    echo "Firefox is already running."
fi
