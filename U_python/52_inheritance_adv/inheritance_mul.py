from types import FunctionType


class Simple_List:

    def __init__(self, elements) -> None:
        self._elements = list(elements)

    def add_element(self, element):
        self._elements.append(element)

    def __getitem__(self, item):
        return self._elements[item]

    def order(self):
        self._elements.sort()
    
    def __len__(self):
        return len(self._elements)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__} ({self._elements!r})'

#-------------------------------------------------------------------

class Ordered_List(Simple_List):

    def __init__(self, elements = []) -> None:
        super().__init__(elements)
        self.order()

    def add_element(self, element):
        super().add_element(element)
        self.order()

#-------------------------------------------------------------------

class Integer_List(Simple_List):

    def __init__(self, elements = []) -> None:
        for element in elements:
            self._validate(element)
        
        super().__init__(elements)
    
    def _validate(self, element):
        if not isinstance(element, int):
            raise ValueError(f'\n\tIt is not an int value: {element}')

    # Overriding the method 'add_element' of the 'Simple_List' class.
    
    def add_element(self, element):
        self._validate(element)
        super().add_element(element)

#-------------------------------------------------------------------

# Class: Ordered_Integer_List.

class Ordered_Integer_List(Integer_List, Ordered_List):
    pass

#-------------------------------------------------------------------

# Simple list.
simple_list = Simple_List([5, 3, 6, 8])
print(f'\n\tExample of simple inheritance.\n\t{simple_list}')

# Ordered list.
ordered_list = Ordered_List([4, 3, 6, 8, 5, -1])
print(f'\n\t{ordered_list}')
ordered_list.add_element(-14)
print(f'\t{ordered_list}')
print(f'\tLength of the ordered list: {len(ordered_list)}')

# Integer list.
integer_list = Integer_List([1, 2, 3, -5])
print(f'\n\t{integer_list}')

# Ordered_Integer_List.
ordered_integer_list = Ordered_Integer_List([4 , 5, -1, 10, 14, -4])
print(f'\n\t{ordered_integer_list}')
ordered_integer_list.add_element(-20)
print(f'\t{ordered_integer_list}')

# Printing the hierarchy of the classes.
print(f'\n\t{Ordered_Integer_List.__bases__}')

# Method Resolution Order (MRO).
print(f'\n\t{Ordered_Integer_List.__mro__}')

#-------------------------------------------------------------------

# Delving into method 'isinstance()': 'True' if the queried instance
# is in the MRO.

print(f'\n\t\'isinstance()\' method:\n\tIs integer?: {isinstance(10, int)}')
print(f'\n\tIs Ordered_Integer_List?: {isinstance(ordered_integer_list, Ordered_Integer_List)}')
print(f'\tIs Integer_List?: {isinstance(ordered_integer_list, Integer_List)}')
print(f'\tIs Ordered_List?: {isinstance(ordered_integer_list, Ordered_List)}')
print(f'\tIs Simple_List?: {isinstance(ordered_integer_list, Simple_List)}')
print(f'\tIs object?: {isinstance(ordered_integer_list, object)}')

# True if the object belongs to at least one type.
print(f'\tQuerying various types: {isinstance(ordered_integer_list, (Integer_List, str, Ordered_List))}')

#-------------------------------------------------------------------
