
# Nested function.

def calculator(a, b, op = 'sum'):
    def sum(a, b):
        return a + b
    
    def subs(a, b):
        return a - b

    if op == 'sum':
        print(f'\n\tSum: {sum(a, b)}')
    elif op == 'substract':
        print(f'\tSubstract: {subs(a, b)}')

calculator(5, 6, 'substract')

#-------------------------------------------------------------------

# Variables scope.

global_var = 'Global variable.'

def prt():
    # Accessing a global variable.
    global global_var
    print(f'\n\tCall to the global var: {global_var}')
    global_var = 'New value Global variable.'
    print(f'\n\tCall to the global var: {global_var}')
    
    # Defining a local variable.
    local_var = 'Local variable'
    print(f'\tCall to the local variable: {local_var}')

    def nested_func():
        print(f'\tCall to the local variable inside the nested func: {local_var}')

    nested_func()

prt()
print(f'\n\tCall to the global var outside the function: {global_var}')

#-------------------------------------------------------------------

# Nested functions and variables scope.

def external_funct():
    local_var_external = 'Local variable external'

    def nested_func():
        nested_local_var = 'Nested local var'

        nonlocal local_var_external
        local_var_external = 'New value of Local variable external.'

    nested_func()
    print(f'\n\tNested_local_var: {local_var_external}')

external_funct()

#-------------------------------------------------------------------

# GLobal variable definition.
counter = 0

def print_counter():
    print(f'\n\tCounter: {counter}')

def modifier_counter(c):
    global counter
    counter = c

modifier_counter(5)
print_counter()

#-------------------------------------------------------------------

# The functions in Python are first class citizens.

def add(a, b):
    return a + b

# Assigning a function to a variable.
sum1 = add

# Verifying the type.
print(f'\n\tVerifying the function type: {sum1}')

# Calling the function by the variable.
result = sum1(4, 5)
print(f'\tResult: {result}')

# Function as argument.
def operation(a, b, sum_arg):
    print(f'\n\tAdd result: {sum_arg(a, b)}')

operation(4, 5, add)

# Function is a return.
def returning_function():
    return add

function_returned = returning_function()
print(f'\n\tReturned function result: {function_returned(78, 45)}')

#-------------------------------------------------------------------










