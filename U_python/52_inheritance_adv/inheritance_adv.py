# Object initialization order.

class Parent:
    
    def __init__(self) -> None:
        print('Parent initializer.')

    def method(self):
        print('Parent method.')


class Son(Parent):
    def __init__(self) -> None:
        Parent.__init__(self)
        print('Son initializer.')

    # Overriding the Parent's method.
    def method(self):
        Parent.method(self)
        print('Son: Parent method overridden.')


# parent1 = Parent()
# parent1.method()

son1 = Son()
son1.method()

#-------------------------------------------------------------------

# Example of simple inheritance.

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

class Ordered_List(Simple_List):

    def __init__(self, elements = []) -> None:
        Simple_List.__init__(self, elements)
        self.order()

    def add_element(self, element):
        super().add_element(element)
        self.order()

class Integer_List(Simple_List):

    def __init__(self, elements = []) -> None:
        for element in elements:
            self._validate(element)
        
        Simple_List.__init__(self, elements)
    
    def _validate(self, element):
        if not isinstance(element, int):
            raise ValueError(f'\n\tIt is not an int value: {element}')

    # Overriding the method 'add_element' of the 'Simple_List' class.
    
    def add_element(self, element):
        self._validate(element)
        super().add_element(element)

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

#-------------------------------------------------------------------
