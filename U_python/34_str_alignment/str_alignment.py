# String alignment in Python.

# Centering a string.
title = 'Website of GlobalMentoring.com.mx'
# print(title.center(50,'*'))
print(title.center(len(title) + 20, '@'))

# Left-alignment of a character string.
print(title.ljust(len(title)+20), '*')

# Right-alignment of a character string.
print(title.rjust(len(title)+20), '-')

# replace method.
print('\n\t', title.replace(' ', ','))

# Removing characters at the start and end of the string.
string = ' *** GlobalMentoring.com.mx *** '
print(f'\n\tInitial string: {string}')
print('\tNumber of characters: ', len(string))

string = string.strip()
print('\n\tModified string: ', string)
print('\tNumber of characters: ', len(string))

string = string.strip('*')
print('\n\tModified string: ', string)
print('\tNumber of characters: ', len(string))

string = '*** GlobalMentoring.com.mx ***'
string = string.lstrip('*')
print('\n\tRemoving characters at the start: ', string)
print('\tNumber of characters: ', len(string))

string = '*** GlobalMentoring.com.mx ***'
string = string.rstrip('*')
print('\n\tRemoving characters at the end: ', string)
print('\tNumber of characters: ', len(string))

string = ' *** GlobalMentoring.com.mx *** '
string = string.strip().strip('*').strip()
print('\n\tModified string: ', string)

#-------------------------------------------------------------------
