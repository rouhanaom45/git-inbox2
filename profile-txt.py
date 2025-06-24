import pyperclip

# Get clipboard content
clipboard_content = pyperclip.paste()

# Save to profile.txt
with open('profile.txt', 'w', encoding='utf-8') as file:
    file.write(clipboard_content)

print("Clipboard content saved to profile.txt")
