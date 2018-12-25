#! python3
# bullet_point_adder.py - Adds a bullet point before each point.

import pyperclip

text = pyperclip.paste().split('\n')
for i in range(0, len(text)):
    text[i] = '* ' + text[i]
retval = '\n'.join(text)

pyperclip.copy(retval)
