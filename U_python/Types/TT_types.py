"""
type() function: x = 10 is int, x = 4.5 is float, x = 'name' is 
a string, x = True (or False) is boolean.
"""

x = 4.5
print('\nx =',x)
print('Type of x:',type(x))

# String concanetation.
str_1 = 'Camilo'
str_2 = 'Alejandro'
str_name = str_1 + ' ' + str_2
print('\nThe name is', str_name)
#print('\nThe name is ' + str_name)

# + can be omitted if the strings are adjacent.
str_test = 'C' 'A'
print('\nThe test is ' + str_test)

# Type conversion.
str_1 = "1"
str_2 = "2"
print("\nThe sum is:", int(str_1) + int(str_2))

#--------------------------------------------------------------------

# Boolean types.
miVar = False
print(miVar)

miVar = 3 > 2
print(miVar)

if miVar:
    print(True)
else:
    print(False)

#--------------------------------------------------------------------

# Input function.
miVar = input('\nInput the value: ')
print('The value is: ', miVar)
print('\nEnd')

num1 = float(input("\nType the first number: "))
num2 = float(input("Type the second number: "))
summ = num1 + num2
print('The sum is:', summ)

#--------------------------------------------------------------------
