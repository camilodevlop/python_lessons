# Transactions management using Python and PostgreSQL.

import psycopg2 as db

# Opening the database.
connection = db.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db'
)

#-------------------------------------------------------------------

'''
try:
    cursor = connection.cursor()
    statement = 'INSERT INTO person(name, last_name, email) VALUES(%s, %s, %s)'
    values = ('Luis', 'Garcia', 'lfgarcia@mail.com')
    cursor.execute(statement, values)

    statement = 'UPDATE person SET name = %s, last_name = %s, email = %s WHERE id_person = %s'
    values = ('Lina', 'Castillo', 'lcastillo@mail.com',1)
    cursor.execute(statement, values)

    connection.commit()
    print(f'\n\tThe transaction has been completed -commit() done-.\n')
except Exception as e:
    connection.rollback()
    print(f'\n\tSomething is wrong: {e}\n\tThe rollback() was called.\n')
finally:
    connection.close()
'''

#-------------------------------------------------------------------
# Using 'with'.

try:
    with connection:
        with connection.cursor() as cursor:
            statement = 'INSERT INTO person(name, last_name, email) VALUES(%s, %s, %s)'
            values = ('Manuel', 'Perez', 'mperez@mail.com')
            cursor.execute(statement, values)

            statement = 'UPDATE person SET name = %s, last_name = %s, email = %s WHERE id_person = %s'
            values = ('Lina Maria', 'Castillo', 'lmcastillo@mail.com',1)
            cursor.execute(statement, values)

            # connection.commit() # This is automatically completed if 'with' is used.
            # print(f'\n\tThe transaction has been completed -commit() done-.\n')
except Exception as e:
    # connection.rollback()       # This is automatically completed if 'with' is used.
    print(f'\n\tSomething is wrong: {e}\n\tThe rollback() was called automatically.\n')
finally:
    connection.close()

print(f'\n\tThe transaction has been completed -commit() done automatically.-.\n')
#-------------------------------------------------------------------
