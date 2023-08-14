# New style of the string format.

name = 'Camilo'
my_string = 'Hola, {}'.format(name)
print(my_string)

# We can do number conversions.
error = 500
string_hexadecimal = 'Hexadecimal Error: {err:x}'.format(err = error)
print(string_hexadecimal)

# Integer to float convertion.

integer = 50
string_float = 'Float number: {integer:0.8f}'.format(integer = integer)
print(string_float)

#-------------------------------------------------------------------
