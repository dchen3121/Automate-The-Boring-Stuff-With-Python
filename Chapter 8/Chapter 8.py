# Chapter 8 - Reading and Writing Files

# A file has two key properties:
# - A filename (usually written as one word)
# - A path
# Example of a file on a Win7 laptop with the filename project.docx:
# C:\Users\dchen\Documents\project.docx

# On Windows, paths are written using backslashes as the separator
# between folder names.
# On OS X and Linux, the forward slash are used as path separators.

import os

'''
print('os.path.join() and os.path.sep examples')
# joining paths with os.path.join()
examplePath = str(os.path.join('Users', 'dchen', 'Documents'))
print(examplePath)
# printing the appropriate type of separator based on system with
# os.path.sep
print(os.path.sep)

print('')

print('os.getcwd() examples')
# current working directory
print(os.getcwd())

print('')

print('os.chdir(path) examples')
# change directories
os.chdir('C:\\Users\\dchen\\OneDrive\\Desktop\\Projects\\'
         'Automate the Boring Stuff with Python\\Chapter 7')
print(os.getcwd())

# creating new folders with os.makedirs()
# os.makedirs('C:\\Users\\dchen\\OneDrive\\Desktop\\Personal\\ILoveSky')

# Relative Paths vs. Absolute Paths
# Relative Paths:
#   ..\     means parent directory
#   .\      means current working directory
# Absolute Paths:
#   The entire path name

print('')

print('os.path.abspath(path) examples')
# converting relative path to absolute path with os.path.abspath(path)
print(os.path.abspath('.'))  # this prints the cwd
print(os.path.abspath('..\\'))  # this prints the parent dir
print(os.path.abspath('..\\Chapter 8'))  # this prints the 'Chapter 8' dir

print('')

print('os.path.relpath(path, start) examples')
# os.path.relpath(path, start) returns a string of a relative path from
# the start to path. If start is not provided, the cwd is used as start
print(os.path.relpath('C:\\Users\\dchen\\OneDrive\\Desktop\\Projects\\'
                      'Automate the Boring Stuff with Python\\Chapter 7',
                      'C:\\Users\\dchen\\OneDrive\\Desktop\\Projects\\'
                      'Automate the Boring Stuff with Python'))
print(os.path.relpath('C:\\Users\\dchen\\OneDrive\\Desktop\\Projects\\'
                      'Automate the Boring Stuff with Python',
                      'C:\\Users\\dchen\\OneDrive\\Desktop\\Projects\\'
                      'Automate the Boring Stuff with Python\\Chapter 7'))
print(os.path.relpath('C:\\Windows', 'C:\\'))

print('')

print('os.path.dirname(path)\nos.path.basename(path)\nExamples')
# os.path.dirname(path) returns a string of everything that comes before
# the last slash in the path argument.
# os.path.basename(path) returns a string of everything that comes after
# the last slash in the path argument.
# os.path.split(path) returns a tuple of both the dir name and the base
# name.
path = 'C:\\Users\\dchen\\OneDrive\\Desktop\\Projects\\' \
       'Automate the Boring Stuff with Python\\Chapter 8'
print(os.path.dirname(path))  # prints the dir name
print(os.path.basename(path))  # prints the base name
print(os.path.split(path))  # prints a tuple of both
print(path.split(os.path.sep))

print('')

print('os.listdir(path) examples')
# os.listdir(path) returns a list of filename strings for each file in
# the path argument
print(os.listdir(os.path.dirname(os.getcwd())))
'''

'''
PART II: Opening, Reading, and Writing data into a .txt file
'''

'''
helloFile = open('C:\\Users\\dchen\\Onedrive\\Desktop\\Projects\\'
                 'Automate the Boring Stuff with Python\\hello.txt')
# default for opening file is read-only mode
helloContent = helloFile.read()
# print(helloContent)

# three modes for opening files:
#   -   read-only mode: 'r'
#   -   append mode: 'a'
#   -   write mode: 'w'
# note: if the filename passed to open() does not exist, both the write
# and append mode will create a new, blank text file.
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello bacon!\n')
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('bacon.txt')
baconContent = baconFile.read()
baconFile.close()
print(baconContent)
'''

'''
Part III: The shelve module to store data
'''

'''
import shelve
shelfFile = shelve.open('myData')
cats = ['Zophie', 'Pooka', 'Simon']
dogs = ['Abby', 'Jon', 'Zoe']
shelfFile['cats'] = cats
shelfFile['dogs'] = dogs
shelfFile.close()
shelfFile = shelve.open('myData')
print(type(shelfFile))
print(shelfFile['cats'])
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
'''

'''
Part IV: Using prettyprint to store variables in new python files
'''
import pprint
cats = [{'name': 'Zophie', 'description': 'chubby'},
        {'name': 'Pooka', 'description': 'fluffy'}]
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

import myCats
print(myCats.cats[0]['name'])


