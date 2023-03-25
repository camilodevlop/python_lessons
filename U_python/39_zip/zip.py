# 'zip' function in Python: it joins iterables.

from os.path import join


numbers1 = (1, 2, 3, 4)
letters1 = ['a', 'b', 'c', 'd', 'e']
set1 = {7, 5, 4, 19, 34, 9}

joint = zip('HelloWorld', range(15), numbers1, letters1)
print(f'\n\tResult of \'zip\' function: {joint}')
print('\t', list(joint))

#-------------------------------------------------------------------

# Iterating in parallel.

new_list = []
print('\n\tIteraring in parallel.')
for number, letter, elem in zip(numbers1, letters1, set1):
    print(f'\tNumber: {number}, Letter: {letter}, Element: {elem}')
    new_list.append(f'{number}-{letter}-{elem}')

print(f'\n\tNew list: {new_list}')

#-------------------------------------------------------------------

# Unzip.

joint = [(1,'a'), (2,'b'), (3,'c')]
print(*joint)
numbers, letters = zip(*joint)
print(f'\n\tUnzip: Numbers {numbers} Letters {letters}')

# Sorting.

letters1 = ['b', 'e', 'a', 'd', 'c']
numbers1 = [3, 4, 7, 8]
joint = zip(letters1, numbers1)

# Disorderly.
print(f'\n\t: Joint: {joint}')
# Sorting by letter.
print(f'\tSorting by letter: {sorted(zip(letters1, numbers1))}')
# Sorting by number.
print(f'\tSorting by number: {sorted(zip(numbers1, letters1))}')

#-------------------------------------------------------------------

# Creating a dictionary using a 'zip' and two iterables.

keys = ['Name', 'Surname', 'Age']
values = ['Camilo', 'Castillo', 35]
dictionary = dict(zip(keys,values))
print(f'\n\tDictionary: {dictionary}')

# Updating a dictionary element.

key = ['Age']
nv = [28]
dictionary.update(zip(key, nv))
print(f'\n\tDictionary: {dictionary}')

#-------------------------------------------------------------------
