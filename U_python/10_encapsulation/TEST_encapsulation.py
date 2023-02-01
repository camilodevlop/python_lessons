# Python: using the Person class fron the module -file-
# EX_encapsulation.py.

from EX_encapsulation import Person

print('\n\tTesting modules and encapsulation:\n')

print('Object creation'.center(30,'-'))
persona2 = Person('Lina', 'María', 25)
persona2.show_details()

print('Object destruction'.center(30,'-'))
del persona2

#-------------------------------------------------------------------
