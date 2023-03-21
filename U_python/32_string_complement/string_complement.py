# Advanced study of the strings' format.

# str multiplication.
print('\n\tstr multiplication.')
string = 5 * 'Hello'
print(f'\tResult: {string}')

#-------------------------------------------------------------------

# Tuples multiplication.
print('\n\tTuples multiplication.')
tpl = 5 * ('Hello', 10)
print(f'\tResult: {tpl}')

#-------------------------------------------------------------------

# Lists multiplication.
print('\n\tLists multiplication.')
lst = 5 * ['Hello', 10]
print(f'\tResult: {lst}, Length = {len(lst)}')

#-------------------------------------------------------------------

# Escape characters.
print('\n\tEscape characters.')

# '\' lets to use reserved characters.
string = 'Hello \' world'
print(f'\tResult: {string}')

# '\b' deletes the last character of the sentence.
string = 'Deleting the last \'e\' in this sentence\b.'
print(f'\tResult: {string}')

# '\\' prints the backslash. 
string = 'c:\\new\\Jhon'
print(f'\tResult: {string}')

# Raw string.
string = r'c:\\new\\Jhon -- r ignores the special characters like \n.'
print(f'\tResult: {string}')

#-------------------------------------------------------------------

# Unicode characters.
print('\n\tUnicode characters.')
print(f'\tHello\u0020World.')      # space character.
print(f'\tPlain notation:', '\u0041')
print(f'\tHexadecimal notation:', '\x41')

print('\tHeart: ', '\u2665')
print('\tSmiling face: ', '\U0001f600')
print('\tSnake: ', '\U0001F40D')

#-------------------------------------------------------------------

# ASCII characters.
print(f'\tUppercase A (ASCII): {chr(65)}')      # space character.
print(f'\tLowercase a (ASCII): {chr(97)}')      # space character.
print(f'\t@ symbol (ASCII): {chr(64)}')      # space character.

#-------------------------------------------------------------------
