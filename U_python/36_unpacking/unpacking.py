# Unpacking.
values = 1,2,3
print(f'\n\tUnpacking.\n\tValues: {values}, {type(values)}')

value1, value2, value3 = values
print('\t', value1, value2, value3)

value1, _, value3 = 1, 2, 3     # '_' indicates that the valued is ignored.
print(f'\t{value1}, {value3}')

value1, value2, *value3 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(f'\t{value1}, {value2}, {value3}')

value1, value2, *value3, value4, value5 = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(f'\t{value1}, {value2}, {value3}, {value4}, {value5}')

# Unpacking using lists.
value1, value2, *value3, value4, value5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'\t{value1}, {value2}, {value3}, {value4}, {value5}')

#-------------------------------------------------------------------

def return_values():
    return 1, 2, 3

value1, value2, value3 = return_values()
print('\n\tReturning the values: ', value1, value2, value3)

value1, *_ = return_values()
print('\n\tReturning the value1: ', value1)

#-------------------------------------------------------------------

# Partition method.
hour, sep, minutes = '17:50'.partition(':')
print('\n\tTime: ', hour, sep, minutes)

#-------------------------------------------------------------------
