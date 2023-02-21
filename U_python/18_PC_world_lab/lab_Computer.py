# PC world: Computer class.

from lab_Keyboard import Keyboard
from lab_Monitor import Monitor
from lab_Mouse import Mouse

class Computer(Monitor, Keyboard, Mouse):
    __computer_counter = 0

    def __init__(self, name, monitor, keyboard, mouse) -> None:
       self._id_computer = Computer._increment_computer_counter()
       self._name = name
       self._monitor = monitor
       self._keyboard = keyboard
       self._mouse = mouse

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @classmethod
    def _increment_computer_counter(cls):
        cls.__computer_counter += 1
        return cls.__computer_counter

    def __str__(self) -> str:
        return f'''
        Computer ID: {self._id_computer} Name: {self._name}

        {self._monitor}
        {self._keyboard}
        {self._mouse}
        '''

#-------------------------------------------------------------------
'''
mon = Monitor('Acer', 27)
computer = Computer('ASUS', mon, Keyboard('Bluetooth', 'Log'), Mouse('Wire', 'Genius'))
print(computer)
computer2 = Computer('Apple', Monitor('St display', 27), Keyboard('Wire', 'Magic'), Mouse('Bluetooth', 'Magic M'))
print(computer2)
'''
