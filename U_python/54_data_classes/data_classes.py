from dataclasses import dataclass
from typing import ClassVar

@dataclass(eq = True, frozen = True)
class Home:
    street: str
    number: int = 0

@dataclass(eq = True, frozen = True)
class Person():
    name: str
    surname: str
    home: Home
    person_counter: ClassVar[int] = 0

    # Useful to check the values.
    def __post_init__(self):
        if not self.name:
            raise ValueError(f'\n\tNo value is assigned to \'name\'.')

#-------------------------------------------------------------------

home1 = Home('Angeles', 25)
person1 = Person('Camilo' , 'Alejandro', home1)
print(f'{person1!r}')

# Class variable.
print(f'Class Variable: {Person.person_counter}')

# Instance variables.
print(f'Instance Variables: {person1.__dict__}')

# Checking the equality between two objects.
home2 = Home('America', 123)
person2 = Person('Lina', 'Maria', home2)
print(f'\n\tAre the objects the same? {person1 == person2}')

# This class is enabled for use in collections (frozen = True).
clltn = {person1, person2}
print(f'\n\tUsing \'Person\' in collections: {clltn} ')


#-------------------------------------------------------------------
