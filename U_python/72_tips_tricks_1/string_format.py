
# Methods for formatting strings.

# Old style.
name = 'Camilo'
my_string = 'Hello, %s' % name
print(my_string)

# We can do number conversions.
error = 500
string_hexadecimal = 'Hexadecimal Error: %x' % error
print(string_hexadecimal)

# We can pass multiple values using a tuple.
string = 'Hello %s, there is an error %x' % (name, error)
print(string)

# We can reference variables by substitution using a dictionary.
string = 'Hello %(name)s, there is an error %(error)x' % {'name': 'Alejandro', 'error': 300}
print(string)

#-------------------------------------------------------------------
