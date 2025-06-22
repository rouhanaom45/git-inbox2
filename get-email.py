import pyperclip

# Read from email.txt
with open("email.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Copy to clipboard
pyperclip.copy(content)

print("Content from email.txt copied to clipboard")
