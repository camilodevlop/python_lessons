# Unpacking operator.

numbers1 = [1, 2, 3]
print(f'\n\tNumbers: {numbers1}')
print('\n\tNumbers unpacked:', *numbers1)
print('\n\tNumbers unpacked using \'-\' separator: ', *numbers1, sep = '-')

def sum(a, b, c):
    print(f'\n\tSum: {a + b + c}')

sum(*numbers1)

#-------------------------------------------------------------------

# Extracting parts of a list:

my_list = list(range(0,20))
a, *b, c, d = my_list
print(f'\n\tExtracted parts of a list: {a, b, c, d}')

#-------------------------------------------------------------------

# Linking the lists.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [list1, list2]
print(f'\n\tList of lists: {list3}')

list3 = [*list1, *list2]
print(f'\tLinking the lists: {list3}')

# Linking dictionaries.

dic1 = {'A':1, 'B':2, 'C':3}
dic2 = {'D':4, 'E':5}
dic3 = {**dic1, **dic2}
print(f'\n\tLinking the dictionaries: {dic3}')

#-------------------------------------------------------------------

# Building a list from a str.

list1 = [*'HelloWorld']
print(f'\n\tBuilding a list from a str: {list1}')
print('\t', *list1)
print(f'\tInitial string: ', *list1, sep = '')

#-------------------------------------------------------------------
