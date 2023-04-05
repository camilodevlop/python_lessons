# Object representation: (__str__, __repr__, __format__)

class Person:

    def __init__(self, name, last_name) -> None:
        self.name = name
        self.last_name = last_name

    # '__repr__ ' is aimed at the programmers.
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(name = {self.name}, last_name = {self.last_name})'

    # '__str__' is aimed at the final user.
    def __str__(self) -> str:
        return f'{self.__class__.__name__}: {self.name} {self.last_name}'

    # '__format__' its implementation by default is str.
    def __format__(self, __format_spec: str) -> str:
        return f'{self.__class__.__name__}: The name is {self.name} and the last_name is {self.last_name}'


person1 = Person('Camilo', 'Castillo')
print(f'\n\t__repr__: {person1!r}')     # !r ensures that __repr__ is called.

# Using __str__
print('\t__str__:', person1)

# Using __format__
print(f'\t__format__: {person1}')


#-------------------------------------------------------------------
