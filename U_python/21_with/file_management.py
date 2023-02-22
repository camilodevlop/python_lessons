# File_Management class.

class File_Management:
    def __init__(self, name) -> None:
        self.name = name

    def __enter__(self):
        print(f'\n\tAccessing the resource')
        self.name = open(self.name, 'r', encoding = 'utf8')
        return self.name

    def __exit__(self, exception_type, exception_value, traceback):
        print(f'\tReleasing the resource.')
        if self.name:
            self.name.close()

#-------------------------------------------------------------------
