# print_table.py prints out a table

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dog', 'cats', 'moose', 'goose']]

def max_len(list):
    maxlen = 0
    for i in list:
        maxlen = max(maxlen, len(i))
    return maxlen

def print_table(table):
    retval = ''
    count = 0
    while count < len(table[0]):
        for i in range(0, len(table)):
            maxlen = max_len(table[i])
            retval = retval + table[i][count].rjust(maxlen) + ' '
        count += 1
        retval += '\n'
    return retval

print(print_table(tableData))