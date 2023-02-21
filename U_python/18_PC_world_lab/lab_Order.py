# PC world: Computer class.


class Order():
    __order_counter = 0

    def __init__(self, computers = []) -> None:
        self._id_order = Order._increment_order_counter()
        self._computers = list(computers)

    @property
    def id_order(self):
        return self._id_order

    def add_computer(self, computer):
        self._computers.append(computer)

    @classmethod
    def _increment_order_counter(cls):
        cls.__order_counter += 1
        return cls.__order_counter

    def __str__(self) -> str:
        str_computers = ''
        for computer in self._computers:
            str_computers += computer.__str__()

        return f'\n\tOrder ID: {self._id_order}\n{str_computers}'

#-------------------------------------------------------------------
