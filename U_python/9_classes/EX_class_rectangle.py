# Classes in the Python language: Rectangle.
class Rectangle:
    def __init__(self, height = 0.0, width  = 0.0) -> None:
        self.height = height
        self.width = width
    
    def area(self):
        if self.height < 0 or self.width < 0:
            return '\n\tError: either height or width are negative.\n'

        return self.height * self.width

#-------------------------------------------------------------------

# Testing the class.
print('\n\tRectangle class.')
height = float(input('\tType the height: '))
width = float(input('\tType the width: '))

rectangle_1 = Rectangle(height, width)
print(f'\tArea = {rectangle_1.area()} u^2')

#-------------------------------------------------------------------
