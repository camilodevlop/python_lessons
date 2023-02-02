# Vehicle class. Car and Bike inherit from Vehicle.

class Vehicle:
    def __init__(self, color = '', wheels = 0) -> None:
        self._color = color
        self._wheels = wheels

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def wheels(self):
        return self._wheels

    @wheels.setter
    def wheels(self, wheels):
        self._wheels = wheels

    # Overriding the __str__ method of Object.
    def __str__(self):
        return f'Color: {self._color}, Wheels: {self._wheels}'
        
#-------------------------------------------------------------------

class Bike(Vehicle):
    def __init__(self, color = '', wheels = 0, b_type = '') -> None:
        super().__init__(color, wheels)
        self._b_type = b_type

    @property
    def b_type(self):
        return self._b_type

    @b_type.setter
    def b_type(self, b_type):
        self._b_type = b_type

    # Overriding the __str__ method of Vehicle.
    def __str__(self):
        return f'{super().__str__() }, Bike type: {self._b_type}'

#-------------------------------------------------------------------

class Car(Vehicle):
    def __init__(self, color = '', wheels = 0, velocity = 0) -> None:
        super().__init__(color, wheels)
        self.__velocity = velocity

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        self.__velocity = velocity

    # Overriding the __str__ method of Vehicle.
    def __str__(self):
        return f'{super().__str__()}, Velocity: {self.__velocity} Km/h'

#-------------------------------------------------------------------

if __name__ == '__main__':
    vehicle1 = Vehicle('Blue', 3)
    print(f'\n\tVehicle 1-> {vehicle1}')
    
    bike1 = Bike('Red', 2, 'Mountain')
    print(f'\n\tBike 1-> {bike1}')

    car1 = Car('Yellow', 4, 45)
    print(f'\n\tCar 1-> {car1}')
    print(car1.velocity)
    car1.velocity = 60
    print(f'\n\tCar 1-> {car1}')

#-------------------------------------------------------------------
