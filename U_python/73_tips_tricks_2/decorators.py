# A decorator is a reutilizable code.
# These allow us to extend and modify the behavior of the functions.

def wrapper_decorator(function_to_decorate):
    print('We are in the wrapper function...')
    return function_to_decorate

# Using the decorator.
def greetings():
    return 'Greetings from my function...'

# Manually calling the decorator (It's not common.).
returned_function = wrapper_decorator(greetings)
print(returned_function())

# Automatically calling the decorator.
@wrapper_decorator
def decorated_greetings():
    return 'Greetings from my decorated function...'

print(decorated_greetings())

#-------------------------------------------------------------------

# Using a decorator to convert the text to uppercase.
def uppercases(function_to_decorate):
    def wrapper_function():
        original_result = function_to_decorate()
        modified_result = original_result.upper()
        return modified_result
    
    return wrapper_function

@uppercases
def greetings_lowercases():
    return 'hello...'

print(greetings_lowercases())

#-------------------------------------------------------------------

# Multiple decorators.
# <strong><em>Hello</em></strong>

def strong(function):
    def wrapper_function():
        print('3')
        return '<strong>' + function() + '</strong>'

    print('2')
    return wrapper_function

def emphasis(function):
    def wrapper_function():
        print('4')
        return '<em>' + function() + '</em>'

    print('1')
    return wrapper_function

@strong
@emphasis
def greetings_html():
    print('5')
    return 'hello'

print(greetings_html())

#-------------------------------------------------------------------

# Including arguments in decorators.

def arguments_in_decorators(function):
    def wrapper_function(*args, **kwargs):
        print('args: ', args)
        print('kwargs: ', kwargs)

        list_arg = []
        for index, tupla_value in enumerate(args):
            list_arg.append(args[index].upper())

        list_arg.append('New value 1')
        list_arg.append('New value 2')
        kwargs['value_1'] = 'New value 1'
        kwargs['value_2'] = 'New value 1'

        return function(*list_arg, **kwargs)

    return wrapper_function

@arguments_in_decorators
def greeting_funct(degree, name, *args, **kwards):
    print(f'{degree}. {name}')
    print('args: ', args)
    print('kwards: ', kwards)

greeting_funct('Engineer', 'Camilo Alejandro')

#-------------------------------------------------------------------
