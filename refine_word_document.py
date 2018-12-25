#! python3
# refine_word_document.py - Removes all spaces and duplicate puntuation

import pyperclip, re

doubleSpaceRegex = re.compile(r'( )( )+')
doublePuncRegex = re.compile(r'([.,!?:;])([.,!?:;]{1,})')

text = str(pyperclip.paste())

text = doubleSpaceRegex.sub(' ', text)
text = doublePuncRegex.sub(r'\1', text)

pyperclip.copy(text)
