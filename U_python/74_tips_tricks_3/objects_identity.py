# Operator == comparison using OOP.
# == compares the content of two objects. It doesn't imply that the
# objects are the same.

# The 'is' operator checks if two objects are equal.

#-------------------------------------------------------------------

# Example.
list_a = [1, 2, 3]
list_b = list_a

# == -> True and is -> True.
print(f'a and b lists have the same content?  {list_a == list_b}')
print(f'a and b lists are the same object?  {list_a is list_b}')

# == -> True and is -> False.
list_c = list(list_a)
print(f'a and c lists have the same content?  {list_a == list_c}')
print(f'a and c lists are the same object?  {list_a is list_c}')

#-------------------------------------------------------------------
