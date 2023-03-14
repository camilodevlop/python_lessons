import math
from decimal import Decimal

# Numerical systems.

print('\n\tNumerical systems')
# Decimal
a = 10
print(f'\t{a}')

# Binary
a = 0b1010
print(f'\t{a}')

# Octal
a = 0o12
print(f'\t{a}')

# Hexadecimal
a = 0xA
print(f'\t{a}')

#-------------------------------------------------------------------

# Converting from string to integer using the base.

print('\n\tConverting from string to integer using the base.')
# Decimal
a = int('23', 10)
print(f'\t{a}')

# Binary
a = int('10111', 2)
print(f'\t{a}')

# Octal
a = int('27', 8)
print(f'\t{a}')

# Hexadecimal
a = int('17', 16)
print(f'\t{a}')

#-------------------------------------------------------------------

# Delving into the float type.

print('\n\tDelving into the float type.')
a = 3.0
print(f'\ta: {a:.2f}')

print('\tThe float constructor accepts str or int.')
a = float(10) 
print(f'\ta: {a:.2f}')
a = float('10') 
print(f'\ta: {a:.2f}')

#-------------------------------------------------------------------

# Exponential notation.

print('\n\tExponential notation.')
a = 3e5
print(f'\ta: {a:.2f}')
a = 3e-5
print(f'\ta: {a:.5f}')

#-------------------------------------------------------------------

# Infinite values management.

print('\n\tInfinite values management.')
#infinite_pos = float('inf')
#infinite_pos = math.inf
infinite_pos = Decimal('Infinity')
print(f'\tPositive infinite: {infinite_pos}')
print(f'\tIs infinite?: {math.isinf(infinite_pos)}')

#infinite_neg = float('-inf')
#infinite_neg = -math.inf
infinite_neg = Decimal('-Infinity')
print(f'\tNegative infinite: {infinite_neg}')
print(f'\tIs infinite?: {math.isinf(infinite_neg)}')

#-------------------------------------------------------------------

# NaN - Not a Number.

print('\n\tNaN - Not a Number.')
a = float('NaN')
print(f'\ta: {a}')
print(f'\tIs NaN (Not a Number)? {math.isnan(a)}')

a = Decimal('NaN')
print(f'\ta: {a}')
print(f'\tIs NaN (Not a Number)? {math.isnan(a)}')

#-------------------------------------------------------------------

# bool type.

print('\n\tbool type.')
value = 0
result = bool(value)
print(f'\tValue = {value}, Result = {result}.')

value = 15
result = bool(value)
print(f'\tValue = {value}, Result = {result}.')

print('\n\tbool applied to str.')
value = ''
result = bool(value)
print(f'\tValue = {value}, Result = {result}.')

value = 'Hola'
result = bool(value)
print(f'\tValue = {value}, Result = {result}.')

print('\n\tbool applied to collections: lists, tuples, dictionaries.')
value = []
result = bool(value)
print(f'\tValue = {value}, Result = {result}.')

value = [1,2,3]
result = bool(value)
print(f'\tValue = {value}, Result = {result}.')

value = ()
result = bool(value)
print(f'\tValue = {value}, Result = {result}.')

value = (1,2,3)
result = bool(value)
print(f'\tValue = {value}, Result = {result}.')

value = {}
result = bool(value)
print(f'\tValue = {value}, Result = {result}.')

value = {'IDE': 'Integrating Development Environtment'}
result = bool(value)
print(f'\tValue = {value}, Result = {result}.')

#-------------------------------------------------------------------
