'''
A database is modified by means of this script. A connection pool is
accessed from 'userDAO.py'. In this script is available a set of CRUD
instructions. These instructions take values from objects of type
User. In 'connection.py' script the pool of conenctions is defined . In
'cursor_pool.py' the cursors of each pool's conenctions are managed. The
cursors are called by 'userDAO.py' script.
'''

from logger_base import log
from userDAO import UserDAO
from user import User

print('''

          Input an option:
          1. List users.
          2. Insert a user.
          3. Update a user.
          4. Delete a user.
          5. Exit.
        ''')

opt = int(input('\tInput a option -5 to exit-: '))

while(opt != 5):

    if opt == 1:
       users = UserDAO.select() 
       for user in users:
           log.info(user)

    elif opt == 2:
        usrnme = input('\n\tNew user\n\tInput the username: ')
        psswrd = input('\tInput the password: ')
        usr = User(username = usrnme, password = psswrd)
        inserted_users = UserDAO.insert(usr)
        log.info(f'Number of inserted users: {inserted_users}')

    elif opt == 3:
        idusr = input('\n\tUpdate user\n\tInput the ID_user: ')
        usrnme = input('\tInput the username: ')
        psswrd = input('\tInput the password: ')
        usr = User(idusr, usrnme, psswrd)
        updated_users = UserDAO.update(usr)
        log.info(f'Number of updated users: {updated_users}')

    elif opt == 4:
        idusr = int(input('\n\tDelete user\n\tInput the ID_user: '))
        usr = User(id_user = idusr)
        deleted_users = UserDAO.delete(usr) 
        log.info(f'Number of deleted users: {deleted_users}')

    else:
        print(f'\n\tThe input is not valid.') 

    opt = int(input('\n\tInput a option -5 to exit-: '))

else:
    print(f'\n\tThanks for using this program.\n')

#-------------------------------------------------------------------
