# Multiple inheritance in Python: testing.

from TT_rectangle import Rectangle
from TT_square import Square

print('\n\tSquare class.')
square1 = Square(5, 'Red')
print(f'\t{square1}')
print(f'\tSquare area: {square1.area()}')

print('\n\tRectangle class.')
rectangle1 = Rectangle(10, 7, 'Blue')
print(f'\t{rectangle1}')
print(f'\tRectangle color: {rectangle1.color}')
print(f'\tRectangle area: {rectangle1.area()}')

print(f'\n\tRectangle: new height and width.')
rectangle1.height = 20
rectangle1.width = 10
print(f'\t{rectangle1}')

# MRO - Method Resolution Order.
print(f'\n\tMethod Resolution Order (Square class):\n\t{Square.mro()}')

#-------------------------------------------------------------------
