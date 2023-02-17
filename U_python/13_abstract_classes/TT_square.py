# Multiple inheritance: Shape class.

from TT_shape import Shape
from TT_color import Color

class Square(Shape, Color):
    def __init__(self, side, color):
        Shape.__init__(self, side, side)
        Color.__init__(self, color)

    def area(self):
        return self._height * self._width

    def __str__(self) -> str:
        return f'{Shape.__str__(self)}, {Color.__str__(self)}'

#-------------------------------------------------------------------
