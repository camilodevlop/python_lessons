# Overloading constructors simulation for Python.

class Person:

    def __init__(self, name, last_name) -> None:
        self.name = name
        self.last_name = last_name

    @classmethod
    def create_person(cls):
        return cls(None, None)      # It calls the __init__ method.

    @classmethod
    def create_person_values(cls, name, last_name):
        return cls(name, last_name)

    def __str__(self) -> str:
        return f'Name: {self.name}, Last_name: {self.last_name}'


person1 = Person('Camilo', 'Alejandro')
print(f'\n\t{person1}')

person2 = Person.create_person()
print(f'\n\t{person2}')

person3 = Person.create_person_values('Lina', 'Castillo')
print(f'\n\t{person3}')

#-------------------------------------------------------------------

class Temperature_converter:
    MAX_CELSIUS = 100
    MAX_FAHRENHEIT = 100
    
    @classmethod
    def c_f(cls, celsius):
        if celsius > cls.MAX_CELSIUS:
            raise ValueError(f'Celsius temperature too high: {celsius}')
        
        return celsius * 9/5 + 32
    
    @classmethod
    def f_c(cls, fahrenheit):
        if fahrenheit > cls.MAX_FAHRENHEIT:
            raise ValueError(f'Fahrenheit temperature too high: {fahrenheit}')
        
        return (fahrenheit - 32) * 5/9

if __name__ == '__main__':
    result = Temperature_converter.c_f(15)
    print(f'\n\tTemperature converter.\n\tC_F(15): {result:.2f}')

    result = Temperature_converter.f_c(59)
    print(f'\n\tF_C(15): {result:.2f}')

#-------------------------------------------------------------------
