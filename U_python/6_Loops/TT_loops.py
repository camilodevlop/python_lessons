# While loop: printing numbers 0 to 100.
print('\n\tPrinting numbers 0 to 100')
counter = 0

while (counter <= 100):
    print(f'\t{counter} ')
    counter += 1
else:
    print(f'\n\tCounter is greater than 100.')

#-------------------------------------------------------------------

# Descending While loop: printing numbers 100 to 0.
print('\n\tPrinting numbers 100 to 0')
counter = 100

while (counter >= 0):
    print(f'\t{counter} ')
    counter -= 1
else:
    print(f'\n\tCounter is less than 0.')

#-------------------------------------------------------------------

# For loop: printing the characters of a string.
print('\n\tPrinting the characters of a string')
string = 'Hello Camilo'

for letter in string:
    print(f'\t{letter} ')
else:
    print('\tEnd of for loop.')

#-------------------------------------------------------------------

# For loop: printing numbers 50 to 100.
print('\n\tPrinting numbers 50 to 100.')
for val in range(50,101,1):
    print(f'\t{val}')
else:
    print('\tEnd of loop.')

# For loop: printing numbers 100 to 50.
print('\n\tPrinting numbers 100 to 50.')
for val in range(100,49,-1):
    print(f'\t{val}')
else:
    print('\tEnd of loop.')

#-------------------------------------------------------------------
