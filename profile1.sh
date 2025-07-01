#!/bin/bash

# Function to create a new Firefox profile and open it without blocking the terminal
create_new_profile() {
    PROFILE_NAME="newprofile-$(date +%s)"
    firefox -CreateProfile "$PROFILE_NAME"
    nohup firefox -P "$PROFILE_NAME" -no-remote > /dev/null 2>&1 &
    echo "$PROFILE_NAME" > current_profile.txt
}

# Call the function
create_new_profile
