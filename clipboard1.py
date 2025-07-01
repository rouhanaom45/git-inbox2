import pyperclip
import re

# Get current clipboard text
text = pyperclip.paste()

# Find first email address in the text
match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
if match:
    email = match.group(0)
    pyperclip.copy(email)
