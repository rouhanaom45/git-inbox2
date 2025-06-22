import pyperclip

# Get text from clipboard
clipboard_content = pyperclip.paste()

# Save to email.txt
with open("email.txt", "w", encoding="utf-8") as f:
    f.write(clipboard_content)

print("Clipboard content saved to email.txt")
