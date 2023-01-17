# Bigger number.
print(f'\n\tEnter two numbers and determine which is greater.')
number1 = int(input('\tInput the first number: '))
number2 = int(input('\tInput the second number: '))

if (number1 > number2):
    print(f'\t{number1} is greater than {number2}')
elif (number1 < number2):
    print(f'\t{number2} is greater than {number1}')
else:
    print(f'\t{number1} is equal to {number2}')

#--------------------------------------------------------------------
