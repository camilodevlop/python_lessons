# Polymorphism in python.

class Employee:
    def __init__(self, name, salary) -> None:
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    def __str__(self) -> str:
        return f'Employee: {self._name}, Salary = {self._salary}'

#-------------------------------------------------------------------
