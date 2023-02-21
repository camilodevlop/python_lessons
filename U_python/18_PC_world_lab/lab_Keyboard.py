# PC world: Keyboard class.

from lab_input_dev import Input_Devices

class Keyboard(Input_Devices):
    __keyboard_counter = 0

    def __init__(self, input_type = 'unspecified', brand = 'unspecified') -> None:
        self._id_keyboard = Keyboard._increment_keyboard_counter()
        Input_Devices.__init__(self, input_type, brand)
    
    @property
    def id_keyboard(self):
        return self._id_keyboard

    @classmethod
    def _increment_keyboard_counter(cls):
        cls.__keyboard_counter += 1
        return cls.__keyboard_counter

    def __str__(self) -> str:
        return f'Keyboard ID: {self._id_keyboard} {Input_Devices.__str__(self)}'
    
    """
    def __del__(self):
        print(f'\n\n\tDeleted Keyboard ID: {self._id_keyboard} {Input_Devices.__str__(self)}')
        Keyboard.__keyboard_counter -= 1
        print(f'\tKeyboard counter = {Keyboard.__keyboard_counter}')
    """
#-------------------------------------------------------------------
