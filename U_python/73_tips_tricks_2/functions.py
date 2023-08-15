# In Python, functions are first class citizens.

def uppercases(text):
    return text.upper()

def lowercases(text):
    return text.lower()

print(uppercases('Hello'))

#-------------------------------------------------------------------

# Using a function as an object.
function_var = uppercases
print(f'uppercases function: {uppercases}')
print(f'Function variable: {function_var}')

# Using the function variable at any time.
print(function_var('New Text.'))

# The original reference can be suppressed to demonstrate that
# objects are functions.
# del uppercases
print(function_var('Greetings...'))
print(f'Default function\'s name: {function_var.__name__}')

#-------------------------------------------------------------------

# How to save a function in a data structure?
functions_list = [uppercases, function_var, str.upper]
print(functions_list)

for function in functions_list:
    print(function, function('Greetings from the function'))

print(functions_list[1]('Greetings from function_var.'))

#-------------------------------------------------------------------

# Higher-order functions.
def greeting(argument_function):
    returned_reference_function = argument_function('Hello, greetings from my function.')
    print(returned_reference_function)

greeting(uppercases)
greeting(lowercases)

# The classical example of the Higher-order function is the map function.
print(list(map(uppercases, ['Text_1', 'Text_2', 'Text_3'])))
print(list(map(lowercases, ['Text_1', 'Text_2', 'Text_3'])))

#-------------------------------------------------------------------

# Nested functions.
def show(text):
    def lowercases_convertion(t):
        return t.lower()

    return lowercases_convertion(text)

print(show('Nested functions test.'))

# Returning the nested functions.
def speak(volume):
    def lowercases(text):
        return text.lower()

    def uppercases(text):
        return text.upper()

    if volume > 0.5:
        return uppercases
    else:
        return lowercases

print(speak(0.6))
print(speak(0.6)('camilo alejandro'))
print(speak(0.4))
print(speak(0.4)('CAMILO ALEJANDRO'))

#-------------------------------------------------------------------

# Closure in Python: an iternal function uses the state of its
# external function.
def speak2(text, volume):
    def lowercases():
        return text.lower()

    def uppercases():
        return text.upper()

    if volume > 0.5:
        return uppercases()
    else:
        return lowercases()

print(speak2('speaking out loud', 0.55))
print(speak2('SPEAKING QUIETLY', 0.4))

# Example 2: pre-set a function. In this case, by the closure
# the state of the function 'greet' is saved.
def show(degree):
    def greet(message):
        return degree + '. ' + message

    return greet

print(show('Engineer')('Camilo Alejandro'))
print(show('Graduate')('Jhon Perez'))

#-------------------------------------------------------------------

# The callable function lets us know if an object can be called or not.
print(f'Is the show object callable as function? {callable(show)}')
show_eng = show('Engineer')
print(f'Is the show_eng (show object ) callable as function? {callable(show_eng)}')
print(f'Is the speak object callable as function? {callable(speak)}')
print(f'Is the str object callable as function? {callable("text")}')

# Callable objects can be created from a class by overriding the
# __call__ method.
class Show:
    def __init__(self, degree) -> None:
        self.degree = degree
    
    def __call__(self, message):
        return self.degree + '. ' + message

show_doctor = Show('Doctor')
print(show_doctor('Carlos Ugalde'))
print(f'Is the show_doctor object callable as function? {callable(show_doctor)}')

#-------------------------------------------------------------------
