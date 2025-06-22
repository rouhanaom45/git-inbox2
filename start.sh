#!/bin/bash


scripts=(
  "google.py"
  "capcha.py"
  "box1.py"
  "proton1.py"
  "confirm0.py"
  "proton2.py"
  "upload1.py"
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

