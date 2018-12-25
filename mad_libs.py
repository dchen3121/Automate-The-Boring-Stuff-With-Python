#! python3

# mad_libs.py
# Takes the file mad_libs.txt and generates new text based on user input

import os
import re

# os.makedirs('.\Mad Libs Files')
os.chdir('C:\\Users\\dchen\\Onedrive\\Desktop\\Projects\\'
         'Automate the Boring Stuff with Python\\Mad Libs Files')

mad_lib = open('madlib1.txt', 'w')
mad_lib.write('The ADJECTIVE panda walked to the NOUN and then VERB.\n'
              'A nearby NOUN was unaffected by these events.')
mad_lib.close()

nounRegex = re.compile(r'NOUN')
verbRegex = re.compile(r'VERB')
adjRegex = re.compile(r'ADJECTIVE')
advRegex = re.compile(r'ADVERB')
fillRegex = re.compile(r'NOUN|VERB|ADJECTIVE|ADVERB')

mad_lib = open('madlib1.txt')
text = mad_lib.read()
# print(text)
mad_lib.close()

fill = fillRegex.findall(text)
# print(fill)
listFill = []
for i in fill:
    if i.lower() == 'adverb' or i.lower() == 'adjective':
        print('Enter an ' + i.lower() + ':')
        listFill.append(str(input()))
    else:
        print('Enter a ' + i.lower() + ':')
        listFill.append(str(input()))

for i in range(len(text)):
    if text[i:i+4] in ['NOUN', 'VERB']:
        text = text[:i] + listFill.pop(0) + text[i+4:]
    elif text[i:i+9] in ['ADJECTIVE']:
        text = text[:i] + listFill.pop(0) + text[i+9:]
    elif text[i:i+6] in ['ADVERB']:
        text = text[:i] + listFill.pop(0) + text[i+6:]

print(text)
mad_generated = open('player_generated_mad_lib.txt', 'w')
mad_generated.write(text)
mad_generated.close()
