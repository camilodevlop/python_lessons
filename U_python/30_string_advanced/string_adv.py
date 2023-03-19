# Advanced study of the strings.

from my_class import MyClass

# Automatic concatenation.
print('\n\tAutomatic concatenation.')
msg = 'Hello' 'world'
print(f'\t{msg}')
var = 'Python'
msg = msg + var
print(f'\t{msg}')
msg += 'University' 'Colombia'
print(f'\t{msg}')

#-------------------------------------------------------------------

# Requesting help.
#help(str.capitalize)

#-------------------------------------------------------------------

# Requesting help.
#help(str.capitalize)

#-------------------------------------------------------------------

# Testing the help of MyClass.
#help(MyClass)
print(MyClass.__doc__)  # Prints the docstring of the class.
print(MyClass.__init__.__doc__)
print(MyClass.my_method.__doc__)

#-------------------------------------------------------------------

# Strings are immutable.
print('\n\tStrings are immutable')
msg1 = 'hello world.'
msg2 = msg1.capitalize()
print(f'\tmsg1: {msg1}, id: {hex(id(msg1))}')
print(f'\tmsg2: {msg2}, id: {hex(id(msg2))}')

# If the content of the variable msg1 is modified, its memory
# address change, i.e., the original string object is not modified and
# a new one is created.
msg1 += ' Python'
print(f'\tmsg1: {msg1}, id: {hex(id(msg1))}')

#-------------------------------------------------------------------

# Join method.
print('\n\tJoin method.')
str_tuple = ('Hello','World','University','Python')
msg = ' '.join(str_tuple)
print(f'\tMessage: {msg}')

str_list = ['Java','Python','Angular','Spring']
msg = ', '.join(str_list)
print(f'\tMessage: {msg}')

string = 'Hello World'
msg = '.'.join(string)
print(f'\tMessage: {msg}')

str_dicc = {'Name': 'Jhon,', 'Surname': 'Smith', 'Age': '18'}
keys = '-'.join(str_dicc.keys())
values = '-'.join(str_dicc.values())
print(f'\tKeys: {keys}, Type: {type(keys)}')
print(f'\tValues: {values}, Type: {type(values)}')

#-------------------------------------------------------------------

# Split method.
print('\n\tSplit method.')
courses = 'Java Python JavaScript Angular Spring Excel'
list_courses = courses.split()
print(f'\tList of courses: {list_courses}')

courses = 'Java,Python,JavaScript,Angular,Spring,Excel'
# list_courses = courses.split(',')
list_courses = courses.split(',', 3)
print(f'\tList of courses: {list_courses}')

#-------------------------------------------------------------------
