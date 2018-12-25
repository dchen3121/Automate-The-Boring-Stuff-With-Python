#! python3

# mapit.py:
#   -   Gets a street address from the command line arguments / clipboard
#   -   Opens the web browser to the Google Maps page for the address

import sys
import pyperclip
import webbrowser
# the webbrowser module:
# webbroser.open(url) opens the url in the browser


address = ''

if len(sys.argv) == 1:
    # get address from clipboard
    address = pyperclip.paste()
else:
    # get address from cmd line
    address = ' '.join(sys.argv[1:])

webbrowser.open('https://www.google.ca/maps/search/' + address)




