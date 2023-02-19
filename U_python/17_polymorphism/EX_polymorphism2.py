# Polymorphism in python.

from EX_polymorphism import Employee


class Executive(Employee):
    def __init__(self, name, salary, department) -> None:
        Employee.__init__(self, name, salary)
        self._department = department

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        self._department = department

    def __str__(self) -> str:
        return f'{Employee.__str__(self)}, Department: {self._department}'

#-------------------------------------------------------------------

if __name__ == '__main__':
    executive1 = Executive('Camilo Alejandro', 3500, 'Sales')
    print(f'\n\tPolymorphism in Python.\n\t{executive1.__str__()}\n')

#-------------------------------------------------------------------
