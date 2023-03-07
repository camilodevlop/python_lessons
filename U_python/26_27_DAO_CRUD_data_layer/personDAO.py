# Class personDAO:
# DAO: Data Access Object.
# CRUD: Create-Read-Update-Delete

from logging import debug
from cursor_pool import Cursor_Pull
from person import Person
from logger_base import log

class PersonDAO:
    _SELECT = 'SELECT * FROM person ORDER BY id_person'    
    _INSERT = 'INSERT INTO person(name, last_name, email) VALUES (%s,%s,%s)'
    _UPDATE = 'UPDATE person SET name = %s, last_name = %s, email = %s WHERE id_person = %s'
    _DELETE = 'DELETE FROM person WHERE id_person = %s'

    @classmethod
    def select(cls):
        with Cursor_Pull() as cursor:
           cursor.execute(cls._SELECT)
           registers = cursor.fetchall()
           persons = []
           for register in registers:
               person = Person(register[0], register[1], register[2], register[3])
               persons.append(person)
           return persons

    @classmethod
    def insert(cls, person):
        with Cursor_Pull() as cursor:
            log.debug(f'Person to be inserted: {person}')
            values = (person.name, person.last_name, person.email)
            cursor.execute(cls._INSERT, values)
            log.debug(f'Inserted person: {person}')
            return cursor.rowcount

    @classmethod
    def update(cls, person):
        with Cursor_Pull() as cursor:
            log.debug(f'Person to be updated: {person}')
            values = (person.name, person.last_name, person.email, person.id_person)
            cursor.execute(cls._UPDATE, values)
            log.debug(f'Updated person: {person}')
            return cursor.rowcount

    @classmethod
    def delete(cls, person):
        with Cursor_Pull() as cursor:
            log.debug(f'ID person to be deleted: {person.id_person}')
            values = (person.id_person,)
            cursor.execute(cls._DELETE, values)
            log.debug(f'Deleted person: {person}')
            return cursor.rowcount
    
#-------------------------------------------------------------------

if __name__ == '__main__':

    # Person object insertion.
    #person1 = Person(name = 'Eder', last_name = 'Peña', email = 'epena@mail.com')
    #inserted_persons = PersonDAO.insert(person1)
    #log.debug(f'Number of inserted persons: {inserted_persons}')

    # Person object update.
    person2 = Person(1,  'Lina', 'Castillo', 'lcastillo@mail.com')
    updated_persons = PersonDAO.update(person2)
    log,debug(f'Number of updated persons: {updated_persons}')

    # Person object deletion:
    person3 = Person(23)
    deleted_persons = PersonDAO.delete(person3)
    log.debug(f'Number of deleted person: {deleted_persons}')

    # Person object selection.
    persons = PersonDAO.select()
    for person in persons:
        log.debug(person)

#-------------------------------------------------------------------
