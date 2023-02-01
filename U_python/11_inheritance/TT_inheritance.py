# Python: simple inheritance. overriding the __str__ method.

class Person:
    def __init__(self, name = '', age = 0) -> None:
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    # Overriding the __str__ method of Object.
    def __str__(self):
        return f'Person: {self._name}, Age: {self._age}'

#-------------------------------------------------------------------

class Employee(Person):
    def __init__(self, name, age, salary = 0) -> None:
        super().__init__(name, age)
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary
 
    # Overriding the __str__ method of Person.
    def __str__(self):
        return f'{super().__str__()}, Salary: {self._salary}'

#-------------------------------------------------------------------

if __name__ == '__main__':
    employee1 = Employee('Camilo', 25, 10000)
    print(employee1.name)
    employee1.age = 30
    print(employee1.age)

#-------------------------------------------------------------------
