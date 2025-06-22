import pyperclip

# Read from email.txt
with open("email1.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Copy to clipboard
pyperclip.copy(content)

print("Content from email1.txt copied to clipboard")
