def print_vector(x, y, z):
    print(f'<{x}, {y}, {z}>')

print_vector(10, 3, 12)

tuple_vector = (8, 12, 15)
print_vector(*tuple_vector)

list_vector = [4, 2, 7]
print_vector(*list_vector)

expression_generator = (x*x for x in range(3))
# print(*expression_generator)
print_vector(*expression_generator)

vector_dict = {'x':10, 'y':15, 'z': 3}
print_vector(*vector_dict)      # Keys.
print_vector(**vector_dict)     # Values.

#-------------------------------------------------------------------
