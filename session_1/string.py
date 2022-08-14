"""
string  functions

"""
# printing a string

print("hello  world")

# Assign string to a variable

MESSAGE = 'hello world'

#  To access a character of a string using index

print(MESSAGE[0])

print(MESSAGE[10])

# print(MESSAGE[11])
#  # "this line throws an error"

# using slicing to access a part of a string
print(MESSAGE[6:])

# conver all characters to lower case

print(str.lower(MESSAGE))

# conver all characters to lower case
print(MESSAGE.lower())

# conver all characters to upper case
print(MESSAGE.upper())

# slice 0:5 characters
print(MESSAGE[:5])

# slice 0:5 characters
print(MESSAGE[0:5])

# find a characters in a string
print(MESSAGE.find('world'))

# find a character in a string ; if not found will return -1
print(MESSAGE.find('Universe'))

# replace 'world' with 'universe'
print(MESSAGE.replace('world' ,'Universe'))

# string concatenation

NAME = 'Michael'

GREETING = 'Hello'

MESSAGE = GREETING + ", " + NAME

print(MESSAGE)

# formatted string

# print('{}, {}. Welcome'.format(GREETING, NAME))

print(f'{GREETING}, {NAME}. Welcome')

# to get help about function print(help(fn_name))

print(help(str.lower))
