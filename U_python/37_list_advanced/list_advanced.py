# Lists are mutable.

names1 = ['Jhon', 'Karla', 'Peter']
names2 = 'Camilo Alexander Brad Enzo'.split()
print(f'\n\tAdd list: {names1 + names2}')

# Extend the lists.
names1.extend(names2)
print(f'\tExtending the list1: {names1}')

#-------------------------------------------------------------------

# Numbers list.
numbers1 = [90, 50, 70, 40, 20, 30, 40]
print(f'\tIndex of 40: {numbers1.index(40)}')

# Reversing the list elements.
numbers1.reverse()
print(f'\tReversed list: {numbers1}')

# Sorting the list elements.
numbers1.sort()
print(f'\n\tSorted list: {numbers1}')

# Sorting the list elements descendingly.
numbers1.sort(reverse = True)
print(f'\tSorted list descendingly: {numbers1}')

# Getting the min and max values of a list.
print(f'\n\tMin value: {min(numbers1)}')
print(f'\tMax value: {max(numbers1)}')

# Copying the list elements.
numbers2 = numbers1.copy()
print(f'\n\tIs the reference equal?: {numbers1 is numbers2}')
print(f'\tIs the content equal?: {numbers1 == numbers2}')

# Using the list constructor.
numbers2 = list(numbers1)
print(f'\n\tIs the reference equal?: {numbers1 is numbers2}')
print(f'\tIs the content equal?: {numbers1 == numbers2}')

# Slicing.
numbers2 = numbers1[:]
print(f'\n\tIs the reference equal?: {numbers1 is numbers2}')
print(f'\tIs the content equal?: {numbers1 == numbers2}')

#-------------------------------------------------------------------

# List multiplication.
list_multiplication = 5 * [[4, 5]]
print(f'\n\tList multiplication: {list_multiplication}')
print(f'\tIs the same reference?: {list_multiplication[0] is list_multiplication[4]}')
print(f'\tIs the content equal?: {list_multiplication[0] == list_multiplication[4]}')

#-------------------------------------------------------------------

# Matrices.
matrix = [ [ 10, 20 ], [30, 40, 50], [60, 70, 80, 90]]
print(f'\n\tOriginal matrix: {matrix}')
print(f'\tRaw 0, column 0: {matrix[0][0]}')
print(f'\tRaw 2, column 2: {matrix[2][2]}')

matrix[2][0] = 65
print(f'\n\tModified matrix: {matrix}')

#-------------------------------------------------------------------

# Function ordering.
list_lists = [[1, 2, 3, 4, 5, 6], [10, 20, 30, 40], [0, 21, 22, 23, 24, 25, 26]]
list_lists.sort(key = len)
print(f'\n\tOrdered list by length: {list_lists}')

#-------------------------------------------------------------------

# Sorted built-in.

names1 = [ 'Victor', 'Lina', 'Camilo', 'Cordula' ]
names1 = sorted(names1)
print(f'\n\tSorted names list: {names1}')

names1 = sorted(names1, reverse = True)
print(f'\n\tReverse sorted names list: {names1}')

names1 = sorted(names1, key = len)
print(f'\n\tSorted by number of characters: {names1}')

# Reversed built-in.
names1 = reversed(names1)
print(f'\n\tReversed names list: {list(names1)}')

#-------------------------------------------------------------------
