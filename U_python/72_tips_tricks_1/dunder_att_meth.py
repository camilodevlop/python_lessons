
class Father:
    def __init__(self) -> None:
        # if vars are defined using dunder, name mangling is not applied.
        self.__dunder_var__ = 10
        self.__private_var = 1000

#-------------------------------------------------------------------

if __name__ == '__main__':
    father = Father()
    print(dir(father))
    print(f'Accessing to dunder var: {father.__dunder_var__}')
    print(f'Accessing to private var (name mangling): {father._Father__private_var}')

#-------------------------------------------------------------------
