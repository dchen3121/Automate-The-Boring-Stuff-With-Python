# Chapter 9 - Organizing Files

import shutil
import os

# os.walk(path) traces everything inside recursively
for folderName, subfolders, filenames in os.walk('C:\\Users\\dchen\\OneDrive\\Desktop\\CS 135'):
    print('The current folder is ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
    print('')