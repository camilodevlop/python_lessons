# Namedtuples are an extension of the tuple type. These are useful
# to define classes. The attributes are immutable.

from collections import namedtuple

# Defining a class that contains immutable attributes.
Person1 = namedtuple('Person1', 'name surname age')
person1 = Person1('Camilo', 'Castillo', 36)

# A method __repr__ is defined automatically.
print(person1)

# The attributes can be difined by a list.
Person2 = namedtuple('Person2', [ 'name', 'surname', 'age' ])
person2 = Person2('Lina', 'Castillo', 29)
print(person2)

# Attributes can be accessed by name.
print(f'Name: {person2.name}')
print(f'Surname: {person2.surname}')
print(f'Age: {person2.age}')

# Attributes can be accessed by name.
print(f'Name: {person2[0]}')
print(f'Surname: {person2[1]}')
print(f'Age: {person2[2]}')

#-------------------------------------------------------------------

# The values can be converted to a tuple.
print(tuple(person2))

# Unpacking attributes. 
name, surname, age = person2
print(f'Person attributes: {name}, {surname}, {age}')

# Unpacking as an argument.
print(*person2)

# Tuples and namedtuples are immutable.
# person2.age = 30

#-------------------------------------------------------------------

# Subclasses of namedtuple.
class Person3(Person2):
    def uppercases(self):
        return f'Full name: {self.name.upper()} {self.surname.upper()}'

person3 = Person3('Córdula', 'Benavides', 65)
print(person3)
print(person3.uppercases())

# Another way to extend the class (using namedtuple).
Person4 = namedtuple('Person4', Person2._fields + ('email',))
person4 = Person4('Victor', 'Castillo', 65, 'victor@castillo.com')
print(person4)

#-------------------------------------------------------------------

# Built-in aid methods of namedtuple.
print(person4._fields)
dict_person4 = person4._asdict()
print(dict_person4)

#-------------------------------------------------------------------
