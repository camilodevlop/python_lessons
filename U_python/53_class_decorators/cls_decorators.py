from inspect import signature
#from generators import generator

# Class decorators: These let .to transform the class
# -metaprogramming-.

def decorator_repr(cls):
    print(f'\n\tDecorator execution')
    print(f'\tClass of the object: {cls.__name__}')

    # Exploring the class attribute by means of the 'vars' method.
    attributes = vars(cls)
    #for name, attribute in attributes.items():
    #    print(name, attribute)

    # Checking if the '__init__' method has been overridden.
    if '__init__' not in attributes:
        raise TypeError(f'{cls.__name__} has not overridden the __init__ method.')

    signature_init = signature(cls.__init__)
    print(f'\n\n\tSignature of the __init__ method: {signature_init}')
    init_parameters = list(signature_init.parameters)[1:]
    print(f'\tInit parameters: {init_parameters}')

    # For each parameters is checked if it has an associated property.
    for parameter in init_parameters:
        is_property_method = isinstance(attributes.get(parameter), property)
        if not is_property_method:
            raise TypeError(f'\n\tThere is not a property method for {parameter}')
    
    # Creating the '__repr__' method dynamically.
    def repr_method(self):
        class_name = self.__class__.__name__

        generator_arg = (f'{name} = {getattr(self, name)!r}' for name in init_parameters)
        list_arg = list(generator_arg)
        args = ', '.join(list_arg)

        return f'{class_name} ({args})'

    setattr(cls, '__repr__', repr_method)

    return cls
    
#-------------------------------------------------------------------

@decorator_repr
class Person:

    def __init__(self, name, surname, age) -> None:
        print(f'\n\tInit execution.')
        self._name = name
        self._surname = surname
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def age(self):
        return self._age

#-------------------------------------------------------------------

person1 = Person('Camilo', 'Castillo', 35)
print(person1)

person2 = Person('Lina', 'Benavides', 28)
print(person2)

#-------------------------------------------------------------------
