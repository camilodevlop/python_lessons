from my_module import *
# from my_module import _protected_function

class MyClass:
    def __init__(self) -> None:
        self.my_public_var = 10
        self.my_private_var = 11

#-------------------------------------------------------------------

# An underscore at the end of the word is used to avoid conflicts
# with reserved words.

# This function receive a var named class_.
def function1(name, class_):
    print(f'Name: {name}, Class: {class_}')

#-------------------------------------------------------------------

if __name__ == '__main__':
    obj = MyClass()
    print(f'Public var: {obj.my_public_var}')

    # We shouldn't access attributes or methods marked as private.
    print(f'Private var: {obj.my_private_var}')

    # Functions of the imported module.
    public_function()

    # This functions cannot be accessed using import *.
    # _protected_function()


    function1('Camilo', 'Engineer')

#-------------------------------------------------------------------
