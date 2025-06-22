import pyperclip
import re

# Get clipboard content
clipboard_content = pyperclip.paste()

# Find the email
matches = re.findall(r'\b[a-zA-Z0-9._%+-]+@inbox\.lv\b', clipboard_content)

if matches:
    email = matches[0]
    pyperclip.copy(email)  # Copy to clipboard
    print(f"Extracted and copied: {email}")
else:
    print("No @inbox.lv email found in clipboard.")
