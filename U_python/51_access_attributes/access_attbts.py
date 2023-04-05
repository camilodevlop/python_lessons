# Example of attributes: publics, protected and privates.

class MyClass:

    def __init__(self, public, protected, private) -> None:
        self.public = public
        self._protected = protected
        self.__private = private

obj = MyClass('Public Value', 'Protected Value','Private Value')

# Accessing and modifying the public value.
print(f'\n\t{obj.public}')
obj.public = 'New Public Value'
print(f'\t{obj.public}')

# Accessing and modifying the protected value.
print(f'\n\t{obj._protected}')
obj._protected = 'New Protected Value'
print(f'\t{obj._protected}')

# Accessing and modifying the private value.
print(f'\n\t{obj._MyClass__private}')
obj._MyClass__private = 'New Private Value'
print(f'\t{obj._MyClass__private}')

#-------------------------------------------------------------------
