def divide_from_10(divideBy):
    try:
        return 10 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid Argument.')

# Chapter 4 - lists


# Comma Code
# Takes a list value as an argument and returns a string with all
# the items seperated by a comma and a space
def comma_code(list_input):
    retVal = ""
    for i in range(0, len(list_input) - 1):
        retVal = retVal + str(list_input[i]) + ", "
    retVal = retVal + "and " + str(list_input[-1])
    return retVal
# Test:
print(comma_code(['apples', 'bananas', 'tofu', 'cats']))


# Character Picture Grid
# Returns picture in ASCII form rotated 90 degrees clockwise
def picture(list_input):
    retVal = ""
    for i in range(0, len(list_input[0])):
        for j in range(len(list_input) - 1, 0, -1):
            retVal += list_input[j][i]
        retVal += "\n"
    return retVal
# Test:
print(picture([['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]))