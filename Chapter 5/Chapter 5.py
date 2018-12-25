# Chapter 5 - Dictionaries and Structuring Data

# .value(), .key(), .items()
spam = {'color': 'red', 'age': 42}
for i in spam.values():
    print(i)
for j in spam.keys():
    print(j)
for k in spam.items():
    print(k)
for a, b in spam.items(): # multiple assignment
    print('Key: ' + a + ' Value: ' + str(b))
print('color' in spam)
print('color' in spam.keys())
# above two lines are exactly the same thing

# .get(key, fallback)
# Retrieves the value from key; if key doesn't exist returns fallback
# Advantage: does not crash program when key is not in dict
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) \
      + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) \
      + ' eggs.')

# .setdefault(key, value)
# Sets new key, value pair if not already existing key
default = {'name': 'Pooka', 'age': 5}
default.setdefault('color', 'black')
print(default)
default.setdefault('color', 'white')
print(default)

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)


# Fantasy Game Inventory
# Takes a dictionary value as a dictionary of inventory and displays it
def display(dict_input):
    retval = 'Inventory:\n'
    for i in dict_input.keys():
        retval = retval + str(dict_input[i]) + ' ' + i + '\n'
    sum = 0
    for j in dict_input.values():
        sum += j
    retval += 'Total number of items: ' + str(sum)
    return retval
# Test:
print(display(
    {'rope': 1,
     'torch': 6,
     'gold coin': 42,
     'dagger': 1,
     'arrow': 12}
))

# List to Dictionary Function for Fantasy Game Inventory
# Adds elements in list value to a dict
def add_to_inventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory
# Test:
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragonLoot)
print(display(inv))
