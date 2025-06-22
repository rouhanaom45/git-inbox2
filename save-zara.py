import pyperclip

# Read from copy-zara.py
with open("copy-zara.py", "r", encoding="utf-8") as f:
    content = f.read()

# Copy to clipboard
pyperclip.copy(content)

print("Content of copy-zara.py copied to clipboard")
