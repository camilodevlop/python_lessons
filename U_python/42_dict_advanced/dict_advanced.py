from pprint import pprint

# Dictionaries keep an order unlike Sets.

dict1 = {'Name':'Camilo','Surname':'Castillo','Age':35}
print(f'\n\tDictionary: {dict1}')

# The dictionaries are mutable, but their keys not. 
# dict2= {[1,2]:'Value'}
dict2= {(1,2):'Value'}
print(f'\n\tTuples are inmutables: {dict2}')

# A key is added if it is not in the dictionary.
dict1['Departament'] = 'Systems'
print(f'\n\tDictionary: {dict1}')

# Dictionaries don't contain similar keys.
dict1['Name'] = 'Camilo Alejandro'
print(f'\n\tDictionary: {dict1}')

# Recovering values from the dictionary keys.
print('\n\tName key contains: ', dict1['Name'])
print('\n\tGet method - Name: ', dict1.get('Name', 'The key was not found.'))

# Setdefault modifies the dictionary if a key has not been found.
name = dict1.setdefault('Name', 'Default value.')
print(f'\n\tName value: {name}')
print(f'\n\tDictionary: {dict1}')

pprint(dict1, sort_dicts = False)

#-------------------------------------------------------------------
