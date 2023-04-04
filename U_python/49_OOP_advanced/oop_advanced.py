# Class and object attributes.
class Person:
    person_counter = 0

    def __init__(self, name, last_name) -> None:
        self.name = name
        self.last_name = last_name

# Showing the object attributes.
person1 = Person('Camilo', 'Alejandro')
print(f'\n\tObject attributes: {person1.__dict__}')

# An object can't modify a class attribute. The object only can read it.
person1.person_counter = 10
print(f'\tObject attributes: {person1.__dict__}')

# The above attribute hides the class attribute.
print(f'\tClass attribute: {Person.person_counter}')
print(f'\tObject attribute: {person1.person_counter}')

# Creating other object.
person2 = Person('Cordula', 'Benavides')
print(f'\n\tObject attributes: {person2.__dict__}')
print(f'\tClass Attribute - person counter: {person2.person_counter}')

# Creating a class attribute.
Person.person_counter2 = 20
print(f'\tNew class Attribute - person_counter2: {Person.person_counter2}')


#-------------------------------------------------------------------
