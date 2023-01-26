# Functions.
def my_function(name, surname):
    print('\n\tMy first function:')
    print(f'\tName: {name}, Surname: {surname}')

my_function('Camilo', 'Castillo')
my_function('Lina', 'Castillo')

#-------------------------------------------------------------------

# Sum of two numbers.
print('\n\tSum of a + b.')
def sum(a = 0, b = 0):
    return a + b

print(f'\tSum: {sum(5, 10)}')

#-------------------------------------------------------------------

# Functions: variable arguments.
print('\n\tFunctions: variable arguments.')
def lst_func(*arg):
    for a in arg:
        print(f'\t{a}')

lst_func('Camilo', 'Alejandro', 14)

# Functions: using *args for add.
print('\n\tFunctions: using *args for add.')
def sum_arg(*args):
    summ = 0
    for a in args:
        summ += a

    return summ

print(f'\tSum: {sum_arg(5,4,3,2,1)}')

# Functions: using *args for multiply.
print('\n\tFunctions: using *args for multiply.')
def multiply_arg(*args):
    multiply = 1
    for multiple in args:
        multiply *= multiple

    return multiply

print(f'\tMultiply: {multiply_arg(5,4,3,2,1)}')

#-------------------------------------------------------------------

# Functions: variable arguments using dictionaries.
print('\n\tFunctions: variable arguments using dictionaries.')
def lst_func_dct(**arg):
    for k,v in arg.items():
        print(f'\t{k}: {v}')

lst_func_dct(IDE = 'Integrated Dev. Environment', PK = 'Primary Key')

#-------------------------------------------------------------------

# Functions: different types of arguments.
print('\n\tFunctions: different types of arguments.')
def print_v_arg(v_arg):
    for va in v_arg:
        print(f'\t{va}')

names = ['Camilo', 'Lina', 'Victor', 'Cordula']
print_v_arg(names)
print_v_arg('Carlos')
print_v_arg(('Carlos',)) # Simple tuple.
print_v_arg([12, 10])

#-------------------------------------------------------------------

# Functions: recursion.
print('\n\tFunctions: recursion.')
def factotial(num):
    if (num == 1):
        return 1
    else:
        return num * factotial(num - 1)

print(f'\tFactorial = {factotial(7)}')

#-------------------------------------------------------------------
