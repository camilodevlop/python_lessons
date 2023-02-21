# PC world: Mouse class.

from lab_input_dev import Input_Devices

class Mouse(Input_Devices):

    __mouse_counter = 0

    def __init__(self, input_type = 'unspecified', brand = 'unspecified') -> None:
        self._id_mouse = Mouse._increment_mouse_counter()
        Input_Devices.__init__(self, input_type, brand)
    
    @property 
    def id_mouse(self):
        return self._id_mouse

    @classmethod
    def _increment_mouse_counter(cls):
        cls.__mouse_counter += 1
        return cls.__mouse_counter

    def __str__(self) -> str:
        return f'Mouse ID: {self._id_mouse} {Input_Devices.__str__(self)}'

    """
    def __del__(self):
        print(f'\n\n\tDeleted mouse ID: {self._id_mouse} {Input_Devices.__str__(self)}')
        Mouse.__mouse_counter -= 1
        print(f'\tMouse counter = {Mouse.__mouse_counter}')
    """
#-------------------------------------------------------------------
