# PC world: Input_Devices class.

class Input_Devices:
    def __init__(self, input_type = 'unspecified', brand = 'unspecified') -> None:
        self._input_type = input_type
        self._brand = brand

    @property
    def input_type(self):
        return self._input_type

    @input_type.setter
    def input_type(self, input_type):
        self._input_type = input_type

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    def __str__(self) -> str:
        return f'\n\tInput type: {self._input_type}, Brand: {self._brand}'

#-------------------------------------------------------------------
