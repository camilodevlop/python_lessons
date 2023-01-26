# Lists: printing its elements.
print('\n\tPrinting the elements of a list.')
lst = ['Camilo', 'Alejandro', 12.3, 1, True]

for i in range(len(lst)):
    print(f'\t{lst[i]}')
else:
    print('\tThe list has been printed.\n')

lst.append(789)
lst.insert(2,'Castillo')
lst.append(('Castillo'))
print(lst)

lst.remove('Castillo') # Erases the first occurrence.
print(lst)

lst.pop()
print(lst)
del lst[4]
print(lst)
lst.clear()
print(lst)
del lst

#-------------------------------------------------------------------

# Use of lists and ranges.
print('\n\tUse of ranges.\n\n\tMultiples of three.')
for i in range(0,11,1):
    if (i % 3 == 0):
        print(f'\t{i}')

print('\n\tRange 2 to 6.')
for i in range(2,7,1):
    print(f'\t{i}')

print('\n\tNumbers range from 3 to 10 with an increment of 2.')
for i in range(3,11,2):
    print(f'\t{i}')

#-------------------------------------------------------------------

# Use of tuples.
print('\n\tUse of Tuples.\n\n\tFruits example.')
fruits = ('Orange','Banana','Apple',1)
print(f'\tLength: {len(fruits)}, {fruits}, {fruits[0]}.')
print(f'\t{fruits[1:4]}.')

for f in fruits:
    print(f'\t{f}', end = ' ')

#-------------------------------------------------------------------

# Tuple's modification.
print('\n\n\tTuple\'s modification.')
listFruits = list(fruits)
print(f'\t{listFruits}')
listFruits[0] = 'Pineapple'
print(f'\t{listFruits}\n')

fruits = tuple(listFruits)
print(f'\tList to tuple convertion.\n\t{fruits}')

#-------------------------------------------------------------------

# Given a tuple, create a list with elements less than 5.
print('\n\tGiven a tuple, create a list with elements less than 5.')
tpl = (13, 1, 8, 3, 2, 5, 8)
print(f'\tTuple: {tpl}')
lst = []

for t in tpl:
    if (t < 5):
        lst.append(t)
print(f'\tlist: {lst}')

#-------------------------------------------------------------------

# Dictionaries.
print('\n\tDictionaries.')
dct = {
    'IDE': 'Integrating Development Environment',
    'OOP': 'Object Oriented Programming.',
    'DBMS': 1
}

print(f'\t{dct}')
print('\t', dct['OOP'])
print('\t', dct.get('DBMS'))
dct['DBMS'] = 'Database Management System'
print(f'\t{dct}')

print('\n\tPrinting the keys of the dictionary:')
for k in dct:
    print(f'\t{k}')

for k in dct.keys():
    print(f'\t{k}')

print('\n\tPrinting the values of the dictionary:')
for v in dct.values():
    print(f'\t{v}')

print('\n\tPrinting the keys and values of the dictionary:')
for k, v in dct.items():
    print(f'\t{k}: {v}')

print('\t','OOP' in dct)

# Add an element.
dct['PK'] = 'Primary Key'
print(f'\n\tAdding an element:\n\t{dct}')

# Remove an item.
dct.pop('DBMS')
print(f'\n\tRemoving an element:\n\t{dct}')

# Clear the dictionary.
dct.clear()
print(f'\n\tClear the dictionary:\n\t{dct}')

#-------------------------------------------------------------------
