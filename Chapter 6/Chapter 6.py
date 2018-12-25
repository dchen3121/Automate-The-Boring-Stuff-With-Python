# Chapter 6 - String Manipulation

# str.join(los)
# joins all items in los with str, returns a string
print(', '.join(['cats', 'rats', 'bats']))

# str.split(split)
# splits the string str by split value, returns a list
print('My name is Jeff'.split())
print('My-name-is-Jeff'.split('-'))

# .ljust(num, str), .rjust(num, str), .center(num, str)
# adjust the string
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

# .strip(), .rstrip(), .lstrip()
spam = '    Hello World     '
print(spam.strip())

