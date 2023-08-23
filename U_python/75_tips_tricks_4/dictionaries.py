from collections import OrderedDict, defaultdict, ChainMap
from os import device_encoding
from types import MappingProxyType

# from typing import ChainMap

# Dictionaries - dicts (key - value)
# Alternative names: maps, hashmaps or lookup tables.

# Example: directory (key = name, value = phone)
directory = {
    'Juan' : 6534745,
    'Alicica' : 98545340,
    'Carlos' : 1234124,
}

print(directory)
print(directory['Juan'])
# print(directory['juan'])  # KeyError.

#-------------------------------------------------------------------

# Using an expression to create a dictionary.
squared_values = {x:x*x for x in range(5)}
print(squared_values)

'''
lst = [1, 2, 3]
wrong_dictionary = {lst : 'A'}
print(wrong_dictionary)
'''

tpl = (1, 2, 3)
right_dictionay = {tpl : 'C'}
print(right_dictionay)

#-------------------------------------------------------------------

# Ordered insertion using OrderedDict.
ordered_dict = OrderedDict(one = 1, two = 2, three = 3)
print(ordered_dict)
ordered_dict['four'] = 4
print(ordered_dict)

print(ordered_dict.keys())
ordered_dict['one'] = -1
print(ordered_dict)

# Deletion and reinsertion of a key.
ordered_dict.pop('three')
print(ordered_dict)
ordered_dict['three'] = 3
print(ordered_dict)

#-------------------------------------------------------------------

# defaultdict.
dict_default = defaultdict(lambda : 'Wrong value...')
dict_default['a'] = 1
dict_default['b'] = 2
print(dict_default.items())
print(dict_default['c'])

# A list can be used as an argument to defaultdict. If the accessed
# key doesn't exist, it is added to a list.
dict_default_lst = defaultdict(list)
dict_default_lst['names'].append('Jhon')
dict_default_lst['names'].append('Karla')
dict_default_lst['names'].append('Laura')
print(dict_default_lst)
print(dict_default_lst.items())
print(dict_default_lst.keys())
print(dict_default_lst.values())

#-------------------------------------------------------------------

# Searching in multiple dictionaries.

dict_1 = {'one' : 1, 'dos' : 2, 'tres' : 3, 'five' : 'A'}
dict_2 = {'four' : 4, 'five' : 5, 'six' : 6}
dict_combination = ChainMap(dict_1, dict_2)
print(dict_combination)
print(dict_combination['five'])

# A KeyError is raised id the key doesn't exist.
# print(dict_combination['seven'])

#-------------------------------------------------------------------

# read-only dictionaries.
dict_mutable = {'one' : 1, 'dos' : 2, 'tres' : 3, 'five' : 'A'}
dict_read_only = MappingProxyType(dict_mutable)
print(dict_read_only)
print(dict_read_only['one'])

# dict_read_only['one'] = -1 # Error if we try to modify any of the values.

# If the mutable dict is modified, it affects the read-only one too.
dict_mutable['dos'] = 22
print(dict_read_only)

#-------------------------------------------------------------------
