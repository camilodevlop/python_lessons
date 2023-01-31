# Classes in the Python language.
class Person:

    def __init__(self, name = '', surname = '', age = 0, lst = [], *args, **kwargs) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.lst = lst       # Using lists.
        self.args = args     # Using tuples.
        self.kwargs = kwargs # Using dictionaries.

    def show_details(self):
        print(f'\tPerson: {self.name} {self.surname} {self.age} {self.lst} {self.args} {self.kwargs}')

#-------------------------------------------------------------------

print(f'\n\tClass Person.\t')

person1 = Person('Camilo', 'Castillo', 35, [1,2,3,4,5], ('t1','t2','t3','t4'), g = 'male')
person1.show_details()

print('\n\tAttribute Modification:')
person1.name = 'Camilo Alejandro'
person1.surname = 'Castillo Benavides'
person1.age = 25
person1.show_details()
person1.phone = '55555'
print(f'\tPhone: {person1.phone}')

person2 = Person('Lina', 'Castillo', 28, [6,7,8,9,10], ('t1','t2','t3','t4'), g = 'female')
print('\t')
person2.show_details()
person2.lst[3] = 20
person2.kwargs['height'] = 1.71
person2.show_details()

#-------------------------------------------------------------------
