#!/bin/bash


scripts=(
  "get-profile.py"
  "profile-txt.py"
  "proton-ready.py"
  "save.py"
  "github1.py"
  "github2.py"
  "confirm.py"
  "repository.py"
  "upload.py"
)

# Run each script in order
for script in "${scripts[@]}"; do
  echo "Running $script..."
  python3 "$script"
  if [ $? -ne 0 ]; then
    echo "Error: $script failed. Exiting."
    exit 1
  fi
  echo "$script finished successfully."
done

sleep 2
