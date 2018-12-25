#! python3
# find_phone_email.py - Finds all phones and emails in a given text.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+=]+   # username
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-Z]{2,4})   # dot something
    )''', re.VERBOSE)

text = str(pyperclip.paste())
allPhone = phoneRegex.findall(text)
allEmail = emailRegex.findall(text)

print(allPhone)
print(allEmail)

retVal = []
for i in allPhone:
    phone = '-'.join([i[1], i[3], i[5]])
    if i[8] != '':
        phone += ' x' + i[8]
    retVal.append(phone)
for i in allEmail:
    email = i[0]
    retVal.append(email)

if len(retVal) > 0:
    pyperclip.copy('\n'.join(retVal))
    print('Copied to clipboard:')
    print('\n'.join(retVal))
else:
    print('No phone numbers or email addresses found.')

