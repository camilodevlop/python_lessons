from contextlib import contextmanager
from typing import ContextManager, final


with open('72_tips_tricks_1/test', 'w') as file:
    file.write('Hello from Python.')

'''
# The code below is equivalent.
file = open('72_tips_tricks_1/test', 'w')

try:
    file.write('Hello from Python 2')
finally:
    file.close()

# The code below doesn't ensure resource closure.
file = open('72_tips_tricks_1/test', 'w')
file.write('Hello from Python 3')
file.close()
'''

#-------------------------------------------------------------------

# Management of the Context Manager for Classes.
# 1. Using the functions of (__enter__) and (__exit__)
# 2. Using the 'contextlib' library.

# Option 1.
class FileManagement:
    def __init__(self, name) -> None:
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exx_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Option 2.
@contextmanager
def file_management(name, ch = 0):
    try:
        file = open(name, 'w')
        ch += 1
        print(ch)
        yield file
    finally:
        ch -= 1
        print(ch)
        file.close()

# Indenter exercise.
class Indenter():
    def __init__(self) -> None:
        self.level = 0
    
    def __enter__(self):
        self.level += 1
        self

    def __exit__(self, exx_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print('   ' *self.level + text) 

# Indenter exercise using contextlib.
class Indenter2():
    def __init__(self) -> None:
        self.level = 0

    @contextmanager
    def indenter_func(self):
        try:
            self.level += 1
            yield self
        finally:
            self.level -= 1
    
    def print(self, text):
        print('   '*self.level + text) 

#-------------------------------------------------------------------

if __name__ == '__main__':

    # Option 1.
    with FileManagement('72_tips_tricks_1/test') as file:
        file.write('Test using classes.')

    # Option 2.
    with file_management('72_tips_tricks_1/test', 0) as file:
        file.write('Test using the contextmanager library.')
        print('Pause')
        file.write('\nBye')

    # Test of the Indenter Class.
    indenter = Indenter()
    with indenter:
        indenter.print('First level.')
        with indenter:
            indenter.print('Second level.')
            indenter.print('Second level continuation.')
            with indenter:
                indenter.print('Third level.')
                indenter.print('Third level continuation.')

    # Test of the Indenter Class based on contextlib.
    print()
    indenter2 = Indenter2()
    with indenter2.indenter_func():
        indenter2.print('First level.')
        indenter2.print('First level continuation.')
        with indenter2.indenter_func():
            indenter2.print('Second level.')
            indenter2.print('Second level continuation.')
            with indenter2.indenter_func():
                indenter2.print('Third level.')
                indenter2.print('Third level continuation.')
        indenter2.print('End of the First level.')

#-------------------------------------------------------------------
