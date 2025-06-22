import re
import pyperclip

content = pyperclip.paste()
match = re.search(r'\b\d{8}\b', content)
if match:
    pyperclip.copy(match.group(0))
