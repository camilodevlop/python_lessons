# Generators return a sequence of values. Generators suspend the
# execution of 'yield' function. These do not use 'return'.

def generator():
    yield 1
    yield 2
    yield 3

# Values are consumed on demand.
gen = generator()
print(f'\tGenerator: {next(gen)}')
print(f'\tGenerator: {next(gen)}')
print(f'\tGenerator: {next(gen)}\n')

# Using a for loop.
for value in generator():
    print(f'\tGenerator - for: {value}')

#-------------------------------------------------------------------

# Example of generators.

def numbers_generator():
    for number in range(1,6):
        yield number
        print(f'\tResumed execution.')

# Using the generator.
print(f'\n\tExample of generator:')
gen = numbers_generator()
for value in gen:
    print(f'\tValue: {value}')

# Consuming values on demand.
print(f'\n\tConsuming values on demand:')
gen = numbers_generator()
print(f'\tGenerator: {next(gen)}')

try:
    print(f'\tGenerator: {next(gen)}')
    print(f'\tGenerator: {next(gen)}')
    print(f'\tGenerator: {next(gen)}')

except StopIteration as e:
    print(f'\n\tConsuming generator error: {e}')

# Alternative method for consuming values on demand.
print(f'\n\tConsuming values on demand:')
gen = numbers_generator()

while True:
    try:
        value = next(gen)
        print(f'\tGenerator: {value}')

    except StopIteration as e:
        print(f'\n\tConsuming generator error: {e}')
        break

#-------------------------------------------------------------------

# Generating expresions.
mult = (value*value for value in range(5))
print(f'\n\tGenerating expresions - Type: {type(mult)}')
print(f'\tGenerator: {next(mult)}')
print(f'\tGenerator: {next(mult)}')
print(f'\tGenerator: {next(mult)}')
print(f'\tGenerator: {next(mult)}')
print(f'\tGenerator: {next(mult)}')

# A generating expression can be included as a function argument.
summ = sum(value*value for value in range(4))
print(f'\n\tGenerating expression as a function argument (Sum): {summ}')

# Generating expresions and iterators.
lst = ['Camilo', 'Lina', 'Cordula', 'Victor']
gen = (name for name in lst)
print(f'\tNames: {next(gen)}')

# Creating a string from generating expresions and iterators.
lst = [ 'Lina', 'María', 'Natalia' ]

counter = 0
def incrementer():
    global counter
    counter += 1
    return counter

# The first part is the 'yield'. The second is the 'for'.
gen = (f'{incrementer()}. {name}' for name in lst)
lst2 = list(gen)
print(f'\n\tList generated: {lst2}')

string = ', '.join(lst2)
print(f'\tConcatenated list elements: {string}')

#-------------------------------------------------------------------













