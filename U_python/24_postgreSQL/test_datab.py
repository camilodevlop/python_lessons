# Python and Postgresql use.

from re import split
import psycopg2

# Opening the database.
connection = psycopg2.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db'
)

#-------------------------------------------------------------------

'''
# Editing the database.
cursor = connection.cursor()
statement = 'SELECT * FROM person'
cursor.execute(statement)
registers = cursor.fetchall()
print(registers)
'''

# Editing the database.
try:
    with connection:
        with connection.cursor() as cursor:

            '''
            # SELECT instruction.
            # statement = 'SELECT * FROM person'
            # statement = 'SELECT id_person, name FROM person WHERE id_person = %s'
            # statement = 'SELECT * FROM person WHERE id_person = %s'
            statement = 'SELECT * FROM person WHERE id_person IN %s'
            inpuT = input('\n\tInput the id\'s -these must be separated by commas-:\n\t')
            primary_keys = (tuple(inpuT.split(',')),)
            cursor.execute(statement, primary_keys)
            registers = cursor.fetchall()
            for register in registers:
                print(register)
            #print(registers)
            '''
           
            '''
            # INSERT instruction.
            statement = 'INSERT INTO person(name, last_name, email) VALUES(%s, %s, %s)'

            # Inserting a register.
            #values = ('Cordula', 'Benavides', 'cbenavides@mail.com')
            #cursor.execute(statement, values)

            # Inserting multiple registers.
            values = (
                ('Arturo', 'Ovalle', 'aovalle@mail.com'),
                ('Manuel', 'Perez', 'mperez@mail.com'),
                ('Felipe', 'Garcia', 'fgarcia@mail.com'),
            )
            cursor.executemany(statement, values)
            # connection.commit()   It is not necessary if 'connection' is activated by 'with'.
            inserted_registers = cursor.rowcount
            print(f'\n\tInserted registers: {inserted_registers}\n')
            '''

            '''
            # UPDATE instruction.
            statement = 'UPDATE person SET name = %s, last_name = %s, email = %s WHERE id_person = %s'

            # Updating a register.
            #values = ('Lina Maria', 'Benavides Ascuntar', 'lmbenavides@mail.com', 1)
            #cursor.execute(statement, values)

            # Updating multiple registers.
            values = (
               ('Camilo Alejandro', 'castillo', 'cacastillo@mail.com', 2),
              ('Victor Herminsul', 'castillo', 'vhcastillo@mail.com', 5)
            )
            cursor.executemany(statement, values)
            updated_registers = cursor.rowcount
            print(f'\n\tUpdated registers: {updated_registers}\n')
            '''
            # DELETE instruction.
            statement = 'DELETE FROM person WHERE id_person IN %s'

            # Deleting a register.
            #inpuT = input(f'\n\tInput the person id:')
            #values = (inpuT,)
            #cursor.execute(statement, values)

            # Deleting multiple registers.
            inpuT = input('\n\tInput the id\'s -these must be separated by commas-: ')
            values = (tuple(inpuT.split(',')),)
            cursor.execute(statement, values)
            deleted_registers = cursor.rowcount
            print(f'\n\tDeleted registers: {deleted_registers}\n')
except Exception as e:
    print(f'\n\tSomething is wrong: {e}\n')
finally:
    connection.close()      # 'with' doesn't close the connection automatically.

# Closing the database.
# cursor.close()

#-------------------------------------------------------------------
