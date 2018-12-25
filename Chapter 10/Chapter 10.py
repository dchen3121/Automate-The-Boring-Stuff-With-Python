# Chapter 10 - Debugging

# Raising exceptions with raise
# e.g.
# raise Exception('This is the error message')

# Raising exceptions for invalid input
# e.g. for a function that prints out a symbol in a box shape
#      three errors in the input may be:
#      - the symbol is not a single character string
#      - the width input is less or equal to 2
#      - the height input is less or equal to 2


def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + ' ' * (width - 2) + symbol)
    print(symbol * width)


for sym, w, h, in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        box_print(sym, w, h)
    except Exception as err:  # the err here is can be seen as a variable name
        print('An exception happened: ' + str(err))


# Writing the error message as a traceback inside another file
# so that the program doesn't crash and stop running immediately
# but you can go look at the file and figure out what and where went wrong afterwards

import traceback

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')


# The assert keyword
# assert basically says:
#   I assert that this condition holds true, and if not, there is a bug
#   somewhere else in the program.
# If an assert fails, the program should crash immediately,
# thus shortening the time between the original cause of the bug and when
# you first notice the bug.

# e.g.
podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
# in plain English, this means:
#   -   The podBayDoorStatus must be 'open'
#   -   If it is not open, raise
#       AssertionError: The pod bay doors need to be "open"

# another example: cars simulation
granville_16th = {'ns': 'green', 'ew': 'red'}
dunbar_41st = {'ns': 'red', 'ew': 'green'}
def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
# note that this is an erroneous application of switchLights
# as the cars will crash!
# but let's say we didn't realize that it was erroneous and didn't realize
# that at an intersection one of the lights have to be red at all times
# so we add an assert statement at the bottom of the function:
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)

# switchLights(granville_16th)

# Think of 'assert' as doing a sanity check


