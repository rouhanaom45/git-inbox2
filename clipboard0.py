import pyperclip
import re

# Step 1: Get the clipboard content
clipboard_content = pyperclip.paste()

# Step 2: Find the six-digit code using regex
six_digit_code = re.search(r'\b\d{6}\b', clipboard_content)

if six_digit_code:
    # Extract the code and save it back to the clipboard
    code = six_digit_code.group()
    pyperclip.copy(code)
    print(f"Extracted code: {code} (saved to clipboard)")
else:
    print("No six-digit code found in the clipboard content.")
