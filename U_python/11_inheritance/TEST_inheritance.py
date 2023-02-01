# Python: using the Person and Employee classes from the module -file-
# TT_inheritance.py

from TT_inheritance import *

person1 = Person('Camilo Alejandro', 25)
print(f'\n\t{person1}')      # print() calls the overridden __str__.

employee1 = Employee('Lina María', 20, 10000)
print(f'\n\t{employee1}')    # print() calls the overridden __str__.

#-------------------------------------------------------------------
