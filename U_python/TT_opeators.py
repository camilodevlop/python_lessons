# Arithmetic operators.
print(f'\n\tArithmetic operators')
var1 = 3
var2 = 2
print(f'\tOperands: {var1} and {var2}\n')

# Operations.
add = var1 + var2
subs = var1 - var2
mult = var1 * var2
div = var1 / var2
div_int = var1 // var2
mod = var1 % var2
exp = var1 ** var2

# Results.
print(f'\tsum = {add}')
print(f'\tsubs = {subs}')
print(f'\tmult = {mult}')
print(f'\tdiv = {div}')
print(f'\tdiv_int = {div_int}')
print(f'\tmod = {mod}')
print(f'\texp = {exp}')

#--------------------------------------------------------------------

# Rectangle.
print(f'\n\tRectangle: calculating the area and perimeter.')
height = float(input('\tInput the height: '))
width = float(input('\tInput the width: '))
print(f'\tArea = {height*width} \n\tPerimeter = {(height+width)*2}')

#--------------------------------------------------------------------

# Assignment operators.
print(f'\n\tAssignment operators.')
var = 100.0;
print(f'\tvar = {var}\n')

# Operations and results.
var += 1
print(f'\t+= {var}')
var -= 2
print(f'\t-= {var}')
var *= 3
print(f'\t*= {var}')
var /= 4
print(f'\t/= {var}')
var %= 5
print(f'\t%= {var}')
var //= 2
print(f'\t//= {var}')
var **= 4
print(f'\t**= {var}')

#--------------------------------------------------------------------

# Comparison operators.
print(f'\n\tComparison operators.')
a = 4;
b = 2;
print(f'\ta = {a} | b = {b}\n')

print(f'\ta==b: {a==b}')
print(f'\ta!=b: {a!=b}')
print(f'\ta>b: {a>b}')
print(f'\ta>=b: {a>=b}')
print(f'\ta<b: {a<b}')
print(f'\ta<=b: {a<=b}')

# Even or odd number.
a = int(input('\n\tInput the number: '))
if (a % 2):
    print(f'\t{a} is Odd')
else:
    print(f'\t{a} is Even')

# Person of legal age.
age = int(input('\n\tInput your age: '))
if (age >= 18):
    print(f'\tYou are of legal age.')
else:
    print(f'\tYou aren\'t of legal age.')


#--------------------------------------------------------------------

# Logic operators.

# "and" operator.
print(f'\n\tValue within the interval 0 <= val <= 5.')
val = int(input('\tInput the val: '))
if (val>=0 and val<=5):
    print(f'\tSuccess: 0<={val}<=5.')
else:
    print(f'\t{val} is out of range.')

# "or" operator.
print('\n\tCan the father\'s John go to the game?')
vacations = True
rest_day = False
if (vacations or rest_day):
    print(f'\tYes, he can.')
else:
    print(f'\tNo, he can\'t.')

# "not" operator.
if not(vacations or rest_day):
    print(f'\tNo, he can\'t.')
else:
    print(f'\tYes, he can.')


#--------------------------------------------------------------------





#--------------------------------------------------------------------
