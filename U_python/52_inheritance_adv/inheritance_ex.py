class Class_1:

    def __init__(self) -> None:
        print(f'\tClass_1.__init__')

    def method(self):
        print(f'\tMethod: Class_1')

#-------------------------------------------------------------------

class Class_2(Class_1):

    def __init__(self) -> None:
        print(f'\tClass_2.__init__')
        super().__init__()

    def method(self):
        print(f'\tMethod: Class_2')
        super().method()

#-------------------------------------------------------------------

class Class_3(Class_1):

    def __init__(self) -> None:
        print(f'\tClass_3.__init__')
        super().__init__()

    def method(self):
        print(f'\tMethod: Class_3')
        super().method()

#-------------------------------------------------------------------

class Class_4(Class_2, Class_3):

    def method(self):
        print(f'\tMethod: Class_4')
        super().method()

#-------------------------------------------------------------------

# Testing the inheritance.

class4 = Class_4()
print(f'\n\t{Class_4.__bases__}')
print(f'\n\t{Class_4.__mro__}')

# Methods.
print(f'\n\t{class4.method()}')

#-------------------------------------------------------------------
