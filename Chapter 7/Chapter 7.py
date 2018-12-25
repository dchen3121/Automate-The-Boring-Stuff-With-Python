# Chapter 7 - Pattern Matching with Regular Expressions

import re

def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

def find_phone_number(string):
    for i in range(0, len(string) - 11):
        if is_phone_number(string[i:i + 12]):
            print('Phone number found: ' + string[i:i + 12])
    print('All done.')

find_phone_number(
    '''T111-231-3444EE4R4555-555-5555op111-111-1111'''
)

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo)
print('Phone number found: ' + mo.group())

# Updating our phoneNumRegex so that it wraps different parts of the
#     information in separate parenthesis
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 123-456-7890.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print(mo.groups())
areaCode, mainNumber = mo.groups() # the trick of multiple assignment
print(areaCode)
print(mainNumber)
# Updating our phoneNumRegex so that actual parenthesis can be wrapped
#     around areaCode
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is (123) 456-7890.')
print(mo.group(1))
print(mo.group(2))
print(mo.groups())

# Using pipe characters | to have multiple possible variants of a regex
randomRegex = re.compile(r'Fan Ge|Shane Bauman|D(aniel|Chen)')
mo1 = randomRegex.search("He is such an amazing prof, Fan Ge. Way \
better than Shane Bauman.")
mo2 = randomRegex.search("DChen or Daniel")
print(mo1.group())
print(mo2.group())

# Using ? to match part of a regex conditionally
batRegex = re.compile(r'Bat(wo)?man')
# batRegex = re.compile(r'Bat(wo|)man')
# the above alternative also works
mo1 = batRegex.search("1 2 2 3 Batman 22")
mo2 = batRegex.search("1 3 2 4 Batwoman 555")
print(mo1.group())
print(mo2.group())

# findall()
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('Cell: 111-123-3211 \
                            Work: 001-901-0912')
# mo is a list of strings
# if the original regex contains more than 1 parts, mo will contain a
#     list of tuples

