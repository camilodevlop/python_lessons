# __str__: its aim is to present the information to the user in an
# appropriate way.
# __repr__: its aim is to present the information in an unambiguous way.
# The default implementation of __str__ calls to __repr__.

class Auto:
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color
        
# By default, the class name and the id are printed.
auto = Auto('BMW', '2023', 'Gray')
print(auto)

#-------------------------------------------------------------------

class AutoStr:
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color
       
    def __str__(self) -> str:
        return f'str: Brand: {self.brand}, Year: {self.year}, Color: {self.color}'

    #def __repr__(self) -> str:
    #    return f'repr: Brand: {self.brand}, Year: {self.year}, Color: {self.color}'

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}('
                f'{self.brand!r}, {self.year!r}, {self.color!r})')

# By default, the class name and the id are printed.
auto = Auto('BMW', '2023', 'Gray')
print(auto)

autostr = AutoStr('BMW', '2023', 'Gray')
print(autostr)
print(autostr.__str__())
print(str(autostr))
print('{}'.format(autostr))
print(f'{autostr}')

#-------------------------------------------------------------------

# It's recommendable to use __repr__ rather than __str__.
# Any collection uses __repr__.
print([autostr])
print(f'{autostr!r}')

# We can choose the method.
print(str(autostr))
print(repr(autostr))

#-------------------------------------------------------------------
