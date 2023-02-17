# Multiple inheritance in Python: testing.

from TT_shape import Shape
from TT_color import Color

class Rectangle(Shape, Color):
    def __init__(self, height = 0, width = 0, color = '') -> None:
        Shape.__init__(self, height, width)
        Color.__init__(self, color)

    def area(self):
        return self._height * self._width

    def __str__(self) -> str:
        return f'{Shape.__str__(self)}, {Color.__str__(self)}'

#-------------------------------------------------------------------
