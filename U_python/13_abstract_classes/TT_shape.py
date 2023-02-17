# Multiple inheritance in Python: Shape class.

# ABC class: Abstract Base Class.
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, height, width) -> None:
        self._height = height
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    # This class is become to "abstract" by this method. 
    @abstractmethod
    def area(self):
        pass

    def __str__(self) -> str:
        return f'Height: {self._height}, Width: {self._width}'

#-------------------------------------------------------------------
