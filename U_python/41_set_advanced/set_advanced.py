# Set advanced.

# It is a mutable collection of unique elements.
# The elements of a set must be inmutables.

set1 = { 'Juan', True, 10, True }
print(f'\n\tSet: {set1}')

# Empty set.
set2 = set()
print(f'\tEmpty set: {set2}')

# Mutable.
set1.add('Jhon')
print(f'\n\tSet: {set1}')

# Set contains singular values.
set1.add('Juan')
print(f'\n\tSet -singular values-: {set1}')

# Creating a set from an iterable.
set3 = set([3, 4, 5, 7, 3])
print(f'\n\tSet created from an iterable: {set3}')

#-------------------------------------------------------------------

# Adding more elements or another Set.

set2 = {100, 200, 300, 400, 400}
set1.update(set2)
print(f'\n\tUpdated set: {set1}')
set1.update([20, 30, 40, 40])
print(f'\n\tUpdated set: {set1}')

# Copying the references of a set.

set_copy = set1.copy()
print(f'\n\tCopied set: {set_copy}')

# Checking the equality. 
print(f'\n\tIs the content equal?: {set1 == set_copy}')

# Checking the reference.
print(f'\n\tChecking the reference: {set1 is set_copy}')

#-------------------------------------------------------------------

# Set operations.

black_hair = {'Jhon', 'Laurene', 'Peter', 'Maria'}
blonde_hair = {'Camilo', 'Lina', 'Emma', 'Rose'}
brown_eyes = {'Camilo', 'Jhon'}
under_30 = {'Jhon', 'Laurene', 'Maria'}

print(f'\n\tUnion function: {brown_eyes.union(blonde_hair)}')
print(f'\n\tIntersection function: {brown_eyes.intersection(blonde_hair)}')
print(f'\n\tDifference function: {black_hair.difference(brown_eyes)}')
#print(f'\n\tSimmetric difference function: {black_hair.simmetric_difference(brown_eyes)}')

print(f'\n\tSubset function: {under_30.issubset(black_hair)}')
print(f'\n\tSuperset function: {under_30.issuperset(black_hair)}')
print(f'\n\tDisjoint function: {black_hair.isdisjoint(blonde_hair)}')

#-------------------------------------------------------------------
