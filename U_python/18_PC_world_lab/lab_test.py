# PC world: Test.
'''
In this project the lessons of variables, types, operators,
control statements, loops, collections, functions, and OOP are applied.

The basic classes of a computer store are defined. The computers
can be customized according to the monitor, keyboard, and mouse.
One or several computers can be added to a shipping order.
'''

from lab_Order import Order
from lab_Computer import *

print('\n\n\tTesting the project PC World\n\t')

computer = Computer('ASUS', Monitor('Acer', 27), Keyboard('Bluetooth', 'Log'), Mouse('Wire', 'Genius'))
computer2 = Computer('Apple', Monitor('St display', 27), Keyboard('Wire', 'Magic'), Mouse('Bluetooth', 'Magic M'))

computers = [computer, computer2]
order1 = Order(computers)

computer3 = Computer('Ryzer Blade', Monitor('RZ display', 24), Keyboard('Bluetooth', 'Ryzer'), Mouse('Wire', 'Corsair'))
order1.add_computer(computer3)

print(order1)

#-------------------------------------------------------------------
