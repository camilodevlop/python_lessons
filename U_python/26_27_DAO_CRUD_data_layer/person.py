# Person class.

from logger_base import log

class Person:

    def __init__(self, id_person = None, name = None, last_name = None, email = None) -> None:
        self._id_person = id_person
        self._name = name
        self._last_name = last_name
        self._email = email

    @property
    def id_person(self):
        return self._id_person

    @id_person.setter
    def id_person(self, id_person):
        self._id_person = id_person

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def __str__(self) -> str:
        return f'''
                    ID: {self._id_person}, Name: {self._name},
                    Last name: {self._last_name}, email: {self._email}
                    '''

if __name__ == '__main__':
   person1 = (1, 'Camilo', 'Castillo', 'ccastillo@mail.com') 
   log.debug(person1)

   # Simulating an INSERT: the id_person is not provided.
   person1 = Person(name = 'Camilo', last_name = 'Castillo', email = 'ccastillo@mail.com')
   log.debug(person1)

   # Simulating a DELETE: only the id_person is provided.
   person1 = Person(id_person = 1)
   log.debug(person1)

#-------------------------------------------------------------------
