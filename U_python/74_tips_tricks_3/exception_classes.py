# Creating a class to define a custom exception class.

def validate(full_name):
    if len(full_name) < 3:
        raise ValueError
    else:
        print('Successful validation...')

name = 'Ca'
# validate(name)

#-------------------------------------------------------------------

'''
# Custom validation
# The class name indicates what the problem is.
class TooShortName(ValueError):
    pass

def improved_validate(full_name):
    if len(full_name) < 3:
        raise TooShortName(full_name)
    else:
        print('Successful validation...')

improved_validate(name)
'''

#-------------------------------------------------------------------

# It's a good idea to define a base class and then to extend the others.
class BaseExceptionClass(TypeError):
    pass

class TooShortName(BaseExceptionClass):
    pass

def improved_validate(full_name):
    if len(full_name) < 3:
        raise TooShortName(full_name)
    else:
        print('Successful validation...')

try:
    improved_validate(name)
except BaseExceptionClass as e:
    print(f'{type(e).__name__}: {e}, Line: {e.__traceback__.tb_lineno} in {__file__}')

#-------------------------------------------------------------------
