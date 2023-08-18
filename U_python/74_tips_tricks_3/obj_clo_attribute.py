import copy

# Object attributes copy.

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Point({self.x!r}, {self.y!r})'    

    def __eq__(self, obj) -> bool:
        return isinstance(obj, Point) and self.x == obj.x and self.y == obj.y

point_a = Point(2, 3)
point_b = copy.copy(point_a)

# Shallow copy.
print(f'Shallow copy:')
print(f'Point a: {point_a}')
print(f'Point b: {point_b}')

print(f'Do the objects have the same content? {point_a == point_b}')
print(f'Do the objects have the same reference? {point_a is point_b}')

#-------------------------------------------------------------------

class Rectangle:
    def __init__(self, upper_left, lower_right) -> None:
        self.upper_left = upper_left
        self.lower_right = lower_right

    def __repr__(self) -> str:
        return f'Rectangle({self.upper_left!r}, {self.lower_right!r})'

rectangle_a = Rectangle(Point(0, 1), Point(3, 4))
rectangle_b = copy.copy(rectangle_a)

# Shallow copy.
print(f'Shallow copy:')
print(f'Rectangle a: {rectangle_a}')
print(f'Rectangle b: {rectangle_b}')

rectangle_a.lower_right.y = 6
print(f'Rectangle a: {rectangle_a}')
print(f'Rectangle b: {rectangle_b}')

# Deep copy.
rectangle_c = Rectangle(Point(2, 4), Point(7, 9))
rectangle_d = copy.deepcopy(rectangle_c)

print(f'Deep copy:')
print(f'Rectangle c: {rectangle_c}')
print(f'Rectangle d: {rectangle_d}')

rectangle_c.lower_right.y = 6
print(f'Rectangle c: {rectangle_c}')
print(f'Rectangle d: {rectangle_d}')

#-------------------------------------------------------------------
