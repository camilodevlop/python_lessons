
class Dog:
    no_paws = 4

    def __init__(self, name) -> None:
        self.name = name

layla = Dog('Layla')
venus = Dog('Venus') 

# Each object has its own name attribute.
print(layla.name, venus.name)

# The class variable can be accessed by both the classes and the instances.
print(layla.no_paws, venus.no_paws, Dog.no_paws)

# Instance vars can't be accessed from the class.
# print(Dog.name)

#-------------------------------------------------------------------

Dog.no_paws = 5
print(layla.no_paws, venus.no_paws, Dog.no_paws)

layla.no_paws = 7   # It creates an instance var. The class var is hidden.
print(layla.no_paws, venus.no_paws, Dog.no_paws)
print(layla.no_paws, layla.__class__.no_paws)

# Definition of a class variable.
Dog.name = 'Dog class'
print(layla.name, venus.name, Dog.name)

# Defining a class var that is not in the objects.
Dog.no_ears = 2
print(layla.no_ears, venus.no_ears, Dog.no_ears)

#-------------------------------------------------------------------

# Object counter of a class.
class WrongObjectCounter:
    no_intances = 0

    def __init__(self) -> None:
        self.no_intances += 1

print(f'Wrong object counter...')
print(WrongObjectCounter.no_intances)
print(WrongObjectCounter().no_intances)
print(WrongObjectCounter().no_intances)
print(WrongObjectCounter.no_intances)

#-------------------------------------------------------------------

# Corrected implementation.
class ObjectsCounter:
    no_instances = 0
    
    def __init__(self) -> None:
        self.__class__.no_instances += 1

print(f'Instances counter:')
print(ObjectsCounter.no_instances)
print(ObjectsCounter().no_instances)
print(ObjectsCounter().no_instances)
print(ObjectsCounter().no_instances)
print(ObjectsCounter().no_instances)
print(ObjectsCounter.no_instances)


#-------------------------------------------------------------------
