# A decorator is a function that takes one function as argument
# and return another. It is used to extend functionalities.

def func_decorator(f_to_be_decorated):
    def decorated_function(*args, **kwargs):
        print(f'\n\tBefore running the function.')
        result = f_to_be_decorated(*args, **kwargs)
        return result
        print(f'\tAfter running the function.')

    return decorated_function

@func_decorator
def show_message():
    print('\tShow message function.')

show_message()

@func_decorator
def printer():
    print('\tShow message function: PRINTER.')

printer()

@func_decorator
def add(a, b):
    return a + b

result = add(4, 3)
print(f'\n\tResult: {result}')

#-------------------------------------------------------------------
