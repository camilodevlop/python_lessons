# Polymorphism in python.

from EX_polymorphism import Employee
from EX_polymorphism2 import Executive

def print_details(object):
    print(f'\n\t{object}\n\t{type(object)}\n')

employee = Employee('Camilo Alejandro', 12000)
print('\n\tPolymorphism in Python.')
print_details(employee)

executive = Executive('Lina Maria', 15000, 'System')
print_details(executive)

if (isinstance(executive, Executive)):
    print(f'\n\tTesting isinstance():\n\t{executive.department}')

#-------------------------------------------------------------------
