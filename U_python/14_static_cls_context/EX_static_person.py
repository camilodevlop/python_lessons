# Static (class) context in Python.

class Person:
    people_counter = 0

    def __init__(self, person, age) -> None:
        self._id_person = Person._increment_people_counter()
        self._person = person
        self._age = age

    @property
    def id_person(self):
        return self._id_person

    @property
    def person(self):
        return self._person

    @person.setter
    def person(self, person):
        self._person = person

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @classmethod
    def _increment_people_counter(cls):
        cls.people_counter += 1
        return cls.people_counter


    def __str__(self) -> str:
        return f'Person: {self._id_person}. {self._person} {self._age}'

    def __del__(self):
        print(f'\tPerson deleted: {self.__str__()}')
        Person.people_counter -= 1
        print(f'\tPerson counter = {Person.people_counter}')


#-------------------------------------------------------------------

person1 = Person('Camilo', 35)
print(f'\t{person1}')

person2 = Person('Lina', 27)
print(f'\t{person2}\n')

#-------------------------------------------------------------------
