# PC world: Keyboard class.

class Monitor:
    __monitor_counter = 0

    def __init__(self, brand = 'unspecified', size = 0) -> None:
        self._id_monitor = Monitor._increment_monitor_counter()
        self._brand = brand
        self._size = size

    @property
    def id_monitor(self):
        return self._id_monitor
    
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    @classmethod
    def _increment_monitor_counter(cls):
        cls.__monitor_counter += 1
        return cls.__monitor_counter

    def __str__(self) -> str:
        return f'Monitor ID: {self._id_monitor}\n\tSize: {self._size} inches, Brand: {self._brand}'

    """
    def __del__(self):
        print(f'\n\n\tDeleted monitor ID: {self._id_monitor}\n\tSize: {self._size}, Brand: {self._brand}')
        Monitor.__monitor_counter -= 1
        print(f'\tMonitor counter = {Monitor.__monitor_counter}')
    """
#-------------------------------------------------------------------
