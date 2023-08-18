import copy


# Shallow copy.
list_a = [[1, 2], [3, 4], [5, 6]]

# Shallow copy.
# The lists are different. These point to different memory addresses.
# In the case of internals lists, only the references were copied.
list_b = list(list_a)

print(f'List_a: {list_a}')
print(f'List_b: {list_b}')

# A change to list_a doesn't affect the list_b, i.e., the objects
# are differents.
list_a.append([7, 8])
print(f'A change to list_a doesn\'t affect the list_b.')
print(f'List_a: {list_a}')
print(f'List_b: {list_b}')

# The internal objects (lists) have the same references.
# A change to one of the lists affects the copied list.
list_a[0][1] = 'A'
print(f'Only the references of the inner elements were copied..')
print(f'List_a: {list_a}')
print(f'List_b: {list_b}')

#-------------------------------------------------------------------

# The 'copy' module allows us to make deep copies.
list_c = [[1, 2], [3, 4], [5, 6]]
list_d = copy.deepcopy(list_c)

# A change to list_c doesn't affect the list_d, i.e., the objects
# are differents.
list_c.append([7, 8])
print(f'A change to list_c doesn\'t affect the list_d.')
print(f'List_c: {list_c}')
print(f'List_d: {list_d}')

# The internal objects are new.
# A change to one of the lists doesn't affect the copied list.
list_c[0][1] = 'A'
print(f'The internal objects are new.')
print(f'List_c: {list_c}')
print(f'List_d: {list_d}')

#-------------------------------------------------------------------
for lst in list_c:
    print(lst)
