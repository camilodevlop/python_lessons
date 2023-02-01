# Python: encapsulation.
# _ It encapsulates the value, however it can be changed.
# __ It encapsulates the value and cannot be changed.

class Person:

    def __init__(self, name = '', surname = '', age = 0) -> None:
        self._name = name
        self._surname = surname
        self._age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def surname(self):
        return self._surname
    
    @surname.setter
    def surname(self, surname):
        self._surname = surname

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age

    def __del__(self):
        print(f'\tType object deleted: Person. Details: {self._name} {self._surname}')

    def show_details(self):
        print(f'\tPerson: {self._name} {self._surname} {self._age}')

#-------------------------------------------------------------------

if __name__ == '__main__':
    print(f'\n\tClass Person: encapsulation.\t')

    person1 = Person('Camilo', 'Castillo', 35)
    person1.show_details()

    print('\n\tAttribute Modification:')
    person1.name = 'Camilo Alejandro'
    print(f'\tModified name: {person1.name}')
    person1.surname = 'Castillo Benavides'
    print(f'\tModified surname: {person1.surname}')
    person1.age = 25
    print(f'\tModified age: {person1.age}\n')
    person1.show_details()

#-------------------------------------------------------------------
