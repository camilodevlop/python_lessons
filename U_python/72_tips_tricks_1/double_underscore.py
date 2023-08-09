# The double underscore affects the access of attributes and methods.

class Father:
    def __init__(self):
        self.public_var = 1
        self._protected_var = 2
        self.__private_var = 3

    def get_private_var(self):
        return self.__private_var

    def __private_method(self):
        print('Accessing the private method from the Father class...')


class Son(Father):
    def __init__(self):
        super().__init__()

        self.public_var = 'Overwritten var = 1'
        self._protected_var = 'Overwritten var = 2'
        self.__private_var = 'Overwritten var = 3'

    def __private_method(self):
        print('Accessing the private method from the Son class...')

#-------------------------------------------------------------------

# Testing using a global variable.
_Test__global_var = 10 

class Test:
    def get_var(self):
        return __global_var

#-------------------------------------------------------------------

if __name__ == '__main__':
    father = Father()
    print(dir(father))

    # Testing the Father class.
    print(f'Public var: {father.public_var}')
    print(f'Protected var: {father._protected_var}')
    # print(f'Private var sends an error: {father.__private_var}')
    # Using name mangling.
    print(f'Private var using name mangling: {father._Father__private_var}')
    print(f'Accessing a private var by a function: {father.get_private_var()}')

    # Testing the Son class.
    son = Son()    
    print(f'Public var accessed from the Son class: : {son.public_var}')
    print(f'Protected var accessed from the Son class: : {son._protected_var}')
    # Error.
    # print(f'Private var accessed from the Son class: : {son.__private_var}')
    # Using name mangling.
    print(f'Private var using name mangling (Son case): {son._Son__private_var}')
    print(f'Private var using name mangling (Father case): {son._Father__private_var}')

    # It is possible to use private methods.
    # father.__private_method()
    father._Father__private_method()
    son._Father__private_method()
    son._Son__private_method()

    # Accessing the global var.
    print(f'Accessing the global var: {_Test__global_var}')

    # Using name mangling and the Test class to access the global var.
    test = Test()
    print(f'Name mangling and the Test class to access the global var: {test.get_var()}')

#-------------------------------------------------------------------
